# 05 — Cancer Screening and Stage at Diagnosis (Breast, Colorectal, Cervical) in Mississippi

**Working title**: Cancer Screening, Primary Care Supply, and Late-Stage Diagnosis of Breast and Colorectal Cancer Across Mississippi Counties: a Public-Data Ecological Analysis  
**Status**: **Public-data analysis complete; abstract draft-v1 written (2026-11-27). WEAK / LOW-NOVELTY — see flag.** Public-data-only by Jake's decision (2026-11-27); no UMMC pull needed.  
**Natural fit**: Family medicine / internal medicine; MAFP and ACP Mississippi.  
**Novelty check (PubMed, 2026-11-27) — FLAG**: Mississippi breast and colorectal cancer screening and disparities have been published several times (Hall 2004 Delta screening; Zahnd 2019 Delta breast subtypes; Whatley 2014 GI cancers; Koutha 2025 and Vijayakumar 2025 colorectal cancer/screening in Mississippi; Barsha 2025 breast cancer research gaps). Our county-level screening → stage result is a null finding using model-based or Medicare-only screening measures. Recommend this be a secondary or merged abstract (e.g., combined with Paper 02 as a cancer-disparities series) rather than a standalone priority.

## Research question
In Mississippi, how do breast, colorectal, and cervical cancer incidence, mortality, and late-stage share compare with the US and by race, and are county screening rates and primary care supply associated with late-stage diagnosis?

## Specific aims (all public)
1. Compare Mississippi with the US and Black with White non-Hispanic residents for incidence, mortality, and late-stage share (SCP).
2. Describe county variation in screening (PLACES model-based; CHR Medicare mammography) by Delta (DRA) and rurality, and relate screening to PCP supply.
3. Test whether county screening and PCP supply are associated with county late-stage share (breast n=69, colorectal n=75 counties with published values).

## Hypotheses and results
| # | Hypothesis | Test | Result |
|---|---|---|---|
| H1 | Mississippi has higher mortality and late-stage share than the US for breast, colorectal, and cervical cancer | SCP state rows | **Supported.** CRC incidence 45.7 vs 36.9, mortality 17.5 vs 12.7, late 63.0% vs 60.2%. Breast incidence 125.9 vs 133.0 (lower), mortality 23.6 vs 18.9, late 35.1% vs 30.7%. Cervix incidence 9.0 vs 7.5, mortality 3.6 vs 2.1, late 55.7% vs 53.3% |
| H2 | Black mortality exceeds White, with incidence similar | Rate ratios from published CIs | **Supported.** Breast mortality 29.5 vs 20.7 (RR 1.43, 1.31–1.55) with incidence RR 1.04; CRC mortality 21.8 vs 15.8 (RR 1.38, 1.28–1.49), CRC incidence 51.2 vs 44.0 |
| H3 | Delta (DRA) and nonmetro counties have lower screening | Mann-Whitney | **Mixed.** Medicare mammography (CHR) DRA median 40% vs 44% (p = 0.003); nonmetro vs metro 42% vs 39.5% (p = 0.30). PLACES mammography and CRC screening differ by <1 point. Medicare flu vaccination lower in nonmetro (34% vs 37%, p = 0.006) |
| H4 | PCP supply is associated with screening | Spearman; OLS (HC3) | **Supported.** Medicare mammography +0.77 percentage points per additional PCP/10k (0.40–1.14; n = 82; R² = 0.37); nonmetro +2.9; CRC screening rho 0.39 with PCP per 100k |
| H5 | Counties with higher screening have lower late-stage share | Spearman; adjusted OLS/WLS | **Not supported after adjustment.** Breast late-stage vs Medicare mammography rho −0.33 (p = 0.006, n = 69) but adjusted coefficient −0.04 per point (−0.35, 0.27) after child poverty and PCP. PLACES mammography rho +0.10; PLACES CRC screening vs CRC late-stage rho −0.04 (n = 75); adjusted +0.14 (−0.70, 0.99); PLACES 2020 sensitivity −0.21 (−0.92, 0.50) |
| H6 (exploratory) | PCP supply is associated with lower late-stage share | OLS (HC3) | **Supported.** Breast late-stage −0.48 percentage points per PCP/10k (−0.86 to −0.10), p = 0.013; CRC −0.91 (−1.55 to −0.27), p = 0.005. Child poverty +2.8 pp per 10 points for breast late-stage (1.2–4.5) |
| H7 (descriptive) | Black–White Medicare mammography differs | Paired Wilcoxon (CHR, n = 81) | **No difference.** Median 42% (Black) vs 41% (White), p = 0.41; flu vaccination 31% vs 37% (p = 8e-12) |

## Data sources (all public; aggregates only)
| Source | URL | Years | Use |
|---|---|---|---|
| State Cancer Profiles (NPCR/CDC + NCHS): breast (055), colorectal (020), cervix (057) | https://statecancerprofiles.cancer.gov/ | Incidence/late stage 2019–2023; mortality 2020–2024 | Rates, % late stage, by county and (state) race |
| CDC PLACES 2025 release | https://data.cdc.gov/d/swc5-untb | BRFSS 2022: CRC screening (45–75), mammography (50–74); 2023: cholesterol screening, checkup | Model-based screening |
| CDC PLACES 2023 release | https://data.cdc.gov/d/h3ej-a9ec | BRFSS 2020: CRC screening (50–75), mammography | Sensitivity |
| County Health Rankings 2025 and 25 Mar 2026 supplement | https://www.countyhealthrankings.org/health-data/methodology-and-sources/data-documentation | Mammography screening 2023 (Medicare FFS women 65–74; Mapping Medicare Disparities Tool); flu vaccination 2023 | Observed (non-modeled) screening, race-specific |
| HRSA AHRF 2024–2025 | https://data.hrsa.gov/data/download?data=AHRF | PCP (MD+DO) 2023; primary-care HPSA 2025 | Access |
| USDA RUCC 2023; Delta Regional Authority list | see `data-sources.md` | | Rurality, Delta |

Reproducibility: `scripts/public-data/` (`p05.py`, `p05b.py`, `build_places2020.py`, `build_ahrf.py`, `build_master.py`, `scp_build.py`) and `results/` here.

## Limits
- PLACES screening estimates are model-based (MRP) and strongly smoothed (county ranges: CRC 49.6–62.7%, mammography 67.0–77.4%), so ecological screening–stage tests have limited power and are partly circular with demographic and poverty covariates.
- CRC screening definitions differ between PLACES releases (ages 45–75 in 2022 vs 50–75 in 2020), so levels are not comparable (median 55.0% vs 67.6%).
- CHR mammography is Medicare fee-for-service women 65–74 only; it excludes younger women and Medicare Advantage.
- SCP county late-stage % available for 69 (breast) and 75 (CRC) counties; cervical county data too sparse (incidence for 12 counties). Stage is defined as regional plus distant.
- Ecological design; screening and stage are measured in different populations and periods; no individual-level inference.

## Deferred / not used (UMMC RDW)
Per Jake's 2026-11-27 decision, Papers 02–05 use public data only. The earlier UMMC Patient Cohort Explorer request (screening procedure codes for mammography, colonoscopy/FIT, and Pap/HPV by race and primary-care encounter; stage at diagnosis from tumor registry) is **not used**. It would link screening completion to stage at the patient level, which public aggregates cannot; it remains a possible later extension.

## Next actions
- [ ] Abstract trimmed to <=300 words (including section labels); Jake to review; 05 merge-into-02 vs drop pending Jake.
- [ ] Jake: decide whether to merge this with Paper 02 as a cancer-disparities series or drop it.
- [ ] Optional manual: CDC BRFSS Mississippi state-level screening by race (SMART/BRFSS prevalence tool) to add a race-specific screening comparison without MRP smoothing.

## Files
- `draft-v1.md` — abstract (draft-v1), intro, methods, results tables, discussion, references
- `results/p05_results.md` — first-pass results; `results/p05b_results.md` — adjusted and sensitivity models
- `results/p05_county_dataset.csv`, `results/p05b_county_dataset.csv` — county aggregates (82 rows)
