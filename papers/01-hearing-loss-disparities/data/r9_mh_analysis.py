#!/usr/bin/env python3
"""R9 age-stratified audiology analysis for Paper 01 (H90.3, UMMC Cohort Explorer).

Computes per-stratum risk, Wald risk difference, Katz risk ratio, Woolf odds ratio,
Pearson chi-square (uncorrected); Mantel-Haenszel risk ratio with Greenland-Robins
(1985) 95% CI; Cochran-Mantel-Haenszel chi-square; Breslow-Day and Tarone tests of
odds-ratio homogeneity; and a sensitivity analysis excluding the 0-17 band.

Counts are Cohort Explorer header Patients totals (Jake Harthcock, 2026-11-26
screenshots). Age is AgeKey (age at encounter), so a patient can contribute to more
than one band; strata are therefore not strictly independent. Do not sum band
counts to recover unique-patient totals (R0/R1/R4).

All cells in these 2x2 tables are >= 11 (no suppression).

Requires: Python 3, numpy, scipy.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np
from scipy.stats import chi2, norm

Z95 = 1.959963984540054

# band, all patients, Black n, Black with Audiology, White n, White with Audiology
STRATA = [
    ("0-17", 2185, 1042, 168, 926, 182),
    ("18-44", 2692, 1261, 82, 1266, 89),
    ("45-64", 6956, 3128, 143, 3543, 178),
    ("65+", 8991, 3225, 243, 5428, 550),
]

UNIQUE_COHORT = 15612
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
    unexposed events, unexposed n). Here exposed = Black.
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
    other = alln - n1 - n0
    cells = [a, n1 - a, c, n0 - c, n1, n0, alln, other]
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


def analyze(strata):
    rows = [(a, n1, c, n0) for _, _, n1, a, n0, c in strata]
    details = [stratum_row(*s) for s in strata]
    return details, mh_rr_greenland_robins(rows), cmh_chi2(rows), breslow_day_tarone(rows)


def results_markdown(details, mh, cmh, bd, details_s, mh_s, cmh_s, bd_s):
    lines = []
    a = lines.append
    a("# R9 results — age-stratified audiology (H90.3), Black vs White")
    a("")
    a("Computed by `r9_mh_analysis.py`. Counts are Cohort Explorer header Patients")
    a("totals from Jake Harthcock screenshots, 2026-11-26. Age is AgeKey (age at")
    a("encounter). The 65+ band used MinAge 65 with MaxAge left blank.")
    a("")
    a("All 2×2 cells and other/unknown remainders are ≥11 (no suppression).")
    a("")
    a("## Per-stratum (Black vs White)")
    a("")
    a("| Age band | All patients | Other/unknown | Black, ≥1 Audiology | White, ≥1 Audiology | RD, pp (Wald 95% CI) | RR (Katz 95% CI) | OR (Woolf 95% CI) | Pearson χ², p |")
    a("|---|---:|---:|---|---|---|---|---|---|")
    for d in details:
        a(
            f"| {d['name']} | {d['all']:,} | {d['other']:,} | {fmt_pct(d['a'], d['n1'])} | "
            f"{fmt_pct(d['c'], d['n0'])} | {fmt_rd(d['rd'], d['rdlo'], d['rdhi'])} | "
            f"{fmt_rr(d['rr'], d['rrlo'], d['rrhi'])} | {fmt_rr(d['or_'], d['orlo'], d['orhi'])} | "
            f"{d['chi']:.2f}, {d['p']:.3g} |"
        )
    a("")
    a("RD is Black minus White, in percentage points. Pearson χ² is uncorrected, 1 df.")
    a("")
    a("## Mantel-Haenszel pooled RR (four bands)")
    a("")
    a(f"- MH RR = **{mh['rr']:.3f}** (Greenland-Robins 95% CI **{mh['lo']:.3f}–{mh['hi']:.3f}**)")
    a(f"- Wald z (ln RR) = {mh['z']:.3f}, p = {mh['p_wald']:.3g}")
    chi, p = cmh
    a(f"- CMH χ² (uncorrected) = **{chi:.2f}**, p = **{p:.3g}**")
    a(f"- MH OR = {bd['or_mh']:.3f}")
    a(f"- Breslow-Day χ²({bd['df']}) = {bd['bd']:.2f}, p = {bd['p_bd']:.3g}")
    a(f"- Tarone χ²({bd['df']}) = {bd['tarone']:.2f}, p = {bd['p_tarone']:.3g}")
    a("")
    a("The primary association p-value reported in the manuscript is the uncorrected CMH p.")
    a("")
    a("## Sensitivity: exclude 0–17")
    a("")
    a("Motivated by the 0–17 Audiology selection showing an encounter window of")
    a("3/2026–9/30/2026 (Black 3/26/2026, White 3/16/2026), which may mean pediatric")
    a("Audiology-department coding only begins in 2026 ([PENDING] verification).")
    a("Adult bands show Audiology encounters from mid/late 2014.")
    a("")
    a(f"- MH RR = **{mh_s['rr']:.3f}** (Greenland-Robins 95% CI **{mh_s['lo']:.3f}–{mh_s['hi']:.3f}**)")
    a(f"- Wald z (ln RR) = {mh_s['z']:.3f}, p = {mh_s['p_wald']:.3g}")
    chi_s, p_s = cmh_s
    a(f"- CMH χ² (uncorrected) = **{chi_s:.2f}**, p = **{p_s:.3g}**")
    a(f"- MH OR = {bd_s['or_mh']:.3f}")
    a(f"- Breslow-Day χ²({bd_s['df']}) = {bd_s['bd']:.2f}, p = {bd_s['p_bd']:.3g}")
    a(f"- Tarone χ²({bd_s['df']}) = {bd_s['tarone']:.2f}, p = {bd_s['p_tarone']:.3g}")
    a("")
    a("## Overlap caveat")
    a("")
    s_all = sum(s[1] for s in STRATA)
    s_b = sum(s[2] for s in STRATA)
    s_ba = sum(s[3] for s in STRATA)
    s_w = sum(s[4] for s in STRATA)
    s_wa = sum(s[5] for s in STRATA)
    a(f"- Band totals sum to {s_all:,} vs unique cohort N = {UNIQUE_COHORT:,} (excess {s_all - UNIQUE_COHORT:,}).")
    a(f"- Black sums to {s_b:,} vs unique {UNIQUE_BLACK:,} (excess {s_b - UNIQUE_BLACK:,}).")
    a(f"- White sums to {s_w:,} vs unique {UNIQUE_WHITE:,} (excess {s_w - UNIQUE_WHITE:,}).")
    a(f"- Black Audiology sums to {s_ba:,} vs unique {UNIQUE_BLACK_AU:,} (excess {s_ba - UNIQUE_BLACK_AU:,}).")
    a(f"- White Audiology sums to {s_wa:,} vs unique {UNIQUE_WHITE_AU:,} (excess {s_wa - UNIQUE_WHITE_AU:,}).")
    a("")
    a("Denominator overlap is substantial; Audiology-event overlap is small. Mantel-Haenszel")
    a("and CMH treat strata as independent, so variance may be understated. Do not add")
    a("band counts to reconstruct unique-patient figures.")
    a("")
    a("## Manuscript rounding")
    a("")
    a("RR and CI to three decimals; RD to two decimals (percentage points); percentages")
    a("to two decimals; χ² to two decimals. Primary MH result: RR 0.812 (0.711–0.928),")
    a("CMH p = 1.89e-5. Sensitivity: 0.810 (0.695–0.943), CMH p = 1.70e-4.")
    a("")
    return "\n".join(lines) + "\n"


def main():
    details, mh, cmh, bd = analyze(STRATA)
    details_s, mh_s, cmh_s, bd_s = analyze(STRATA[1:])
    text = results_markdown(details, mh, cmh, bd, details_s, mh_s, cmh_s, bd_s)
    out = Path(__file__).resolve().with_name("r9_mh_results.md")
    out.write_text(text)
    print(text)
    print(f"Wrote {out}")
    mins = [d["min_cell"] for d in details]
    if min(mins) < 11:
        raise SystemExit(f"suppression needed: min cell {min(mins)}")


if __name__ == "__main__":
    main()
