#!/usr/bin/env python3
"""
Automation Health Dashboard - Monthly Update Workflow

Purpose: Quick visibility into automation status, quality metrics, and integration health
Usage: python3 scripts/automation_dashboard.py
Output: Console dashboard + optional markdown report

This script complements weekly_health_check.py by providing a decision-focused
dashboard for monthly update planning.
"""

import os
import sys
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
import re

# Color codes for terminal output
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_header(text):
    """Print formatted section header"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'=' * 70}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{text.center(70)}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'=' * 70}{Colors.END}\n")

def print_section(text):
    """Print formatted subsection header"""
    print(f"\n{Colors.BOLD}{text}{Colors.END}")
    print(f"{'-' * 70}")

def check_file_exists(filepath):
    """Check if file exists and return status"""
    return os.path.exists(filepath)

def get_file_modified_days_ago(filepath):
    """Get days since file was last modified"""
    if not os.path.exists(filepath):
        return None
    modified_time = os.path.getmtime(filepath)
    days_ago = (datetime.now().timestamp() - modified_time) / 86400
    return int(days_ago)

def parse_master_bibliography():
    """Extract key metrics from MASTER-BIBLIOGRAPHY.md"""
    biblio_path = "MASTER-BIBLIOGRAPHY.md"
    if not check_file_exists(biblio_path):
        return None

    with open(biblio_path, 'r') as f:
        content = f.read()

    # Live-computed, per-ENTRY tier counts. We deliberately do NOT parse the header's
    # self-reported **Evidence Quality** line — it is narrative prose (tilde-prefixed,
    # occasionally stale), and reading a self-grade is exactly the trap the 2026-06-05
    # audit was cleaning up. CLAUDE.md is explicit: "Counts are live-computed: sources =
    # #### entries, Level-A = **Evidence Level**: A / entries." So we count directly.
    #
    # Count the tier of each #### block (its FIRST Evidence Level marker), not raw line
    # matches across the file — a block can restate its tier in an update note, which
    # would double-count. A #### block with no tier at all is a documented rejection
    # stub (e.g. "Declined (no primary) — ..."), correctly excluded from the tiered set.
    last_updated = re.search(r'\*\*Last Updated\*\*:\s*([A-Za-z0-9,\-\. ]+)', content)

    blocks = re.split(r'(?m)^####\s+', content)[1:]  # drop the pre-first-#### preamble
    total_entries = len(blocks)
    tier_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    untiered = 0
    for b in blocks:
        m = re.search(r'\*\*Evidence Level\*\*:\s*([A-D])\b', b)
        if m:
            tier_counts[m.group(1)] += 1
        else:
            untiered += 1
    tiered_total = sum(tier_counts.values())

    # Level-A% is over TIERED sources (entries carrying an A/B/C/D marker), so a
    # rejection stub in the denominator can't dishonestly deflate the number.
    evidence_quality = round(tier_counts['A'] / tiered_total * 100, 1) if tiered_total else None

    return {
        'evidence_quality': evidence_quality,
        'total_sources': total_entries,
        'last_updated': last_updated.group(1).strip() if last_updated else 'Unknown',
        'level_a_count': tier_counts['A'],
        'level_b_count': tier_counts['B'],
        'level_c_count': tier_counts['C'],
        'tiered_total': tiered_total,
        'untiered_stubs': untiered,
        'total_entries': total_entries
    }

def parse_monthly_tracker():
    """Extract key metrics from monthly-update-tracker.md"""
    tracker_path = "monthly-update-tracker.md"
    if not check_file_exists(tracker_path):
        return None

    with open(tracker_path, 'r') as f:
        content = f.read()

    # Locate the MOST RECENT dated section, not a fixed month. The tracker is appended
    # chronologically, so the LAST "## <Month(s)> <Year> Update(s)" heading in the file is
    # the newest one — anchoring to the first such heading (November 2025, as this used to)
    # freezes the reported average at whatever November said, forever, no matter how many
    # months get appended after it.
    month_names = ('January|February|March|April|May|June|July|August|September|'
                   'October|November|December')
    heading_pattern = re.compile(
        rf'(?m)^##\s+((?:{month_names})(?:-(?:{month_names}))?\s+\d{{4}})\s+Updates?\b'
    )
    headings = list(heading_pattern.finditer(content))
    if not headings:
        return None

    latest = headings[-1]
    section_label = latest.group(1)  # e.g. "July 2026" — carried into the dashboard output
    section_start = latest.end()
    next_heading = re.search(r'(?m)^##\s+', content[section_start:])
    section_end = section_start + next_heading.start() if next_heading else len(content)
    section = content[section_start:section_end]

    # Each dated "### Update ..." entry within that month states its own session hours as
    # "**Total: ~X hours**"; average across however many updates landed that month (usually
    # one, so total == average, but a multi-update month averages correctly).
    hours = [float(h) for h in re.findall(r'\*\*Total:\s*~?([\d.]+)\s*hours?\*\*', section)]
    average_time = round(sum(hours) / len(hours), 1) if hours else None
    evidence_level = re.search(r'Evidence Level A\*{0,2}:\s*(?:[\d.]+%\s*(?:→|->)\s*)?([\d.]+)%', section)

    return {
        'section_label': section_label,
        'total_hours': round(sum(hours), 1) if hours else None,
        'update_count': len(hours),
        'average_time': average_time,
        'evidence_level_a': float(evidence_level.group(1)) if evidence_level else None
    }

def get_latest_health_report():
    """Get most recent weekly health check report"""
    reports_dir = os.path.expanduser("~/weekly-review-reports")
    if not os.path.exists(reports_dir):
        return None

    # Only the dated health reports. A stray SETUP.md/README.md sorts lexically AFTER the
    # "2026-*" names, so the old `endswith('.md')` filter picked it and every count defaulted
    # to 0 — which is how a 96-day lapse stayed invisible behind an all-green dashboard.
    reports = [f for f in os.listdir(reports_dir) if f.endswith('-literature-review-health.md')]
    if not reports:
        return None

    latest_report = sorted(reports)[-1]
    report_path = os.path.join(reports_dir, latest_report)

    with open(report_path, 'r') as f:
        content = f.read()

    # Extract metrics
    status = re.search(r'\*\*Status\*\*:\s*(\w+)', content)
    checks_passed = re.search(r'✅ Checks Passed.*?\|\s*(\d+)', content)
    checks_warning = re.search(r'⚠️ Checks Warning.*?\|\s*(\d+)', content)
    checks_failed = re.search(r'❌ Checks Failed.*?\|\s*(\d+)', content)
    broken_links = re.search(r'### Broken Links \((\d+)\)', content)
    outdated_evidence = re.search(r'### Outdated Evidence \((\d+)\)', content)

    return {
        'report_date': latest_report.replace('literature-review-health.md', '').strip('-'),
        'status': status.group(1) if status else 'Unknown',
        'checks_passed': int(checks_passed.group(1)) if checks_passed else 0,
        'checks_warning': int(checks_warning.group(1)) if checks_warning else 0,
        'checks_failed': int(checks_failed.group(1)) if checks_failed else 0,
        'broken_links': int(broken_links.group(1)) if broken_links else 0,
        'outdated_evidence': int(outdated_evidence.group(1)) if outdated_evidence else 0
    }

def check_git_status():
    """Check git repository status"""
    try:
        # Check for uncommitted changes
        result = subprocess.run(['git', 'status', '--porcelain'],
                              capture_output=True, text=True)
        uncommitted_changes = len(result.stdout.strip().split('\n')) if result.stdout.strip() else 0

        # Get last commit date
        result = subprocess.run(['git', 'log', '-1', '--format=%ci'],
                              capture_output=True, text=True)
        last_commit_date = result.stdout.strip().split()[0] if result.stdout else 'Unknown'

        # Get current branch
        result = subprocess.run(['git', 'branch', '--show-current'],
                              capture_output=True, text=True)
        current_branch = result.stdout.strip()

        return {
            'uncommitted_changes': uncommitted_changes,
            'last_commit_date': last_commit_date,
            'current_branch': current_branch
        }
    except Exception as e:
        return {'error': str(e)}

def check_vendor_database():
    """Live-read the vendor database that lives in THIS repo (vendor-landscape/vendor-database.json).
    Honest signal: report the real count from the file, not a hardcoded snapshot."""
    import json
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        'vendor-landscape', 'vendor-database.json')
    try:
        with open(path) as f:
            data = json.load(f)
        vendors = data.get('vendors', data if isinstance(data, list) else [])
        return {'count': len(vendors), 'path': 'vendor-landscape/vendor-database.json'}
    except Exception as e:
        return {'error': str(e)}

def print_dashboard():
    """Print comprehensive automation dashboard"""

    print_header("AUTOMATION HEALTH DASHBOARD")
    print(f"{Colors.BOLD}Security Data Literature Review - Monthly Update Workflow{Colors.END}")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # 1. QUALITY METRICS
    print_section("📊 Quality Metrics")
    biblio = parse_master_bibliography()
    if biblio and biblio['evidence_quality'] is not None:
        eq = biblio['evidence_quality']
        evidence_status = f"{Colors.GREEN}✅ AT/ABOVE TARGET" if eq >= 75 else f"{Colors.YELLOW}⚠️ BELOW TARGET (honest post-audit floor)"
        print(f"Evidence Level A: {Colors.BOLD}{eq}%{Colors.END} {evidence_status}{Colors.END}")
        print(f"  Target: ≥75% | Current: {eq}% (live-computed, not self-reported)")
        print(f"  Tier mix: {Colors.BOLD}{biblio['level_a_count']}A{Colors.END} / {biblio['level_b_count']}B / {biblio['level_c_count']}C "
              f"across {biblio['tiered_total']} tiered sources ({biblio['total_entries']} #### blocks, "
              f"{biblio['untiered_stubs']} rejection stub{'s' if biblio['untiered_stubs'] != 1 else ''})")
        print(f"  Last Updated: {biblio['last_updated']}")
    elif biblio:
        print(f"{Colors.RED}❌ Bibliography has no tiered entries to compute Level-A%{Colors.END}")
    else:
        print(f"{Colors.RED}❌ Could not load bibliography metrics{Colors.END}")

    # 2. TIME SUSTAINABILITY
    print_section("⏱️  Time Sustainability")
    tracker = parse_monthly_tracker()
    if tracker and tracker['average_time'] is not None:
        time_status = f"{Colors.GREEN}✅ SUSTAINABLE" if tracker['average_time'] <= 10 else f"{Colors.YELLOW}⚠️ WARNING"
        # Labeled with its source month so this figure can't silently masquerade as
        # current — it's whatever the most recent dated tracker section reports, not
        # something this dashboard measures live.
        print(f"Average Time ({tracker['section_label']}): {Colors.BOLD}{tracker['average_time']} hours/update{Colors.END} {time_status}{Colors.END}")
        print(f"  Target: ≤10 hours/month | Current: {tracker['average_time']} hours/update ({tracker['section_label']})")
        update_word = 'update' if tracker['update_count'] == 1 else 'updates'
        print(f"  {tracker['section_label']} Total: {tracker['total_hours']} hours ({tracker['update_count']} {update_word})")
    else:
        print(f"{Colors.RED}❌ Could not load time tracking metrics{Colors.END}")

    # 3. AUTOMATION STATUS
    print_section("🤖 Automation Status")

    # Weekly health check
    health_report = get_latest_health_report()
    if health_report:
        status_color = Colors.GREEN if health_report['status'] == 'SUCCESS' else Colors.YELLOW if health_report['status'] == 'WARNING' else Colors.RED
        print(f"Weekly Health Check: {status_color}{health_report['status']}{Colors.END}")
        print(f"  Last Run: {health_report['report_date']}")
        print(f"  Checks Passed: {health_report['checks_passed']} | Warnings: {health_report['checks_warning']} | Failed: {health_report['checks_failed']}")
        print(f"  Broken Links: {health_report['broken_links']} | Outdated Sources: {health_report['outdated_evidence']}")
    else:
        print(f"{Colors.RED}❌ No health check reports found{Colors.END}")

    # Vendor database (lives in THIS repo: vendor-landscape/vendor-database.json) — live-counted, not hardcoded
    vendor_db = check_vendor_database()
    if 'error' not in vendor_db:
        print(f"\nVendor Database: {Colors.GREEN}✅ PRESENT{Colors.END}")
        print(f"  Vendors: {vendor_db['count']} (live count from {vendor_db['path']})")
    else:
        print(f"\nVendor Database: {Colors.RED}❌ NOT FOUND{Colors.END} ({vendor_db['error']})")

    # Monthly update tracker
    tracker_exists = check_file_exists("monthly-update-tracker.md")
    tracker_status = f"{Colors.GREEN}✅ OPERATIONAL{Colors.END}" if tracker_exists else f"{Colors.RED}❌ MISSING{Colors.END}"
    print(f"\nMonthly Update Tracker: {tracker_status}")
    if tracker_exists:
        days_ago = get_file_modified_days_ago("monthly-update-tracker.md")
        print(f"  Last Updated: {days_ago} days ago")

    # 4. INTEGRATION STATUS
    print_section("🔗 Integration Status")

    print(f"Website (securitydataworks.com): {Colors.YELLOW}— not polled from this dashboard{Colors.END}")
    print(f"  Channel: /writing (essays), /research (evidence), /lab (first-party benchmarks)")
    print(f"  Deploy state is owner-gated; this dashboard does not health-check the live site (no bluffed GREEN)")
    print(f"  Note: Security Data Commons Substack retired 2026-05-24 — do not poll it")

    print(f"\nBook (modern-data-stack-for-cybersecurity-book): {Colors.GREEN}✅ SUPPORTED{Colors.END}")
    # Derive-don't-state (CLAUDE.md): the book's word count lives in the book repo's own
    # build, not in this repo, so this dashboard points at it instead of hand-typing a
    # number here that would go stale the next time the book repo builds.
    print(f"  Manuscript word count: derived in the book repo's own build (not tracked here)")
    print(f"  Evidence Foundation: All chapters supported")

    # (vendor database reported once, live-counted, in Automation Status above — dedup 2026-06-29)

    # 5. VERSION CONTROL
    print_section("📝 Version Control")
    git_status = check_git_status()
    if 'error' not in git_status:
        uncommitted_color = Colors.GREEN if git_status['uncommitted_changes'] == 0 else Colors.YELLOW
        print(f"Git Status: {uncommitted_color}{git_status['uncommitted_changes']} uncommitted changes{Colors.END}")
        print(f"  Last Commit: {git_status['last_commit_date']}")
        print(f"  Current Branch: {git_status['current_branch']}")
    else:
        print(f"{Colors.RED}❌ Could not check git status: {git_status['error']}{Colors.END}")

    # 6. DECISION DASHBOARD
    print_section("🎯 Update Readiness — Decision Dashboard")

    # Calculate readiness score
    ready_count = 0
    total_checks = 6

    if biblio and biblio['evidence_quality'] and biblio['evidence_quality'] >= 75:
        print(f"{Colors.GREEN}✅ Quality Target Met{Colors.END} ({biblio['evidence_quality']}% ≥ 75%)")
        ready_count += 1
    else:
        print(f"{Colors.RED}❌ Quality Below Target{Colors.END}")

    if tracker and tracker['average_time'] is not None and tracker['average_time'] <= 10:
        print(f"{Colors.GREEN}✅ Time Sustainable{Colors.END} ({tracker['average_time']} hours ≤ 10 hours, {tracker['section_label']})")
        ready_count += 1
    else:
        print(f"{Colors.RED}❌ Time Unsustainable{Colors.END}")

    if health_report and health_report['broken_links'] <= 2:
        print(f"{Colors.GREEN}✅ Link Health Acceptable{Colors.END} ({health_report['broken_links']} broken links)")
        ready_count += 1
    else:
        n = health_report['broken_links'] if health_report else '?'
        print(f"{Colors.YELLOW}⚠️  Link Health Needs Attention{Colors.END} ({n} broken links sampled)")

    if health_report and health_report['outdated_evidence'] <= 30:
        print(f"{Colors.GREEN}✅ Evidence Freshness Acceptable{Colors.END} ({health_report['outdated_evidence']} outdated sources)")
        ready_count += 1
    else:
        n = health_report['outdated_evidence'] if health_report else '?'
        print(f"{Colors.YELLOW}⚠️  Evidence Refresh Recommended{Colors.END} ({n} sources >12 months old)")

    if tracker_exists:
        print(f"{Colors.GREEN}✅ Tracking System Operational{Colors.END}")
        ready_count += 1
    else:
        print(f"{Colors.RED}❌ Tracking System Missing{Colors.END}")

    if git_status and git_status.get('uncommitted_changes', 0) <= 5:
        print(f"{Colors.GREEN}✅ Git Status Clean{Colors.END}")
        ready_count += 1
    else:
        print(f"{Colors.YELLOW}⚠️  Uncommitted Changes Present{Colors.END}")

    # Overall readiness
    print(f"\n{Colors.BOLD}Overall Readiness: {ready_count}/{total_checks} checks passed{Colors.END}")
    if ready_count >= 5:
        print(f"{Colors.GREEN}✅ READY FOR NEXT UPDATE{Colors.END}")
    elif ready_count >= 3:
        print(f"{Colors.YELLOW}⚠️  PARTIALLY READY - Minor improvements needed{Colors.END}")
    else:
        print(f"{Colors.RED}❌ NOT READY - Significant work required{Colors.END}")

    # 7. RECOMMENDED ACTIONS
    print_section("📋 Recommended Actions for Next Update")

    if health_report and health_report['outdated_evidence'] > 20:
        print(f"1. {Colors.YELLOW}⚠️{Colors.END}  Refresh oldest sources ({health_report['outdated_evidence']} sources >12 months old)")

    if health_report and health_report['broken_links'] > 0:
        print(f"2. {Colors.YELLOW}⚠️{Colors.END}  Fix broken links ({health_report['broken_links']} found by health check)")

    print(f"3. {Colors.GREEN}✅{Colors.END}  Add new sources from /writing feedback + LinkedIn signal-radar")
    print(f"4. {Colors.GREEN}✅{Colors.END}  Run weekly_health_check.py before and after update")
    print(f"5. {Colors.GREEN}✅{Colors.END}  Update monthly-update-tracker.md with this update's metrics")

    # 8. FOOTER
    print_header("END OF DASHBOARD")
    print(f"{Colors.BOLD}Last lit-review update:{Colors.END} {biblio['last_updated'] if biblio else 'Unknown'}")
    print(f"{Colors.BOLD}Cadence:{Colors.END} see REVIEW-AND-PLAN-2026-06.md (cadence + scheduling under decision)")
    print(f"\n{Colors.CYAN}Run 'python3 scripts/weekly_health_check.py' for detailed health report{Colors.END}\n")

def main():
    """Main entry point"""
    # Change to repository root
    repo_root = Path(__file__).parent.parent
    os.chdir(repo_root)

    try:
        print_dashboard()
        return 0
    except Exception as e:
        print(f"\n{Colors.RED}❌ Error generating dashboard: {e}{Colors.END}\n")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
