# 05 — Cancer Screening Gaps and Stage at Diagnosis in Mississippi Counties

**Working title**: County-Level Cancer Screening, Primary Care Access, and Late-Stage Colorectal and Breast Cancer in Mississippi: Delta and Rural Patterns  
**Status**: First-pass public-data analysis done (2026-11-26); draft skeleton in `draft-v1.md`; UMMC add-on requests ready to run  
**Target**: MAFP, ACP Mississippi, UMMC Research Day (preventive care angle)  
**Public-data sufficiency**: Yes for colorectal and breast (65–80 counties with published outcomes). Cervical cancer is too sparse at county level (12 counties with incidence).

## Research question
Are county screening rates (colorectal, mammography) lower in Delta and rural counties and where primary care supply is lower, and do counties with higher screening show less late-stage disease and lower mortality?

## Specific aims
1. Describe county screening measures and compare DRA (Delta) vs non-DRA and nonmetro vs metro counties.
2. Test associations of screening with PCP supply, uninsurance, poverty, and racial composition.
3. Test ecological associations between screening and colorectal/breast stage and mortality, favoring claims-based screening (CHR mammography) over model-based PLACES.
4. Describe Black–White differences in Medicare mammography and flu vaccination, and in cancer incidence/mortality (state level).

## Hypotheses and planned tests (with first-pass status)
| # | Hypothesis | Planned test | First-pass result |
|---|---|---|---|
| H1 | Screening is lower in DRA (Delta) and nonmetro counties | Mann-Whitney | **Mixed.** CHR Medicare mammography: DRA median 40% vs 44% (p = 0.003), nonmetro 42% vs metro 39.5% (p = 0.304). PLACES CRC screening: 54.7% vs 55.1% (p = 0.174); nonmetro 54.8% vs 55.4% (p = 0.111). PLACES mammography: 72.6% vs 72.4% (p = 0.925) |
| H2 | Screening rises with PCP supply and falls with uninsurance and poverty | Spearman; OLS (HC3) | **Supported.** CRC screening vs PCP rho 0.390 (p < 0.001), uninsured −0.294 (p = 0.007), child poverty −0.442 (p < 0.001). CHR mammography vs PCP rho 0.402 (p < 0.001); OLS (n = 79, R2 = 0.39): PCP +0.69 points per +1 PCP/10,000 (95% CI 0.28–1.11), nonmetro +3.07 (1.13–5.02), DRA −1.89 (−3.93 to 0.15) |
| H3 | Higher screening is associated with lower late-stage share and mortality | Spearman | **Mixed.** CHR mammography vs breast % late: rho −0.331 (p = 0.006, n = 69); vs breast mortality −0.349 (p = 0.016, n = 47); vs breast M:I ratio −0.521 (p < 0.001, n = 47). PLACES CRC screening vs CRC % late: rho −0.037 (p = 0.754, n = 75); vs CRC mortality −0.477 (p < 0.001, n = 65); vs CRC incidence −0.384 (p < 0.001, n = 80) |
| H4 | Black women have lower Medicare mammography than White women | Paired Wilcoxon | **Not supported.** Median 42.0% vs 41.0% (n = 81; p = 0.408). Flu vaccination is lower for Black beneficiaries: 31% vs 37% median, Black lower in 71 of 81 counties (p = 7.7e-12) |

Primary tests for the abstract: H2 (CHR mammography model) and H3 (CHR mammography vs breast stage). Others exploratory. PLACES findings are descriptive (see caveat).

## Statewide context (State Cancer Profiles)
Mississippi vs US (age-adjusted per 100k): colorectal incidence 45.7 vs 36.9; colorectal mortality 17.5 vs 12.7; breast mortality 23.6 vs 18.9; cervical mortality 3.6 vs 2.1. Black NH vs White NH in Mississippi: colorectal mortality 21.8 vs 15.8 (RR 1.38; 1.28–1.49); breast mortality 29.5 vs 20.7 (RR 1.43; 1.31–1.55) with similar incidence (130.6 vs 125.5). Late-stage share: colorectal 63.0% (US 60.2%); breast 35.1% (US 30.7%); cervical 55.7% (US 53.3%). Full tables: `results/p05_results.md`.

## Data sources (public; aggregates only)
| Source | URL | Years | Use |
|---|---|---|---|
| CDC PLACES county data, 2025 release | https://data.cdc.gov/d/swc5-untb | CRC screening and mammography 2022; cholesterol screening, checkup 2023 (BRFSS, model-based) | Screening prevalence |
| County Health Rankings supplemental release (25 Mar 2026) | https://www.countyhealthrankings.org/health-data/methodology-and-sources/data-documentation | Mammography (Medicare FFS 65–74) 2023, flu vaccination 2023, race-specific; PCP 2022; uninsured 2023 | Claims-based screening; access |
| State Cancer Profiles: colon & rectum (020), breast female (055), cervix (057), lung (047) | https://statecancerprofiles.cancer.gov/ | Incidence & stage 2019–2023; mortality 2020–2024 | Stage and mortality outcomes |
| USDA RUCC 2023; DRA list | https://www.ers.usda.gov/data-products/rural-urban-continuum-codes ; https://dra.gov/wp-content/uploads/2022/04/Mississippi.pdf | 2023 / 2016–2024 | Rural/Delta |
| HRSA HPSA data | https://data.hrsa.gov/data/download | latest | [PENDING] shortage designations |
| MSTAHRS cancer deaths by race/county | https://mstahrs.msdh.ms.gov/ | through 2024 | [PENDING] |

## Feasibility notes and limits
- **PLACES caveat**: PLACES estimates are model-based (multilevel regression and poststratification using age, sex, race/ethnicity, education, and county poverty; Greenlund 2022). PLACES-vs-covariate correlations are partly built in; the CHR Medicare mammography measure is claims-based but covers only fee-for-service women 65–74 and is not representative of all Mississippi women.
- PLACES "dental visit" excluded: published values 4.9–12.9% are implausible and need verification [PENDING].
- County cancer outcomes are suppressed where fewer than 16 cases in 5 years; stage analyses cover 65–80 counties, biased toward larger counties.
- Ecological; screening is measured in a different population (age and payer) than the cancer outcomes.
- Colorectal screening measure is age 45–75 (PLACES 2022), spanning a recommendation change in 2021 (USPSTF lowered start age to 45; Grade B for 45–49) — interpret trend vs prior eras carefully.

## Next actions
- [ ] [PENDING] BRFSS state-level screening by race (CDC BRFSS Prevalence & Trends: https://www.cdc.gov/brfss/brfssprevalence/) to complement county data.
- [ ] [PENDING] Cervical screening (Pap/HPV) county measure: no county measure available in PLACES 2025; check CHR/other.
- [ ] [PENDING] HRSA HPSA and FQHC (UDS) screening quality measures for Mississippi health centers.
- [ ] Add lung cancer incidence/mortality and smoking for a tobacco-linked sub-analysis (data already pulled).
- [ ] Draft abstract around H2/H3 with CHR mammography.

## Optional UMMC RDW add-on (data-use cleared by Jake 2026-11-26; ready to run)
Aggregates only; suppress cells under 11; one selection per box.
1. Colorectal: Procedure code **45378** (diagnostic colonoscopy) and, separately, **82274** (fecal immunochemical test) / **Z12.11** (encounter for screening for malignant neoplasm of colon): patients and by race, age group (45–54, 55–64, 65–75).
2. Breast: Procedure **77067** (screening mammography, bilateral) / **Z12.31**: patients, by race and age group (40–49, 50–59, 60–74).
3. Cervical: **Z12.4** (encounter for screening for malignant neoplasm of cervix): patients by race and age group (21–29, 30–64).
4. Denominator: patients with ≥1 Family Medicine or Internal Medicine outpatient encounter in the last 24 months, by race and age group (use the Explorer's encounter/department filters if present).
5. Cancers found: **C18.x/C20** (colorectal), **C50.x** (breast), by race, with stage if the Explorer exposes it (otherwise [PENDING]).
Use: screening-completion proportions among UMMC primary care patients by race, to complement county patterns.

## Files
- `draft-v1.md`, `results/p05_results.md`, `results/p05_county_dataset.csv`
