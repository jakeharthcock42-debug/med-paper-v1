#!/usr/bin/env python3
"""H-S1 sex-stratified audiology analysis for Paper 01 (H90.3, UMMC Cohort Explorer).

Computes, for Black vs White within Female and within Male:
  per-stratum risk, Wald risk difference, Katz risk ratio, Woolf odds ratio,
  Pearson chi-square (uncorrected);
  Mantel-Haenszel risk ratio with Greenland-Robins (1985) 95% CI across sex;
  Cochran-Mantel-Haenszel chi-square; Breslow-Day and Tarone tests of
  odds-ratio homogeneity.

Also computes female vs male audiology within each race, and a race-adjusted
Mantel-Haenszel RR (female vs male).

Counts are Cohort Explorer header Patients totals (Jake Harthcock, 2026-11-27
screenshots), H90.3 cohort, no age filter. Clicked counts only; pie-chart
percentages are not used to back-calculate cells.

Male all-patients (no race selected) was not captured (duplicate screenshot)
and is recorded as [PENDING]; it is not required for H-S1 (the Black and White
male counts were captured). Do not back-calculate Male all from Female all
or from the earlier pie-chart sex percentages.

Female Black + White = 8,156 vs Female all = 8,562; the remainder 406 is
other/unknown and is not used in the Black vs White contrasts.

Consistency with R1/R4 unique-patient totals (no age filter, so sex strata
do not overlap):
  Female Black 3,788 + Male Black 2,388 = 6,176 (R1 Black)
  Female White 4,368 + Male White 4,229 = 8,597 (R1 White)
  Female Black Audiology 393 + Male Black Audiology 237 = 630 (R4 Black)
  Female White Audiology 532 + Male White Audiology 464 = 996 (R4 White)

All cells in these 2x2 tables are >= 11 (no suppression).

Requires: Python 3, numpy, scipy.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np
from scipy.stats import chi2, norm

Z95 = 1.959963984540054

# Sex-stratified Black vs White (clicked counts, no age filter)
# name, all_in_sex or None if pending, Black n, Black with Audiology, White n, White with Audiology
FEMALE_ALL = 8562
MALE_ALL = None  # [PENDING]; not captured; not required for H-S1
STRATA_SEX = [
    ("Female", FEMALE_ALL, 3788, 393, 4368, 532),
    ("Male", MALE_ALL, 2388, 237, 4229, 464),
]

# Female vs male within race (same cells, rearranged)
# name, Female n, Female with Audiology, Male n, Male with Audiology
STRATA_RACE = [
    ("Black", 3788, 393, 2388, 237),
    ("White", 4368, 532, 4229, 464),
]

UNIQUE_BLACK = 6176
UNIQUE_WHITE = 8597
UNIQUE_BLACK_AU = 630
UNIQUE_WHITE_AU = 996


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


def mh_rr_greenland_robins(rows):
    """MH risk ratio and Greenland-Robins (1985) variance of ln(RR_MH).

    rows: sequence of (a, n1, c, n0) = (exposed events, exposed n,
    unexposed events, unexposed n).
    """
    R = S = sum_PR = sum_QS = sum_PS_QR = 0.0
    for a, n1, c, n0 in rows:
        N = n1 + n0
        Ri = a * n0 / N
        Si = c * n1 / N
        Pi = (n1 - a) / N
        Qi = (n0 - c) / N
        R += Ri
        S += Si
        sum_PR += Pi * Ri
        sum_QS += Qi * Si
        sum_PS_QR += Pi * Si + Qi * Ri
    rr = R / S
    var = sum_PR / (R * R) + sum_QS / (S * S) + sum_PS_QR / (R * S)
    se = math.sqrt(var)
    lo = math.exp(math.log(rr) - Z95 * se)
    hi = math.exp(math.log(rr) + Z95 * se)
    z = math.log(rr) / se
    p_wald = 2 * float(norm.sf(abs(z)))
    return {"rr": rr, "lo": lo, "hi": hi, "se_log": se, "R": R, "S": S, "z": z, "p_wald": p_wald}


def cmh_chi2(rows, continuity=False):
    """Cochran-Mantel-Haenszel chi-square (1 df) for a 2x2xk set of tables."""
    num = den = 0.0
    for a, n1, c, n0 in rows:
        N = n1 + n0
        m1 = a + c
        E = n1 * m1 / N
        V = n1 * n0 * m1 * (N - m1) / (N * N * (N - 1))
        num += a - E
        den += V
    if continuity:
        chi = (abs(num) - 0.5) ** 2 / den
    else:
        chi = num ** 2 / den
    return chi, float(chi2.sf(chi, 1))


def _expected_a(n1, n0, m1, or_mh):
    """Expected exposed-event count under a common odds ratio (quadratic)."""
    N = n1 + n0
    if abs(or_mh - 1) < 1e-15:
        return n1 * m1 / N
    A = or_mh - 1
    B = -(or_mh * (n1 + m1) + (n0 - m1))
    C = or_mh * n1 * m1
    disc = B * B - 4 * A * C
    sqrt_d = math.sqrt(disc)
    r1 = (-B + sqrt_d) / (2 * A)
    r2 = (-B - sqrt_d) / (2 * A)
    lo, hi = max(0, m1 - n0), min(n1, m1)
    for r in (r1, r2):
        if lo - 1e-8 <= r <= hi + 1e-8:
            return r
    mid = (lo + hi) / 2
    return r1 if abs(r1 - mid) < abs(r2 - mid) else r2


def breslow_day_tarone(rows):
    """Breslow-Day and Tarone tests of odds-ratio homogeneity."""
    num = den = 0.0
    tables = []
    for a, n1, c, n0 in rows:
        N = n1 + n0
        b, d = n1 - a, n0 - c
        num += a * d / N
        den += b * c / N
        tables.append((a, n1, n0, a + c, N))
    or_mh = num / den
    bd = 0.0
    sum_diff = 0.0
    sum_v = 0.0
    for a, n1, n0, m1, N in tables:
        ea = _expected_a(n1, n0, m1, or_mh)
        eb, ec = n1 - ea, m1 - ea
        ed = n0 - ec
        va = 1.0 / (1 / ea + 1 / eb + 1 / ec + 1 / ed)
        bd += (a - ea) ** 2 / va
        sum_diff += a - ea
        sum_v += va
    tarone = bd - (sum_diff ** 2) / sum_v
    df = len(rows) - 1
    return {
        "or_mh": or_mh,
        "bd": bd,
        "p_bd": float(chi2.sf(bd, df)),
        "tarone": tarone,
        "p_tarone": float(chi2.sf(tarone, df)),
        "df": df,
    }


def stratum_row(name, alln, n1, a, n0, c):
    rd, rdlo, rdhi, _ = wald_rd(a, n1, c, n0)
    rr, rrlo, rrhi, _ = katz_rr(a, n1, c, n0)
    or_, orlo, orhi = woolf_or(a, n1, c, n0)
    chi, p = pearson_chi2(a, n1, c, n0)
    other = None if alln is None else alln - n1 - n0
    cells = [a, n1 - a, c, n0 - c, n1, n0]
    if alln is not None:
        cells.extend([alln, other])
    return {
        "name": name,
        "all": alln,
        "other": other,
        "a": a,
        "n1": n1,
        "c": c,
        "n0": n0,
        "p1": a / n1,
        "p0": c / n0,
        "rd": rd,
        "rdlo": rdlo,
        "rdhi": rdhi,
        "rr": rr,
        "rrlo": rrlo,
        "rrhi": rrhi,
        "or_": or_,
        "orlo": orlo,
        "orhi": orhi,
        "chi": chi,
        "p": p,
        "min_cell": min(cells),
    }


def fmt_pct(a, n):
    return f"{a:,}/{n:,} ({100 * a / n:.2f}%)"


def fmt_rr(rr, lo, hi):
    return f"{rr:.3f} ({lo:.3f}–{hi:.3f})"


def fmt_rd(rd, lo, hi):
    return f"{100 * rd:.2f} ({100 * lo:.2f} to {100 * hi:.2f})"


def fmt_all(alln):
    return "[PENDING]" if alln is None else f"{alln:,}"


def fmt_other(other):
    return "[PENDING]" if other is None else f"{other:,}"


def analyze(strata):
    # strata: name, alln or None, n1, a, n0, c
    rows = [(a, n1, c, n0) for _, _, n1, a, n0, c in strata]
    details = [stratum_row(*s) for s in strata]
    return details, mh_rr_greenland_robins(rows), cmh_chi2(rows), breslow_day_tarone(rows)


def results_markdown(d_sex, mh_sex, cmh_sex, bd_sex, d_race, mh_race, cmh_race, bd_race):
    lines = []
    a = lines.append
    a("# H-S1 results — sex-stratified audiology (H90.3), Black vs White")
    a("")
    a("Computed by `hs1_sex_analysis.py`. Counts are Cohort Explorer header Patients")
    a("totals from Jake Harthcock screenshots, 2026-11-27. H90.3 cohort, no age filter.")
    a("Clicked counts only; pie-chart percentages were not used to back-calculate cells.")
    a("")
    a("Male all-patients (Sex = Male, race and Audiology cleared) was not captured")
    a("(duplicate screenshot) and is **[PENDING]**. It is not required for H-S1.")
    a("Do not back-calculate it from Female all or from earlier pie-chart sex percentages.")
    a("")
    a("Female Black + White = 8,156 vs Female all = 8,562; other/unknown = **406**.")
    a("Male other/unknown is **[PENDING]** because Male all is missing.")
    a("")
    a("Consistency with R1/R4 (no age filter, so Female and Male do not overlap):")
    a("- Female Black 3,788 + Male Black 2,388 = 6,176 (R1 Black).")
    a("- Female White 4,368 + Male White 4,229 = 8,597 (R1 White).")
    a("- Female Black Audiology 393 + Male Black Audiology 237 = 630 (R4 Black).")
    a("- Female White Audiology 532 + Male White Audiology 464 = 996 (R4 White).")
    a("")
    a("All 2×2 cells used below are ≥11 (no suppression). Female other/unknown = 406 ≥11.")
    a("")
    a("## Per-sex, Black vs White")
    a("")
    a("| Sex | All patients | Other/unknown | Black, ≥1 Audiology | White, ≥1 Audiology | RD, pp (Wald 95% CI) | RR (Katz 95% CI) | OR (Woolf 95% CI) | Pearson χ², p |")
    a("|---|---:|---:|---|---|---|---|---|---|")
    for d in d_sex:
        a(
            f"| {d['name']} | {fmt_all(d['all'])} | {fmt_other(d['other'])} | {fmt_pct(d['a'], d['n1'])} | "
            f"{fmt_pct(d['c'], d['n0'])} | {fmt_rd(d['rd'], d['rdlo'], d['rdhi'])} | "
            f"{fmt_rr(d['rr'], d['rrlo'], d['rrhi'])} | {fmt_rr(d['or_'], d['orlo'], d['orhi'])} | "
            f"{d['chi']:.2f}, {d['p']:.3g} |"
        )
    a("")
    a("RD is Black minus White, in percentage points. Pearson χ² is uncorrected, 1 df.")
    a("")
    a("## Mantel-Haenszel pooled RR, Black vs White (stratified by sex)")
    a("")
    a(f"- MH RR = **{mh_sex['rr']:.3f}** (Greenland-Robins 95% CI **{mh_sex['lo']:.3f}–{mh_sex['hi']:.3f}**)")
    a(f"- Wald z (ln RR) = {mh_sex['z']:.3f}, p = {mh_sex['p_wald']:.3g}")
    chi, p = cmh_sex
    a(f"- CMH χ² (uncorrected) = **{chi:.2f}**, p = **{p:.3g}**")
    a(f"- MH OR = {bd_sex['or_mh']:.3f}")
    a(f"- Breslow-Day χ²({bd_sex['df']}) = {bd_sex['bd']:.2f}, p = {bd_sex['p_bd']:.3g}")
    a(f"- Tarone χ²({bd_sex['df']}) = {bd_sex['tarone']:.2f}, p = {bd_sex['p_tarone']:.3g}")
    a("")
    a("The primary association p-value reported in the manuscript is the uncorrected CMH p.")
    a("Sex strata do not overlap (age was not filtered), so the independence assumption")
    a("of MH/CMH is not threatened by the AgeKey overlap that affects the R9 age analysis.")
    a("")
    a("## Female vs male audiology, within race and race-adjusted")
    a("")
    a("Exposed = Female; reference = Male. RD is Female minus Male.")
    a("")
    a("| Race | Female, ≥1 Audiology | Male, ≥1 Audiology | RD, pp (Wald 95% CI) | RR (Katz 95% CI) | OR (Woolf 95% CI) | Pearson χ², p |")
    a("|---|---|---|---|---|---|---|")
    for d in d_race:
        a(
            f"| {d['name']} | {fmt_pct(d['a'], d['n1'])} | {fmt_pct(d['c'], d['n0'])} | "
            f"{fmt_rd(d['rd'], d['rdlo'], d['rdhi'])} | {fmt_rr(d['rr'], d['rrlo'], d['rrhi'])} | "
            f"{fmt_rr(d['or_'], d['orlo'], d['orhi'])} | {d['chi']:.2f}, {d['p']:.3g} |"
        )
    a("")
    a("## Mantel-Haenszel pooled RR, Female vs Male (stratified by race)")
    a("")
    a(f"- MH RR = **{mh_race['rr']:.3f}** (Greenland-Robins 95% CI **{mh_race['lo']:.3f}–{mh_race['hi']:.3f}**)")
    a(f"- Wald z (ln RR) = {mh_race['z']:.3f}, p = {mh_race['p_wald']:.3g}")
    chi_r, p_r = cmh_race
    a(f"- CMH χ² (uncorrected) = **{chi_r:.2f}**, p = **{p_r:.3g}**")
    a(f"- MH OR = {bd_race['or_mh']:.3f}")
    a(f"- Breslow-Day χ²({bd_race['df']}) = {bd_race['bd']:.2f}, p = {bd_race['p_bd']:.3g}")
    a(f"- Tarone χ²({bd_race['df']}) = {bd_race['tarone']:.2f}, p = {bd_race['p_tarone']:.3g}")
    a("")
    a("## Manuscript rounding")
    a("")
    a("RR and CI to three decimals; RD to two decimals (percentage points); percentages")
    a("to two decimals; χ² to two decimals. Sex-stratified Black vs White MH RR and")
    a("race-adjusted Female vs Male MH RR as printed above.")
    a("")
    return "\n".join(lines) + "\n"


def main():
    details, mh, cmh, bd = analyze(STRATA_SEX)
    # Female vs male strata: name, all unused, female n, female au, male n, male au
    race_input = [(name, None, n_f, a_f, n_m, a_m) for name, n_f, a_f, n_m, a_m in STRATA_RACE]
    details_r, mh_r, cmh_r, bd_r = analyze(race_input)
    text = results_markdown(details, mh, cmh, bd, details_r, mh_r, cmh_r, bd_r)
    out = Path(__file__).resolve().with_name("hs1_sex_results.md")
    out.write_text(text)
    print(text)
    print(f"Wrote {out}")
    mins = [d["min_cell"] for d in details + details_r]
    if min(mins) < 11:
        raise SystemExit(f"suppression needed: min cell {min(mins)}")

    # consistency checks (must not be used to invent Male all)
    assert details[0]["n1"] + details[1]["n1"] == UNIQUE_BLACK
    assert details[0]["n0"] + details[1]["n0"] == UNIQUE_WHITE
    assert details[0]["a"] + details[1]["a"] == UNIQUE_BLACK_AU
    assert details[0]["c"] + details[1]["c"] == UNIQUE_WHITE_AU
    assert FEMALE_ALL - 3788 - 4368 == 406


if __name__ == "__main__":
    main()
