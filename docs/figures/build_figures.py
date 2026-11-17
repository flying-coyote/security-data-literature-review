#!/usr/bin/env python3
"""Generate the two reader figures in docs/figures/ as SVG.

Every number drawn here is a named constant below, and its file:line source is
tabulated once, in docs/figures/README.md, so that table is the one place to
keep current. Render to PNG with sharp (see README.md, "Rebuilding").
Palette: SDW Diagram standard (Harbor Haze).
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent
W = 1080
FONT = '"DM Sans Variable","DM Sans",Arial,"Liberation Sans",sans-serif'
MONO = '"JetBrains Mono Variable","JetBrains Mono","DejaVu Sans Mono",monospace'

# Harbor Haze
DEEP, HEAD, DARK, ANCHOR = "#36608f", "#2c4f74", "#243f5b", "#5c8dc5"
TINT, TINT2, ONDARK = "#eef3f9", "#87aacf", "#dbe6f2"
MUTED, RULE, SUBTLE = "#5b6878", "#e2e6ea", "#f4f6f8"
AZURE, AZURE_INK = "#1f8fe0", "#0f5f9e"

# ---- numbers (source: docs/figures/README.md, "Review method" table) ------
N_IDENT, N_OPENALEX, N_DBLP = 400, 354, 46
N_DUP = 5
N_SCREENED, N_EXCL, N_INCL = 395, 355, 40
N_OVERLAP = 0
N_REFUSED, N_PRED, N_NOTPR = 14, 8, 3
N_UNREAD, N_REFUTED = 1, 2
N_CITABLE = 26
N_SECOND_FLAG, N_SECOND_ADMIT = 11, 1
N_FOOTNOTES = 283


def text(x, y, s, size=28, weight=400, fill=DARK, anchor="start", family=FONT):
    return (f'<text x="{x}" y="{y}" font-family=\'{family}\' font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{escape(s)}</text>')


def lines(x, y, rows, size=28, gap=1.25, **kw):
    out = []
    for i, r in enumerate(rows):
        out.append(text(x, y + i * size * gap, r, size=size, **kw))
    return "\n".join(out)


def rect(x, y, w, h, fill=SUBTLE, stroke=RULE, sw=2, rx=12, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"{d}/>')


def arrow(x1, y1, x2, y2, color=MUTED, sw=4):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" '
            f'stroke-width="{sw}" marker-end="url(#ah)"/>')


def svg(h, title, desc, body, slug):
    defs = (f'<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" '
            f'markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" '
            f'fill="{MUTED}"/></marker></defs>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" '
            f'height="{h}" role="img" aria-labelledby="{slug}-t {slug}-d">\n'
            f'<title id="{slug}-t">{escape(title)}</title>\n<desc id="{slug}-d">{escape(desc)}</desc>\n'
            f'{defs}\n<rect width="{W}" height="{h}" fill="#ffffff"/>\n{body}\n</svg>\n')


# ---- figure 1: review method ----------------------------------------------
def dashed_arrow(x1, y1, x2, y2, color=MUTED, sw=3):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" '
            f'stroke-width="{sw}" stroke-dasharray="8 6" marker-end="url(#ah)"/>')


def fig_method():
    b = []
    b.append(lines(48, 70, ["Two routes into the corpus, and the 40", "database finds met an appraisal gate"],
                   size=42, weight=700, fill=HEAD))
    b.append(text(48, 182, "Method of this review; database search run 2026-07-13", size=26, fill=MUTED))

    # arm headers
    LX, LW, RX, RW = 48, 372, 452, 580
    b.append(text(LX, 250, "CURATION ARM", size=24, weight=700, fill=MUTED))
    b.append(text(RX, 250, "DATABASE ARM", size=24, weight=700, fill=MUTED))

    # curation column, sized to its content
    CB = 750
    b.append(rect(LX, 268, LW, CB - 268, fill=TINT, stroke=TINT2))
    b.append(lines(LX + 24, 318, ["Built by reading,", "2025 to 2026"], size=30, weight=700, fill=DARK))
    b.append(lines(LX + 24, 410, [f"Started from {N_FOOTNOTES}", "footnotes in a 2024", "practitioner manuscript"],
                   size=28, fill=DARK))
    b.append(lines(LX + 24, 530, ["Then vendor and", "project docs,", "standards, analyst", "reports, talks"],
                   size=28, fill=DARK))
    b.append(lines(LX + 24, 690, ["Mostly grey literature", "a database cannot index"], size=24, fill=MUTED))

    # database column stages
    y = 268
    stages = [
        (f"{N_IDENT} records identified", f"OpenAlex {N_OPENALEX}, dblp {N_DBLP}, run 2026-07-13"),
        (f"{N_SCREENED} screened", f"after {N_DUP} duplicates removed"),
        (f"{N_INCL} included", f"{N_EXCL} excluded; {N_OVERLAP} of {N_INCL} already in corpus"),
    ]
    for i, (a, s) in enumerate(stages):
        b.append(rect(RX, y, RW, 110, fill=TINT, stroke=TINT2))
        b.append(text(RX + 24, y + 48, a, size=32, weight=700, fill=DARK))
        b.append(text(RX + 24, y + 88, s, size=26, fill=MUTED))
        if i < len(stages) - 1:
            b.append(arrow(RX + RW / 2, y + 110, RX + RW / 2, y + 140))
        y += 150
    INC_BOTTOM = y - 40  # bottom edge of the "40 included" box

    GY = 880
    # the 40 go straight to the gate
    AX = RX + 60
    b.append(arrow(AX, INC_BOTTOM, AX, GY - 2))
    # side annotation: the second screen of the exclusions adds one record through the same gate
    NX, NY, NW, NH = RX + 120, 706, RW - 120, 130
    b.append(rect(NX, NY, NW, NH, fill="#ffffff", stroke=TINT2, dash="8 6"))
    b.append(lines(NX + 20, NY + 38, [f"+{N_SECOND_ADMIT} via second screen of",
                                      f"the {N_EXCL} exclusions",
                                      f"({N_SECOND_FLAG} flagged, {N_SECOND_ADMIT} admitted)"], size=26, fill=MUTED))
    b.append(dashed_arrow(NX + NW / 2, NY + NH, NX + NW / 2, GY - 2))

    # appraisal gate (focal): azure band for the headline, light inset for the breakdown
    GH = 308
    b.append(rect(RX, GY, RW, GH, fill=AZURE, stroke=AZURE_INK, sw=3))
    b.append(text(RX + 24, GY + 50, "Appraisal gate", size=34, weight=700, fill="#ffffff"))
    b.append(text(RX + 24, GY + 92, f"{N_REFUSED} of {N_INCL} refused:", size=30, weight=700, fill="#ffffff"))
    b.append(rect(RX + 16, GY + 116, RW - 32, 176, fill=TINT, stroke=TINT, rx=8))
    b.append(lines(RX + 36, GY + 154, [f"{N_PRED} predatory or compromised venue",
                                       f"{N_NOTPR} not peer-reviewed, {N_UNREAD} unreadable",
                                       f"{N_REFUTED} refuted by an independent",
                                       "verification pass"], size=28, gap=1.3, fill=DARK))

    # merge
    MY = GY + GH + 80
    b.append(arrow(LX + LW / 2, CB, LX + LW / 2, MY - 4))
    b.append(arrow(RX + RW / 2, GY + GH, RX + RW / 2, MY - 4))
    b.append(text(RX + RW / 2 + 14, GY + GH + 48, f"{N_CITABLE} admitted", size=26, weight=700, fill=DARK))

    merged = [
        ("Each source tiered A to D", ["Level A is peer review and official standards only"], None),
        ("Rule: carried numbers checked at the primary",
         ["Verdict per number in methods/verification-2026-11/ledger.json;",
          "paywalled numbers are marked unverifiable"], "10 8"),
        ("MASTER-BIBLIOGRAPHY.md", ["Live counts derived by scripts/count_reconcile.py"], None),
    ]
    y = MY
    for i, (a, subs, dash) in enumerate(merged):
        h = 72 + 36 * len(subs)
        b.append(rect(48, y, W - 96, h, fill=SUBTLE if not dash else "#ffffff", stroke=RULE if not dash else MUTED,
                      dash=dash))
        fam = MONO if a.endswith(".md") else FONT
        b.append(text(72, y + 48, a, size=32, weight=700, fill=DARK, family=fam))
        b.append(lines(72, y + 88, subs, size=26, gap=1.38, fill=MUTED))
        if i < len(merged) - 1:
            b.append(arrow(W / 2, y + h, W / 2, y + h + 30))
        y += h + 40
    H = y - 10
    title = "Two routes into the corpus, and the 40 database finds met an appraisal gate"
    desc = (f"Flow diagram. The curation arm built most of the corpus by reading, starting from {N_FOOTNOTES} "
            f"footnotes in a 2024 practitioner manuscript and continuing with vendor and project documentation, "
            f"standards, analyst reports and talks. The database arm searched OpenAlex and dblp on 2026-07-13: "
            f"{N_IDENT} records identified, {N_DUP} duplicates removed, {N_SCREENED} screened, {N_EXCL} excluded "
            f"and {N_INCL} included, none of which was already in the corpus. The {N_INCL} went to an appraisal gate, "
            f"which refused {N_REFUSED} ({N_PRED} predatory or compromised venues, {N_NOTPR} not peer-reviewed, "
            f"{N_UNREAD} unreadable, {N_REFUTED} refuted by an independent verification pass) and admitted {N_CITABLE}. "
            f"Separately, a second screen of all {N_EXCL} exclusions flagged {N_SECOND_FLAG}, and {N_SECOND_ADMIT} of "
            f"them was later admitted through the same gate. Both arms then pass through tiering A to D before "
            f"entering MASTER-BIBLIOGRAPHY.md, whose live counts are derived by scripts/count_reconcile.py. A dashed "
            f"box marks the standing rule that carried numbers are checked at the primary, with a verdict per number "
            f"in methods/verification-2026-11/ledger.json and paywalled numbers marked unverifiable.")
    return svg(H, title, desc, "\n".join(b), "fm")


# ---- figure 2: evidence-tier ladder ---------------------------------------
def fig_tiers():
    b = []
    b.append(lines(48, 70, ["Level A is peer review and standards;", "production evidence, however good, is B"],
                   size=42, weight=700, fill=HEAD))
    b.append(text(48, 182, "Evidence levels, METHODOLOGY.md section 3.1", size=26, fill=MUTED))
    tiers = [
        ("A", "Peer review and standards", [
            "Peer-reviewed work at a named venue",
            "NIST, ISO/IEC, IETF RFC, W3C, OASIS",
            "Formal specs (Iceberg table spec, OCSF schema)",
            "MITRE D3FEND, ATLAS: structure, not efficacy"], DEEP, "#ffffff"),
        ("B", "Practice and production", [
            "Deployments and case studies with real numbers",
            "Vendor engineering blogs, talks, trade books",
            "Analyst reports, expert interviews",
            "Advisories and official project docs",
            "Preprints with no named venue"], ANCHOR, "#ffffff"),
        ("C", "Unmeasured vendor material and talks", [
            "Vendor posts, product docs and talks",
            "with no production measurement behind them",
            "Kept with bias flagged; never carries",
            "a hypothesis on its own"], TINT2, DARK),
        ("D", "Marketing and speculation", [
            "Unverified claims, marketing, speculation",
            "Excluded from the review"], RULE, DARK),
    ]
    y = 220
    for i, (L, name, rows, badge, ink) in enumerate(tiers):
        h = 84 + 39 * len(rows)
        dash = "10 8" if L == "D" else None
        b.append(rect(48, y, W - 96, h, fill=SUBTLE if L != "D" else "#ffffff", stroke=RULE, dash=dash))
        b.append(rect(48, y, 120, h, fill=badge, stroke=badge, rx=12))
        b.append(text(108, y + h / 2 + 26, L, size=76, weight=700, fill=ink, anchor="middle"))
        b.append(text(196, y + 52, name, size=34, weight=700, fill=DARK))
        b.append(lines(196, y + 96, rows, size=29, gap=1.35, fill=DARK))
        y += h
        if L == "A":
            # focal boundary
            y += 14
            b.append(f'<rect x="48" y="{y}" width="{W - 96}" height="64" rx="10" fill="{AZURE}"/>')
            b.append(text(W / 2, y + 43, "The line: no production evidence above it",
                          size=30, weight=700, fill="#ffffff", anchor="middle"))
            y += 64 + 14
        else:
            y += 22
    H = y + 10
    title = "Level A is peer review and standards; production evidence, however good, is B"
    desc = ("Four stacked evidence levels. Level A: peer-reviewed work at a named venue; NIST, ISO/IEC, IETF RFC, "
            "W3C and OASIS standards; formal specifications such as the Iceberg table spec and the OCSF schema; "
            "and MITRE D3FEND and ATLAS, authoritative on structure but not on efficacy. A highlighted line "
            "below Level A marks that no production evidence sits above it. Level B: deployments and case studies "
            "with real numbers, vendor engineering blogs, talks, trade books, analyst reports, expert interviews, "
            "advisories, official project documentation and preprints with no named venue. Level C: vendor posts, "
            "product documentation and talks with no production measurement behind them, kept with bias flagged and never carrying a hypothesis alone. "
            "Level D: unverified claims, marketing and speculation, excluded from the review.")
    return svg(H, title, desc, "\n".join(b), "ft")


if __name__ == "__main__":
    for name, fn in [("review-method", fig_method), ("evidence-tiers", fig_tiers)]:
        (OUT / f"{name}.svg").write_text(fn(), encoding="utf-8")
        print("wrote", OUT / f"{name}.svg")
