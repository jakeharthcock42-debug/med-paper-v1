# 03 — Primary Care Supply and the Black–White Premature Mortality Gap Across Mississippi Counties

**Working title**: Primary Care Physician Supply and the Black–White Gap in Premature Mortality Across Mississippi's 82 Counties: a Public-Data Ecological Analysis  
**Status**: **Public-data analysis complete; abstract draft-v1 written (2026-11-27).** Public-data-only by Jake's decision (2026-11-27); no UMMC pull needed.  
**Natural fit**: Family medicine / internal medicine (MAFP, ACP Mississippi).  
**Novelty check (PubMed, 2026-11-27) — PARTIAL OVERLAP, FLAG**: Lee JE et al., *Prev Chronic Dis* 2026;23:E32 (PMID 42594183) modeled county premature mortality (YPLL) in Mississippi 2015–2025 from the same County Health Rankings source, with spatial models and socioeconomic drivers, but not race-specific rates, primary care supply, or the Black–White gap. No Mississippi paper on primary care supply by race and premature mortality was found. The contribution here is the race-stratified PCP–mortality association and gap analysis; the descriptive Black–White gap is not new in itself. Moderate-to-low novelty; best as an MAFP/ACP abstract.

## Research question
Across Mississippi's counties, is primary care physician supply associated with premature mortality, and does the association (and the Black–White gap in premature mortality) differ by race and county context?

## Specific aims (all public)
1. Quantify the Black–White gap in age-adjusted premature mortality, years of potential life lost (YPLL), and life expectancy in counties where both are published.
2. Test the association of primary care supply (AHRF MD+DO per 10,000; CHR PCP rate) with premature mortality overall and separately for White and Black residents, adjusting for child poverty, uninsurance, rurality, and % Black.
3. Test whether the Black–White gap varies with PCP supply, child poverty, % Black, and residential segregation.
4. Describe chronic-disease prevalence (PLACES; model-based) by Delta (DRA) and rurality, and its relation to PCP supply.

## Hypotheses and results
| # | Hypothesis | Test | Result |
|---|---|---|---|
| H1 | Black premature mortality exceeds White in nearly all counties | Paired Wilcoxon (CHR 2021–23) | **Supported.** Median age-adjusted premature mortality 742 vs 601 per 100k; Black higher in 71 of 80 counties; p = 3e-12. YPLL median 16,569 vs 12,377 (73/80). Life expectancy median 70.0 vs 72.5 years (Black lower in 64/75). State: 715 vs 550 per 100k (ratio 1.30); life expectancy 70.3 vs 73.6 |
| H2 | Higher PCP supply is associated with lower overall premature mortality after adjustment | OLS (HC3), n = 82 | **Not supported.** AHRF PCP per 10k −3.6 (95% CI −13.9 to 6.7) per 100k, p = 0.49. Unadjusted rho −0.10. CHR-based first pass: −1.9 (−10.2 to 6.4) |
| H3 | The PCP association differs by race | Race-specific OLS; gap model (Black − White) | **Supported (exploratory).** White premature mortality −10.0 per 100k per additional PCP/10k (−17.0 to −2.9), p = 0.006 (WLS −10.3, −19.7 to −0.9); Black +3.6 (−6.1 to 13.3), p = 0.47. Gap model (n = 80): PCP +11.4 per 10k (0.8 to 22.0), p = 0.035, i.e. more PCPs per capita goes with a wider gap |
| H4 | Child poverty is the dominant correlate of mortality and of the gap | OLS | **Supported.** Child poverty +83.0 per 100k per 10 points (24.6–141.4), p = 0.005 (first pass, n = 79); in race-specific models Black +109 (67–151), White +50 (23–78); gap +64 (32–97) per 10 points. Segregation not associated (rho −0.004) |
| H5 | Chronic disease prevalence is higher in Delta (DRA) counties and where PCPs are scarce | Mann-Whitney; Spearman (PLACES BRFSS 2023, model-based) | **Supported, descriptive.** Diabetes DRA 15.3% vs 13.5% (p = 0.00015); CHD 7.1 vs 6.6; stroke 4.5 vs 3.9; hypertension 44.3 vs 41.3. PCP/10k vs CHD rho −0.36, stroke −0.27, diabetes −0.23 |

H2–H5 exploratory; unadjusted p-values; H3 is the key finding to treat cautiously (race-specific county rates are published for larger counties only; PCP supply tracks urbanicity and affluence).

## Data sources (all public; aggregates only)
| Source | URL | Years | Use |
|---|---|---|---|
| County Health Rankings 2025 annual and 25 Mar 2026 supplement | https://www.countyhealthrankings.org/health-data/methodology-and-sources/data-documentation | Premature death (YPLL), age-adjusted premature mortality, life expectancy 2021–2023 (NCHS); PCP 2022 and dentists 2023 (AHRF); uninsured 2023; preventable hospital stays 2023 (Medicare); children in poverty 2023 (SAIPE); unemployment 2023 (BLS); segregation 2019–2023 (ACS) | Outcomes and covariates (race-specific where published) |
| HRSA AHRF 2024–2025 | https://data.hrsa.gov/data/download?data=AHRF | PCP (MD+DO non-federal, excl. residents) 2023; primary-care HPSA 2025; population 2023 | Primary exposure |
| CDC PLACES 2025 release | https://data.cdc.gov/d/swc5-untb | BRFSS 2023 | Chronic-disease prevalence (model-based; MRP circularity with demographics/poverty) |
| USDA RUCC 2023; Delta Regional Authority list | see `data-sources.md` | | Rurality, Delta |

CHR measure years are taken from the CHR 2025 technical documentation and the supplement codebook (previous [PENDING] resolved).

Reproducibility: `scripts/public-data/` (`p03.py`, `p03b.py`, `build_ahrf.py`, `build_master.py`) and `results/` here.

## Limits
- Ecological; county race-specific premature mortality is published for 80–81 of 82 counties but with wide uncertainty in small counties.
- AHRF PCP counts are physician counts (not FTE, no NPs/PAs); correlated with urbanicity and affluence (AHRF vs CHR PCP rate rho = 0.97).
- Primary-care HPSA code definitions (0/1/2) were not in the downloaded AHRF technical documentation (2023–24 edition); used descriptively only.
- PLACES is model-based; PLACES–poverty and demographic associations are partly circular. Premature-mortality outcomes come from NCHS vital statistics (not modeled).
- Overlap with Lee 2026 (same CHR premature death data; county spatial trends).
- CDC WONDER county mortality by race, cause, and age is not accessible by API (national-only per CDC) and was not used.

## Deferred / not used (UMMC RDW)
Per Jake's 2026-11-27 decision, Papers 02–05 use public data only. The earlier UMMC Patient Cohort Explorer request (E11.x, I10 patients by race with ≥1 primary-care encounter; visit counts and A1c/BP control by race) is **not used**. It would show UMMC-clinic chronic-disease management by race, which public aggregates cannot, and remains a possible later extension.

## Next actions
- [ ] Jake: review/edit `draft-v1.md` abstract; decide whether the Lee 2026 overlap warrants reframing to emphasize the race-specific PCP finding.
- [ ] Optional manual: CDC WONDER state-level premature deaths by race and cause; MSTAHRS county data (cells under 11 suppressed).
- [ ] Optional: add NP/PA supply from AHRF (NPI-based variables `np_npi_23`) as a sensitivity analysis.

## Files
- `draft-v1.md` — abstract (draft-v1), intro, methods, results tables, discussion, references
- `results/p03_results.md` — CHR/PLACES first pass; `results/p03b_results.md` — AHRF PCP analyses by race
- `results/p03_county_dataset.csv`, `results/p03b_county_dataset.csv` — county aggregates (82 rows)
