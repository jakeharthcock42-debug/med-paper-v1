# 03 — Primary Care Supply, Poverty, and the Black–White Gap in Premature Mortality Across Mississippi Counties

**Working title**: Primary Care Physician Supply, Socioeconomic Context, and the Black–White Gap in Premature Mortality and Chronic Disease Burden Across 82 Mississippi Counties  
**Status**: First-pass public-data analysis done (2026-11-26); draft skeleton in `draft-v1.md`; UMMC add-on requests ready to run  
**Target**: MAFP, ACP Mississippi, UMMC Research Day (primary care / internal medicine audience)  
**Public-data sufficiency**: Yes. All 82 counties; race-specific outcomes published for 80 counties.

## Research question
Across Mississippi counties, how large is the Black–White gap in premature mortality, and how much of county variation in premature mortality, the racial gap, and chronic disease prevalence is related to primary care physician (PCP) supply versus poverty, insurance, rurality, and Delta-region location?

## Specific aims
1. Quantify the Black–White gap in premature death (YPLL <75), age-adjusted premature mortality, and life expectancy across counties with both values published.
2. Test whether PCP supply is associated with county premature mortality independent of child poverty, uninsurance, rurality, racial composition, and Delta-region (DRA) status.
3. Test whether the Black–White gap is larger in counties with more residential segregation, lower PCP supply, or higher poverty.
4. Compare diabetes, coronary heart disease, stroke, hypertension, and obesity prevalence between DRA/non-DRA and nonmetro/metro counties.

## Hypotheses and planned tests (with first-pass status)
| # | Hypothesis | Planned test | First-pass result |
|---|---|---|---|
| H1 | Black premature mortality exceeds White in nearly all counties | Paired Wilcoxon across counties with both values | **Supported.** Median age-adjusted premature mortality 742 vs 601 per 100k (median county difference 148); Black higher in 71 of 80 counties; p = 3.0e-12. YPLL median 16,569 vs 12,377 (diff 4,391), 73 of 80 counties. Life expectancy median 70.0 vs 72.5 y; Black lower in 64 of 75 |
| H2 | Lower PCP supply is associated with higher premature mortality after adjusting for child poverty | OLS, HC3 robust SE | **Not supported.** PCP alone: −8.4 per 10 PCP/100k (95% CI −19.6 to 2.8), p = 0.142 (see note below); with child poverty: PCP −1.9 (95% CI −10.2 to 6.4), p = 0.66; child poverty +83.0 per 10 pts (24.6 to 141.4), p = 0.005; n = 79 |
| H3 | Black–White gap is larger where segregation is higher and PCP supply lower | Spearman; OLS | **Not supported for segregation or PCP.** Segregation rho −0.004 (p = 0.972); PCP rho 0.198 (p = 0.085). Gap rises with child poverty: rho 0.369 (p = 0.001); OLS +64.8 per 10 pts (29.3 to 100.3), p < 0.001, n = 77, R2 = 0.21 |
| H4 | Chronic disease prevalence is higher in DRA and nonmetro counties | Mann-Whitney | **Supported for DRA.** Diabetes median 15.3% vs 13.5% (p = 0.00015); CHD 7.1% vs 6.6% (p = 0.0007); stroke 4.5% vs 3.9% (p = 9e-5); hypertension 44.3% vs 41.3% (p = 4e-5). Nonmetro vs metro: diabetes p = 0.073; CHD p = 0.009; stroke p = 0.027 |

Note on units in H2: PCP coefficient is per 10 additional PCPs per 100,000 residents (PCP rate 2022; median county rate 35.6 per 100k). Exact model tables are in `results/p03_results.md`.

Primary tests for the abstract: H1 and H2. Others exploratory.

## Data sources (public; aggregates only)
| Source | URL | Years | Use |
|---|---|---|---|
| County Health Rankings supplemental release (25 Mar 2026) | https://www.countyhealthrankings.org/health-data/methodology-and-sources/data-documentation | Premature death, premature age-adjusted mortality, life expectancy 2021–2023 (NCHS), race-specific; PCP 2022 (AHRF/AMA); uninsured 2023 (SAHIE); preventable stays 2023 (Medicare) | Outcomes, access |
| CHR 2025 annual release (analytic_data2025_v3.csv) | same page | Child poverty, % Black NH, residential segregation, median income, % rural (measure-level years per CHR 2025 documentation) [year-by-measure PENDING] | Covariates |
| CDC PLACES county 2025 release | https://data.cdc.gov/d/swc5-untb | BRFSS 2023 | Diabetes, CHD, stroke, hypertension, obesity |
| USDA ERS RUCC 2023 | https://www.ers.usda.gov/data-products/rural-urban-continuum-codes | 2023 | Metro/nonmetro |
| Delta Regional Authority list | https://dra.gov/wp-content/uploads/2022/04/Mississippi.pdf | 2016–2024 | DRA indicator (47 counties) |
| MSTAHRS | https://mstahrs.msdh.ms.gov/ | 2023–2024 available | [PENDING] cause-specific (diabetes, heart disease) death counts by race/county |

## Feasibility notes and limits
- Ecological design; county associations do not imply individual effects.
- **PLACES caveat**: PLACES models include county-level poverty (Greenlund 2022), so PLACES–poverty correlations (e.g., diabetes vs child poverty rho 0.915) are partly built-in. Use CHR/NCHS mortality (not modeled) as the primary outcome; treat PLACES results as descriptive.
- Race-specific CHR values are published only where reliable; gap analysis is restricted to counties with both values (n = 80), which favors larger counties.
- PCP supply is an imperfect access measure (2022 AMA/AHRF data; excludes NP/PA; 1 county has a rate of 0; 3 counties missing). `otherpcp_per100k` is available in the county dataset for a sensitivity analysis [PENDING].
- Segregation index direction/definition per CHR (Black/White index of dissimilarity) [verify definition before reporting].
- MSTAHRS cause-specific mortality would sharpen the diabetes/CVD angle but is interactive (not scripted) [PENDING].

## Next actions
- [ ] Add NP/PA ("other primary care providers") sensitivity model.
- [ ] [PENDING] HRSA HPSA primary care designations by county (https://data.hrsa.gov/data/download) as an alternative access measure.
- [ ] [PENDING] MSTAHRS: diabetes (E10–E14) and heart disease deaths by race and county/region, 2020–2024.
- [ ] Spatial sensitivity (Delta vs non-Delta stratified models).
- [ ] Draft abstract around H1 + H2 + the poverty finding.

## Optional UMMC RDW add-on (data-use cleared by Jake 2026-11-26; ready to run)
Aggregates only; suppress cells under 11; one selection per box.
1. Diagnosis code **E11.9** (type 2 diabetes without complications) and, separately, **E11.65** (with hyperglycemia): total patients; by race (Black / White / other); by age group (<45, 45–64, 65+).
2. Within each: patients with ≥1 Family Medicine or Internal Medicine outpatient encounter (use Encounter/Department filters if available) vs none, by race.
3. If the Lab box permits: patients with HbA1c result ≥9.0% vs <9.0%, by race.
4. Same structure for **I10** (essential hypertension): total, by race, with/without a primary care encounter.
5. ED encounters: patients with E11.9 and ≥1 ED encounter, by race.
Use: UMMC clinical-population corroboration of the county-level Black–White gap and primary care contact.

## Files
- `draft-v1.md`, `results/p03_results.md`, `results/p03_county_dataset.csv`
