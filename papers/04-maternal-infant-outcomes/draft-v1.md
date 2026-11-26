# Racial Disparities in Low Birth Weight, Teen Births, and Infant Mortality Across Mississippi Counties

**Status**: Skeleton v1 (2026-11-26). Results tables intentionally empty; first-pass values are in `results/p04_results.md` and must be re-verified before use.

## Abstract (skeleton)
**Background.** Black women in the United States have markedly higher pregnancy-related mortality than White women, and rural loss of obstetric services is linked to worse birth outcomes. [PENDING]  
**Objective.** To quantify Black–White differences in low birth weight (LBW), teen births, and infant mortality across Mississippi counties and test county correlates.  
**Methods.** Ecological analysis of County Health Rankings natality and mortality measures (NCHS; LBW and teen births 2018–2024; infant mortality 2017–2023) for 82 counties, linked to poverty, racial composition, rurality, Delta-region status, PCP supply, and residential segregation.  
**Results.** [PENDING]  
**Conclusions.** [PENDING]

## 1. Introduction
Racial disparities in maternal outcomes are large and persistent. From 2007 to 2016, US pregnancy-related mortality was 16.7 deaths per 100,000 live births overall, 40.8 for Black women (3.2 times the 12.7 for White women), and the disparity persisted across age groups and education levels, including among college-educated Black women (Petersen 2019). Biosocial pathways, including stress and structural factors, have been proposed to explain racial differences in preterm birth [PENDING: add a verified citation], and structural racism is a recognized driver of health inequities (Bailey 2017).

Geography matters as well. Among rural US counties not adjacent to urban areas, loss of hospital-based obstetric services was associated with a 0.67 percentage-point increase in preterm births and a 3.06 percentage-point increase in births at hospitals without obstetric units (Kozhimannil 2018). Mississippi is predominantly rural, has a large Black population, and has high poverty. [PENDING: verified Mississippi LBW/infant mortality citation, e.g., CDC NCHS state profiles.]

**Gap.** County-level Black–White differences in LBW, teen births and infant mortality in Mississippi, and whether the gap varies with poverty, segregation, or primary care supply, are not summarized in the sources reviewed to date. [PENDING: PubMed search before claiming novelty.]

**Aims and hypotheses.** H1 Black LBW exceeds White LBW in nearly all counties. H2 Teen birth rates are higher for Black than White females. H3 Black infant mortality exceeds White. H4 County LBW rises with child poverty. H5 The Black–White LBW gap is larger where segregation or Black child poverty is higher.

## 2. Methods
**Design.** Cross-sectional ecological analysis, 82 Mississippi counties.  
**Outcomes.** LBW (% of live births <2,500 g), teen birth rate per 1,000 females 15–19, infant mortality per 1,000 live births; overall and for White and Black mothers/infants where published by CHR (suppressed or unreliable values excluded by CHR). Source: CHR supplemental release, 25 March 2026 (NCHS natality and linked files).  
**Covariates.** Child poverty (overall and Black), % non-Hispanic Black, Black/White residential segregation index, PCP per 100,000 (2022), uninsured, nonmetro (RUCC 2023), Delta (DRA county), high school completion, median household income.  
**Analysis.** Paired Wilcoxon tests (counties with both values); Spearman correlations; OLS with HC3 robust standard errors for county LBW and for the Black–White LBW gap (Black minus White, percentage points). Primary: H1 and H4. Other tests exploratory; α = 0.05, unadjusted.  
**Ethics.** Public aggregates only. [PENDING: IRB/non-human-subjects confirmation.]

## 3. Results (tables to populate after verification)

**Table 1. Black vs White outcomes (counties with both values)**

| Measure | n | White median | Black median | Median diff | Counties Black higher | p |
|---|---|---|---|---|---|---|
| LBW % | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] |
| Teen births /1,000 | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] |
| Infant deaths /1,000 | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] |

**Table 2. Mississippi state values (All / White / Black)** [PENDING]

**Table 3. OLS: county LBW %**

| Predictor | Model 1 coef (95% CI) | Model 2 coef (95% CI) |
|---|---|---|
| Child poverty (per 10 pts) | [PENDING] | [PENDING] |
| PCP per 10,000 | [PENDING] | [PENDING] |
| % Black NH (per 10 pts) | — | [PENDING] |
| Nonmetro | — | [PENDING] |
| Delta county | — | [PENDING] |

**Table 4. Correlates of the Black–White LBW gap** [PENDING]

**Table 5 (optional UMMC).** Delivery and complication counts by race; cells under 11 suppressed. [PENDING]

## 4. Discussion (outline)
- Principal findings [PENDING]; uniform gap across county contexts would suggest factors not captured by county poverty or segregation measures.
- Limits: ecological; race-specific county data sparse; no preterm or prenatal care data in this version; CHR measure definitions.
- Next: MSTAHRS preterm and prenatal care, OB access measure, UMMC obstetric complications.

## References (verified)
1. Petersen EE, Davis NL, Goodman D, et al. Racial/ethnic disparities in pregnancy-related deaths — United States, 2007–2016. *MMWR Morb Mortal Wkly Rep.* 2019;68(35):762–765. doi:10.15585/mmwr.mm6835a3
2. Kozhimannil KB, Hung P, Henning-Smith C, Casey MM, Prasad S. Association between loss of hospital-based obstetric services and birth outcomes in rural counties in the United States. *JAMA.* 2018;319(12):1239–1247. doi:10.1001/jama.2018.1830
3. Bailey ZD, Krieger N, Agénor M, Graves J, Linos N, Bassett MT. Structural racism and health inequities in the USA: evidence and interventions. *Lancet.* 2017;389(10077):1453–1463. doi:10.1016/S0140-6736(17)30569-X
4. County Health Rankings & Roadmaps supplemental release (25 March 2026). https://www.countyhealthrankings.org/health-data/methodology-and-sources/data-documentation
