# H-S2 / R3 results — H90.3 vs RDW base population, Black vs White

Computed by `hs2_r3_analysis.py`. Counts are Cohort Explorer header Patients
totals from Jake Harthcock screenshots, 2026-11-27 (R3) and 2026-11-26 (R0/R1).
R3 used no diagnosis or other filters. Data window: encounters 1/1/2013–9/30/2026.

The unfiltered pie-chart values Unknown 6.04% and Other 2.73% are encounter
shares and are **not** converted to patient counts.

## R3 — unfiltered RDW base

- All patients = **1,658,574**; Encounters = **73,271,189**.
- Black or African American: Patients = **684,322** (41.26% of 1,658,574); Encounters = **39,081,291**.
- White or Caucasian: Patients = **699,367** (42.17% of 1,658,574); Encounters = **30,228,243**.
- Other/unknown combined: Patients = **274,885** (16.57% of 1,658,574), computed as 1,658,574 − 684,322 − 699,367. Reported as one combined row only.

Consistency with previously displayed “% of RDW” figures (not back-calculated
at the time; now confirmed):
- H90.3 15,612 / 1,658,574 = 0.94% (displayed 0.94%).
- H90.3 Black 6,176 / 1,658,574 = 0.37% (displayed 0.37%).
- H90.3 White 8,597 / 1,658,574 = 0.52% (displayed 0.52%).
- H90.3 encounters 4,244,868 / 73,271,189 = 5.79% (displayed 5.79%).

All cells ≥11 (no suppression).

## Crude ever-diagnosed H90.3 prevalence, Black vs White

Prevalence is ever-diagnosed at UMMC within the data window, not community
incidence or point prevalence. This comparison is **crude** (not age-adjusted).
No age-by-race RDW base counts were pulled; the base age structure may differ
by race. Age-stratified base counts are a suggested future pull.

- Black: 6,176/684,322 (0.902%)
- White: 8,597/699,367 (1.229%)
- Overall: 15,612/1,658,574 (0.94%)
- RD (Black − White), percentage points: **-0.327 (-0.361 to -0.293)**
- RR (Black vs White): **0.734 (0.711–0.758)** (Katz 95% CI)
- OR: **0.732 (0.708–0.756)** (Woolf 95% CI)
- Pearson χ²(1) = **349.63**, p = **5.11e-78**

## H90.3 cohort race share vs RDW base share

Likewise unadjusted for age. Other/unknown is a combined remainder in both the
cohort and the base (not further split).

| Group | H90.3 cohort | RDW base | Difference, pp (Wald 95% CI) | Pearson χ², p |
|---|---|---|---|---|
| Black | 6,176/15,612 (39.6%) | 684,322/1,658,574 (41.26%) | -1.70 (-2.47 to -0.93) | 18.45, 1.74e-05 |
| White | 8,597/15,612 (55.1%) | 699,367/1,658,574 (42.17%) | 12.90 (12.12 to 13.68) | 1054.58, 2.46e-231 |
| Other/unknown | 839/15,612 (5.4%) | 274,885/1,658,574 (16.57%) | -11.20 (-11.56 to -10.84) | 1410.16, 1.3e-308 |

Cohort Black share / base Black share = 0.959.
Cohort White share / base White share = 1.306.

The White over-representation in the cohort, and the Black under-representation,
are partly the counterpart of a much smaller other/unknown share in the H90.3
cohort than in the RDW base. The prevalence contrast (section above) compares
Black and White denominators directly and does not depend on the other/unknown share.

## Manuscript rounding

Prevalence percentages to two or three decimals (three when the contrast is
sub-percentage-point); RR and CI to three decimals; RD to two decimals in
percentage points for share contrasts and three for prevalence contrasts;
χ² to two decimals.

