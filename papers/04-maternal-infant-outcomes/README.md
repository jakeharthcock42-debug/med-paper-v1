# 04 — Maternal and Infant Outcomes: Black–White Gaps and Obstetric Access Across Mississippi Counties

**Working title**: Black–White Differences in Birth Outcomes and Obstetric Care Access Across Mississippi's 82 Counties: a Public-Data Ecological Analysis  
**Status**: **Public-data analysis complete; abstract draft-v1 written (2026-11-27).** Public-data-only by Jake's decision (2026-11-27); no UMMC pull needed.  
**Natural fit**: OB/GYN, pediatrics, family medicine; MAFP and Research Day.  
**Novelty check (PubMed, 2026-11-27)**: Mississippi birth-outcome papers exist (e.g., Eudy 2009, Lower Delta infant mortality; Smith 2014, Delta maternal mortality; Sandlin 2015, Delta fetal mortality), but no county-level analysis linking Mississippi obstetric-service availability to Black–White birth outcomes was found. Moderate novelty; the state-level Black–White gaps are well known, so the contribution is the county-level gap uniformity and the obstetric access mapping.

## Research question
How large are Black–White differences in low birth weight, teen births, and infant mortality across Mississippi counties, how are they related to county socioeconomic context, and how are obstetric hospital and OB-GYN availability distributed and related to county preterm birth and low birth weight?

## Specific aims (all public)
1. Quantify Black vs White differences in low birth weight (LBW), teen birth rate, and infant mortality at county level (where published) and statewide, and add state preterm and infant mortality figures by race from NCHS/MSDH/March of Dimes sources.
2. Test whether the Black–White LBW gap varies with county poverty, segregation, primary care supply, or rurality.
3. Map obstetric access (hospitals with obstetric care, OB-GYN physicians, APN midwives) and the share of births in counties without it; test association with preterm birth and LBW after adjustment.

## Hypotheses and results
| # | Hypothesis | Test | Result |
|---|---|---|---|
| H1 | Black LBW exceeds White LBW in most counties | Paired Wilcoxon, counties with both values (CHR 2018–24) | **Supported.** Black higher in 77 of 77 counties; median 17.9% vs 8.78%; p = 2.5e-14. State: 17.65% vs 8.65% |
| H2 | Black teen birth rate exceeds White | Paired Wilcoxon | **Supported.** Black higher in 50 of 71 counties; median 33.4 vs 26.9 per 1,000; p = 9.8e-5. State 31.62 vs 21.08 |
| H3 | The Black–White LBW gap is larger in poorer, more segregated, or less-served counties | Spearman; OLS (HC3), n = 74 | **Not supported.** Gap uncorrelated with segregation (rho −0.02), Black child poverty (−0.003), PCP supply (−0.03); R² = 0.04. The gap is a near-uniform ~9 percentage points |
| H4 | Counties without a hospital offering obstetric care have higher preterm and LBW rates after adjustment | OLS and birth-weighted WLS (HC3) adjusting child poverty, % Black, nonmetro | **Not supported.** Preterm: OB hospital −0.08 pp (−0.93 to 0.77) OLS; WLS +0.26 (−0.54 to 1.06). LBW: +0.29 (−0.33 to 0.92) OLS; WLS +0.42 (−0.06 to 0.89). Unadjusted medians equal (preterm 17.0 vs 17.3%) |
| H5 (descriptive) | Obstetric services are concentrated in a minority of counties | Counts | **Supported.** 55 of 82 counties (67%) have no hospital with obstetric care and hold 37.5% of births; 42 (51%) have neither an obstetric hospital nor an OB-GYN, with 23.7% of births (76% nonmetro) |
| H6 (exploratory) | Teen birth rate is lower where an obstetric hospital exists | Mann-Whitney | **Supported unadjusted.** 29.2 vs 33.1 per 1,000; p = 0.0135 |
| State | Mississippi infant mortality and preterm birth exceed the US, with a Black–White gap | Published NCHS, MSDH and March of Dimes values | IMR 2022 9.11 (highest of any state; NVSR); Black 12.1 vs White 7.2 (MSDH, RR 1.68); preterm 2022–24 Black 18.5% vs White 12.7% (RR 1.46) |

County LBW tracks child poverty (rho 0.73) and % Black (rho 0.84); the % Black association is largely compositional (the county rate averages a high-LBW Black group and a lower-LBW White group), so it is not evidence of a county-level causal effect. County poverty alone: +2.31 pp LBW per 10 pp child poverty (1.85–2.77), R² = 0.62; adding % Black, poverty is no longer significant (+0.42; −0.46 to 1.31) while % Black is +0.92 per 10 pp (0.54–1.29), R² = 0.73.

## Data sources (all public; aggregates only)
| Source | URL | Years | Use |
|---|---|---|---|
| County Health Rankings 2025 and supplement (25 Mar 2026): NCHS natality and linked files | https://www.countyhealthrankings.org/health-data/methodology-and-sources/data-documentation | LBW and teen births 2018–2024; infant mortality 2017–2023 | County and race-specific outcomes (published counties only) |
| HRSA AHRF 2024–2025 | https://data.hrsa.gov/data/download?data=AHRF | OB-GYN MDs (AMA masterfile 2023); hospitals with obstetric care (AHA 2023); APN midwives with NPI 2023; 3-yr average births and preterm births 2021–23 (NCHS natality); population 2023 | Obstetric access, preterm births |
| NCHS NVSR 73(5), Infant Mortality in the US, 2022 | https://www.cdc.gov/nchs/data/nvsr/nvsr73/nvsr73-05.pdf | 2022 | State IMR (MS 9.11) |
| Mississippi State Department of Health, Child Death Review 2021–2022 | https://msdh.ms.gov/resources/media/21025.pdf | 2022; 2013–2022 | IMR by race (Black 12.1, White 7.2) |
| March of Dimes PeriStats (NCHS final natality) | https://www.marchofdimes.org/peristats/data?obj=1&reg=99&slev=4&sreg=28&stop=63&top=3 | 2022–2024 average | Preterm by race (Black 18.5%, White 12.7%) |
| NCHS VSRR 35, Births: Provisional Data for 2023 | https://www.cdc.gov/nchs/data/vsrr/vsrr035.pdf | 2023 | US preterm by race (Black 14.65%, White 9.45%); MS 14.95% |
| USDA RUCC 2023; Delta Regional Authority list; CDC PLACES 2025 | see `data-sources.md` | | Rurality, Delta indicator |

Reproducibility: `scripts/public-data/` (`p04.py`, `p04b.py`, `build_ahrf.py`, `build_master.py`) and `results/` here.

## Limits
- CHR race-specific county values are published only for larger counties (infant mortality: only 37 counties overall, 9 with both Black and White), so county results over-represent larger counties and infant mortality county analysis is not feasible.
- Ecological; compositional effects; no individual-level adjustment (age, parity, insurance, risk factors).
- AHRF county preterm % (births with gestation <37 weeks, 3-yr average 2021–23) gives a birth-weighted statewide figure of 16.9% vs the official NCHS state preterm rate of 14.95% (2023); definitions may differ, so the county preterm variable is used only for within-state comparisons.
- "Obstetric access" here is hospital obstetric care (AHA survey 2023), OB-GYN physicians (AMA masterfile) and NPI midwives; it excludes family physicians who deliver, birth centers, and distance to care, so it is narrower than the March of Dimes "maternity care desert" definition.
- State race comparisons use different periods (MSDH 2022; PeriStats 2022–24; US 2023) and are descriptive.
- CDC WONDER natality county/state queries are not available by API (national-only per CDC), and MSTAHRS is interactive; neither was scripted. [PENDING if Jake wants them done manually]
- PRAMS Mississippi data are not in the public data.cdc.gov PRAMStat files (2011 and earlier only); not used.

## Deferred / not used (UMMC RDW)
Per Jake's 2026-11-27 decision, Papers 02–05 use public data only. The earlier UMMC Patient Cohort Explorer request (delivery encounters by method and race; hypertensive disorders O10–O16, gestational diabetes O24, postpartum hemorrhage O72, preterm labor O60; postpartum visit within 12 weeks; insurance) is **not used**. It would add UMMC-only clinical outcomes and care-use patterns that public aggregates cannot show; it remains a possible later extension.

## Next actions
- [ ] Abstract trimmed to <=300 words (including section labels); Jake to review; 05 merge-into-02 vs drop pending Jake.
- [ ] Jake: review and edit the `draft-v1.md` abstract; choose venue (MAFP / Research Day).
- [ ] Optional manual: CDC WONDER natality (state level by race: preterm, prenatal care timing) and MSTAHRS county birth/infant death counts; suppress cells under 11.
- [ ] Optional: replace AHRF preterm variable with CDC WONDER county-group data for validation.

## Files
- `draft-v1.md` — abstract (draft-v1), intro, methods, results tables, discussion, references
- `results/p04_results.md` — CHR county Black–White analyses
- `results/p04b_results.md` — AHRF obstetric access analyses
- `results/p04_county_dataset.csv`, `results/p04_county_dataset_ahrf.csv` — county aggregates (82 rows)
