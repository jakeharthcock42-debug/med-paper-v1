# 04 — Maternal and Infant Outcome Disparities in Mississippi Counties

**Working title**: Racial Disparities in Low Birth Weight, Teen Births, and Infant Mortality Across Mississippi Counties: The Role of Poverty, Rurality, Delta Region, and Primary Care Access  
**Status**: First-pass public-data analysis done (2026-11-26); draft skeleton in `draft-v1.md`; UMMC add-on requests ready to run  
**Target**: UMMC Research Day, MAFP (family medicine/OB), ACP Mississippi  
**Public-data sufficiency**: Yes for low birth weight and teen births (80+ counties). Infant mortality is published for only 37 counties overall (20 Black, 12 White), so it is a secondary outcome.

## Research question
How large are Black–White differences in low birth weight (LBW), teen births, and infant mortality across Mississippi counties, and are county LBW levels and the racial gap related to poverty, % Black population, rurality, Delta region, PCP supply, and residential segregation?

## Specific aims
1. Describe Black vs White LBW, teen birth rate, and infant mortality statewide and across counties.
2. Model county LBW on poverty, PCP supply, racial composition, rurality, and DRA status.
3. Test whether the Black–White LBW gap varies with segregation, Black child poverty, PCP supply, or rurality.
4. (Optional UMMC add-on) Describe delivery and pregnancy-complication counts by race at UMMC.

## Hypotheses and planned tests (with first-pass status)
| # | Hypothesis | Planned test | First-pass result |
|---|---|---|---|
| H1 | Black LBW exceeds White LBW in essentially every county | Paired Wilcoxon (counties with both values) | **Supported.** Median 17.9% vs 8.8% (median difference 8.96 points); Black higher in 77 of 77 counties; p = 2.5e-14. State (CHR, 2018–2024): 17.65% vs 8.65% |
| H2 | Teen birth rate is higher among Black than White females | Paired Wilcoxon | **Supported.** Median 33.4 vs 26.9 per 1,000; Black higher in 50 of 71 counties; p = 9.8e-5. State: 31.62 vs 21.08 |
| H3 | Infant mortality is higher for Black infants | Paired Wilcoxon (n small) | **Supported but tiny n.** 9 counties with both values: medians 11.5 vs 6.37 per 1,000; Black higher in 9 of 9; p = 0.0039. State (2017–2023): 11.95 vs 6.37 |
| H4 | County LBW rises with child poverty and falls with PCP supply | OLS (HC3) | **Poverty supported; PCP not.** Poverty +2.31 points per 10 points child poverty (95% CI 1.85–2.77); PCP coefficient positive (+0.21 per +1 PCP/10,000; p = 0.001) in the simple model; in the full model (n = 78, R2 = 0.73) poverty +0.42 (p = 0.35), % Black +0.92 per 10 points (95% CI 0.54–1.29), PCP +0.07 (p = 0.31) |
| H5 | The Black–White LBW gap is larger where segregation is higher or Black child poverty is higher | Spearman; OLS | **Not supported.** Segregation rho −0.020 (p = 0.862); Black child poverty rho −0.003 (p = 0.982); OLS R2 = 0.04. The gap is roughly uniform across county contexts |

Primary tests for the abstract: H1 and H4. Others exploratory.

## Data sources (public; aggregates only)
| Source | URL | Years | Use |
|---|---|---|---|
| County Health Rankings supplemental release (25 Mar 2026): Low Birth Weight (v037), Teen Births (v014), Infant Mortality (v129) with White/Black values | https://www.countyhealthrankings.org/health-data/methodology-and-sources/data-documentation | LBW 2018–2024, teen births 2018–2024 (NCHS natality), infant mortality 2017–2023 | Outcomes |
| CHR 2025 annual release | same | Child poverty (overall and Black), % Black NH, segregation, income, education (measure years per CHR 2025 documentation) [year-by-measure PENDING] | Covariates |
| CDC PLACES 2025 | https://data.cdc.gov/d/swc5-untb | BRFSS 2022–2023 | Context |
| USDA ERS RUCC 2023; DRA list | https://www.ers.usda.gov/data-products/rural-urban-continuum-codes ; https://dra.gov/wp-content/uploads/2022/04/Mississippi.pdf | 2023 / 2016–2024 | Rural/Delta |
| MSTAHRS (births by race/county/age; infant deaths; pregnancy outcomes) | https://mstahrs.msdh.ms.gov/ | through 2024 | [PENDING] preterm birth, prenatal care, cesarean by race/county (interactive; cells <5 suppressed by MSTAHRS, we suppress <11) |
| CDC WONDER natality | https://wonder.cdc.gov/natality.html | 2016–2024 | [PENDING] county-level data suppressed for small counties; interactive; API is national-only |
| HRSA Area Health Resource File (OB-GYN supply, hospitals with obstetrics) | https://data.hrsa.gov/topics/health-workforce/ahrf | latest | [PENDING] OB access measure |
| March of Dimes maternity care deserts | https://www.marchofdimes.org/maternity-care-deserts-report | latest report | [PENDING] verify and download |

## Feasibility notes and limits
- County LBW and teen births are published for ~80 counties. Infant mortality is too sparse for a county-level paper; use state-level and the 9 paired counties only descriptively.
- LBW is strongly correlated with % Black NH (rho 0.844) and child poverty (0.732); the full model shows % Black retains a large coefficient after poverty, but this is ecological and cannot separate individual-level factors. Avoid interpreting % Black as an individual race effect; discuss structural racism (Bailey 2017).
- The positive PCP coefficient in the simple model reflects confounding (high-need counties); do not interpret causally.
- Preterm birth, prenatal care timing, cesarean, and maternal morbidity/mortality need MSTAHRS/WONDER or UMMC data [PENDING].
- Public county race-specific values exclude unreliable cells, so they over-represent larger counties.

## Next actions
- [ ] [PENDING] MSTAHRS queries (Jake or a later worker): births by race and county region — preterm (<37 wk), LBW, prenatal care first trimester, cesarean; 2019–2024. Suppress cells under 11.
- [ ] [PENDING] HRSA AHRF / March of Dimes OB access measure by county.
- [ ] Sensitivity: add Medicaid/uninsured women measure [PENDING source].
- [ ] Run UMMC add-on if a local delivery-service angle is wanted.

## Optional UMMC RDW add-on (data-use cleared by Jake 2026-11-26; ready to run)
Aggregates only; suppress cells under 11; one selection per box.
1. Diagnosis **O80** (single full-term spontaneous delivery) or **Z37.0** (single live birth): total patients and by race (Black / White / other), age group (<20, 20–34, 35+).
2. Preterm and complication counts, one code per query, by race: **O60.1x** (preterm labor with preterm delivery), **O14.x** (pre-eclampsia; run O14.90 and O14.00 separately), **O24.4x** (gestational diabetes), **O99.0x** (anemia complicating pregnancy), **O10.x** (pre-existing hypertension).
3. Newborn: **P07.1x** (low birth weight) and **P07.3x** (other preterm) by maternal race if the Explorer links; otherwise infant race.
4. Postpartum: **Z39.2** (routine postpartum follow-up) as a proxy for postpartum visit; counts by race.
Use: UMMC-specific disparity table for obstetric complications that complements the county LBW findings.

## Files
- `draft-v1.md`, `results/p04_results.md`, `results/p04_county_dataset.csv`
