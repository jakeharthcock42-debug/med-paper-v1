# County-Level Cancer Screening, Primary Care Access, and Late-Stage Colorectal and Breast Cancer in Mississippi

**Status**: Skeleton v1 (2026-11-26). Results tables intentionally empty; first-pass values are in `results/p05_results.md` and must be re-verified before use.

## Abstract (skeleton)
**Background.** Colorectal cancer screening is recommended for average-risk adults aged 45–75. Rural residents have higher incidence of colorectal and cervical cancers, which are amenable to screening. [PENDING]  
**Objective.** To test whether county screening is lower in Delta and rural Mississippi, is related to primary care supply, and is associated with stage and mortality.  
**Methods.** Ecological analysis of CDC PLACES 2025 screening estimates, CHR Medicare mammography (2023), and State Cancer Profiles stage and mortality (2019–2024) for 82 counties, with PCP supply, uninsurance, poverty, USDA RUCC and Delta Regional Authority status.  
**Results.** [PENDING]  
**Conclusions.** [PENDING]

## 1. Introduction
The US Preventive Services Task Force recommends colorectal cancer screening for average-risk, asymptomatic adults aged 45 to 75 years (Grade A for 50–75, Grade B for 45–49), using stool-based tests, CT colonography, flexible sigmoidoscopy, or colonoscopy (USPSTF 2021). Rural populations in the United States have higher incidence of colorectal and cervical cancers, cancers for which screening is effective, as well as higher incidence of tobacco-associated and HPV-associated cancers (Zahnd 2018).

Local screening estimates are rarely measured directly. CDC PLACES provides model-based county estimates from BRFSS using multilevel regression and poststratification with age, sex, race/ethnicity, education, and county poverty (Greenlund 2022); claims-based measures such as Medicare fee-for-service mammography provide a less model-dependent comparison. [PENDING: verified Mississippi screening-rate citation, e.g., BRFSS state estimates.]

**Gap.** Whether, within Mississippi, county screening tracks primary care supply and relates to stage and mortality, particularly in the Delta, is not established in the sources reviewed to date. [PENDING: PubMed search before claiming novelty.]

**Aims and hypotheses.** H1 Screening is lower in DRA (Delta) and nonmetro counties. H2 Screening rises with PCP supply and falls with uninsurance and poverty. H3 Higher screening is associated with lower late-stage share and mortality. H4 Black women have lower Medicare mammography than White women.

## 2. Methods
**Design.** Cross-sectional ecological analysis, 82 Mississippi counties.  
**Screening measures.** PLACES age-adjusted prevalence: colorectal screening (adults 45–75; 2022), mammography use (women 50–74; 2022), cholesterol screening and routine checkup (2023). CHR Medicare fee-for-service mammography (women 65–74; 2023) and flu vaccination, overall and White/Black.  
**Outcomes.** State Cancer Profiles: colorectal and female breast cancer incidence and late-stage (regional + distant) share, 2019–2023; mortality 2020–2024; counties with suppressed values (fewer than 16 cases in 5 years) excluded; mortality-to-incidence ratio is the ratio of published age-adjusted rates (descriptive).  
**Covariates.** PCP per 100,000 (2022), uninsured (2023), child poverty, % Black NH, median household income, nonmetro (RUCC 2023), Delta (DRA county).  
**Analysis.** Mann-Whitney (DRA, nonmetro); Spearman correlations; OLS with HC3 robust SE for Medicare mammography; paired Wilcoxon for Black vs White Medicare measures. Primary: H2 (CHR mammography model) and H3 (CHR mammography vs stage). Others exploratory; α = 0.05, unadjusted. PLACES-based associations are descriptive because the model uses demographic inputs.  
**Ethics.** Public aggregates only. [PENDING: IRB/non-human-subjects confirmation.]

## 3. Results (tables to populate after verification)

**Table 1. Screening by Delta and metro status**

| Measure | DRA median | non-DRA median | p | Nonmetro median | Metro median | p |
|---|---|---|---|---|---|---|
| CRC screening (PLACES) | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] |
| Mammography (CHR Medicare) | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] |
| Mammography (PLACES) | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] |

**Table 2. OLS: Medicare mammography ~ PCP, child poverty, uninsured, nonmetro, DRA** [PENDING]

**Table 3. Screening vs stage and mortality (Spearman)**

| Screening | Outcome | n | rho | p |
|---|---|---|---|---|
| CHR mammography | Breast % late stage | [PENDING] | [PENDING] | [PENDING] |
| CHR mammography | Breast mortality | [PENDING] | [PENDING] | [PENDING] |
| PLACES CRC screening | CRC % late stage | [PENDING] | [PENDING] | [PENDING] |
| PLACES CRC screening | CRC mortality | [PENDING] | [PENDING] | [PENDING] |

**Table 4. Mississippi vs US cancer incidence, mortality, stage; Black vs White** [PENDING]

**Table 5 (optional UMMC).** Screening completion among UMMC primary care patients by race; cells under 11 suppressed. [PENDING]

## 4. Discussion (outline)
- Principal findings [PENDING].
- Interpretation depends on measure type: modeled (PLACES) vs claims-based (CHR) screening.
- Limits: ecological; screening and outcomes measured in different populations; suppressed counties; the 2021 CRC age change.
- Implications for primary care and community screening programs in the Delta [PENDING citations].

## References (verified)
1. US Preventive Services Task Force. Screening for colorectal cancer: US Preventive Services Task Force recommendation statement. *JAMA.* 2021;325(19):1965–1977. doi:10.1001/jama.2021.6238
2. Zahnd WE, James AS, Jenkins WD, et al. Rural–urban differences in cancer incidence and trends in the United States. *Cancer Epidemiol Biomarkers Prev.* 2018;27(11):1265–1274. doi:10.1158/1055-9965.EPI-17-0430
3. Greenlund KJ, Lu H, Wang Y, et al. PLACES: Local Data for Better Health. *Prev Chronic Dis.* 2022;19:210459. doi:10.5888/pcd19.210459
4. National Cancer Institute and CDC. State Cancer Profiles. https://statecancerprofiles.cancer.gov/ (accessed 2026-11-26).
