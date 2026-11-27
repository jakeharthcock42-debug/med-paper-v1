# Primary Care Physician Supply and the Black–White Gap in Premature Mortality Across Mississippi Counties: A Public-Data Ecological Analysis

**Status**: draft-v1 (2026-11-27). Values are published aggregates reproducible with `scripts/public-data/`. Public-data only (Jake's decision, 2026-11-27). **Novelty flag:** partial overlap with Lee et al. 2026 (county YPLL trends in Mississippi from the same CHR source).

## Abstract (draft-v1; ≤300 words incl. section labels; conference style)
**Background.** Mississippi has some of the highest premature mortality in the US, and Black residents bear a disproportionate share. Primary care supply is associated with lower population mortality nationally, but whether this holds for Black as well as White residents across Mississippi counties is unknown.

**Methods.** Ecological analysis of all 82 Mississippi counties using public aggregates: County Health Rankings (NCHS age-adjusted premature mortality [<75 years], 2021–2023, race-specific where published), HRSA Area Health Resources File (primary care physicians, MD+DO excluding residents, 2023), CDC PLACES, and USDA rural–urban codes. We compared Black and White county values with paired Wilcoxon tests and fit linear regression with robust standard errors, adjusting for child poverty, uninsurance, rurality, and percent Black, with separate models by race and for the Black–White gap.

**Results.** Black premature mortality exceeded White in 71 of 80 counties with both values published (median 742 vs 601 per 100,000; p<0.001); statewide rates were 715 vs 550 (ratio 1.30). Overall, primary care supply was not associated with premature mortality after adjustment (−3.6 per 100,000 per additional physician per 10,000 residents; 95% CI −13.9 to 6.7). By race, each additional physician per 10,000 was associated with 10.0 fewer premature deaths per 100,000 among White residents (95% CI −17.0 to −2.9; p=0.006) but not Black residents (+3.6; −6.1 to 13.3; p=0.47), so the gap was wider where supply was higher (+11.4; 0.8 to 22.0; p=0.035). Child poverty was the strongest correlate: +83 per 100,000 per 10 percentage points (95% CI 25 to 141).

**Conclusions.** The Black–White gap in premature mortality is present in nearly every county and is not closed by greater physician supply, which tracked White but not Black mortality. These ecological, exploratory findings need individual-level confirmation.

## 1. Introduction
Greater primary care physician supply has been associated with lower mortality across US counties (Basu 2019). Structural racism, including residential segregation, is a recognized driver of health inequity (Bailey 2017). Mississippi's premature mortality has been described at county level over time using County Health Rankings YPLL data (Lee 2026), which showed worsening statewide trends, rural hot spots in the Delta and spatial dependence, but that analysis did not stratify by race or evaluate primary care supply. We did not find (PubMed, 2026-11-27) a Mississippi analysis of primary care supply and the Black–White gap in premature mortality.

**Aims.** (1) Quantify the county-level Black–White gap. (2) Test whether primary care supply is associated with premature mortality overall and by race. (3) Test whether the gap varies with PCP supply, child poverty, % Black, and segregation.

**Hypotheses.** H1 Black premature mortality exceeds White in nearly all counties. H2 Greater PCP supply is associated with lower premature mortality after adjustment. H3 The association differs by race. H4 Child poverty is the dominant correlate of mortality and of the gap.

## 2. Methods
**Design.** Cross-sectional ecological analysis of public aggregate data (no patient-level or UMMC data).

**Sources.** County Health Rankings (2025 annual release; 25 March 2026 supplement): premature death (YPLL <75 per 100,000), age-adjusted premature mortality, and life expectancy for 2021–2023 (NCHS), race-specific values where published (unreliable or suppressed values excluded by CHR); child poverty 2023, uninsured 2023, unemployment 2023, residential segregation (Black/White index, ACS 2019–2023). HRSA AHRF 2024–2025: non-federal MD and DO primary care physicians excluding residents (2023; AMA masterfile) and Census 2023 population (rate per 10,000); primary care HPSA code (2025; descriptive). CDC PLACES 2025 release (BRFSS 2023; model-based; MRP) for chronic-disease prevalence. USDA RUCC 2023 (nonmetro 4–9); Delta Regional Authority county list.

**Analysis.** Paired Wilcoxon tests (counties with both values published). OLS with HC3 robust SEs of premature mortality on PCP per 10,000 adjusted for child poverty per 10 points, uninsured %, nonmetro, and (for overall) % Black; separate models for White and Black mortality; a gap model (Black − White) with PCP, child poverty, nonmetro, segregation; WLS weighted by county population as sensitivity. Chronic disease: Mann-Whitney and Spearman. Two-sided α=0.05; H2–H4 exploratory and unadjusted. Python (pandas, scipy, statsmodels); scripts in `scripts/public-data/`.

**Ethics.** Published aggregates only; no cell under 11 events reported. Confirm with UMMC IRB whether a determination letter is needed. [PENDING: IRB/RDW confirmation]

## 3. Results
**Table 1. Black–White premature mortality (counties with both published)**

| Measure | n | White median | Black median | Black worse | Wilcoxon p |
|---|---|---|---|---|---|
| Age-adjusted premature mortality /100k | 80 | 601 | 742 | 71 | 3e-12 |
| YPLL <75 /100k | 80 | 12,377 | 16,569 | 73 | 5e-13 |
| Life expectancy, years | 75 | 72.5 | 70.0 | 64 | 5e-10 |

State (CHR supplement 2021–23): premature mortality overall 600, White 550, Black 715 per 100k; YPLL 12,827 (White 11,187; Black 15,883); life expectancy 72.5 (White 73.6, Black 70.3).

**Table 2. Primary care physicians per 10,000 and premature mortality per 100,000 (OLS HC3; adjusted for child poverty/10, uninsured, nonmetro; overall also % Black)**

| Outcome | n | PCP/10k coefficient (95% CI) | p | Child poverty/10 coefficient (95% CI) |
|---|---|---|---|---|
| All | 82 | −3.6 (−13.9, 6.7) | 0.49 | 58.9 (−88.9, 206.6) |
| White | 80 | −10.0 (−17.0, −2.9) | 0.006 | 50.4 (23.2, 77.6) |
| Black | 81 | +3.6 (−6.1, 13.3) | 0.47 | 109.0 (67.4, 150.5) |

WLS (population-weighted): White −10.3 (−19.7, −0.9); Black −0.8 (−9.7, 8.0). Statewide 1,651 PCPs (MD+DO) for 2,939,690 residents = 5.6 per 10,000; 5 counties have none and 39 have fewer than 3 per 10,000.

**Table 3. Black–White gap (Black − White premature mortality) vs county context**

| Predictor | Spearman rho | p | OLS coefficient (95% CI) |
|---|---|---|---|
| PCP per 10k (AHRF) | 0.225 | 0.045 | +11.4 (0.8, 22.0) |
| Child poverty, % (per 10 pts in OLS) | 0.369 | 0.001 | +64.2 (31.6, 96.7) |
| % Black NH | 0.321 | 0.004 | — |
| Residential segregation | −0.004 | 0.972 | +1.1 (−1.9, 4.1) |

**Table 4. Chronic disease prevalence (PLACES, BRFSS 2023; model-based)**

| Condition | Delta (DRA) median | Non-DRA median | p | Spearman with PCP/10k |
|---|---|---|---|---|
| Diabetes | 15.3% | 13.5% | 0.00015 | −0.23 |
| Coronary heart disease | 7.1% | 6.6% | — | −0.36 |
| Stroke | 4.5% | 3.9% | — | −0.27 |
| High blood pressure | 44.3% | 41.3% | 3.9e-5 | −0.22 |

Full output: `results/p03_results.md`, `results/p03b_results.md`.

## 4. Discussion (outline)
- Principal findings: universal Black–White gap; null overall PCP association after poverty adjustment; PCP supply inversely related to White but not Black premature mortality; poverty explains the gap more than segregation or supply.
- Interpretation: physician supply may not reach Black residents equally (insurance, quality, trust, location within county); alternatively the race-specific analysis reflects confounding by urbanicity and noisy small-county Black rates. Cannot distinguish with ecological data.
- Limits: ecological; physician counts not FTE; no NPs/PAs; exploratory race-specific tests; PLACES circularity; period alignment.
- Next: add NP/PA supply; Medicaid/uninsurance by race; individual-level data.

## References (verified)
1. Basu S, Berkowitz SA, Phillips RL, Bitton A, Landon BE, Phillips RS. Association of primary care physician supply with population mortality in the United States, 2005–2015. *JAMA Intern Med.* 2019;179(4):506–514.
2. Bailey ZD, Krieger N, Agénor M, Graves J, Linos N, Bassett MT. Structural racism and health inequities in the USA: evidence and interventions. *Lancet.* 2017;389(10077):1453–1463.
3. Lee JE, Sung J, Lee JY, Barner Y, Offiah E, Hays A. Spatiotemporal modeling of premature mortality in Mississippi: a county-level analysis of years of potential life lost, 2015–2025. *Prev Chronic Dis.* 2026;23:E32. doi:10.5888/pcd23.260035
4. Greenlund KJ, Lu H, Wang Y, et al. PLACES: Local Data for Better Health. *Prev Chronic Dis.* 2022;19:210459.
5. County Health Rankings & Roadmaps. 2025 annual data and 25 March 2026 supplemental release. https://www.countyhealthrankings.org/
6. HRSA NCHWA. Area Health Resources Files 2024–2025. https://data.hrsa.gov/data/download?data=AHRF (accessed 2026-11-27).
