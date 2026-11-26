# Paper 01 — County-level analysis (public data, 82 Mississippi counties)

**Run date**: 2026-11-26. **Script**: [`data/build_and_analyze.py`](data/build_and_analyze.py). **Merged data**: [`data/ms_county_merged.csv`](data/ms_county_merged.csv) (82 rows, public aggregate data only; the UMMC RDW suppression rule does not apply here).
**Scope**: tests only the county-level hypotheses (H-C1 to H-C5, defined in [`draft-v1.md`](draft-v1.md) §2.2). UMMC-cohort hypotheses (H-U1 to H-U6) are **[PENDING]**: no RDW numbers have been received.

## 1. Sources and data years

| Variable (column prefix) | Source | Data year | URL |
|---|---|---|---|
| Hearing disability among adults, crude and age-adjusted % (`places_*`) | CDC PLACES, County Data, **2025 release** (model-based; BRFSS-based). Measure ID `HEARING`; dataset `swc5-untb`, rows updated 2025-12-04 | **BRFSS 2023** | https://data.cdc.gov/500-Cities-Places/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb (API: `https://data.cdc.gov/resource/swc5-untb.csv?$where=stateabbr='MS' AND measureid='HEARING'`) |
| Hearing difficulty (`acs_hearing_*`), % Black alone (`acs_pct_black_alone`), % below poverty (`acs_pct_poverty`), % 65+ (`acs_pct_65plus`) | U.S. Census Bureau, ACS **5-year 2020–2024**, tables B18102 (Sex by Age by Hearing Difficulty; civilian noninstitutionalized), B02001, B17001 via the Table-Based Summary File | 2020–2024 | https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/ (the Census API now requires a key, so bulk files were used) |
| Primary care physicians per 100,000 (`chr_pcp_per100k`) | County Health Rankings & Roadmaps (CHR&R) 2025 release; AHRF/AMA; computed as 100,000 × CHR numerator ÷ denominator | **2021** | https://www.countyhealthrankings.org/sites/default/files/media/document/analytic_data2025_v3.csv |
| Uninsured, % under 65 (`chr_uninsured_pct_u65`) | CHR&R 2025; Small Area Health Insurance Estimates | **2022** | same file |
| % rural (`chr_pct_rural`) | CHR&R 2025; 2020 Decennial Census DHC | **2020** | same file |
| % non-Hispanic Black, population, % 65+, children in poverty, median household income (`chr_*`) | CHR&R 2025; Census PEP (2023), SAIPE (2023) | 2023 | same file |

Year information: CHR&R "2025 Select Measures and Data Sources" (https://www.countyhealthrankings.org/sites/default/files/media/document/2025%20Select%20and%20additional%20measures%2C%20data%20sources%20and%20years.pdf). PLACES details: https://www.cdc.gov/places. Raw files are on the box in `/workspace/paper01-data/raw/` (ACS `.dat` files are about 275 MB and are not committed).

## 2. Definitions fixed before testing

- **Primary outcome**: PLACES *age-adjusted* adult hearing disability prevalence (%), 2023 BRFSS, 2025 release. Sensitivity outcomes: PLACES crude %, ACS crude % with hearing difficulty (all ages), ACS % with hearing difficulty among 65+.
- **Rural county**: CHR&R % rural (2020 Census) ≥ 50% (66 counties) vs < 50% (16 counties). Sensitivity: 100% rural (43) vs < 100% (39).
- **Tests**: Spearman rank correlation (n = 82) for H-C1 and H-C2 to H-C5; Mann-Whitney U (and Welch t) for rural vs non-rural; Holm correction across the 5 primary Spearman tests; α = 0.05, two-sided; OLS with HC3 robust SE as an exploratory multivariable model. All counties weighted equally.
- **PCP supply**: Issaquena (n = 0 physicians, population denominator 1,280) and Quitman (n = 0, denominator 5,935) have zero physicians in the CHR&R numerator. CHR&R leaves Quitman's raw value blank; both are set to 0 per 100,000 here because the reported numerator is 0. Excluding both gives rho = −0.459, p = 1.8e-5 (n = 80), the same conclusion.

## 3. Descriptive statistics (unweighted across 82 counties)

| Measure | Mean | SD | Median | Min (county) | Max (county) |
|---|---|---|---|---|---|
| PLACES hearing disability, age-adjusted % | 7.41 | 0.53 | 7.5 | 5.7 (Madison) | 8.5 (Neshoba) |
| PLACES hearing disability, crude % | 8.73 | 1.03 | 8.7 | 6.2 | 11.1 |
| ACS % with hearing difficulty (all ages) | 4.90 | 2.19 | 4.67 | 1.08 | 14.54 |
| ACS % with hearing difficulty, age 65+ | 15.82 | 5.96 | 15.19 | 2.82 | 33.98 |
| % rural (2020) | 77.52 | 27.32 | 100.0 | 17.58 | 100.0 |
| % Black alone (ACS 2020–24) | 40.84 | 21.46 | 36.29 | 1.19 | 86.10 |
| % below poverty (ACS 2020–24) | 21.81 | 5.81 | 20.93 | 9.71 | 36.36 |
| PCP per 100,000 (2021) | 38.19 | 26.80 | 35.43 | 0 | 129.31 |
| % uninsured, under 65 (2022) | 13.91 | 1.81 | 13.81 | 9.70 | 22.95 |

Highest PLACES age-adjusted values: Neshoba 8.5, Tishomingo 8.4, Lawrence 8.3, Issaquena 8.2, Calhoun 8.1, Yazoo 8.1. Lowest: Madison 5.7, Hinds 5.9, Rankin 6.3, DeSoto 6.3, Warren 6.4, Lowndes 6.6.
PLACES 95% intervals for single counties are about ±0.9–1.0 points wide on each side (e.g., Neshoba 8.5, 7.4–9.6), so most county-to-county differences are within model uncertainty; only the broad patterns below are interpretable.
State context from the same ACS table: summing county estimates gives 124,867 people with hearing difficulty out of 2,883,649 civilian noninstitutionalized residents = 4.33% (derived by summing; not a CHR&R/Census-published state figure).
PLACES vs ACS agreement across counties: Spearman rho = 0.382 (p = 4.0e-4), modest.

## 4. Results by hypothesis

### H-C1. Rural counties have higher adult hearing disability prevalence — **SUPPORTED**
- Spearman, % rural vs PLACES age-adjusted: **rho = 0.477, p = 6.0e-6** (Holm p = 2.4e-5), n = 82.
- Rural (≥ 50%, n = 66) vs non-rural (n = 16), PLACES age-adjusted %: **7.54 (SD 0.42) vs 6.91 (SD 0.64)**, difference 0.63 points (Welch 95% CI 0.28 to 0.98); Mann-Whitney p = 1.5e-4; Welch p = 0.0014; probability of superiority 0.81.
- 100% rural (n = 43) vs others (n = 39): 7.60 vs 7.21, Mann-Whitney p = 0.0013.
- Same direction on all other outcomes (Mann-Whitney p): PLACES crude 9.00 vs 7.63 (p = 1.3e-5); ACS all ages 5.20 vs 3.66 (p = 0.0063); ACS 65+ 16.53 vs 12.89 (p = 0.017).

| Outcome | Rural mean (SD) | Non-rural mean (SD) | Difference | Mann-Whitney p | Welch p |
|---|---|---|---|---|---|
| PLACES age-adjusted % | 7.54 (0.42) | 6.91 (0.64) | 0.63 | 1.5e-4 | 0.0014 |
| PLACES crude % | 9.00 (0.83) | 7.63 (1.08) | 1.38 | 1.3e-5 | 1.3e-4 |
| ACS % hearing difficulty | 5.20 (2.26) | 3.66 (1.33) | 1.55 | 0.0063 | 9.7e-4 |
| ACS % hearing difficulty, 65+ | 16.53 (6.14) | 12.89 (4.13) | 3.63 | 0.017 | 0.0076 |

### H-C2. County % Black is associated with hearing disability prevalence (two-sided; literature predicts a negative association) — **SUPPORTED, negative**
- PLACES age-adjusted: **rho = −0.321, p = 0.0033** (Holm p = 0.0066). PLACES crude: rho = −0.205, p = 0.064. ACS all ages: rho = −0.411, p = 1.3e-4. ACS 65+: rho = −0.488, p = 3.4e-6.
- Meaning: counties with larger Black populations have *lower* measured/reported hearing disability, matching the national pattern of lower measured prevalence among Black adults (Introduction). This says nothing about care use, which is what the UMMC cohort tests. Ecological: it cannot be read as an individual-level race effect.

### H-C3. County poverty is positively associated with hearing disability prevalence — **NOT SUPPORTED**
- PLACES age-adjusted: **rho = 0.017, p = 0.88** (n = 82). PLACES crude: rho = 0.054, p = 0.63.
- ACS direct estimates go the *opposite* way: all ages rho = −0.283, p = 0.010; 65+ rho = −0.332, p = 0.0023 (county poverty and % Black are tightly correlated, Spearman rho = 0.786, p = 2.2e-18, and % Black tracks lower measured hearing difficulty, so poverty likely proxies it).

### H-C4. Fewer primary care physicians per capita is associated with higher hearing disability prevalence — **SUPPORTED, but confounded by rurality**
- PLACES age-adjusted: **rho = −0.470, p = 8.5e-6** (Holm p = 2.5e-5), n = 82. Also negative on PLACES crude (rho = −0.407, p = 1.5e-4), ACS all ages (rho = −0.357, p = 9.9e-4), ACS 65+ (rho = −0.252, p = 0.022).

### H-C5. Higher uninsured share (under 65) is associated with higher hearing disability prevalence — **PARTIALLY SUPPORTED (PLACES only)**
- PLACES age-adjusted: **rho = 0.490, p = 3.0e-6** (Holm p = 1.5e-5). PLACES crude: rho = 0.415, p = 1.1e-4.
- Not supported on ACS direct estimates: all ages rho = 0.178, p = 0.109; 65+ rho = 0.102, p = 0.36. The uninsured measure covers under-65 only, while hearing difficulty is concentrated in older adults.

### Summary table: Spearman correlations (n = 82 counties)

| Predictor | PLACES age-adj | PLACES crude | ACS all ages | ACS 65+ |
|---|---|---|---|---|
| % rural (2020) | 0.477 (6.0e-6) | 0.534 (2.4e-7) | 0.354 (0.0011) | 0.247 (0.025) |
| % Black alone (ACS 2020–24) | −0.321 (0.0033) | −0.205 (0.064) | −0.411 (1.3e-4) | −0.488 (3.4e-6) |
| % below poverty (ACS 2020–24) | 0.017 (0.88) | 0.054 (0.63) | −0.283 (0.010) | −0.332 (0.0023) |
| PCP per 100k (2021) | −0.470 (8.5e-6) | −0.407 (1.5e-4) | −0.357 (9.9e-4) | −0.252 (0.022) |
| % uninsured <65 (2022) | 0.490 (3.0e-6) | 0.415 (1.1e-4) | 0.178 (0.109) | 0.102 (0.36) |

Cells show rho (p). Only the PLACES age-adjusted column is the pre-specified primary analysis; Holm-adjusted p for those five tests: 2.4e-5, 0.0066, 0.88, 2.5e-5, 1.5e-5. The other columns are sensitivity analyses and are not multiplicity-adjusted.

### Exploratory multivariable OLS (PLACES age-adjusted %; n = 82; HC3 robust SE; R² = 0.718, adjusted R² = 0.699; max VIF 2.80)

| Predictor | Coefficient (per unit) | 95% CI | p |
|---|---|---|---|
| % rural (per 1 point) | 0.0030 | −0.0004 to 0.0065 | 0.083 |
| % Black alone (per 1 point) | −0.0200 | −0.0273 to −0.0126 | 1.0e-7 |
| % below poverty (per 1 point) | 0.0590 | 0.0313 to 0.0868 | 3.1e-5 |
| PCP per 100k (per 1) | −0.0048 | −0.0075 to −0.0020 | 6.9e-4 |
| % uninsured <65 (per 1 point) | 0.0981 | 0.0238 to 0.1723 | 0.0096 |

With ACS direct estimates as the outcome (all ages) the same model has R² = 0.356 and no predictor reaches p < 0.05 (PCP p = 0.071).

## 5. Interpretation and caveats

1. **Rurality is the robust finding.** Rural > non-rural holds on all four outcome definitions. Poverty is not associated with hearing disability in the raw PLACES data.
2. **PLACES is modeled, not measured.** CDC builds the county estimates from BRFSS plus county demographic and socioeconomic inputs from the ACS, so correlations of PLACES with race, poverty, and insurance partly reflect the model's own inputs. The strong multivariable R² (0.72) and the sign flip on poverty (null alone; positive after adjusting for % Black) should not be read as independent effects. CDC cautions against using PLACES for program or policy evaluation. The ACS direct estimates agree with PLACES only moderately (rho = 0.38).
3. **ACS hearing difficulty is self-reported and county-level noise is large** (margins of error are not propagated here; small counties have 41 to a few hundred cases). The all-ages ACS rate is influenced by county age structure (county % rural and % 65+ correlate, rho = 0.448, p = 2.4e-5); the 65+ version partly addresses this.
4. **Ecological design.** County associations do not describe individuals. Differences in county % Black or poverty do not show who has hearing loss or who receives care.
5. **Different years.** BRFSS 2023, ACS 2020–2024, AMA 2021, SAHIE 2022, Census 2020 are mixed.
6. 82 counties, equal weights, no spatial correction. Neighboring counties are likely correlated, so p-values are optimistic.
7. These county tests give context only. They do not test the paper's main disparity question (race and rural differences in audiology/ENT use at UMMC); that needs the RDW counts listed in [`rdw-data-requests.md`](rdw-data-requests.md), **[PENDING]**.

## 6. Reproduce
`python build_and_analyze.py` from a folder with `raw/` containing the PLACES CSV, CHR analytic CSV, and ACS `.dat` files (URLs above). Needs pandas, scipy, statsmodels.
