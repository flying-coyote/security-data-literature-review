#!/usr/bin/env python3
"""
Literature Review - Weekly Health Check

Automated maintenance script to check literature review health:
- Evidence source link validation
- Outdated evidence detection (>12 months)
- Bibliography completeness
- Hypothesis validation status
- Publication manuscript status
- Quarterly update schedule tracking

Run weekly via cron to maintain "living literature review" quality.
"""

import json
import os
import re
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass, field
from urllib.parse import urlparse
import requests


@dataclass
class HealthCheckResult:
    """Results from health check."""

    timestamp: str
    status: str  # "healthy", "warning", "critical"
    checks_passed: int = 0
    checks_failed: int = 0
    checks_warning: int = 0

    # Specific findings
    broken_links: List[str] = field(default_factory=list)
    unreachable_links: List[str] = field(default_factory=list)  # inconclusive (egress/DNS), not counted as broken
    outdated_evidence: List[str] = field(default_factory=list)
    missing_bibliography: List[str] = field(default_factory=list)
    stale_hypotheses: List[str] = field(default_factory=list)
    publication_issues: List[str] = field(default_factory=list)
    quarterly_update_status: Dict = field(default_factory=dict)

    # Git status
    uncommitted_changes: int = 0
    last_commit_date: str = ""
    days_since_commit: int = 0

    # Summary metrics
    total_sources: int = 0
    tier_a_percentage: float = 0.0
    evidence_freshness_avg_days: int = 0


class LiteratureReviewHealthCheck:
    """Weekly health check for literature review repository."""

    def __init__(self, repo_path: str = None):
        # Resolve the repo relative to this script by default so a direct run works
        # wherever the repo is checked out (local tree, or a fresh clone in a remote
        # scheduled routine). The old hardcoded ~/security-data-literature-review
        # default crashed on any machine that wasn't the original author's laptop.
        if repo_path is None:
            repo_path = Path(__file__).resolve().parent.parent
        self.repo_path = Path(repo_path).expanduser().resolve()
        self.result = HealthCheckResult(
            timestamp=datetime.now().isoformat(),
            status="healthy"
        )

    def run_all_checks(self) -> HealthCheckResult:
        """Run all health checks."""
        print("🏥 Running Literature Review Health Check...")
        print(f"📁 Repository: {self.repo_path}")
        print(f"🕐 Timestamp: {self.result.timestamp}\n")

        # Core health checks
        self.check_git_status()
        self.check_bibliography_links()
        self.check_evidence_freshness()
        self.check_hypothesis_status()
        self.check_publication_status()
        self.check_quarterly_update_schedule()
        self.check_vendor_landscape_status()

        # Calculate overall status
        self.calculate_overall_status()

        return self.result

    def check_git_status(self):
        """Check git repository status."""
        print("📊 Checking Git Status...")

        try:
            os.chdir(self.repo_path)

            # Check for uncommitted changes
            status_output = subprocess.run(
                ["git", "status", "--porcelain"],
                capture_output=True,
                text=True,
                check=True
            )
            uncommitted = len(status_output.stdout.strip().split('\n')) if status_output.stdout.strip() else 0
            self.result.uncommitted_changes = uncommitted

            # Get last commit date
            last_commit_output = subprocess.run(
                ["git", "log", "-1", "--format=%ci"],
                capture_output=True,
                text=True,
                check=True
            )
            last_commit_str = last_commit_output.stdout.strip()
            if last_commit_str:
                last_commit_date = datetime.fromisoformat(last_commit_str.rsplit(' ', 1)[0])
                self.result.last_commit_date = last_commit_date.strftime("%Y-%m-%d")
                self.result.days_since_commit = (datetime.now() - last_commit_date).days

            # Warnings
            if uncommitted > 0:
                self.result.checks_warning += 1
                print(f"  ⚠️  {uncommitted} uncommitted changes")
            else:
                self.result.checks_passed += 1
                print(f"  ✅ No uncommitted changes")

            if self.result.days_since_commit > 30:
                self.result.checks_warning += 1
                print(f"  ⚠️  Last commit {self.result.days_since_commit} days ago (stale)")
            else:
                self.result.checks_passed += 1
                print(f"  ✅ Last commit {self.result.days_since_commit} days ago")

        except subprocess.CalledProcessError as e:
            self.result.checks_failed += 1
            print(f"  ❌ Git check failed: {e}")

    def check_bibliography_links(self):
        """Validate URLs in MASTER-BIBLIOGRAPHY.md."""
        print("\n🔗 Checking Bibliography Links...")

        bib_path = self.repo_path / "MASTER-BIBLIOGRAPHY.md"
        if not bib_path.exists():
            self.result.checks_failed += 1
            print(f"  ❌ MASTER-BIBLIOGRAPHY.md not found")
            return

        with open(bib_path, 'r') as f:
            content = f.read()

        # total_sources is the count of catalogued ENTRIES ("#### Title"), which is the
        # canonical number every other surface cites — not the URL count, which differs
        # because some entries carry several URLs or none (placeholder/"Various" sources).
        self.result.total_sources = len(re.findall(r'^#### ', content, re.MULTILINE))
        urls = re.findall(r'\*\*URL\*\*:\s*(https?://[^\s\)]+)', content)
        print(f"  📚 {self.result.total_sources} entries · {len(urls)} URLs to sample")

        # Check a sample of URLs (checking all of them every run would be slow).
        import random
        sample_size = min(10, len(urls))
        sample_urls = random.sample(urls, sample_size) if urls else []

        broken, unreachable = [], []
        for url in sample_urls:
            verdict, code = self._classify_url(url)
            if verdict == "broken":
                broken.append(url)
                print(f"  ❌ Broken: {url} (status {code})")
            elif verdict == "unreachable":
                unreachable.append(url)
                print(f"  ⚠️  Unreachable (inconclusive): {url} ({code})")

        self.result.broken_links = broken
        self.result.unreachable_links = unreachable

        if broken:
            # A confirmed dead link (404/410) is a real failure, not a soft warning —
            # this is what lets the overall status actually go red.
            self.result.checks_failed += 1
            print(f"  ❌ {len(broken)}/{sample_size} sampled links confirmed broken")
        elif unreachable:
            self.result.checks_warning += 1
            print(f"  ⚠️  {len(unreachable)}/{sample_size} unreachable from here (not counted as broken)")
        else:
            self.result.checks_passed += 1
            print(f"  ✅ All {sample_size} sampled links reachable")

    @staticmethod
    def _classify_url(url):
        """Classify a URL as 'ok', 'broken', or 'unreachable'.

        Only a definitive 404/410 (and a persistent 5xx) counts as 'broken'. A live server
        that refuses a bot — 403/405/429/999 — is reachable, not broken, so we retry with a
        real-UA ranged GET before judging. A connection/DNS/timeout error is 'unreachable':
        inconclusive (could be restricted egress in a sandbox), so it is reported but never
        counted as broken — false reds are as corrosive to trust as false greens.
        """
        ua = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
        bot_blocked = {403, 405, 406, 429, 999}
        try:
            r = requests.head(url, timeout=8, allow_redirects=True, headers={"User-Agent": ua})
            if r.status_code in bot_blocked or r.status_code >= 500:
                r = requests.get(url, timeout=10, allow_redirects=True, stream=True,
                                 headers={"User-Agent": ua, "Range": "bytes=0-2047"})
            if r.status_code in (404, 410):
                return "broken", r.status_code
            if r.status_code >= 500:
                return "broken", r.status_code  # persistent server error after GET retry
            return "ok", r.status_code
        except requests.RequestException as e:
            return "unreachable", type(e).__name__

    def check_evidence_freshness(self):
        """Check for outdated evidence sources (>12 months)."""
        print("\n📅 Checking Evidence Freshness...")

        bib_path = self.repo_path / "MASTER-BIBLIOGRAPHY.md"
        if not bib_path.exists():
            return

        # Extract dates and validation status.
        # Capture the FULL Date value, then resolve it to its most-recent 4-digit
        # year. The old r'\*\*Date\*\*:\s*(\d{4})' only matched a year at the START
        # of the value, so prose dates ("May 19, 2026", "October 2022") were missed
        # entirely and ranges ("2022-2024") were mis-aged to their oldest year.
        # Reading every 19xx/20xx year in the value and taking the max is the honest
        # reading: an entry dated "2022-2024" is current as of 2024.
        date_line_pattern = re.compile(r'\*\*Date\*\*:\s*([^\n]+)')
        year_pattern = re.compile(r'\b(?:19|20)\d{2}\b')
        validation_pattern = re.compile(r'\*\*Validation Status\*\*:\s*([^\\n]+)')

        with open(bib_path, 'r') as f:
            content = f.read()
            date_values = date_line_pattern.findall(content)
            validations = validation_pattern.findall(content)

        # Resolve each Date line to its most-recent year (prose, range, or Month YYYY).
        dates = []
        for _val in date_values:
            _years = year_pattern.findall(_val)
            if _years:
                dates.append(str(max(int(y) for y in _years)))

        # Check for sources older than 12 months
        current_year = datetime.now().year
        outdated = [d for d in dates if int(d) < current_year - 1]

        self.result.outdated_evidence = [f"Year {d}" for d in outdated]

        # 40% matches weekly_scheduled_check.OUTDATED_FRACTION_RED so the two surfaces
        # agree on what "too stale" means; some staleness is normal for a living review.
        if dates and len(outdated) > len(dates) * 0.4:
            self.result.checks_warning += 1
            print(f"  ⚠️  {len(outdated)}/{len(dates)} sources >12 months old")
        else:
            self.result.checks_passed += 1
            print(f"  ✅ {len(dates) - len(outdated)}/{len(dates)} sources recent")

    def check_hypothesis_status(self):
        """Check hypothesis validation status."""
        print("\n🧪 Checking Hypothesis Status...")

        hyp_path = self.repo_path / "LITERATURE-HYPOTHESIS-GAP-ANALYSIS.md"
        if not hyp_path.exists():
            self.result.checks_warning += 1
            print(f"  ⚠️  Hypothesis gap analysis not found")
            return

        with open(hyp_path, 'r') as f:
            content = f.read()

        # Count validated vs pending hypotheses
        validated = len(re.findall(r'(STRONGLY VALIDATED|VALIDATED|STRONG)', content, re.IGNORECASE))
        pending = len(re.findall(r'(PENDING|INSUFFICIENT|WEAK)', content, re.IGNORECASE))

        if validated > 0:
            self.result.checks_passed += 1
            print(f"  ✅ {validated} hypotheses validated")

        if pending > validated:
            self.result.checks_warning += 1
            print(f"  ⚠️  {pending} hypotheses still pending validation")

    def check_publication_status(self):
        """Check publication manuscript status."""
        print("\n📝 Checking Publication Status...")

        pub_path = self.repo_path / "PUBLICATION-MANUSCRIPT.md"
        if not pub_path.exists():
            self.result.checks_warning += 1
            print(f"  ⚠️  Publication manuscript not found")
            return

        with open(pub_path, 'r') as f:
            content = f.read()

        # Check word count (target: ~10,000 words)
        word_count = len(content.split())

        # Check for required sections
        required_sections = [
            "Abstract", "Introduction", "Methodology",
            "Findings", "Discussion", "Conclusion", "References"
        ]
        missing_sections = [s for s in required_sections if s not in content]

        if missing_sections:
            self.result.publication_issues = missing_sections
            self.result.checks_warning += 1
            print(f"  ⚠️  Missing sections: {', '.join(missing_sections)}")
        else:
            self.result.checks_passed += 1
            print(f"  ✅ All required sections present")

        if 9000 <= word_count <= 11000:
            self.result.checks_passed += 1
            print(f"  ✅ Word count: {word_count:,} (target range)")
        else:
            self.result.checks_warning += 1
            print(f"  ⚠️  Word count: {word_count:,} (target: 9,000-11,000)")

    def check_quarterly_update_schedule(self):
        """Check if quarterly update is due."""
        print("\n📆 Checking Quarterly Update Schedule...")

        # Determine current quarter
        now = datetime.now()
        quarter = (now.month - 1) // 3 + 1
        quarter_str = f"{now.year}-Q{quarter}"

        # Quarterly update months: January (Q4 previous year), April (Q1), July (Q2), October (Q3)
        update_months = [1, 4, 7, 10]
        current_month = now.month

        # Check if we're in update month
        is_update_month = current_month in update_months

        # Check if update file exists
        updates_dir = self.repo_path / "vendor-landscape" / "quarterly-updates"
        if updates_dir.exists():
            update_file = updates_dir / f"{quarter_str}-update.md"
            update_exists = update_file.exists()
        else:
            update_exists = False

        self.result.quarterly_update_status = {
            "current_quarter": quarter_str,
            "is_update_month": is_update_month,
            "update_exists": update_exists,
            "days_into_quarter": ((now.month - 1) % 3) * 30 + now.day
        }

        if is_update_month and not update_exists:
            self.result.checks_warning += 1
            print(f"  ⚠️  Quarterly update due for {quarter_str} (not found)")
        elif update_exists:
            self.result.checks_passed += 1
            print(f"  ✅ Quarterly update {quarter_str} complete")
        else:
            self.result.checks_passed += 1
            # Find next update month
            next_update = None
            for month in update_months:
                if month > current_month:
                    next_update = month
                    break
            if next_update is None:
                next_update = update_months[0]  # Next year's first update
            print(f"  ✅ Not in update month (next: Month {next_update})")

    def check_vendor_landscape_status(self):
        """Check vendor landscape integration status."""
        print("\n🏢 Checking Vendor Landscape Status...")

        vendor_db = self.repo_path / "vendor-landscape" / "vendor-database.json"

        if vendor_db.exists():
            with open(vendor_db, 'r') as f:
                try:
                    data = json.load(f)
                    vendor_count = len(data.get("vendors", []))
                    self.result.checks_passed += 1
                    print(f"  ✅ Vendor database exists ({vendor_count} vendors)")
                except json.JSONDecodeError:
                    self.result.checks_failed += 1
                    print(f"  ❌ Vendor database JSON invalid")
        else:
            self.result.checks_warning += 1
            print(f"  ⚠️  Vendor database not yet created (integration pending)")

    def calculate_overall_status(self):
        """Calculate overall health status."""
        # A confirmed-dead link or a missing core file is critical. Anything that needs
        # attention — a stale corpus, links we couldn't reach — is a warning. The old
        # ">3 warnings" gate is what let real degradation keep reading as "healthy"; a
        # dashboard that can't go red is worse than no dashboard.
        if self.result.checks_failed > 0:
            self.result.status = "critical"
        elif self.result.checks_warning > 0 or self.result.unreachable_links:
            self.result.status = "warning"
        else:
            self.result.status = "healthy"

    def generate_report(self, output_path: Path) -> str:
        """Generate markdown health report."""
        report = f"""# Literature Review - Weekly Health Check

**Date**: {datetime.fromisoformat(self.result.timestamp).strftime('%Y-%m-%d %H:%M:%S')}
**Status**: {self.result.status.upper()} {"🟢" if self.result.status == "healthy" else "🟡" if self.result.status == "warning" else "🔴"}

---

## Summary

| Metric | Value |
|--------|-------|
| ✅ Checks Passed | {self.result.checks_passed} |
| ⚠️ Checks Warning | {self.result.checks_warning} |
| ❌ Checks Failed | {self.result.checks_failed} |
| 📚 Total Sources | {self.result.total_sources} |
| 📅 Last Commit | {self.result.last_commit_date} ({self.result.days_since_commit} days ago) |
| 📝 Uncommitted Changes | {self.result.uncommitted_changes} |

---

## Issues Found

### Broken Links ({len(self.result.broken_links)})

"""
        if self.result.broken_links:
            for link in self.result.broken_links:
                report += f"- ❌ {link}\n"
        else:
            report += "_No broken links detected_\n"

        report += f"""
### Unreachable Links — inconclusive ({len(self.result.unreachable_links)})

_Could not be reached from the run host (restricted egress, DNS, or timeout). Not counted as broken — re-check from a networked host before treating as dead._

"""
        if self.result.unreachable_links:
            for link in self.result.unreachable_links:
                report += f"- ⚠️ {link}\n"
        else:
            report += "_All sampled links reachable_\n"

        report += f"""
### Outdated Evidence ({len(self.result.outdated_evidence)})

"""
        if self.result.outdated_evidence:
            for evidence in self.result.outdated_evidence[:10]:  # Limit to 10
                report += f"- ⚠️ {evidence}\n"
        else:
            report += "_All evidence sources recent_\n"

        report += f"""
### Publication Issues ({len(self.result.publication_issues)})

"""
        if self.result.publication_issues:
            for issue in self.result.publication_issues:
                report += f"- ⚠️ Missing section: {issue}\n"
        else:
            report += "_Publication manuscript complete_\n"

        report += f"""
---

## Quarterly Update Status

- **Current Quarter**: {self.result.quarterly_update_status.get('current_quarter', 'Unknown')}
- **Update Month**: {"Yes" if self.result.quarterly_update_status.get('is_update_month') else "No"}
- **Update Exists**: {"Yes ✅" if self.result.quarterly_update_status.get('update_exists') else "No ⚠️"}
- **Days Into Quarter**: {self.result.quarterly_update_status.get('days_into_quarter', 0)}

---

## Recommendations

"""
        # Generate actionable recommendations
        if self.result.days_since_commit > 30:
            report += "- 📝 **Action**: Review and commit recent work (stale repository)\n"

        if len(self.result.broken_links) > 0:
            report += "- 🔗 **Action**: Fix broken bibliography links\n"

        if len(self.result.outdated_evidence) > self.result.total_sources * 0.2:
            report += "- 📅 **Action**: Update evidence sources (>20% outdated)\n"

        if self.result.publication_issues:
            report += f"- 📝 **Action**: Complete publication manuscript (missing: {', '.join(self.result.publication_issues)})\n"

        if self.result.quarterly_update_status.get('is_update_month') and not self.result.quarterly_update_status.get('update_exists'):
            report += f"- 📆 **Action**: Create quarterly update for {self.result.quarterly_update_status.get('current_quarter')}\n"

        if not any([self.result.days_since_commit > 30, self.result.broken_links, self.result.publication_issues]):
            report += "_No critical actions needed - repository healthy! 🎉_\n"

        report += f"""
---

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Script**: `scripts/weekly_health_check.py`
"""

        # Write report
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w') as f:
            f.write(report)

        return report


def main():
    """Run weekly health check."""
    checker = LiteratureReviewHealthCheck()
    result = checker.run_all_checks()

    # Generate report
    report_dir = Path("~/weekly-review-reports").expanduser()
    report_path = report_dir / f"{datetime.now().strftime('%Y-%m-%d')}-literature-review-health.md"

    report_content = checker.generate_report(report_path)

    print(f"\n📊 Health Check Complete!")
    print(f"📄 Report: {report_path}")
    print(f"🏥 Status: {result.status.upper()}")

    # Return exit code based on status
    if result.status == "critical":
        return 1
    elif result.status == "warning":
        return 0  # Don't fail on warnings
    else:
        return 0


if __name__ == "__main__":
    exit(main())
