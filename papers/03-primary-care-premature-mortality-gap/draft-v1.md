# Primary Care Supply, Poverty, and the Black–White Gap in Premature Mortality Across Mississippi Counties

**Status**: Skeleton v1 (2026-11-26). Results tables intentionally empty; first-pass values are in `results/p03_results.md` and must be re-verified before use.

## Abstract (skeleton)
**Background.** Greater primary care physician supply is associated with lower population mortality nationally; Mississippi has large racial gaps in health outcomes. [PENDING]  
**Objective.** To test whether county PCP supply, poverty, uninsurance, rurality, and Delta-region location explain county premature mortality and the Black–White gap.  
**Methods.** Ecological analysis of all 82 Mississippi counties using County Health Rankings (2021–2023 mortality), CDC PLACES 2025, USDA RUCC, and Delta Regional Authority designation.  
**Results.** [PENDING]  
**Conclusions.** [PENDING]

## 1. Introduction
Primary care supply matters for population health. In a national county-level analysis, each additional 10 primary care physicians per 100,000 population was associated with a 51.5-day increase in life expectancy and 0.9% to 1.4% lower cardiovascular, cancer, and respiratory mortality (Basu 2019). Structural factors, including residential segregation and unequal access to care, are proposed drivers of racial health inequities in the United States (Bailey 2017).

Mississippi has persistently high premature mortality and large racial differences. [PENDING: add verified citation(s) for Mississippi life expectancy/premature mortality ranking and for Mississippi PCP workforce.] Whether primary care supply tracks premature mortality within a single high-burden, majority-rural state, and whether it relates to the Black–White gap, is not established in the sources reviewed to date. [PENDING: PubMed search "Mississippi primary care supply mortality county" before claiming novelty.]

**Aims and hypotheses.** H1 Black premature mortality exceeds White in nearly all counties. H2 Lower PCP supply is associated with higher premature mortality after adjustment for child poverty. H3 The Black–White gap is larger where segregation is higher and PCP supply lower. H4 Chronic disease prevalence (diabetes, CHD, stroke) is higher in Delta-region and nonmetro counties.

## 2. Methods
**Design.** Cross-sectional ecological analysis of public aggregate data for 82 Mississippi counties (FIPS 28001–28163).  
**Outcomes.** Age-adjusted premature mortality per 100,000 and years of potential life lost before 75 per 100,000 (NCHS via CHR supplemental release, 2021–2023), overall and for Black and White residents where published; life expectancy; PLACES age-adjusted prevalence of diagnosed diabetes, coronary heart disease, stroke, high blood pressure, and obesity (BRFSS 2023).  
**Exposures and covariates.** PCP per 100,000 (2022 AHRF/AMA), child poverty, uninsured, % non-Hispanic Black, Black/White residential segregation index, nonmetro (RUCC 4–9, 2023), Delta (DRA-designated county, 47 in Mississippi).  
**Analysis.** (1) Paired Wilcoxon signed-rank tests of Black vs White outcomes in counties with both values. (2) OLS with HC3 robust standard errors for county premature mortality on PCP supply with sequential adjustment (child poverty; then uninsured, nonmetro, % Black; then DRA). (3) Spearman correlations and OLS for the Black–White gap (Black minus White premature mortality). (4) Mann-Whitney comparisons of PLACES prevalences by DRA and metro status. Primary tests: H1 and H2. Others exploratory; two-sided α = 0.05, unadjusted. PLACES estimates are model-based and include county poverty as a model input (Greenlund 2022); PLACES–poverty associations are interpreted descriptively.  
**Ethics.** Public aggregate data only. [PENDING: confirm exempt/non-human-subjects status with UMMC IRB for the abstract.]

## 3. Results (tables to populate after verification)

**Table 1. Premature mortality by race (counties with both values)**

| Measure | n counties | White median | Black median | Median difference | Counties Black worse | p |
|---|---|---|---|---|---|---|
| Age-adjusted premature mortality /100k | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] |
| YPLL <75 /100k | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] |
| Life expectancy (y) | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] |

**Table 2. OLS: premature mortality ~ PCP supply and covariates**

| Model | PCP coefficient (95% CI) | Child poverty coefficient (95% CI) | n | R2 |
|---|---|---|---|---|
| 1 PCP only | [PENDING] | — | [PENDING] | [PENDING] |
| 2 + child poverty | [PENDING] | [PENDING] | [PENDING] | [PENDING] |
| 3 + uninsured, nonmetro, % Black | [PENDING] | [PENDING] | [PENDING] | [PENDING] |
| 4 + Delta county | [PENDING] | [PENDING] | [PENDING] | [PENDING] |

**Table 3. Chronic disease prevalence (PLACES) by Delta and metro status**

| Condition | DRA median | non-DRA median | p | Nonmetro median | Metro median | p |
|---|---|---|---|---|---|---|
| Diabetes | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] |
| CHD | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] |
| Stroke | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] |

**Table 4. Correlates of the Black–White gap** [PENDING]

## 4. Discussion (outline)
- Principal findings [PENDING].
- If PCP supply is not independently associated with mortality once poverty is accounted for, this is compatible with ecological confounding by poverty and with PCP counts being a crude access measure; avoid causal language.
- Limits: ecological fallacy; race-specific estimates only where reliable; PCP measure excludes NP/PA; model-based PLACES; cross-sectional.
- Implications for primary care workforce and social-needs interventions [PENDING citations].

## References (verified)
1. Basu S, Berkowitz SA, Phillips RL, Bitton A, Landon BE, Phillips RS. Association of primary care physician supply with population mortality in the United States, 2005–2015. *JAMA Intern Med.* 2019;179(4):506–514. doi:10.1001/jamainternmed.2018.7624
2. Bailey ZD, Krieger N, Agénor M, Graves J, Linos N, Bassett MT. Structural racism and health inequities in the USA: evidence and interventions. *Lancet.* 2017;389(10077):1453–1463. doi:10.1016/S0140-6736(17)30569-X
3. Greenlund KJ, Lu H, Wang Y, et al. PLACES: Local Data for Better Health. *Prev Chronic Dis.* 2022;19:210459. doi:10.5888/pcd19.210459
4. County Health Rankings & Roadmaps. Analytic data, 2025 annual release and March 2026 supplemental release. https://www.countyhealthrankings.org/health-data/methodology-and-sources/data-documentation
