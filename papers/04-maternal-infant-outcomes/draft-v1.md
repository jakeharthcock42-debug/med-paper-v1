# Black–White Differences in Birth Outcomes and Obstetric Care Access Across Mississippi Counties: A Public-Data Ecological Analysis

**Status**: draft-v1 (2026-11-27). All values are published aggregates reproducible with `scripts/public-data/`. Public-data only (Jake's decision, 2026-11-27).

## Abstract (draft-v1; conference style)
**Background.** Mississippi has the highest infant mortality rate in the US (9.11 per 1,000 live births in 2022), with a large Black–White gap. Whether the gap varies by county context, and whether the uneven geography of obstetric services is related to county birth outcomes, is not well described.

**Methods.** Ecological analysis of all 82 Mississippi counties using public aggregates: County Health Rankings (NCHS natality; low birth weight and teen births 2018–2024; infant mortality 2017–2023, race-specific where published), HRSA Area Health Resources File 2024–2025 (hospitals with obstetric care, OB-GYN physicians, midwives, and preterm births 2021–2023), and state figures from NCHS, the Mississippi State Department of Health, and March of Dimes. We used paired Wilcoxon tests, Spearman correlations, and OLS and birth-weighted regression with robust SEs.

**Results.** Statewide, low birth weight was 17.65% for Black and 8.65% for White births, teen birth rates were 31.6 and 21.1 per 1,000, and infant mortality in 2022 was 12.1 vs 7.2 per 1,000 (rate ratio 1.68); preterm birth in 2022–2024 was 18.5% vs 12.7%. Black low birth weight exceeded White in all 77 counties with both values published (median 17.9% vs 8.8%, p<0.001), a gap of about 9 percentage points that was unrelated to county poverty, segregation, primary care supply, or rurality (R²=0.04). Teen births were higher for Black than White residents in 50 of 71 counties. Of 82 counties, 55 (67%; 76% nonmetro) had no hospital offering obstetric care, containing 37.5% of state births; 42 counties (51%; 23.7% of births) had neither an obstetric hospital nor an OB-GYN physician. After adjustment for child poverty, percent Black, and rurality, counties without an obstetric hospital did not have higher preterm birth (−0.08 percentage points, 95% CI −0.93 to 0.77) or low birth weight (+0.29, −0.33 to 0.92).

**Conclusions.** The Black–White gap in birth outcomes in Mississippi is large and nearly uniform across counties, and obstetric hospital services are absent from two thirds of counties. County-level obstetric hospital presence did not explain county differences in preterm birth or low birth weight, suggesting that the gap reflects factors beyond local service availability, such as health before conception, insurance, and care quality. These ecological findings need confirmation with individual-level data.

## 1. Introduction
Infant mortality in Mississippi was 9.11 per 1,000 live births in 2022, the highest of any state (Ely and Driscoll, NVSR 2024). Mississippi Department of Health data show Black non-Hispanic infants died at 12.1 per 1,000 vs 7.2 for White non-Hispanic infants (MSDH 2025). Earlier Mississippi and Delta work documented infant mortality by geography, poverty, and race (Eudy 2009), fetal mortality (Sandlin 2015), and maternal mortality (Smith 2014) in the Delta. In a national study of rural counties, loss of hospital-based obstetric services was followed by more out-of-hospital births, more births in hospitals without obstetric units, and, in counties not adjacent to urban areas, more preterm births (Kozhimannil 2018). Our cross-sectional county comparison tests levels, not changes after closure. We did not find (PubMed, 2026-11-27) a Mississippi analysis relating county obstetric service availability to Black–White birth outcomes across all counties.

**Aims.** (1) Quantify county-level Black–White differences in LBW, teen births, and infant mortality. (2) Test whether the LBW gap varies with county context. (3) Describe obstetric access and test its association with preterm birth and LBW.

**Hypotheses.** H1 Black LBW exceeds White LBW in most counties. H2 Black teen births exceed White. H3 The LBW gap is larger in poorer, more segregated, or less-served counties. H4 Counties without a hospital offering obstetric care have higher preterm birth and LBW after adjustment.

## 2. Methods
**Design.** Cross-sectional ecological analysis of public aggregate data (no patient-level or UMMC data).

**Sources.** County Health Rankings 2025 annual release and 25 March 2026 supplement: LBW (% of live births <2,500 g, 2018–2024), teen births (per 1,000 females 15–19, 2018–2024), infant mortality (2017–2023), race-specific values where CHR publishes (unreliable/suppressed values excluded); child poverty, % Black, residential segregation, PCP rate. HRSA AHRF 2024–2025: non-federal OB-GYN physicians (AMA masterfile 2023), short-term general hospitals with obstetric care (AHA survey 2023), APN midwives with NPI (2023), 3-year average births and preterm births (gestation <37 weeks; NCHS natality 2021–2023), Census 2023 population and female population. State figures: NCHS NVSR 73(5), MSDH Child Death Review (2021–2022), March of Dimes PeriStats (NCHS final natality 2022–2024), NCHS VSRR 35. USDA RUCC 2023 (nonmetro 4–9); Delta Regional Authority list.

**Analysis.** Paired Wilcoxon tests for Black vs White within counties with both values; Spearman correlations; OLS with HC3 robust SEs; WLS weighted by births for preterm and LBW models. Obstetric access: hospital with obstetric care (yes/no), OB-GYN per 10,000 females, and "no OB hospital and no OB-GYN" counties with share of births. Two-sided α=0.05; secondary analyses exploratory. Python (pandas, scipy, statsmodels); scripts in `scripts/public-data/`.

**Ethics.** Only published aggregates. No public cell under 11 events is reported (AHRF births and preterm values are 3-year averages with minimum 13 per year). Confirm with UMMC IRB whether a determination letter is needed for the abstract. [PENDING: IRB/RDW confirmation]

## 3. Results
**Table 1. Mississippi vs US: state-level Black–White differences (published values)**

| Measure | Mississippi Black | Mississippi White | RR | US Black | US White | Source |
|---|---|---|---|---|---|---|
| Low birth weight, % (2018–24) | 17.65 | 8.65 | 2.04 | — | — | CHR 2026 supplement |
| Teen births per 1,000 (2018–24) | 31.62 | 21.08 | 1.50 | — | — | CHR 2026 supplement |
| Infant mortality per 1,000 (2022) | 12.1 | 7.2 | 1.68 | 10.9 | 4.5 | MSDH 2025; CDC (NVSR) |
| Preterm birth % (MS 2022–24; US 2023) | 18.5 | 12.7 | 1.46 | 14.65 | 9.45 | PeriStats; NCHS VSRR 35 |

Mississippi overall: IMR 9.11 (2022, highest of 50 states and DC); preterm 14.95% in 2023 vs US 10.41%.

**Table 2. County-level Black vs White (counties with both values published)**

| Measure | n counties | White median | Black median | Black > White | Wilcoxon p |
|---|---|---|---|---|---|
| Low birth weight, % | 77 | 8.78 | 17.9 | 77 | 2.5e-14 |
| Teen births per 1,000 | 71 | 26.9 | 33.4 | 50 | 9.8e-5 |
| Infant deaths per 1,000 | 9 | 6.37 | 11.5 | 9 | 0.004 |

County LBW gap (Black − White) was unrelated to segregation (rho −0.02), Black child poverty (−0.003), PCP supply (−0.03), or nonmetro status (0.18, p=0.12); OLS R² = 0.04 (n = 74).

**Table 3. Obstetric access (HRSA AHRF 2024–25; births = 3-year average 2021–23)**

| Definition | Counties (% of 82) | Avg annual births (% of state) | % nonmetro |
|---|---|---|---|
| No hospital with obstetric care | 55 (67%) | 13,026 (37.5%) | 76 |
| No OB-GYN and no obstetric hospital | 42 (51%) | 8,240 (23.7%) | 76 |
| No OB-GYN, hospital, or NPI midwife | 38 (46%) | 7,128 (20.5%) | 79 |

Statewide 309 non-federal OB-GYN physicians, 33 hospitals with obstetric care in 27 counties, and 30 APN midwives with NPI.

**Table 4. County preterm births and LBW by obstetric hospital presence (adjusted for child poverty/10, % Black/10, nonmetro)**

| Outcome | Unadjusted medians (OB hospital vs none) | OLS coef for OB hospital (95% CI) | WLS (births) coef (95% CI) |
|---|---|---|---|
| Preterm % (n=80) | 17.0 vs 17.3 | −0.08 (−0.93, 0.77) | +0.26 (−0.54, 1.06) |
| LBW % (n=81) | 12.5 vs 12.8 | +0.29 (−0.33, 0.92) | +0.42 (−0.06, 0.89) |

Percent Black was the strongest correlate in adjusted models (preterm +0.82 pp per 10 pp, 95% CI 0.46–1.18; LBW +0.93, 0.64–1.22); this is largely compositional. Teen births were lower in counties with an obstetric hospital (median 29.2 vs 33.1 per 1,000; p = 0.0135, unadjusted). Full output: `results/p04_results.md`, `results/p04b_results.md`.

## 4. Discussion (outline)
- Principal findings: universal Black–White LBW gap of about 9 points; obstetric hospital services absent from two thirds of counties; no county-level association between obstetric hospital presence and preterm birth or LBW.
- Interpretation: a uniform gap across poverty, segregation, and rurality suggests state-wide drivers (health before pregnancy, insurance, quality of care, racism) rather than local service gaps; null obstetric-access results do not exclude effects on maternal morbidity, transport, or neonatal outcomes not measured here.
- Limits: ecological; compositional effects; AHRF preterm definition differs from NCHS official state rate (16.9% weighted vs 14.95%); narrow access definition; race-specific county data are available only for larger counties; periods differ.
- Next: individual-level analysis (birth certificate microdata, Medicaid claims) to test mechanisms; CDC WONDER state series by race.

## References (verified)
1. Ely DM, Driscoll AK. Infant Mortality in the United States, 2022: Data From the Period Linked Birth/Infant Death File. *Natl Vital Stat Rep.* 2024;73(5). https://www.cdc.gov/nchs/data/nvsr/nvsr73/nvsr73-05.pdf
2. Mississippi State Department of Health. Mississippi Child Death Review: Review of 2021 and 2022 Child Deaths. February 2025. https://msdh.ms.gov/resources/media/21025.pdf
3. March of Dimes. PeriStats: Preterm birth rate by race/ethnicity, Mississippi, 2022–2024 average (NCHS final natality). Retrieved 2026-11-27. https://www.marchofdimes.org/peristats/data?obj=1&reg=99&slev=4&sreg=28&stop=63&top=3
4. Hamilton BE, Martin JA, Osterman MJK. Births: Provisional Data for 2023. *Vital Statistics Rapid Release* No. 35. April 2024. https://www.cdc.gov/nchs/data/vsrr/vsrr035.pdf
5. Eudy RL. Infant mortality in the Lower Mississippi Delta: geography, poverty and race. *Matern Child Health J.* 2009;13:806–813. doi:10.1007/s10995-008-0311-y
6. Sandlin AT, Bronstein JM, Rabie NZ, Wendel PJ, Hughes DS, Magann EF. Fetal mortality in the Delta. *South Med J.* 2015;108:389–392.
7. Smith BL, Sandlin AT, Bird TM, Steelman SC, Magann EF. Maternal mortality in the Mississippi Delta region. *South Med J.* 2014;107:275–279.
8. Kozhimannil KB, Hung P, Henning-Smith C, Casey MM, Prasad S. Association between loss of hospital-based obstetric services and birth outcomes in rural counties in the United States. *JAMA.* 2018;319(12):1239–1247.
9. Greenlund KJ, et al. PLACES: Local Data for Better Health. *Prev Chronic Dis.* 2022;19:210459.
10. HRSA NCHWA. Area Health Resources Files 2024–2025. https://data.hrsa.gov/data/download?data=AHRF (accessed 2026-11-27).
11. County Health Rankings & Roadmaps. 2025 annual data and 25 March 2026 supplemental release. https://www.countyhealthrankings.org/
