# Data Sources Catalog — Mississippi County-Level Health Disparities

**Project context**: Supporting secondary data analysis for a medical student research paper/abstract on disparities of care across Mississippi counties (race, rural-urban, access). Target: local/regional conference abstract (e.g., MAFP, ACP MS chapter, UMMC Research Day).

**Last updated**: 2026-11-26 (Paper 01 county pull added)  
**Maintainer notes**: Focus on publicly available or low-barrier datasets. UMMC internal resources noted separately for potential enrichment.

---

## Tier 1 — Core Public Datasets (Highest Priority)

### 1. County Health Rankings & Roadmaps (CHR&R)
- **What it provides**: County-level health outcomes (premature death, low birthweight, etc.), health factors (primary care physician ratio, uninsured, preventable hospital stays, social/economic factors), rankings within Mississippi.
- **Geographic level**: All 82 Mississippi counties.
- **Years**: Multi-year downloads available (recent releases 2023–2025).
- **Access**: Free Excel/CSV downloads from [countyhealthrankings.org](https://www.countyhealthrankings.org/health-data/mississippi/data-and-resources).
- **Strengths for project**: Best single source for access metrics + outcomes. Easy merge on FIPS. Supports rural-urban and disparity framing.
- **Limitations**: Some measures are modeled or lagged; limited race stratification in core files.
- **ENT relevance**: Low (general access/outcomes only).
- **Suggested use**: Primary backbone for access → outcome analyses; stratify by rurality or poverty quintiles.
- **PULLED 2026-11-26 (Paper 01)**: 2025 release analytic file, all 82 MS counties: https://www.countyhealthrankings.org/sites/default/files/media/document/analytic_data2025_v3.csv. Variables used: PCP (AMA 2021), uninsured <65 (SAHIE 2022), % rural (2020 Census), % non-Hispanic Black (2023), children in poverty, median household income (2023). Year list: https://www.countyhealthrankings.org/sites/default/files/media/document/2025%20Select%20and%20additional%20measures%2C%20data%20sources%20and%20years.pdf. Results: `papers/01-hearing-loss-disparities/county-analysis.md`.

### 2. MSTAHRS (Mississippi Statistically Automated Health Resource System)
- **What it provides**: Vital statistics — births, deaths (cause-specific), infant deaths, pregnancies, early elective deliveries, population. Queryable by year, age, race, ethnicity, sex, county/region of residence.
- **Geographic level**: County or multi-county region.
- **Years**: Through 2023–2024 available.
- **Access**: Free public web query system — [mstahrs.msdh.ms.gov](https://mstahrs.msdh.ms.gov/).
- **Strengths**: Official state vital stats with race stratification. Ideal for mortality and maternal/infant disparities.
- **Limitations**: Aggregate only; some small-cell suppression; limited clinical detail.
- **ENT relevance**: Possible cause-of-death queries for head/neck cancers or related respiratory categories.
- **Suggested use**: Race-specific mortality rates (CVD, diabetes, cancer, infant) as primary outcomes; link to CHR access measures.

### 3. CDC PLACES: Local Data for Better Health (County Data)
- **What it provides**: Model-based county estimates for ~36–40 measures including health outcomes, preventive services, risk behaviors, disabilities, health status, and social needs. Includes **hearing disability among adults**.
- **Geographic level**: County (also tract and ZCTA available).
- **Years**: Annual releases (2023–2025 versions use recent BRFSS).
- **Access**: Free download from [data.cdc.gov](https://data.cdc.gov/) (search PLACES County Data).
- **Strengths**: Uniform small-area estimates; includes disability measures; easy to map and merge.
- **Limitations**: Model-based (not direct survey counts); caution against using for intervention evaluation.
- **ENT relevance**: **High** — hearing disability prevalence is the strongest free county-level ENT-related measure available.
- **Suggested use**: Primary source for hearing disability disparities; secondary for other chronic conditions or preventive care gaps.
- **PULLED 2026-11-26 (Paper 01)**: 2025 release (dataset `swc5-untb`, rows updated 2025-12-04; BRFSS 2023), measure `HEARING` (crude and age-adjusted % adults with hearing disability), 82 MS counties via the Socrata API: https://data.cdc.gov/resource/swc5-untb.csv?$where=stateabbr='MS' AND measureid='HEARING'. Dataset page: https://data.cdc.gov/500-Cities-Places/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb. Other disability measures in the same file (vision, cognition, mobility, self-care, independent living, any disability) are available for later papers.

### 4. State Cancer Profiles (NCI / CDC)
- **What it provides**: Cancer incidence and mortality rates by county, site, race, sex, age, stage (where available), rural-urban continuum.
- **Geographic level**: County.
- **Years**: Recent 5-year periods (e.g., 2019–2023).
- **Access**: Free interactive tables and downloads — [statecancerprofiles.cancer.gov](https://statecancerprofiles.cancer.gov/).
- **Strengths**: High-quality registry data; race and rural-urban stratification; oral cavity & pharynx (head/neck) site available.
- **Limitations**: Incidence more complete than detailed stage/treatment; small numbers in low-population counties.
- **ENT relevance**: **High** — Oral Cavity & Pharynx incidence is directly relevant to otolaryngology / head & neck oncology.
- **Suggested use**: Examine county-level disparities in head/neck cancer incidence or rates by race/rurality, linked to access metrics.

---

## Tier 2 — Supporting Public / Semi-Public Datasets

### 5. CMS Hospital Compare / Provider Data + Hospital Service Area
- **What it provides**: Hospital quality ratings, some process/outcome measures; Medicare inpatient claims summarized by hospital and patient ZIP (service area files).
- **Geographic level**: Hospital / ZIP / aggregatable to county.
- **Access**: Free from [data.cms.gov](https://data.cms.gov/).
- **Strengths**: Facility-level quality and utilization geography.
- **Limitations**: Medicare-focused; not all-payer.
- **ENT relevance**: Low–moderate (can identify hospitals offering ENT services indirectly).

### 6. HRSA Data Warehouse (Shortage Designations, UDS)
- **What it provides**: Primary care / mental health / dental HPSA designations; Uniform Data System (UDS) for FQHCs (patient demographics, quality measures, costs) for Mississippi.
- **Geographic level**: County / service area / state.
- **Access**: Free from [data.hrsa.gov](https://data.hrsa.gov/).
- **Strengths**: Official shortage designations; FQHC performance.
- **ENT relevance**: Low (primary care focused).

### 7. America’s Health Rankings + KFF State Health Facts
- **What it provides**: State and some sub-state rankings, disparities snapshots, insurance and access indicators.
- **Access**: Free.
- **Use**: Quick context and validation tables for manuscripts.

### 8. HCUP State Inpatient Databases (SID) — Mississippi
- **What it provides**: All-payer inpatient discharge abstracts (diagnoses, procedures, charges, demographics, hospital).
- **Geographic level**: Hospital / can aggregate to county of residence (if available).
- **Access**: Restricted; fee-based via HCUP Central Distributor. Student pricing sometimes available. Requires DUA + training.
- **Strengths**: Rich clinical detail (ICD codes for ENT procedures/diagnoses possible).
- **Limitations**: Cost and access barriers; not “public” in the free sense.
- **ENT relevance**: Potentially high if obtained (otitis, sinus procedures, tonsillectomy, head/neck cancer admissions, etc.).

---

## Tier 1b — Added during Paper 01 (public)

### 4b. American Community Survey (ACS) 5-year 2020–2024, Table-Based Summary File (U.S. Census Bureau)
- **What it provides**: County estimates for hearing difficulty by sex and age (B18102), race (B02001), poverty (B17001), and thousands of other tables; all 82 MS counties.
- **Years**: ACS 5-year 2020–2024.
- **Access**: Free bulk files, no key: https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/ (file names `acsdt5y2024-<table>.dat`, pipe-delimited, all geographies; geography key in `documentation/Geos20245YR.txt`; labels in `ACS20245YR_Table_Shells.txt`). The Census API (`api.census.gov`) returned "Missing Key" on 2026-11-26, so bulk files were used instead of requesting a key.
- **Limitations**: Self-reported difficulty; sampling error is large in small counties (margins of error are in the `_M` columns; not propagated in Paper 01); civilian noninstitutionalized population only.
- **Used in**: Paper 01 (`papers/01-hearing-loss-disparities/county-analysis.md`).

---

## UMMC-Internal Resources

### Patient Cohort Explorer / Research Data Warehouse (RDW) — ACCESS CONFIRMED
- **Data-use status**: Data use confirmed by Jake Harthcock 2026-11-26 per the Cohort Explorer guide. Extracted rules with page cites: [`data-use-rules.md`](data-use-rules.md). Jake runs all queries; AI tools have no direct access to the Explorer.
- **Suppression rule (project)**: never record a UMMC RDW cell under 11 ("<11 (suppressed)"), with complementary suppression where a hidden cell could be backed out. The app itself only allows report view/export when the population is greater than 25 (guide p. 20). Public county data are unaffected.
- **Active request list (Paper 01)**: `papers/01-hearing-loss-disparities/rdw-data-requests.md`.
- **Status**: Student has confirmed access and can run queries / export aggregate or de-identified results.
- **What it provides**: De-identified, date-shifted data from Epic covering ~750,000 patients and ~24 million encounters (updated quarterly). Supports rapid cohort discovery by diagnosis, procedure, demographics, encounter type, etc.
- **Potential for this project**:
  - Race/ethnicity and (if available) patient residence ZIP or county → disparities within UMMC catchment.
  - ENT-relevant cohorts: hearing loss, chronic otitis, chronic sinusitis, tonsil/adenoid disease, head & neck cancers, dysphagia, etc.
  - Utilization patterns (ED vs outpatient vs inpatient), comorbidity burden, and simple outcome proxies.
  - Ability to generate counts, demographic tables, and basic stratified rates that complement public county-level data.
- **Access notes**: Queries run by the student; results can be shared as aggregate tables or limited exports that remain de-identified.
- **Suggested early queries** (see dedicated section below).

### UMMC Biobank
- Specimens + linked clinical data (application required).

---

## Proposed RDW Queries (for student to run)

These are designed to be low-burden exploratory queries that can quickly inform whether an ENT-focused or broader disparities abstract is feasible with UMMC data.

**Query set A — Feasibility / Denominators**
1. Total unique patients in RDW with any encounter in the last 5 years (or most recent available window).
2. Breakdown of those patients by race/ethnicity and by sex.
3. If ZIP or county of residence is available in the de-identified data: count of patients by Mississippi county (or by rural vs non-rural ZIP).

**Query set B — ENT-relevant cohorts (pick 1–2 to start)**
1. Patients with any diagnosis of hearing loss / sensorineural hearing loss / conductive hearing loss (use common ICD-10 codes or the Explorer’s diagnosis search).
2. Patients with chronic sinusitis or chronic rhinosinusitis.
3. Patients with head & neck cancer diagnoses (oral cavity, pharynx, larynx, etc.).
4. For each of the above: age distribution, race/ethnicity distribution, and (if possible) proportion with at least one ENT specialty encounter or relevant procedure.

**Query set C — Access / utilization signal**
1. Among patients with a hearing-loss diagnosis, proportion who had an audiology or ENT encounter within 12 months of the first coded diagnosis (if timing is feasible).
2. Simple comparison of ED utilization or inpatient admission rates for ENT-related diagnoses by race.

**Output preference**: Aggregate counts and percentages in tables (no row-level data needed). Suppress any cell under 11 (project rule).

Once results from A + one of B are available, we can decide whether to lean into an ENT-specific abstract (e.g., disparities in documented hearing loss or head/neck cancer care at UMMC) or keep the broader county-level public-data frame and use RDW only for complementary local context.

---

## Recommended Starter Stack for Current Project

**Option 1 — Pure public data (fastest to abstract)**  
CHR + MSTAHRS + PLACES (hearing disability) ± State Cancer Profiles.

**Option 2 — Hybrid (higher clinical specificity)**  
Public county data for context + RDW-derived UMMC cohort tables for race/utilization disparities in one or two ENT conditions.

Merge public data on county FIPS; use RDW for within-catchment clinical detail.

---

## Next Steps / Living Document Notes

- [x] Confirm RDW / Patient Cohort Explorer access.
- [x] Download latest CHR Mississippi data and PLACES county file (done 2026-11-26 for Paper 01: CHR 2025 analytic data, PLACES 2025 release; also ACS 2020–2024).
- [ ] Run sample MSTAHRS queries for diabetes / CVD / infant mortality by race and county.
- [ ] Check State Cancer Profiles for Oral Cavity & Pharynx rates in MS counties.
- [ ] Run RDW Query set A + at least one from set B and share aggregate results (Paper 01 version: `rdw-data-requests.md`, R0 to R11).
- [x] Decide primary outcome / niche for Paper 01: hearing loss (H90.3) at UMMC + county-level hearing disability context. Other niches: later papers.
- [ ] Draft specific aims once primary outcome chosen.

**File history**:  
- Created 2026-11-26 as initial catalog.  
- Updated 2026-11-26: Confirmed student RDW access; added proposed query sets and hybrid analysis option.
- 2026-11-26: Paper 01 pass: pulled CDC PLACES 2025 (HEARING), ACS 2020–2024 (B18102, B02001, B17001), CHR&R 2025 for 82 counties; linked `data-use-rules.md`; recorded Jake's data-use confirmation and the <11 suppression rule.
