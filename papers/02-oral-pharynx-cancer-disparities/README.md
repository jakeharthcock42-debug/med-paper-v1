# 02 — Racial Disparities in Oral Cavity & Pharynx, Breast, and Colorectal Cancer in Mississippi (merged with former Paper 05)

**Working title**: Racial Disparities in Oral Cavity and Pharynx, Breast, and Colorectal Cancer Incidence, Stage, and Mortality in Mississippi: a Public-Data Ecological Analysis  
**Status**: **Merged 2026-11-27 (Jake decision): former Paper 05 (screening gaps and cancer stage) folded into this paper as a cancer-disparities pair.** Public-data analysis complete; merged abstract written (draft-v1) and revised 2026-11-27 against the writing-guide review (370 words). Public-data-only by Jake's decision (2026-11-27); no UMMC pull is needed or planned.  
**Abstract limit (project standard, Jake 2026-11-27): ≤500 words including section labels.**  
**Natural fit**: ENT / head & neck oncology (oral cavity and pharynx) plus family/internal medicine (screening-amenable cancers); companion to Paper 01 (hearing loss).  
**Target**: UMMC Research Day, MAFP, ACP Mississippi abstracts → possible full paper  
**Novelty check (PubMed, 2026-11-27)**: no Mississippi-specific, race-stratified oral cavity/pharynx incidence–stage–mortality paper found (title searches); closest Mississippi precedents are other sites (Walker 2023 oesophageal; Kruse-Diehr 2021 CRC). For breast and colorectal cancer, Mississippi papers exist (Hall 2004; Zahnd 2019; Whatley 2014; Koutha 2025; Vijayakumar 2025; Barsha 2025), so Part B is low-novelty and serves as the screening-amenable comparison to the oral cavity/pharynx analysis. Moderate novelty overall; local framing. See `draft-v1.md` references.

## Research question
In Mississippi, how do incidence, late-stage share, and mortality differ by race (Black vs White non-Hispanic) for oral cavity and pharynx cancer and for breast and colorectal cancer, and are county patterns related to rurality, primary care and dental supply, and screening?

## Specific aims (all answerable from public sources)
**Part A — oral cavity and pharynx cancer (former Paper 02)**
1. Quantify Black vs White non-Hispanic differences in incidence, late-stage share, and mortality statewide (and male-only) and compare Mississippi with the US.
2. Describe county variation in incidence (54 of 82 counties have a published rate) and test rural (RUCC 4–9) vs metro (RUCC 1–3) differences.
3. Test county-level correlates of incidence and late-stage share: smoking, binge drinking, uninsurance, PCP and dentist supply (CHR and HRSA AHRF), dental HPSA status, dental visit and tooth loss (PLACES 2020), poverty, % Black.

**Part B — breast and colorectal cancer (former Paper 05)**
4. Compare Mississippi with the US and Black with White non-Hispanic residents for breast and colorectal incidence, mortality, and late-stage share (SCP); cervical cancer shown descriptively.
5. Describe county screening (PLACES model-based; CHR Medicare mammography) by Delta (DRA) and rurality, and relate it to PCP supply.
6. Test whether county screening and PCP supply are associated with county late-stage share (breast n = 69, colorectal n = 75 counties with published values). Null screening–stage results are reported as secondary findings and limitations.

## Hypotheses and results (public data)
**Part A**
| # | Hypothesis | Test | Result |
|---|---|---|---|
| A1 | Black NH residents have lower incidence but similar or higher mortality than White NH (higher mortality-to-incidence ratio) | Rate ratio from published age-adjusted rates and CIs (log-normal approx.); descriptive M:I | **Supported.** Incidence 9.5 (8.8–10.4) vs 15.6 (14.9–16.4) per 100k; RR 0.61 (0.55–0.67). Mortality 3.7 (3.2–4.2) vs 3.5 (3.2–3.9); RR 1.06 (0.89–1.25). M:I 0.39 vs 0.22 (men 0.44 vs 0.24) |
| A2 | Late-stage share is higher in Black than White NH | Chi-square on counts reconstructed from published average annual counts ×5 (approximate) | **Supported.** 73.1% vs 64.8%; approx. chi2 = 13.81, p < 0.001 |
| A3 | Nonmetro counties have higher incidence than metro | Mann-Whitney; WLS (weights = avg annual count), HC3 | **Not supported.** Median 14.6 (n=39) vs 13.9 (n=15); p = 0.306; WLS +1.10 per 100k (−0.36 to 2.56) |
| A4 | County incidence rises with smoking/binge drinking and falls with dentist/PCP supply | Spearman; OLS HC3 (n=54) | **Partly.** Smoking rho 0.03, binge 0.12 (n.s.). Dentists in private practice per 10k (AHRF 2023) rho −0.33 (p = 0.015); CHR dentists −0.26 (p = 0.054); PCP −0.16 (n.s.). Adjusted OLS dentists −0.53 per 10k (−1.10 to 0.04), p = 0.069 |
| A5 | Counties with fewer dentists/PCPs have a higher late-stage share | Spearman (n=34 counties with published % late) | **Supported (exploratory).** Dentists per 10k rho −0.51 (p = 0.002); CHR dentists −0.49 (p = 0.003); PCP −0.45 (p = 0.007); % Black −0.37 (p = 0.031). Dental visit, teeth lost, dental HPSA not associated |

**Part B**
| # | Hypothesis | Test | Result |
|---|---|---|---|
| B1 | Mississippi has higher mortality and late-stage share than the US for breast, colorectal, and cervical cancer | SCP state rows | **Supported.** CRC incidence 45.7 vs 36.9, mortality 17.5 vs 12.7, late 63.0% vs 60.2%. Breast incidence 125.9 vs 133.0 (lower), mortality 23.6 vs 18.9, late 35.1% vs 30.7%. Cervix incidence 9.0 vs 7.5, mortality 3.6 vs 2.1, late 55.7% vs 53.3% |
| B2 | Black mortality exceeds White, with incidence similar | Rate ratios from published CIs | **Supported.** Breast mortality 29.5 vs 20.7 (RR 1.43, 1.31–1.55), incidence RR 1.04; CRC mortality 21.8 vs 15.8 (RR 1.38, 1.28–1.49), CRC incidence 51.2 vs 44.0 |
| B3 | Delta (DRA) and nonmetro counties have lower screening | Mann-Whitney | **Mixed.** Medicare mammography (CHR) DRA median 40% vs 44% (p = 0.003); nonmetro vs metro 42% vs 39.5% (p = 0.30). PLACES mammography and CRC screening differ by <1 point |
| B4 | PCP supply is associated with screening | Spearman; OLS (HC3) | **Supported.** Medicare mammography +0.77 percentage points per additional PCP/10k (0.40–1.14; n = 82; R² = 0.37); nonmetro +2.9; CRC screening rho 0.39 with PCP per 100k |
| B5 | Counties with higher screening have lower late-stage share | Spearman; adjusted OLS/WLS | **Not supported after adjustment (secondary finding/limitation).** Breast late-stage vs Medicare mammography rho −0.33 (p = 0.006, n = 69) but adjusted coefficient −0.04 per point (−0.35, 0.27) after child poverty and PCP. PLACES mammography rho +0.10; PLACES CRC screening vs CRC late-stage rho −0.04 (n = 75); adjusted +0.14 (−0.70, 0.99) |
| B6 (exploratory) | PCP supply is associated with lower late-stage share | OLS (HC3) | **Supported.** Breast late-stage −0.48 percentage points per PCP/10k (−0.86 to −0.10), p = 0.013; CRC −0.91 (−1.55 to −0.27), p = 0.005. Child poverty +2.8 pp per 10 points for breast late-stage (1.2–4.5) |
| B7 (descriptive) | Black–White Medicare mammography differs | Paired Wilcoxon (CHR, n = 81) | **No difference.** Median 42% (Black) vs 41% (White), p = 0.41; flu vaccination 31% vs 37% (p = 8e-12) |

Primary tests: A1, A2, B1, B2 (state level). All county analyses are exploratory; unadjusted p-values (Bonferroni α for five Part A hypotheses = 0.01; A5 dentist and PCP results remain below it).

## Data sources (all public; aggregates only)
| Source | URL | Years | Use |
|---|---|---|---|
| State Cancer Profiles (NPCR/CDC + NCHS): oral cavity & pharynx (003), colorectal (020), breast (055), cervix (057) | https://statecancerprofiles.cancer.gov/ | Incidence and late stage 2019–2023; mortality 2020–2024 | Rates, CIs, counts, % late stage by county, race, sex |
| USDA ERS Rural-Urban Continuum Codes | https://www.ers.usda.gov/data-products/rural-urban-continuum-codes | 2023 | Metro (1–3) vs nonmetro (4–9) |
| HRSA Area Health Resources Files (AHRF) 2024–2025 | https://data.hrsa.gov/data/download?data=AHRF | Dentists in private practice 2023 (ADA masterfile); PCP (MD+DO) 2023; dental and primary-care HPSA 2025; population 2023 | Dentist and PCP supply, shortage designation |
| CDC PLACES 2025 release | https://data.cdc.gov/d/swc5-untb | BRFSS 2023 (2022 for teeth lost, CRC screening 45–75, mammography 50–74) | Smoking, binge drinking, uninsured, model-based screening |
| CDC PLACES 2023 release (BRFSS 2020) | https://data.cdc.gov/d/h3ej-a9ec | 2020 | Dental visit, all-teeth-lost, CRC screening (50–75), mammography (sensitivity; see limits) |
| County Health Rankings (2025 annual; 25 Mar 2026 supplement) | https://www.countyhealthrankings.org/health-data/methodology-and-sources/data-documentation | PCP 2022; dentists 2023; Medicare FFS mammography (women 65–74) and flu vaccination 2023 | Access and observed screening, race-specific where published |
| Delta Regional Authority county list | https://dra.gov/wp-content/uploads/2022/04/Mississippi.pdf | 2016–2024 | Delta (DRA) indicator, 47 MS counties |

Reproducibility: `scripts/public-data/` (`p02.py`, `p02b.py`, `p05.py`, `p05b.py`, `build_ahrf.py`, `build_places2020.py`, `build_master.py`, `scp_build.py`). Results: `results/` here (Part A) and `papers/05-screening-gaps-cancer-stage/results/` (Part B, kept for provenance; linked, not copied).

## Limits
- SCP suppresses cells with fewer than 16 cases in 5 years. Oral cavity/pharynx, of 82 counties: incidence published for 54; mortality 11; late-stage 34; Black NH incidence 10; White NH 35. County race and mortality analyses are not feasible, so race stays at state level. Published counties are larger (median population 28,768 vs 9,951), less Black (median 34.5% vs 50.8%) and less poor (child poverty 25.7% vs 32.1%) than suppressed ones. Breast and colorectal late-stage % are published for 69 and 75 counties; cervical county data are too sparse (incidence for 12 counties).
- Mortality period (2020–2024) differs from incidence (2019–2023); M:I is a descriptive ratio of published age-adjusted rates, not survival.
- SCP does not separate oral cavity vs oropharynx subsites or give HPV status; USCS/NPCR subsite data could not be scripted (interactive).
- Ecological design; county correlations cannot be interpreted at the individual level. Dentist and PCP supply are correlated with each other and with urbanicity.
- PLACES is model-based (MRP; Greenlund 2022) and strongly smoothed (county ranges: CRC 49.6–62.7%, mammography 67.0–77.4%), so screening–stage tests have limited power and are partly circular with demographic and poverty covariates. CRC screening definitions differ between PLACES releases (ages 45–75 in 2022 vs 50–75 in 2020), so levels are not comparable. CHR mammography is Medicare fee-for-service women 65–74 only.
- CDC's 2024 and 2025 PLACES releases give Mississippi dental-visit values of 4.9–12.9% (BRFSS 2022), far below every other state sampled (about 39–66%) and the national estimate (63.9%); these were excluded and the 2023 release (BRFSS 2020; MS counties 38.5–69.1%) was used as a sensitivity covariate, with the caveat that it is older.
- Dental HPSA code values (0/1/2) were taken as published in AHRF 2025; code definitions were not in the downloaded technical documentation (2023–24 edition), so HPSA results are descriptive only.
- CDC WONDER mortality (state/county) is not accessible by API (national-only per CDC); not used.

## Deferred / not used (UMMC RDW)
Per Jake's 2026-11-27 decision, Papers 02–05 use public data only because UMMC pulls make him the bottleneck. Not used: (a) the earlier UMMC Patient Cohort Explorer request for this paper (ICD-10 C01–C06, C09, C10 by race/sex/age; ENT/radiation/medical oncology encounters; tobacco documentation), which would add subsite detail, local referral patterns and tobacco documentation; and (b) the former Paper 05 request (mammography, colonoscopy/FIT, and Pap/HPV procedure codes by race and primary-care encounter; stage from the tumor registry), which would link screening completion to stage at the patient level. Both remain possible later extensions.

## Next actions
- [x] Abstract merged and written (draft-v1, 2026-11-27); limit is ≤500 words incl. labels.
- [x] Abstract revised 2026-11-27 against [`guides/abstract-review-2026-11-27.md`](../../guides/abstract-review-2026-11-27.md) (Jake approved applying the fixes; 370 words). Isolated p-values dropped; approximate 95% CI added for breast incidence ratio 1.04 (see `results/abstract-ci-breast-incidence-rr.md`); conclusions no longer imply treatment or follow-up were measured; NPCR/NCHS/USDA/HRSA spelled out.
- [ ] Jake to review the revised `draft-v1.md` abstract and choose venue.
- [ ] Papers/05 folder kept for provenance; its status is "Merged into 02 on 2026-11-27 (Jake decision)".
- [ ] Re-verify SCP figures against live SCP pages immediately before any abstract submission (SCP updates yearly).
- [ ] Optional: query MSTAHRS (https://mstahrs.msdh.ms.gov/) manually for oral cavity/pharynx death counts by race and region (interactive; suppress cells under 5 by source rule, and under 11 in anything we report).
- [ ] Optional: US Cancer Statistics (https://gis.cdc.gov/Cancer/USCS/) manual query for MS subsite rates; CDC BRFSS Mississippi screening by race (unsmoothed) for Part B.

## Files
- `draft-v1.md` — merged abstract (revised 2026-11-27, 370 words), intro, methods, results tables (Parts A and B), discussion, references
- `results/abstract-ci-breast-incidence-rr.md` — approximate 95% CI for the breast incidence ratio 1.04, from published rate CIs
- `results/p02_results.md`, `results/p02b_results.md` — oral cavity/pharynx state and county output (AHRF dentist supply, HPSA, PLACES 2020)
- `results/p02_county_dataset.csv`, `results/p02b_county_dataset.csv` — county-level aggregates (82 rows)
- `../05-screening-gaps-cancer-stage/results/p05_results.md`, `p05b_results.md` and county CSVs — Part B output (provenance)
