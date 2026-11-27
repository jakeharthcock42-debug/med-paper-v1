# H-S1 results — sex-stratified audiology (H90.3), Black vs White

Computed by `hs1_sex_analysis.py`. Counts are Cohort Explorer header Patients
totals from Jake Harthcock screenshots, 2026-11-27. H90.3 cohort, no age filter.
Clicked counts only; pie-chart percentages were not used to back-calculate cells.

Male all-patients (Sex = Male, race and Audiology cleared) was not captured
(duplicate screenshot) and is **[PENDING]**. It is not required for H-S1.
Do not back-calculate it from Female all or from earlier pie-chart sex percentages.

Female Black + White = 8,156 vs Female all = 8,562; other/unknown = **406**.
Male other/unknown is **[PENDING]** because Male all is missing.

Consistency with R1/R4 (no age filter, so Female and Male do not overlap):
- Female Black 3,788 + Male Black 2,388 = 6,176 (R1 Black).
- Female White 4,368 + Male White 4,229 = 8,597 (R1 White).
- Female Black Audiology 393 + Male Black Audiology 237 = 630 (R4 Black).
- Female White Audiology 532 + Male White Audiology 464 = 996 (R4 White).

All 2×2 cells used below are ≥11 (no suppression). Female other/unknown = 406 ≥11.

## Per-sex, Black vs White

| Sex | All patients | Other/unknown | Black, ≥1 Audiology | White, ≥1 Audiology | RD, pp (Wald 95% CI) | RR (Katz 95% CI) | OR (Woolf 95% CI) | Pearson χ², p |
|---|---:|---:|---|---|---|---|---|---|
| Female | 8,562 | 406 | 393/3,788 (10.37%) | 532/4,368 (12.18%) | -1.80 (-3.18 to -0.43) | 0.852 (0.753–0.963) | 0.835 (0.727–0.958) | 6.57, 0.0104 |
| Male | [PENDING] | [PENDING] | 237/2,388 (9.92%) | 464/4,229 (10.97%) | -1.05 (-2.57 to 0.48) | 0.905 (0.780–1.049) | 0.894 (0.758–1.055) | 1.77, 0.184 |

RD is Black minus White, in percentage points. Pearson χ² is uncorrected, 1 df.

## Mantel-Haenszel pooled RR, Black vs White (stratified by sex)

- MH RR = **0.873** (Greenland-Robins 95% CI **0.765–0.997**)
- Wald z (ln RR) = -2.010, p = 0.0445
- CMH χ² (uncorrected) = **7.93**, p = **0.00485**
- MH OR = 0.859
- Breslow-Day χ²(1) = 0.39, p = 0.532
- Tarone χ²(1) = 0.39, p = 0.532

The primary association p-value reported in the manuscript is the uncorrected CMH p.
Sex strata do not overlap (age was not filtered), so the independence assumption
of MH/CMH is not threatened by the AgeKey overlap that affects the R9 age analysis.

## Female vs male audiology, within race and race-adjusted

Exposed = Female; reference = Male. RD is Female minus Male.

| Race | Female, ≥1 Audiology | Male, ≥1 Audiology | RD, pp (Wald 95% CI) | RR (Katz 95% CI) | OR (Woolf 95% CI) | Pearson χ², p |
|---|---|---|---|---|---|---|
| Black | 393/3,788 (10.37%) | 237/2,388 (9.92%) | 0.45 (-1.09 to 1.99) | 1.045 (0.897–1.218) | 1.051 (0.886–1.245) | 0.32, 0.569 |
| White | 532/4,368 (12.18%) | 464/4,229 (10.97%) | 1.21 (-0.14 to 2.56) | 1.110 (0.987–1.248) | 1.125 (0.986–1.285) | 3.06, 0.0803 |

## Mantel-Haenszel pooled RR, Female vs Male (stratified by race)

- MH RR = **1.085** (Greenland-Robins 95% CI **0.952–1.237**)
- Wald z (ln RR) = 1.226, p = 0.22
- CMH χ² (uncorrected) = **2.99**, p = **0.0838**
- MH OR = 1.096
- Breslow-Day χ²(1) = 0.39, p = 0.532
- Tarone χ²(1) = 0.39, p = 0.532

## Manuscript rounding

RR and CI to three decimals; RD to two decimals (percentage points); percentages
to two decimals; χ² to two decimals. Sex-stratified Black vs White MH RR and
race-adjusted Female vs Male MH RR as printed above.

