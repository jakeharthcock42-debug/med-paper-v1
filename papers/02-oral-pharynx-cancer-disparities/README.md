# 02 — Oral Cavity & Pharynx Cancer: Racial and Rural Disparities in Mississippi

**Working title**: Racial and Geographic Disparities in Oral Cavity and Pharynx Cancer Incidence, Stage at Diagnosis, and Mortality in Mississippi, 2019–2024  
**Status**: First-pass public-data analysis done (2026-11-26); draft skeleton in `draft-v1.md`; UMMC add-on requests ready to run  
**Natural fit**: ENT / head & neck oncology; companion to Paper 01 (hearing loss).  
**Target**: UMMC Research Day, MAFP, ACP Mississippi abstracts → possible full paper  
**Public-data sufficiency**: Yes at state level (race) and for the 54 counties with published rates (rurality). County-level race and mortality are mostly suppressed at the source.

## Research question
In Mississippi, how do oral cavity and pharynx cancer incidence, late-stage share, and mortality differ by race (Black vs White non-Hispanic), sex, and rurality, and are county patterns related to tobacco/alcohol use and access to primary care or dental care?

## Specific aims
1. Quantify Black vs White non-Hispanic differences in incidence, late-stage share, and mortality statewide (and male-only) and compare Mississippi with the US.
2. Describe county variation in incidence (54 of 82 counties have a published rate) and test rural (RUCC 4–9) vs metro (RUCC 1–3) differences.
3. Test county-level correlates: smoking, binge drinking, uninsurance, PCP and dentist supply, poverty.
4. (Optional UMMC add-on) Describe UMMC patients with oral cavity/oropharyngeal cancer by race, sex, and receipt of specialty care.

## Hypotheses and planned tests (with first-pass status)
| # | Hypothesis | Planned test | First-pass result (public data) |
|---|---|---|---|
| H1 | Black NH residents have lower incidence but equal or higher mortality than White NH (higher mortality-to-incidence ratio) | Rate ratio from published age-adjusted rates and 95% CIs (log-normal approx); descriptive M:I ratio | **Supported (descriptive).** Incidence 9.5 (8.8–10.4) vs 15.6 (14.9–16.4) per 100k; RR 0.61 (0.55–0.67). Mortality 3.7 (3.2–4.2) vs 3.5 (3.2–3.9); RR 1.06 (0.89–1.25). M:I 0.39 vs 0.22 |
| H2 | Late-stage share is higher in Black than White NH | Chi-square on counts reconstructed from published average annual counts ×5 (approximate) | **Supported.** 73.1% vs 64.8%; approx chi2 = 13.81, p < 0.001 |
| H3 | Nonmetro counties have higher incidence than metro counties | Mann-Whitney; WLS (weights = avg annual count) with HC3 SE | **Not supported / underpowered.** Median 14.6 (n=39) vs 13.9 (n=15); MW p = 0.306; WLS +1.10 per 100k (95% CI −0.36 to 2.56), p = 0.138 |
| H4 | County incidence correlates positively with smoking and binge drinking, negatively with PCP/dentist supply | Spearman; OLS (HC3) | **Not supported.** Smoking rho 0.026 (p = 0.851); binge 0.116 (p = 0.405); dentists −0.263 (p = 0.054); PCP −0.160 (p = 0.249); n = 54 |
| H5 (exploratory) | Counties with lower PCP supply have a higher late-stage share | Spearman | rho −0.454 (p = 0.007), n = 34 counties; exploratory, one of several tests |

Planned primary tests for the abstract: H1 and H2 (state level). H3–H5 are exploratory; report unadjusted p-values and state that no multiplicity correction was applied (or use Bonferroni α = 0.01 for the five tests).

## Data sources (all public; aggregates only)
| Source | URL | Years | Use |
|---|---|---|---|
| State Cancer Profiles (NPCR/CDC + NCHS), cancer code 003 Oral Cavity & Pharynx | https://statecancerprofiles.cancer.gov/ | Incidence 2019–2023 (NPCR 2025 submission); mortality 2020–2024 | Rates, CIs, avg annual counts, % late stage, by county, race, sex |
| USDA ERS Rural-Urban Continuum Codes | https://www.ers.usda.gov/data-products/rural-urban-continuum-codes | 2023 | Metro (1–3) vs nonmetro (4–9) |
| CDC PLACES county data, 2025 release | https://data.cdc.gov/d/swc5-untb | BRFSS 2022–2023 | Smoking, binge drinking, uninsured, teeth lost |
| County Health Rankings supplemental release (25 Mar 2026) | https://www.countyhealthrankings.org/health-data/methodology-and-sources/data-documentation | PCP 2022; dentists 2023 | Access measures |
| Delta Regional Authority county list | https://dra.gov/wp-content/uploads/2024/03/DRA-FY-2025-Buget-Justification-FINAL_Updated03072025.pdf and https://dra.gov/wp-content/uploads/2022/04/Mississippi.pdf | 2016–2024 | Delta (DRA) indicator, 47 MS counties |

Reproducibility: `results/` files here plus `scripts/public-data/` at the repo root.

## Feasibility notes and limits
- SCP suppresses any area-race-sex cell with fewer than 16 cases in 5 years. Of 82 counties: incidence rate published for 54; mortality 11; late-stage 34; Black NH incidence 10; White NH incidence 35. County Black/White and mortality analyses are therefore not feasible; keep race at state level.
- Suppression removes mostly small rural counties, so rural vs metro comparisons are biased toward larger rural counties.
- The mortality period (2020–2024) differs from the incidence period (2019–2023); M:I ratios are descriptive ratios of published age-adjusted rates, not survival.
- Oral cavity and pharynx includes HPV-associated oropharynx and tobacco/alcohol-associated oral cavity; SCP does not separate subsites. Subsite and HPV status need UMMC data or registry access.
- Ecological analysis; no individual-level inference.
- The PLACES "dental visit" measure was excluded (published values 4.9–12.9% are implausible and need verification) [PENDING].

## Next actions
- [ ] Verify SCP figures against the live SCP pages once more before an abstract is submitted (SCP updates yearly).
- [ ] [PENDING] Query MSTAHRS (https://mstahrs.msdh.ms.gov/) for oral cavity/pharynx cause-of-death counts by race and region (interactive; suppress cells under 11).
- [ ] [PENDING] Check US Cancer Statistics (https://gis.cdc.gov/Cancer/USCS/) for MS subsite-level (oral cavity vs oropharynx) rates by race.
- [ ] Decide framing: state-level race story (H1–H2) is the strongest.
- [ ] Run the UMMC add-on below if Jake wants a local clinical angle.

## Optional UMMC RDW add-on (data-use cleared by Jake 2026-11-26; ready to run)
Run in Patient Cohort Explorer; one selection per box; report **aggregates only, suppress any cell under 11**.
1. One query per ICD-10 code, in priority order: **C10** (oropharynx), **C09** (tonsil), **C01** (base of tongue), **C02** (other tongue), **C04** (floor of mouth), **C03** (gum), **C06** (other/unspecified mouth). For each: total patients; by race (Black / White / other); by sex; by age group (<50, 50–64, 65+).
2. For each code with enough patients: count with at least one Otolaryngology encounter, and (if the Explorer's department/encounter filters allow) Radiation Oncology and Medical Oncology encounters, by race.
3. Cross-box (different boxes): same code + Diagnosis Name containing "nicotine dependence" or "tobacco" to estimate tobacco-use documentation by race.
4. Return a small table: code × race × (N, ENT encounter N).
Use: UMMC Table 1 and a care-utilization comparison that complements the state-level public findings.

## Files
- `draft-v1.md` — manuscript skeleton (cited intro, methods, empty tables)
- `results/p02_results.md` — full first-pass output with all tests
- `results/p02_county_dataset.csv` — county-level public aggregates used (82 rows)
