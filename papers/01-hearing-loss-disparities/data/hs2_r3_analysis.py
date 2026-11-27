#!/usr/bin/env python3
"""H-S2 / R3 analysis for Paper 01 (H90.3 vs RDW base population, UMMC Cohort Explorer).

Computes:
  1. Crude ever-diagnosed H90.3 prevalence, Black vs White, in the unfiltered RDW
     base population (Wald RD, Katz RR, Woolf OR, Pearson chi-square).
  2. H90.3 cohort race shares vs RDW base race shares (two-proportion z / Pearson
     chi-square on the Black share, and on the White share, separately).

Counts are Cohort Explorer header Patients totals (Jake Harthcock, 2026-11-27
screenshots). R3 used no diagnosis or other filters; data window 1/1/2013–9/30/2026.
H90.3 counts are the previously recorded R0/R1 unique-patient totals.

The displayed pie-chart Unknown 6.04% and Other 2.73% are encounter shares of the
unfiltered RDW and are NOT converted to patient counts. Other/unknown patients
are reported as one combined remainder: RDW total minus Black minus White.

Caveats:
  - Prevalence is ever-diagnosed at UMMC within the data window, not community
    incidence or point prevalence.
  - The Black vs White prevalence comparison is crude (not age-adjusted). No
    age-by-race base-population counts were pulled; the RDW age structure may
    differ by race. Age-stratified base counts are a suggested future pull.
  - Cohort vs base share comparisons are likewise unadjusted for age.

All cells used below are far above 11 (no suppression).

Requires: Python 3, numpy, scipy.
"""

from __future__ import annotations

import math
from pathlib import Path

from scipy.stats import chi2, norm

Z95 = 1.959963984540054

# R3: unfiltered RDW (no diagnosis), 2026-11-27 screenshots
RDW_ALL = 1_658_574
RDW_ENC = 73_271_189
RDW_BLACK = 684_322
RDW_BLACK_ENC = 39_081_291
RDW_WHITE = 699_367
RDW_WHITE_ENC = 30_228_243

# R0/R1: H90.3 unique-patient totals (already recorded)
H903 = 15_612
H903_ENC = 4_244_868
H903_BLACK = 6_176
H903_WHITE = 8_597
H903_OTHER = H903 - H903_BLACK - H903_WHITE  # 839


def katz_rr(a, n1, c, n0):
    rr = (a / n1) / (c / n0)
    se = math.sqrt(1 / a - 1 / n1 + 1 / c - 1 / n0)
    return rr, math.exp(math.log(rr) - Z95 * se), math.exp(math.log(rr) + Z95 * se), se


def wald_rd(a, n1, c, n0):
    p1, p0 = a / n1, c / n0
    rd = p1 - p0
    se = math.sqrt(p1 * (1 - p1) / n1 + p0 * (1 - p0) / n0)
    return rd, rd - Z95 * se, rd + Z95 * se, se


def woolf_or(a, n1, c, n0):
    b, d = n1 - a, n0 - c
    or_ = (a * d) / (b * c)
    se = math.sqrt(1 / a + 1 / b + 1 / c + 1 / d)
    return or_, math.exp(math.log(or_) - Z95 * se), math.exp(math.log(or_) + Z95 * se)


def pearson_chi2(a, n1, c, n0):
    b, d = n1 - a, n0 - c
    N = n1 + n0
    chi = N * (a * d - b * c) ** 2 / (n1 * n0 * (a + c) * (b + d))
    return chi, float(chi2.sf(chi, 1))


def two_prop_z(x1, n1, x0, n0):
    """Unpooled Wald two-proportion z for p1 - p0 (same as Wald RD / SE)."""
    p1, p0 = x1 / n1, x0 / n0
    rd = p1 - p0
    se = math.sqrt(p1 * (1 - p1) / n1 + p0 * (1 - p0) / n0)
    z = rd / se
    p = 2 * float(norm.sf(abs(z)))
    return rd, rd - Z95 * se, rd + Z95 * se, z, p


def fmt_pct_count(a, n, decimals=2):
    return f"{a:,}/{n:,} ({100 * a / n:.{decimals}f}%)"


def fmt_rr(rr, lo, hi):
    return f"{rr:.3f} ({lo:.3f}–{hi:.3f})"


def fmt_rd_pp(rd, lo, hi):
    return f"{100 * rd:.2f} ({100 * lo:.2f} to {100 * hi:.2f})"


def fmt_rd_pp3(rd, lo, hi):
    # prevalence is ~1%, two decimals in pp is 0.01 pp; use three for the small RD
    return f"{100 * rd:.3f} ({100 * lo:.3f} to {100 * hi:.3f})"


def main():
    rdw_other = RDW_ALL - RDW_BLACK - RDW_WHITE
    # displayed percentages (verify)
    black_share = RDW_BLACK / RDW_ALL
    white_share = RDW_WHITE / RDW_ALL
    assert abs(black_share - 0.4126) < 5e-5
    assert abs(white_share - 0.4217) < 5e-5
    # R0 % of RDW checks
    assert abs(H903 / RDW_ALL - 0.0094) < 5e-5  # 0.94%
    assert abs(H903_BLACK / RDW_ALL - 0.0037) < 5e-5  # 0.37%
    assert abs(H903_WHITE / RDW_ALL - 0.0052) < 5e-5  # 0.52%
    assert abs(H903_ENC / RDW_ENC - 0.0579) < 5e-5  # 5.79%

    # 1. Prevalence Black vs White
    a, n1, c, n0 = H903_BLACK, RDW_BLACK, H903_WHITE, RDW_WHITE
    rd, rdlo, rdhi, _ = wald_rd(a, n1, c, n0)
    rr, rrlo, rrhi, _ = katz_rr(a, n1, c, n0)
    or_, orlo, orhi = woolf_or(a, n1, c, n0)
    chi, pchi = pearson_chi2(a, n1, c, n0)

    # overall prevalence
    prev_all = H903 / RDW_ALL

    # 2. Cohort share vs base share
    # Black
    b_rd, b_lo, b_hi, b_z, b_p = two_prop_z(H903_BLACK, H903, RDW_BLACK, RDW_ALL)
    b_chi, b_pchi = pearson_chi2(H903_BLACK, H903, RDW_BLACK, RDW_ALL)
    # White
    w_rd, w_lo, w_hi, w_z, w_p = two_prop_z(H903_WHITE, H903, RDW_WHITE, RDW_ALL)
    w_chi, w_pchi = pearson_chi2(H903_WHITE, H903, RDW_WHITE, RDW_ALL)
    # Other/unknown combined
    o_rd, o_lo, o_hi, o_z, o_p = two_prop_z(H903_OTHER, H903, rdw_other, RDW_ALL)
    o_chi, o_pchi = pearson_chi2(H903_OTHER, H903, rdw_other, RDW_ALL)

    # RR of being in the H90.3 cohort: Black vs White among base (same as prevalence RR)
    # Also ratio of shares: (cohort Black share) / (base Black share)
    share_ratio_b = (H903_BLACK / H903) / (RDW_BLACK / RDW_ALL)
    share_ratio_w = (H903_WHITE / H903) / (RDW_WHITE / RDW_ALL)

    lines = []
    a_ = lines.append
    a_("# H-S2 / R3 results — H90.3 vs RDW base population, Black vs White")
    a_("")
    a_("Computed by `hs2_r3_analysis.py`. Counts are Cohort Explorer header Patients")
    a_("totals from Jake Harthcock screenshots, 2026-11-27 (R3) and 2026-11-26 (R0/R1).")
    a_("R3 used no diagnosis or other filters. Data window: encounters 1/1/2013–9/30/2026.")
    a_("")
    a_("The unfiltered pie-chart values Unknown 6.04% and Other 2.73% are encounter")
    a_("shares and are **not** converted to patient counts.")
    a_("")
    a_("## R3 — unfiltered RDW base")
    a_("")
    a_(f"- All patients = **{RDW_ALL:,}**; Encounters = **{RDW_ENC:,}**.")
    a_(f"- Black or African American: Patients = **{RDW_BLACK:,}** ({100*black_share:.2f}% of {RDW_ALL:,}); Encounters = **{RDW_BLACK_ENC:,}**.")
    a_(f"- White or Caucasian: Patients = **{RDW_WHITE:,}** ({100*white_share:.2f}% of {RDW_ALL:,}); Encounters = **{RDW_WHITE_ENC:,}**.")
    a_(f"- Other/unknown combined: Patients = **{rdw_other:,}** ({100*rdw_other/RDW_ALL:.2f}% of {RDW_ALL:,}), computed as {RDW_ALL:,} − {RDW_BLACK:,} − {RDW_WHITE:,}. Reported as one combined row only.")
    a_("")
    a_("Consistency with previously displayed “% of RDW” figures (not back-calculated")
    a_("at the time; now confirmed):")
    a_(f"- H90.3 {H903:,} / {RDW_ALL:,} = {100*prev_all:.2f}% (displayed 0.94%).")
    a_(f"- H90.3 Black {H903_BLACK:,} / {RDW_ALL:,} = {100*H903_BLACK/RDW_ALL:.2f}% (displayed 0.37%).")
    a_(f"- H90.3 White {H903_WHITE:,} / {RDW_ALL:,} = {100*H903_WHITE/RDW_ALL:.2f}% (displayed 0.52%).")
    a_(f"- H90.3 encounters {H903_ENC:,} / {RDW_ENC:,} = {100*H903_ENC/RDW_ENC:.2f}% (displayed 5.79%).")
    a_("")
    a_("All cells ≥11 (no suppression).")
    a_("")
    a_("## Crude ever-diagnosed H90.3 prevalence, Black vs White")
    a_("")
    a_("Prevalence is ever-diagnosed at UMMC within the data window, not community")
    a_("incidence or point prevalence. This comparison is **crude** (not age-adjusted).")
    a_("No age-by-race RDW base counts were pulled; the base age structure may differ")
    a_("by race. Age-stratified base counts are a suggested future pull.")
    a_("")
    a_(f"- Black: {fmt_pct_count(H903_BLACK, RDW_BLACK, 3)}")
    a_(f"- White: {fmt_pct_count(H903_WHITE, RDW_WHITE, 3)}")
    a_(f"- Overall: {fmt_pct_count(H903, RDW_ALL, 2)}")
    a_(f"- RD (Black − White), percentage points: **{fmt_rd_pp3(rd, rdlo, rdhi)}**")
    a_(f"- RR (Black vs White): **{fmt_rr(rr, rrlo, rrhi)}** (Katz 95% CI)")
    a_(f"- OR: **{fmt_rr(or_, orlo, orhi)}** (Woolf 95% CI)")
    a_(f"- Pearson χ²(1) = **{chi:.2f}**, p = **{pchi:.3g}**")
    a_("")
    a_("## H90.3 cohort race share vs RDW base share")
    a_("")
    a_("Likewise unadjusted for age. Other/unknown is a combined remainder in both the")
    a_("cohort and the base (not further split).")
    a_("")
    a_("| Group | H90.3 cohort | RDW base | Difference, pp (Wald 95% CI) | Pearson χ², p |")
    a_("|---|---|---|---|---|")
    a_(f"| Black | {fmt_pct_count(H903_BLACK, H903, 1)} | {fmt_pct_count(RDW_BLACK, RDW_ALL, 2)} | {fmt_rd_pp(b_rd, b_lo, b_hi)} | {b_chi:.2f}, {b_pchi:.3g} |")
    a_(f"| White | {fmt_pct_count(H903_WHITE, H903, 1)} | {fmt_pct_count(RDW_WHITE, RDW_ALL, 2)} | {fmt_rd_pp(w_rd, w_lo, w_hi)} | {w_chi:.2f}, {w_pchi:.3g} |")
    a_(f"| Other/unknown | {fmt_pct_count(H903_OTHER, H903, 1)} | {fmt_pct_count(rdw_other, RDW_ALL, 2)} | {fmt_rd_pp(o_rd, o_lo, o_hi)} | {o_chi:.2f}, {o_pchi:.3g} |")
    a_("")
    a_(f"Cohort Black share / base Black share = {share_ratio_b:.3f}.")
    a_(f"Cohort White share / base White share = {share_ratio_w:.3f}.")
    a_("")
    a_("The White over-representation in the cohort, and the Black under-representation,")
    a_("are partly the counterpart of a much smaller other/unknown share in the H90.3")
    a_("cohort than in the RDW base. The prevalence contrast (section above) compares")
    a_("Black and White denominators directly and does not depend on the other/unknown share.")
    a_("")
    a_("## Manuscript rounding")
    a_("")
    a_("Prevalence percentages to two or three decimals (three when the contrast is")
    a_("sub-percentage-point); RR and CI to three decimals; RD to two decimals in")
    a_("percentage points for share contrasts and three for prevalence contrasts;")
    a_("χ² to two decimals.")
    a_("")

    text = "\n".join(lines) + "\n"
    out = Path(__file__).resolve().with_name("hs2_r3_results.md")
    out.write_text(text)
    print(text)
    print(f"Wrote {out}")
    # also print raw for easy copy
    print("RAW")
    print("prev_b", a / n1, "prev_w", c / n0)
    print("rr", rr, rrlo, rrhi, "rd", rd, rdlo, rdhi, "chi", chi, pchi, "or", or_, orlo, orhi)
    print("black share rd", b_rd, b_lo, b_hi, b_chi, b_pchi)
    print("white share rd", w_rd, w_lo, w_hi, w_chi, w_pchi)
    print("other share rd", o_rd, o_lo, o_hi, o_chi, o_pchi)
    print("rdw_other", rdw_other)


if __name__ == "__main__":
    main()
