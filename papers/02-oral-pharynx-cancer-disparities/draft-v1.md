# Racial Differences in Oral Cavity and Pharynx Cancer Incidence, Stage, and Mortality in Mississippi: A Public-Data Ecological Analysis

**Status**: draft-v1 (2026-11-27). All numbers are from published aggregates and reproducible with `scripts/public-data/`; re-verify State Cancer Profiles (SCP) values on the live site before submission. Public-data only (Jake's decision, 2026-11-27).

## Abstract (draft-v1; ≤300 words incl. section labels; conference style)
**Background.** Oral cavity and pharynx cancers are largely tobacco-, alcohol-, and HPV-related, and are detected earlier when dental and primary care are accessible. Race-stratified incidence, stage, and mortality for these cancers have not been summarized together for Mississippi.

**Methods.** Ecological analysis of public aggregate data: State Cancer Profiles (NPCR incidence and stage 2019–2023; NCHS mortality 2020–2024) for Mississippi, the US, and 82 counties; USDA rural–urban codes; HRSA Area Health Resources File dentist supply (2023); CDC PLACES and County Health Rankings covariates. Black and White non-Hispanic rate ratios and approximate 95% CIs were derived from published CIs; late-stage shares were compared by chi-square on counts reconstructed from published averages. County analyses used the 54 counties with published rates (cells under 16 cases in 5 years are suppressed), with Mann-Whitney, Spearman, and robust regression.

**Results.** Mississippi incidence was 13.4 (95% CI 12.9–14.0) per 100,000 vs 12.3 in the US; mortality was 3.6 vs 2.7. Black residents had lower incidence than White residents (9.5 vs 15.6; rate ratio 0.61, 0.55–0.67) but similar mortality (3.7 vs 3.5; rate ratio 1.06, 0.89–1.25); mortality-to-incidence ratios were 0.39 vs 0.22. Late-stage diagnosis was more common among Black residents (73.1% vs 64.8%; approximate p<0.001). Incidence did not differ between nonmetro and metro counties (median 14.6 vs 13.9; p=0.31). Among 34 counties with a published late-stage share, fewer dentists per 10,000 residents (Spearman rho −0.51, p=0.002) and fewer primary care physicians (rho −0.45, p=0.007) were associated with higher late-stage share; county smoking prevalence (PLACES, model-based) was not associated with incidence (rho 0.03).

**Conclusions.** Black residents are diagnosed less often but later, and die at similar rates to White residents, suggesting worse outcomes after diagnosis. County dental and primary care supply tracks stage. These ecological findings are hypothesis-generating and need individual-level confirmation.

## 1. Introduction
Head and neck cancers have a large attributable fraction from tobacco and alcohol. In a pooled analysis of 17 case-control studies in the INHANCE consortium, tobacco or alcohol use accounted for an estimated 72% of head and neck cancers overall, 64% of oral cavity cancers, and 72% of pharyngeal cancers (Hashibe 2009). Rural populations have higher incidence of tobacco-associated cancers, including oral cavity and pharynx, than urban populations (Zahnd 2018). National registry studies show Black–White differences in survival for oral and oropharyngeal cancer (Osazuwa-Peters 2016) and in patterns of care (Shavers 2003), and HPV-associated cancer incidence clusters geographically (Burus 2026).

Mississippi is predominantly rural and has large racial differences in health outcomes. [PENDING: verified citation for Mississippi smoking prevalence and rural share, e.g., CDC BRFSS and Census.] Prior Mississippi and Delta cancer work has described other sites: esophageal cancer by race and county (Walker 2023), colorectal cancer mortality and segregation in the Delta (Kruse-Diehr 2021), and Delta cancer mortality overall (Zahnd 2017). In PubMed title searches on 2026-11-27 we did not find a Mississippi-specific, race-stratified analysis of oral cavity and pharynx cancer incidence, stage, and mortality.

**Aims.** (1) Compare Black and White non-Hispanic incidence, late-stage share, and mortality statewide and against the US. (2) Compare rural and metro county incidence. (3) Examine county correlates (tobacco and alcohol use, insurance, primary care and dentist supply, dental HPSA status, poverty).

**Hypotheses.** H1 Black incidence is lower and mortality similar or higher (higher mortality-to-incidence ratio). H2 Late-stage share is higher in Black residents. H3 Nonmetro counties have higher incidence. H4 County incidence rises with smoking and binge drinking and falls with dentist and PCP supply. H5 (exploratory) Late-stage share falls with dentist and PCP supply.

## 2. Methods
**Design.** Cross-sectional ecological analysis of publicly available aggregate data. No patient-level data. No UMMC data were used.

**Sources.** (all public; URLs and years in `README.md` and `data-sources.md`)
- *State Cancer Profiles* (https://statecancerprofiles.cancer.gov/): Oral Cavity & Pharynx; age-adjusted incidence 2019–2023, mortality 2020–2024, late-stage (regional + distant) counts and percent; all races, White NH, Black NH; both sexes and male. SCP suppresses cells with fewer than 16 cases in 5 years.
- *USDA ERS Rural-Urban Continuum Codes 2023* (metro 1–3; nonmetro 4–9).
- *HRSA AHRF 2024–2025*: dentists in private practice (ADA masterfile, 2023), dental HPSA code (2025), Census 2023 population.
- *CDC PLACES*: 2025 release (BRFSS 2023): current smoking, binge drinking, uninsured 18–64; 2023 release (BRFSS 2020): dental visit and all-teeth-lost (age ≥65). PLACES estimates are model-based (multilevel regression and poststratification; Greenlund 2022), so associations with demographic or poverty variables are partly circular. The 2024/2025 releases give implausibly low Mississippi dental-visit values (4.9–12.9%) and were not used.
- *County Health Rankings* (2025; supplement 2026-03-25): PCP and dentists per 100,000, child poverty, % Black.
- *Delta Regional Authority* county list.

**Analysis.** State rates as published. Rate ratios (Black/White) with approximate 95% CIs from published CIs on the log scale. Late-stage proportions compared with chi-square on counts reconstructed from published average annual counts ×5 (approximate). County analyses restricted to counties with published rates. Rural vs metro: Mann-Whitney and WLS (weights = average annual count; HC3). Correlates: Spearman; OLS with HC3. Primary tests H1 and H2; H3–H5 exploratory, two-sided α=0.05 unadjusted (Bonferroni α=0.01 shown for the five hypotheses). Python (pandas, scipy, statsmodels); scripts in `scripts/public-data/`.

**Ethics.** Only published aggregates are used; no cell under 11 events is reported from public sources and SCP's own suppression (fewer than 16 cases in 5 years) is respected. Not human-subjects research on identifiable data; confirm with the UMMC IRB whether any determination letter is required before submission. [PENDING: IRB/RDW confirmation]

## 3. Results
**Table 1. Mississippi oral cavity & pharynx cancer by race/ethnicity (SCP)**

| Group | Incidence/100k (95% CI), 2019–23 | Mortality/100k (95% CI), 2020–24 | % late stage | Mortality-to-incidence ratio |
|---|---|---|---|---|
| All races, Mississippi | 13.4 (12.9–14.0) | 3.6 (3.3–3.9) | 66.8 | 0.27 |
| White NH | 15.6 (14.9–16.4) | 3.5 (3.2–3.9) | 64.8 | 0.22 |
| Black NH | 9.5 (8.8–10.4) | 3.7 (3.2–4.2) | 73.1 | 0.39 |
| US (SEER+NPCR) | 12.3 (12.2–12.3) | 2.7 (2.7–2.7) | 64.9 | 0.22 |
| Men, White NH | 23.4 (22.1–24.8) | 5.5 (4.8–6.1) | — | 0.24 |
| Men, Black NH | 15.4 (13.9–17.0) | 6.7 (5.7–7.8) | — | 0.44 |

Black/White incidence rate ratio 0.61 (0.55–0.67); mortality rate ratio 1.06 (0.89–1.25); late stage chi2 = 13.81, p < 0.001 (approximate). Mortality-to-incidence ratios compare rates from different periods and are descriptive.

**Table 2. County incidence by metro status (54 counties with published rates)**

| Group | n counties | Median (IQR), per 100k | Test |
|---|---|---|---|
| Metro (RUCC 1–3) | 15 | 13.9 (12.2–14.6) | Mann-Whitney p = 0.306 |
| Nonmetro (RUCC 4–9) | 39 | 14.6 (12.4–16.4) | WLS difference +1.10 (−0.36 to 2.56), p = 0.138 |

**Table 3. County correlates (Spearman); incidence n = 54, % late stage n = 34**

| Variable | rho (incidence) | p | rho (% late) | p |
|---|---|---|---|---|
| Dentists in private practice per 10k (AHRF 2023) | −0.329 | 0.015 | −0.514 | 0.002 |
| Dentists per 100k (CHR) | −0.263 | 0.054 | −0.488 | 0.003 |
| PCP per 100k (CHR) | −0.160 | 0.249 | −0.454 | 0.007 |
| Current smoking (PLACES 2023) | 0.026 | 0.851 | 0.199 | 0.260 |
| Binge drinking (PLACES 2023) | 0.116 | 0.405 | — | — |
| Dental visit past year (PLACES, BRFSS 2020) | −0.042 | 0.766 | −0.090 | 0.613 |
| Dental HPSA code (AHRF 2025) | 0.026 | 0.851 | −0.023 | 0.899 |
| % Black NH | −0.176 | 0.204 | −0.370 | 0.031 |
| Child poverty % | −0.103 | 0.459 | −0.042 | 0.812 |

Adjusted OLS for incidence (smoking, dental visit, nonmetro, child poverty, dentists/10k; n = 54, R² = 0.14): dentists −0.53 per 10k (95% CI −1.10 to 0.04), p = 0.069. Full output: `results/p02_results.md`, `results/p02b_results.md`.

## 4. Discussion (outline)
- **Principal finding:** lower incidence with similar mortality in Black residents (M:I 0.39 vs 0.22) and later stage (73.1% vs 64.8%) are consistent with differences in detection and post-diagnosis care rather than exposure alone; lower incidence in Black residents also fits lower smoking/alcohol/HPV exposure patterns reported nationally, but our data cannot separate these.
- **County findings:** the dentist–stage association (rho −0.51) is exploratory (n = 34), shares variance with PCP supply and urbanicity, and uses published counties that are larger and less poor than suppressed ones.
- **Limits:** SCP suppression; ecological design; no subsite/HPV; model-based covariates; period mismatch; PLACES dental visit excluded for 2022 data issue; approximate chi-square and rate ratios derived from published CIs.
- **Implications:** dental and primary care visits as oral cancer detection touchpoints; follow-up with individual-level data (registry or UMMC) could test stage and treatment pathways. [UMMC data deferred by decision; see README.]

## References (verified)
1. Hashibe M, Brennan P, Chuang SC, et al. Interaction between tobacco and alcohol use and the risk of head and neck cancer: pooled analysis in the INHANCE consortium. *Cancer Epidemiol Biomarkers Prev.* 2009;18(2):541–550. https://pubmed.ncbi.nlm.nih.gov/19190158/
2. Zahnd WE, James AS, Jenkins WD, et al. Rural–urban differences in cancer incidence and trends in the United States. *Cancer Epidemiol Biomarkers Prev.* 2018;27(11):1265–1274. doi:10.1158/1055-9965.EPI-17-0430
3. Greenlund KJ, Lu H, Wang Y, et al. PLACES: Local Data for Better Health. *Prev Chronic Dis.* 2022;19:210459. doi:10.5888/pcd19.210459
4. Osazuwa-Peters N, Massa ST, Christopher KM, et al. Race and sex disparities in long-term survival of oral and oropharyngeal cancer in the United States. *J Cancer Res Clin Oncol.* 2016;142:521–528. doi:10.1007/s00432-015-2061-8 (PMID 26507889)
5. Shavers VL, Harlan LC, Winn D, Davis WW. Racial/ethnic patterns of care for cancers of the oral cavity, pharynx, larynx, sinuses, and salivary glands. *Cancer Metastasis Rev.* 2003;22:25–38. doi:10.1023/a:1022255800411 (PMID 12716034)
6. Burus T, Lang Kuhs KA, Deshmukh AA, et al. Geographic clusters of human papillomavirus-associated cancer incidence in the US, 2008–2022. *Prev Med.* 2026;203:108491. doi:10.1016/j.ypmed.2025.108491
7. Walker A, Abnet CC, Shiels MS. Racial and geographical disparities in oesophageal cancer incidence, mortality and county-level risk factors in the state of Mississippi. *BMJ Public Health.* 2023;1. doi:10.1136/bmjph-2023-000316
8. Kruse-Diehr AJ, McDaniel JT, Lewis-Thames MW, et al. Racial residential segregation and colorectal cancer mortality in the Mississippi Delta region. *Prev Chronic Dis.* 2021;18:E14. doi:10.5888/pcd18.200483
9. Zahnd WE, Jenkins WD, Mueller-Luckey GS. Cancer mortality in the Mississippi Delta region: descriptive epidemiology and needed future research and interventions. *J Health Care Poor Underserved.* 2017;28:315–328. doi:10.1353/hpu.2017.0025
10. National Cancer Institute and CDC. State Cancer Profiles. https://statecancerprofiles.cancer.gov/ (accessed 2026-11-26).
11. HRSA National Center for Health Workforce Analysis. Area Health Resources Files 2024–2025. https://data.hrsa.gov/data/download?data=AHRF (accessed 2026-11-27).
