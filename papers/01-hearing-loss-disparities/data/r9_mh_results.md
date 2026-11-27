# R9 results — age-stratified audiology (H90.3), Black vs White

Computed by `r9_mh_analysis.py`. Counts are Cohort Explorer header Patients
totals from Jake Harthcock screenshots, 2026-11-26. Age is AgeKey (age at
encounter). The 65+ band used MinAge 65 with MaxAge left blank.

All 2×2 cells and other/unknown remainders are ≥11 (no suppression).

## Per-stratum (Black vs White)

| Age band | All patients | Other/unknown | Black, ≥1 Audiology | White, ≥1 Audiology | RD, pp (Wald 95% CI) | RR (Katz 95% CI) | OR (Woolf 95% CI) | Pearson χ², p |
|---|---:|---:|---|---|---|---|---|---|
| 0-17 | 2,185 | 217 | 168/1,042 (16.12%) | 182/926 (19.65%) | -3.53 (-6.93 to -0.14) | 0.820 (0.678–0.992) | 0.786 (0.623–0.990) | 4.18, 0.0409 |
| 18-44 | 2,692 | 165 | 82/1,261 (6.50%) | 89/1,266 (7.03%) | -0.53 (-2.49 to 1.43) | 0.925 (0.692–1.236) | 0.920 (0.674–1.255) | 0.28, 0.598 |
| 45-64 | 6,956 | 285 | 143/3,128 (4.57%) | 178/3,543 (5.02%) | -0.45 (-1.48 to 0.57) | 0.910 (0.734–1.128) | 0.906 (0.723–1.135) | 0.74, 0.389 |
| 65+ | 8,991 | 338 | 243/3,225 (7.53%) | 550/5,428 (10.13%) | -2.60 (-3.81 to -1.38) | 0.744 (0.644–0.859) | 0.723 (0.617–0.846) | 16.40, 5.13e-05 |

RD is Black minus White, in percentage points. Pearson χ² is uncorrected, 1 df.

## Mantel-Haenszel pooled RR (four bands)

- MH RR = **0.812** (Greenland-Robins 95% CI **0.711–0.928**)
- Wald z (ln RR) = -3.062, p = 0.0022
- CMH χ² (uncorrected) = **18.29**, p = **1.89e-05**
- MH OR = 0.794
- Breslow-Day χ²(3) = 3.55, p = 0.315
- Tarone χ²(3) = 3.55, p = 0.315

The primary association p-value reported in the manuscript is the uncorrected CMH p.

## Sensitivity: exclude 0–17 (concordance check)

A follow-up check with race cleared (H90.3 + AgeKey 0–17 + Audiology;
screenshot 2026-11-26) showed Patients = 401 (0.02% of RDW), Encounters = 868,
and an included-encounter window of 9/3/2015–9/30/2026. Pediatric
Audiology-department coding spans 2015–2026; the 3/2026 start previously seen
with a race selected (Black 3/26/2026, White 3/16/2026) is a display artifact,
not a coding window. The 0–17 band is retained in the primary MH estimate;
this sensitivity is a concordance check only. Adult bands show Audiology
encounters from mid/late 2014.

- MH RR = **0.810** (Greenland-Robins 95% CI **0.695–0.943**)
- Wald z (ln RR) = -2.706, p = 0.00682
- CMH χ² (uncorrected) = **14.13**, p = **0.00017**
- MH OR = 0.796
- Breslow-Day χ²(2) = 3.53, p = 0.171
- Tarone χ²(2) = 3.53, p = 0.171

## Overlap caveat

- Band totals sum to 20,824 vs unique cohort N = 15,612 (excess 5,212).
- Black sums to 8,656 vs unique 6,176 (excess 2,480).
- White sums to 11,163 vs unique 8,597 (excess 2,566).
- Black Audiology sums to 636 vs unique 630 (excess 6).
- White Audiology sums to 999 vs unique 996 (excess 3).

Denominator overlap is substantial; Audiology-event overlap is small. Mantel-Haenszel
and CMH treat strata as independent, so variance may be understated. Do not add
band counts to reconstruct unique-patient figures.

## Manuscript rounding

RR and CI to three decimals; RD to two decimals (percentage points); percentages
to two decimals; χ² to two decimals. Primary MH result: RR 0.812 (0.711–0.928),
CMH p = 1.89e-5. Sensitivity: 0.810 (0.695–0.943), CMH p = 1.70e-4.

