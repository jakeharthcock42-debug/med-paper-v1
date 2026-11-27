# 02 — Oral Cavity & Pharynx Cancer: Racial and Rural Disparities in Mississippi

**Working title**: Racial Differences in Oral Cavity and Pharynx Cancer Incidence, Stage, and Mortality in Mississippi, 2019–2024: a Public-Data Ecological Analysis  
**Status**: **Public-data analysis complete; abstract draft-v1 written (2026-11-27).** Public-data-only by Jake's decision (2026-11-27); no UMMC pull is needed or planned.  
**Natural fit**: ENT / head & neck oncology; companion to Paper 01 (hearing loss).  
**Target**: UMMC Research Day, MAFP, ACP Mississippi abstracts → possible full paper  
**Novelty check (PubMed, 2026-11-27)**: no Mississippi-specific, race-stratified oral cavity/pharynx incidence–stage–mortality paper found (title searches); closest Mississippi precedents are other sites (Walker 2023 oesophageal; Kruse-Diehr 2021 CRC). Moderate novelty, local framing; nationally the Black–White oral cancer pattern is established. See `draft-v1.md` references.

## Research question
In Mississippi, how do oral cavity and pharynx cancer incidence, late-stage share, and mortality differ by race (Black vs White non-Hispanic), sex, and rurality, and are county patterns related to tobacco use and access to dental or primary care?

## Specific aims (all answerable from public sources)
1. Quantify Black vs White non-Hispanic differences in incidence, late-stage share, and mortality statewide (and male-only), and compare Mississippi with the US.
2. Describe county variation in incidence (54 of 82 counties have a published rate) and test rural (RUCC 4–9) vs metro (RUCC 1–3) differences.
3. Test county-level correlates of incidence and late-stage share: smoking, binge drinking, uninsurance, PCP and dentist supply (CHR and HRSA AHRF), dental HPSA status, dental visit and tooth loss (PLACES 2020), poverty, % Black.

## Hypotheses and results (public data)
| # | Hypothesis | Test | Result |
|---|---|---|---|
| H1 | Black NH residents have lower incidence but similar or higher mortality than White NH (higher mortality-to-incidence ratio) | Rate ratio from published age-adjusted rates and CIs (log-normal approx.); descriptive M:I | **Supported.** Incidence 9.5 (8.8–10.4) vs 15.6 (14.9–16.4) per 100k; RR 0.61 (0.55–0.67). Mortality 3.7 (3.2–4.2) vs 3.5 (3.2–3.9); RR 1.06 (0.89–1.25). M:I 0.39 vs 0.22 (men 0.44 vs 0.24) |
| H2 | Late-stage share is higher in Black than White NH | Chi-square on counts reconstructed from published average annual counts ×5 (approximate) | **Supported.** 73.1% vs 64.8%; approx. chi2 = 13.81, p < 0.001 |
| H3 | Nonmetro counties have higher incidence than metro | Mann-Whitney; WLS (weights = avg annual count), HC3 | **Not supported.** Median 14.6 (n=39) vs 13.9 (n=15); p = 0.306; WLS +1.10 per 100k (−0.36 to 2.56) |
| H4 | County incidence rises with smoking/binge drinking and falls with dentist/PCP supply | Spearman; OLS HC3 (n=54) | **Partly.** Smoking rho 0.03, binge 0.12 (n.s.). Dentists in private practice per 10k (AHRF 2023) rho −0.33 (p = 0.015); CHR dentists −0.26 (p = 0.054); PCP −0.16 (n.s.). In adjusted OLS dentists −0.53 per 10k (−1.10 to 0.04), p = 0.069 |
| H5 | Counties with fewer dentists/PCPs have a higher late-stage share | Spearman (n=34 counties with published % late) | **Supported (exploratory).** Dentists per 10k rho −0.51 (p = 0.002); CHR dentists −0.49 (p = 0.003); PCP −0.45 (p = 0.007); % Black −0.37 (p = 0.031). Dental visit, teeth lost, dental HPSA not associated |

Primary tests: H1 and H2 (state level). H3–H5 exploratory; unadjusted p-values (Bonferroni α for five hypotheses = 0.01; H5 dentist and PCP results remain below it).

## Data sources (all public; aggregates only)
| Source | URL | Years | Use |
|---|---|---|---|
| State Cancer Profiles (NPCR/CDC + NCHS), cancer code 003 Oral Cavity & Pharynx | https://statecancerprofiles.cancer.gov/ | Incidence and late stage 2019–2023; mortality 2020–2024 | Rates, CIs, counts, % late stage by county, race, sex |
| USDA ERS Rural-Urban Continuum Codes | https://www.ers.usda.gov/data-products/rural-urban-continuum-codes | 2023 | Metro (1–3) vs nonmetro (4–9) |
| HRSA Area Health Resources Files (AHRF) 2024–2025 | https://data.hrsa.gov/data/download?data=AHRF | Dentists in private practice 2023 (ADA masterfile); dental HPSA 2025; population 2023 | Dentist supply, shortage designation |
| CDC PLACES 2025 release | https://data.cdc.gov/d/swc5-untb | BRFSS 2023 (2022 for teeth lost) | Smoking, binge drinking, uninsured |
| CDC PLACES 2023 release (BRFSS 2020) | https://data.cdc.gov/d/h3ej-a9ec | 2020 | Dental visit and all-teeth-lost (see limits) |
| County Health Rankings (2025 annual; 25 Mar 2026 supplement) | https://www.countyhealthrankings.org/health-data/methodology-and-sources/data-documentation | PCP 2022; dentists 2023 | Access measures |
| Delta Regional Authority county list | https://dra.gov/wp-content/uploads/2022/04/Mississippi.pdf | 2016–2024 | Delta (DRA) indicator, 47 MS counties |

Reproducibility: `scripts/public-data/` (`p02.py`, `p02b.py`, `build_ahrf.py`, `build_places2020.py`, `build_master.py`, `scp_build.py`) and `results/` here.

## Limits
- SCP suppresses cells with fewer than 16 cases in 5 years. Of 82 counties: incidence published for 54; mortality 11; late-stage 34; Black NH incidence 10; White NH 35. County race and mortality analyses are not feasible, so race stays at state level. Published counties are larger (median population 28,768 vs 9,951), less Black (median 34.5% vs 50.8%) and less poor (child poverty 25.7% vs 32.1%) than suppressed counties.
- Mortality period (2020–2024) differs from incidence (2019–2023); M:I is a descriptive ratio of published age-adjusted rates, not survival.
- SCP does not separate subsites (oral cavity vs HPV-associated oropharynx) or give HPV status; USCS/NPCR subsite data could not be scripted (interactive).
- Ecological design; county correlations cannot be interpreted at the individual level. Dentist supply and PCP supply are correlated with each other and with urbanicity.
- PLACES is model-based (MRP; Greenlund 2022). CDC's 2024 and 2025 releases give Mississippi dental-visit values of 4.9–12.9% (BRFSS 2022), far below every other state sampled (about 39–66%) and the national estimate (63.9%); these were excluded and the 2023 release (BRFSS 2020; MS counties 38.5–69.1%) was used as a sensitivity covariate, with the caveat that it is older. Flag to CDC PLACES if desired.
- Dental HPSA code values (0/1/2) were taken as published in AHRF 2025; code definitions were not in the downloaded technical documentation (2023–24 edition), so HPSA results are descriptive only.
- CDC WONDER mortality (state/county) is not accessible by API (national-only per CDC); not used.

## Deferred / not used (UMMC RDW)
Per Jake's 2026-11-27 decision, Papers 02–05 use public data only because UMMC pulls make him the bottleneck. The earlier UMMC Patient Cohort Explorer request (ICD-10 C01–C06, C09, C10 by race/sex/age; ENT/radiation/medical oncology encounters; tobacco documentation) is **not used**. It would add subsite detail (oral cavity vs oropharynx), local referral patterns and tobacco documentation that SCP cannot provide, and remains a possible follow-up if Jake later chooses.

## Next actions
- [ ] Re-verify SCP figures against live SCP pages immediately before any abstract submission (SCP updates yearly).
- [ ] Optional: query MSTAHRS (https://mstahrs.msdh.ms.gov/) manually for oral cavity/pharynx death counts by race and region (interactive; suppress cells under 5 by source rule, and under 11 in anything we report).
- [ ] Optional: US Cancer Statistics (https://gis.cdc.gov/Cancer/USCS/) manual query for MS subsite rates (oral cavity vs oropharynx) by race.
- [ ] Jake: review and edit `draft-v1.md` abstract; choose venue.

## Files
- `draft-v1.md` — abstract (draft-v1), intro, methods, results tables, discussion, references
- `results/p02_results.md` — first-pass state and county output
- `results/p02b_results.md` — AHRF dentist supply, HPSA, PLACES 2020 dental analyses
- `results/p02_county_dataset.csv`, `results/p02b_county_dataset.csv` — county-level public aggregates used (82 rows)
