# Racial and Geographic Disparities in Oral Cavity and Pharynx Cancer in Mississippi

**Status**: Skeleton v1 (2026-11-26). Numbers in Results are intentionally empty; first-pass values live in `results/p02_results.md` and must be re-verified before they go into any abstract.

## Abstract (skeleton)
**Background.** Oral cavity and pharynx cancers are strongly tobacco- and alcohol-associated. [PENDING: one-sentence Mississippi burden from verified SCP figures.]  
**Objective.** To describe racial and rural–urban differences in incidence, stage at diagnosis, and mortality in Mississippi.  
**Methods.** Ecological analysis of State Cancer Profiles (NPCR incidence 2019–2023; NCHS mortality 2020–2024) for Mississippi and its 82 counties, linked to USDA RUCC 2023, CDC PLACES 2025, and County Health Rankings.  
**Results.** [PENDING]  
**Conclusions.** [PENDING]

## 1. Introduction
Head and neck cancers have a large attributable fraction from tobacco and alcohol. In a pooled analysis of 17 case-control studies in the INHANCE consortium, tobacco or alcohol use accounted for an estimated 72% of head and neck cancers overall, 64% of oral cavity cancers, and 72% of pharyngeal cancers, and a substantial share of oral cavity cancers could not be attributed to either exposure (Hashibe 2009). Nationally, rural populations have higher incidence of tobacco-associated cancers, which include oral cavity and pharynx cancer, than urban populations (Zahnd 2018).

Mississippi combines high smoking prevalence, a predominantly rural population, and large racial differences in health outcomes. [PENDING: add a verified citation on Mississippi smoking prevalence and rural share, e.g., CDC BRFSS and Census.] Public county-level registry data allow these patterns to be described, but county estimates for a rare cancer are often suppressed, so race-specific and rural–urban comparisons need to be framed carefully.

**Gap.** Mississippi-specific, race-stratified oral cavity and pharynx cancer data on incidence, stage, and the mortality-to-incidence relationship are not summarized together in the abstracts and papers we have reviewed. [PENDING: complete a literature search (PubMed: "oral cavity pharynx cancer Mississippi") before claiming novelty.]

**Aims.** (1) Compare Black and White non-Hispanic incidence, late-stage share, and mortality statewide. (2) Compare rural and metro county incidence. (3) Examine county correlates (smoking, alcohol, insurance, primary care and dentist supply, poverty). (4) [Optional] Describe UMMC patients with oropharyngeal and oral cavity cancer.

**Hypotheses.** H1 Black NH incidence is lower and mortality is similar or higher than White NH (higher mortality-to-incidence ratio). H2 Late-stage share is higher in Black NH. H3 Nonmetro counties have higher incidence. H4 County incidence rises with smoking and binge drinking and falls with PCP and dentist supply.

## 2. Methods
**Design.** Cross-sectional ecological analysis of publicly available aggregate data; no patient-level data. The optional UMMC component, if run, uses only aggregate counts from the UMMC Patient Cohort Explorer with cells under 11 suppressed.

**Data sources.**
- *State Cancer Profiles* (https://statecancerprofiles.cancer.gov/): Oral Cavity & Pharynx (cancer code 003); age-adjusted incidence 2019–2023 (NPCR 2025 submission), age-adjusted mortality 2020–2024, late-stage (regional + distant) incidence and percent late stage; all races, White NH, Black NH; both sexes and male. SCP suppresses cells with fewer than 16 cases in 5 years.
- *USDA ERS Rural-Urban Continuum Codes 2023* (metro = 1–3; nonmetro = 4–9).
- *CDC PLACES 2025 release* (https://data.cdc.gov/d/swc5-untb): age-adjusted adult prevalence of current smoking, binge drinking, lack of insurance (18–64), all teeth lost (≥65). PLACES estimates are model-based (Greenlund 2022).
- *County Health Rankings supplemental release (March 2026)*: primary care physicians per 100,000 (2022), dentists per 100,000 (2023); 2025 annual release for child poverty and % Black.
- *Delta Regional Authority* county list for the Delta indicator.

**Analysis.** State rates are as published. Black/White rate ratios and approximate 95% CIs were derived from published rate CIs on the log scale. Late-stage proportions were compared with a chi-square test using counts reconstructed from published average annual counts × 5 (approximate; stated as such). County analyses were restricted to counties with a published (unsuppressed) rate. Rural vs metro: Mann-Whitney and weighted least squares (weights = average annual count; HC3 robust SEs). Correlates: Spearman and OLS with HC3 robust SEs. Primary tests: H1 and H2. H3–H4 and secondary tests are exploratory; two-sided α = 0.05, unadjusted unless stated. Python (pandas, scipy, statsmodels); scripts in `scripts/public-data/`.

**Suppression and ethics.** Only published aggregates are used. No cell with fewer than 11 events is reported from public sources; UMMC cells under 11 are suppressed. [PENDING: confirm with UMMC IRB/RDW team whether a determination letter is needed for the abstract.]

## 3. Results (tables to populate from `results/p02_results.md` after verification)

**Table 1. Mississippi oral cavity & pharynx cancer by race/ethnicity**

| Group | Incidence/100k (95% CI) | Mortality/100k (95% CI) | % late stage | Mortality-to-incidence ratio |
|---|---|---|---|---|
| All races | [PENDING] | [PENDING] | [PENDING] | [PENDING] |
| White NH | [PENDING] | [PENDING] | [PENDING] | [PENDING] |
| Black NH | [PENDING] | [PENDING] | [PENDING] | [PENDING] |
| United States (all races) | [PENDING] | [PENDING] | [PENDING] | [PENDING] |

**Table 2. County incidence by metro status (counties with published rates)**

| Group | n counties | Median (IQR) | Test |
|---|---|---|---|
| Metro (RUCC 1–3) | [PENDING] | [PENDING] | [PENDING] |
| Nonmetro (RUCC 4–9) | [PENDING] | [PENDING] | [PENDING] |

**Table 3. County correlates of incidence (Spearman)**

| Variable | n | rho | p |
|---|---|---|---|
| Current smoking | [PENDING] | [PENDING] | [PENDING] |
| Binge drinking | [PENDING] | [PENDING] | [PENDING] |
| PCP per 100k | [PENDING] | [PENDING] | [PENDING] |
| Dentists per 100k | [PENDING] | [PENDING] | [PENDING] |

**Table 4 (optional UMMC).** Patients by code × race × specialty encounter; cells under 11 suppressed. [PENDING]

## 4. Discussion (outline)
- Principal findings [PENDING].
- If H1–H2 hold: lower incidence with similar mortality implies worse outcomes after diagnosis, pointing toward stage at diagnosis and access to treatment; frame as hypothesis-generating.
- Limits: suppression, ecological design, no subsite or HPV information, model-based covariates, period mismatch.
- Implications: dental/primary-care visits as an oral-cancer screening touchpoint [PENDING citation]; UMMC head and neck oncology referral patterns.

## References (verified)
1. Hashibe M, Brennan P, Chuang SC, et al. Interaction between tobacco and alcohol use and the risk of head and neck cancer: pooled analysis in the International Head and Neck Cancer Epidemiology Consortium. *Cancer Epidemiol Biomarkers Prev.* 2009;18(2):541–550. https://pubmed.ncbi.nlm.nih.gov/19190158/
2. Zahnd WE, James AS, Jenkins WD, et al. Rural–urban differences in cancer incidence and trends in the United States. *Cancer Epidemiol Biomarkers Prev.* 2018;27(11):1265–1274. doi:10.1158/1055-9965.EPI-17-0430
3. Greenlund KJ, Lu H, Wang Y, et al. PLACES: Local Data for Better Health. *Prev Chronic Dis.* 2022;19:210459. doi:10.5888/pcd19.210459
4. National Cancer Institute and CDC. State Cancer Profiles. https://statecancerprofiles.cancer.gov/ (accessed 2026-11-26).
