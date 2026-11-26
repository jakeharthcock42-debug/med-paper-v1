# Data Sources Catalog — Mississippi County-Level Health Disparities

**Project context**: Supporting secondary data analysis for a medical student research paper/abstract on disparities of care across Mississippi counties (race, rural-urban, access). Target: local/regional conference abstract (e.g., MAFP, ACP MS chapter, UMMC Research Day).

**Last updated**: 2026-11-26  
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

## UMMC-Internal Resources (Not Public, but High-Value for This Project)

### Patient Cohort Explorer / Research Data Warehouse (RDW)
- ~750k patients, ~24M encounters; de-identified, date-shifted Epic data.
- Designed for rapid cohort discovery by UMMC researchers.
- **Potential**: True clinical ENT volumes, comorbidities, utilization patterns, race disparities within UMMC catchment.
- Access: Through Center for Informatics and Analytics / mentor.

### UMMC Biobank
- Specimens + linked clinical data (application required).

---

## Recommended Starter Stack for Current Project

For a free, public-data, conference-ready abstract on **county-level disparities**:

1. **County Health Rankings** → access metrics + premature death / preventable stays.
2. **MSTAHRS** → race-stratified mortality or maternal/infant outcomes.
3. **CDC PLACES** → hearing disability (ENT niche) or other condition prevalence.
4. **State Cancer Profiles** → if pursuing oral cavity & pharynx / head-neck angle.

Merge on county FIPS codes. Stratify by race (where available), rural-urban continuum, and access quintiles.

---

## Next Steps / Living Document Notes

- [ ] Download latest CHR Mississippi Excel and PLACES county file.
- [ ] Run sample MSTAHRS queries for diabetes / CVD / infant mortality by race and county.
- [ ] Check State Cancer Profiles for Oral Cavity & Pharynx rates in MS counties.
- [ ] Decide primary outcome (hearing disability vs mortality vs cancer incidence vs preventable stays).
- [ ] Identify UMMC mentor and confirm RDW access pathway.
- [ ] Draft specific aims once primary outcome chosen.

**File history**: Created 2026-11-26 as initial catalog for med-paper-v1. Expand with download links, variable dictionaries, and analysis notes as work progresses.
