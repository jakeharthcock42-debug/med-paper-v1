# Racial Disparities in Oral Cavity and Pharynx, Breast, and Colorectal Cancer in Mississippi: A Public-Data Ecological Analysis

**Status**: draft-v1 merged (2026-11-27): former Paper 05 (screening and stage) folded into Paper 02 by Jake's decision. All numbers are from published aggregates and reproducible with `scripts/public-data/`; re-verify State Cancer Profiles (SCP) values on the live site before submission. Public-data only. Abstract limit (project standard): ≤500 words including section labels.

## Abstract (draft-v1; 358 words incl. section labels; limit ≤500; conference style)
**Background.** Race-stratified incidence, stage, and mortality for oral cavity and pharynx cancer, and for breast and colorectal cancer in relation to screening and primary care supply, have not been summarized together for Mississippi.

**Methods.** Ecological analysis of public aggregate data: State Cancer Profiles (NPCR incidence and stage 2019–2023; NCHS mortality 2020–2024) for Mississippi, the US, and 82 counties; USDA rural–urban codes; HRSA Area Health Resources File dentists and primary care physicians (2023); CDC PLACES; and County Health Rankings Medicare mammography (2023). Black and White non-Hispanic rate ratios and approximate 95% CIs were derived from published CIs. County analyses used counties with published rates (cells under 16 cases in 5 years are suppressed) and Spearman, Mann-Whitney, and robust regression.

**Results.** For oral cavity and pharynx cancer, Black residents had lower incidence than White residents (9.5 vs 15.6 per 100,000; rate ratio 0.61, 0.55–0.67) but similar mortality (3.7 vs 3.5; 1.06, 0.89–1.25) and more late-stage diagnosis (73.1% vs 64.8%; approximate p<0.001); Mississippi mortality was 3.6 vs 2.7 in the US. Incidence did not differ between nonmetro and metro counties (median 14.6 vs 13.9; p=0.31). Black mortality exceeded White for breast (29.5 vs 20.7; rate ratio 1.43, 1.31–1.55; incidence ratio 1.04) and colorectal cancer (21.8 vs 15.8; 1.38, 1.28–1.49); Mississippi mortality exceeded the US for breast (23.6 vs 18.9) and colorectal cancer (17.5 vs 12.7). Medicare mammography was similar for Black and White women (42% vs 41%; p=0.41). Counties with fewer dentists (oral cancer late-stage share, rho −0.51, p=0.002) and fewer primary care physicians (rho −0.45, p=0.007) had higher late-stage share; primary care supply also predicted lower late-stage share for breast (−0.48 points per physician/10,000, 95% CI −0.86 to −0.10) and colorectal cancer (−0.91, −1.55 to −0.27). Model-based and Medicare screening rates were not associated with breast late-stage share after adjustment (−0.04 per point, −0.35 to 0.27).

**Conclusions.** Excess Black mortality from breast and colorectal cancer is not matched by lower Medicare mammography, and oral cavity and pharynx cancer is diagnosed later in Black residents despite lower incidence, pointing to stage, treatment, and follow-up. County dental and primary care supply tracked stage. These ecological findings are hypothesis-generating and need individual-level confirmation.

## 1. Introduction
Head and neck cancers have a large attributable fraction from tobacco and alcohol. In a pooled analysis of 17 case-control studies in the INHANCE consortium, tobacco or alcohol use accounted for an estimated 72% of head and neck cancers overall, 64% of oral cavity cancers, and 72% of pharyngeal cancers (Hashibe 2009). Rural populations have higher incidence of tobacco-associated cancers, including oral cavity and pharynx, than urban populations (Zahnd 2018). National registry studies show Black–White differences in survival for oral and oropharyngeal cancer (Osazuwa-Peters 2016) and in patterns of care (Shavers 2003), and HPV-associated cancer incidence clusters geographically (Burus 2026).

Colorectal cancer screening is recommended from age 45 (USPSTF 2021) and is generally delivered through primary care. Mississippi's Delta has documented gaps in breast and cervical cancer screening (Hall 2004), distinct breast cancer subtype patterns (Zahnd 2019), and high gastrointestinal cancer burden (Whatley 2014); recent reviews address colorectal cancer outcomes and screening (Koutha 2025; Vijayakumar 2025) and gaps in breast cancer research (Barsha 2025). Other Mississippi cancer work has described esophageal cancer by race and county (Walker 2023), colorectal cancer mortality and segregation in the Delta (Kruse-Diehr 2021), and Delta cancer mortality overall (Zahnd 2017).

Mississippi is predominantly rural and has large racial differences in health outcomes. [PENDING: verified citation for Mississippi smoking prevalence and rural share, e.g., CDC BRFSS and Census.] In PubMed title searches on 2026-11-27 we did not find a Mississippi-specific, race-stratified analysis of oral cavity and pharynx cancer incidence, stage, and mortality, nor one combining county screening, primary care and dental supply, and late-stage share across all 82 counties. We pair oral cavity and pharynx cancer (no routine screening; dental and primary care touchpoints) with breast and colorectal cancer (screening-amenable) to ask whether racial and access patterns differ.

**Aims.** (1) Compare Black and White non-Hispanic incidence, late-stage share, and mortality statewide and against the US for oral cavity and pharynx, breast, and colorectal cancer. (2) Compare rural and metro county incidence (oral cavity and pharynx). (3) Examine county correlates (tobacco and alcohol use, insurance, dental and primary care supply, dental HPSA status, poverty, screening) of incidence and late-stage share.

**Hypotheses.** A1 Black oral cavity/pharynx incidence is lower and mortality similar or higher. A2 Late-stage share is higher in Black residents. A3 Nonmetro counties have higher incidence. A4 County incidence rises with smoking and binge drinking and falls with dentist and PCP supply. A5 (exploratory) Late-stage share falls with dentist and PCP supply. B1 Mississippi exceeds the US in breast and colorectal mortality and late-stage share. B2 Black breast and colorectal mortality exceeds White with similar incidence. B3–B4 Delta and nonmetro counties have lower screening, and PCP supply is associated with screening. B5 Higher county screening is associated with lower late-stage share. B6 (exploratory) PCP supply is associated with lower late-stage share.

## 2. Methods
**Design.** Cross-sectional ecological analysis of publicly available aggregate data. No patient-level data. No UMMC data were used.

**Sources.** (all public; URLs and years in `README.md` and `data-sources.md`)
- *State Cancer Profiles* (https://statecancerprofiles.cancer.gov/): oral cavity & pharynx, colorectal, breast, and cervix; age-adjusted incidence 2019–2023, mortality 2020–2024, late-stage (regional + distant) counts and percent 2019–2023; all races, White NH, Black NH (oral cavity also male-only); county, state, and US rows. SCP suppresses cells with fewer than 16 cases in 5 years.
- *USDA ERS Rural-Urban Continuum Codes 2023* (metro 1–3; nonmetro 4–9).
- *HRSA AHRF 2024–2025*: dentists in private practice (ADA masterfile, 2023), MD and DO primary care physicians excluding residents (2023), dental and primary-care HPSA codes (2025; descriptive), Census 2023 population.
- *CDC PLACES*: 2025 release (BRFSS 2023): current smoking, binge drinking, uninsured 18–64; BRFSS 2022: colorectal screening (45–75), mammography (50–74); 2023 release (BRFSS 2020): dental visit, all-teeth-lost (age ≥65), colorectal screening (50–75), mammography, as sensitivity. PLACES estimates are model-based (multilevel regression and poststratification; Greenlund 2022), so associations with demographic or poverty variables are partly circular. The 2024/2025 releases give implausibly low Mississippi dental-visit values (4.9–12.9%) and were not used.
- *County Health Rankings* (2025; supplement 2026-03-25): PCP and dentists per 100,000, Medicare fee-for-service mammography (women 65–74, 2023), flu vaccination, child poverty, % Black.
- *Delta Regional Authority* county list.

**Analysis.** State rates as published. Rate ratios (Black/White) with approximate 95% CIs from published CIs on the log scale. Oral cavity/pharynx late-stage proportions compared with chi-square on counts reconstructed from published average annual counts ×5 (approximate). County analyses restricted to counties with published rates. Rural vs metro and Delta vs non-Delta: Mann-Whitney and WLS (weights = average annual count; HC3). Correlates: Spearman; OLS with HC3 (WLS weighted by late-stage average annual count as sensitivity for breast). Primary tests: A1, A2, B1, B2 (state level). County tests are exploratory, two-sided α=0.05 unadjusted (Bonferroni α=0.01 shown for the five Part A hypotheses). Python (pandas, scipy, statsmodels); scripts in `scripts/public-data/`.

**Ethics.** Only published aggregates are used; no cell under 11 events is reported from public sources and SCP's own suppression (fewer than 16 cases in 5 years) is respected. Not human-subjects research on identifiable data; confirm with the UMMC IRB whether any determination letter is required before submission. [PENDING: IRB/RDW confirmation]

## 3. Results
### Part A — Oral cavity and pharynx cancer
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

### Part B — Breast and colorectal cancer (former Paper 05)
**Table 4. Mississippi vs US (SCP; rates per 100,000 with 95% CI)**

| Cancer | Measure | Mississippi | US |
|---|---|---|---|
| Colorectal | Incidence | 45.7 (44.6–46.7) | 36.9 (36.9–37.0) |
| Colorectal | Mortality | 17.5 (16.9–18.1) | 12.7 (12.7–12.8) |
| Colorectal | % late stage | 63.0 | 60.2 |
| Breast | Incidence | 125.9 (123.5–128.3) | 133.0 (132.8–133.3) |
| Breast | Mortality | 23.6 (22.6–24.6) | 18.9 (18.8–19.0) |
| Breast | % late stage | 35.1 | 30.7 |
| Cervix | Incidence | 9.0 (8.4–9.7) | 7.5 (7.4–7.6) |
| Cervix | Mortality | 3.6 (3.2–4.0) | 2.1 (2.1–2.2) |
| Cervix | % late stage | 55.7 | 53.3 |

**Table 5. Mississippi Black vs White non-Hispanic (SCP)**

| Cancer | Measure | Black NH | White NH | Rate ratio (approx. 95% CI) |
|---|---|---|---|---|
| Colorectal | Incidence | 51.2 (49.3–53.2) | 44.0 (42.8–45.3) | 1.16 |
| Colorectal | Mortality | 21.8 (20.6–23.1) | 15.8 (15.1–16.6) | 1.38 (1.28–1.49) |
| Breast | Incidence | 130.6 (126.6–134.8) | 125.5 (122.5–128.6) | 1.04 |
| Breast | Mortality | 29.5 (27.6–31.5) | 20.7 (19.6–21.9) | 1.43 (1.31–1.55) |

**Table 6. County screening by Delta (DRA, n=47) vs non-DRA (n=35), median %**

| Measure | DRA | Non-DRA | p |
|---|---|---|---|
| Medicare mammography (CHR 2023) | 40 | 44 | 0.003 |
| Mammography, women 50–74 (PLACES 2022) | 72.6 | 72.4 | 0.93 |
| Colorectal screening, 45–75 (PLACES 2022) | 54.7 | 55.1 | 0.17 |

**Table 7. County late-stage share (Spearman; breast n=69, colorectal n=75)**

| Predictor | Breast % late rho (p) | Colorectal % late rho (p) |
|---|---|---|
| Medicare mammography (CHR) | −0.33 (0.006) | — |
| PLACES mammography 2022 / CRC screening 2022 | 0.10 (0.40) | −0.04 (0.75) |
| PLACES 2020 mammography / CRC screening | 0.12 (0.32) | −0.11 (0.34) |
| PCP per 10k (AHRF) | −0.37 (0.002) | −0.32 (0.005) |
| Child poverty % | 0.51 (<0.001) | −0.17 (0.15) |
| % Black NH | 0.43 (<0.001) | −0.22 (0.054) |

Adjusted (OLS, HC3): breast late-stage on Medicare mammography −0.04 (−0.35, 0.27), PCP/10k −0.48 (−0.86, −0.10), child poverty/10 +2.85 (1.19, 4.50), nonmetro −0.85 (−3.76, 2.05); R² = 0.35 (n = 69). Colorectal late-stage on PLACES screening +0.14 (−0.70, 0.99), PCP/10k −0.91 (−1.55, −0.27); R² = 0.15 (n = 75). Black vs White Medicare mammography medians 42% vs 41% (n = 81, p = 0.41). Full output (kept for provenance in the former Paper 05 folder): `../05-screening-gaps-cancer-stage/results/p05_results.md`, `p05b_results.md`.

## 4. Discussion (outline)
- **Principal findings:** for oral cavity and pharynx cancer, lower incidence with similar mortality in Black residents (M:I 0.39 vs 0.22) and later stage (73.1% vs 64.8%), consistent with differences in detection and post-diagnosis care rather than exposure alone; for breast and colorectal cancer, Black mortality is 1.43 and 1.38 times White without lower Medicare mammography, pointing to stage, treatment, and follow-up. Mississippi mortality exceeds the US for both.
- **County findings:** dentist–stage (rho −0.51, n = 34) and PCP–stage associations (oral, breast, and colorectal) are exploratory, share variance with urbanicity, and use published counties that are larger and less poor than suppressed ones. County screening estimates did not explain stage after adjustment, but PLACES smoothing and Medicare-only mammography limit the ability to detect screening effects (secondary finding).
- **Limits:** SCP suppression; ecological design; no subsite/HPV; model-based covariates; period mismatch; PLACES dental visit excluded for 2022 data issue; approximate chi-square and rate ratios derived from published CIs.
- **Implications:** dental and primary care visits as detection touchpoints; follow-up with individual-level data (registry, BRFSS by race, or UMMC) could test stage and treatment pathways. [UMMC data deferred by decision; see README.]

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
12. US Preventive Services Task Force. Screening for colorectal cancer: US Preventive Services Task Force recommendation statement. *JAMA.* 2021;325(19):1965–1977.
13. Hall HI, Jamison PM, Coughlin SS, Uhler RJ. Breast and cervical cancer screening among Mississippi Delta women. *J Health Care Poor Underserved.* 2004;15:375–389. doi:10.1353/hpu.2004.0042
14. Zahnd WE, Sherman RL, Klonoff-Cohen H, et al. Disparities in breast cancer subtypes among women in the lower Mississippi Delta Region states. *Cancer Causes Control.* 2019;30:591–601. doi:10.1007/s10552-019-01168-0
15. Whatley Z, Daram SR, Yousuf S, et al. Gastrointestinal cancers in Mississippi. *South Med J.* 2014;107:229–234. doi:10.1097/SMJ.0000000000000093
16. Koutha S, Vijayakumar S, Young CC. Colorectal cancer in Mississippi: how to change the tide of bad news to a success story? *Cureus.* 2025;17:e90164. doi:10.7759/cureus.90164
17. Vijayakumar S, Koutha S, Young C, et al. Current status of colorectal cancer screenings: tailoring them to Mississippi's rural geography, demographics, infrastructure and community needs. *Cureus.* 2025;17:e97517. doi:10.7759/cureus.97517
18. Barsha RAA, Miller-Kleinhenz J. Left behind: the unmet need for breast cancer research in Mississippi. *Cancers (Basel).* 2025;17(10):1652. doi:10.3390/cancers17101652
