# Data Sources Catalog — Mississippi County-Level Health Disparities

**Project context**: Supporting secondary data analysis for a medical student research paper/abstract on disparities of care across Mississippi counties (race, rural-urban, access). Target: local/regional conference abstract (e.g., MAFP, ACP MS chapter, UMMC Research Day).

**Last updated**: 2026-11-27 (Paper 01 draft-v2 literature sources logged; official RDW citation already recorded)  
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

## Tier 1c — Added during Papers 02–05 (public)

### 4c. State Cancer Profiles — detailed county extracts (NCI/CDC)
- **Pulled**: Oral cavity & pharynx (code 003), colon & rectum (020), female breast (055), cervix (057), lung & bronchus (047); incidence (2019–2023, NPCR 2025 submission), mortality (2020–2024), late-stage incidence and % late stage; all races, White NH (07), Black NH (28), male/female for oral cavity.
- **Access**: CSV export via the SCP table URL with `output=1` (e.g., `https://statecancerprofiles.cancer.gov/incidencerates/index.php?stateFIPS=28&areatype=county&cancer=003&race=00&sex=0&age=001&stage=999&year=0&type=incd&sortVariableName=rate&sortOrder=default&output=1`; mortality uses `/deathrates/` and `type=death`).
- **Suppression**: SCP suppresses area-race-sex cells with fewer than 16 cases in 5 years. For oral cavity: all-race county incidence published for 54/82 counties, mortality 11, Black NH incidence 10. County race-specific analysis is not feasible for rare cancers.
- **Saved**: `data/public/scp_all_long.csv`; scripts in `scripts/public-data/`.

### 4d. County Health Rankings — March 2026 supplemental release
- 2026 has **no annual release**; CHR&R published a supplemental release on 2026-03-25 (updated mortality 2021–2023, LBW and teen births 2018–2024, infant mortality 2017–2023, PCP 2022, mammography 2023, with White/Black values) and the website goes offline after Dec 2026 — download is already saved in the pipeline; re-download from https://www.countyhealthrankings.org/health-data/methodology-and-sources/data-documentation if needed.
- Race-specific county values are published only where reliable. Raw files store rates as fractions; scale as in `scripts/public-data/build_master.py`.

### 4e. USDA ERS Rural-Urban Continuum Codes 2023
- https://www.ers.usda.gov/data-products/rural-urban-continuum-codes (metro = 1–3, nonmetro = 4–9). Used in Papers 02–05.

### 4f. Delta Regional Authority (DRA) Mississippi county list
- 47 DRA-designated counties (distressed + non-distressed). Sources: https://dra.gov/wp-content/uploads/2024/03/DRA-FY-2025-Buget-Justification-FINAL_Updated03072025.pdf (2024 designations) and https://dra.gov/wp-content/uploads/2022/04/Mississippi.pdf (2016–2019 plan; adds Jasper). DRA ≠ the narrow Mississippi Delta floodplain; label as "DRA (Delta region) county".

### 4g. Notes on PLACES (all papers)
- Dataset ids: county long format `swc5-untb`; GIS-friendly wide `i46a-9kgh` (2025 release; https://data.cdc.gov). Model-based (MRP; Greenlund 2022) with county poverty as an input, so PLACES–poverty correlations are partly built in.
- **Data-quality flag**: the PLACES `DENTAL` measure ("visited dentist, past year", 2022) is 4.9–12.9% across MS counties, which is implausibly low for adults; excluded. **Update 2026-11-27:** confirmed anomalous in CDC's own 2024 and 2025 releases; see 4j (2020-based sensitivity measure).

### 4h. Interactive or not yet scripted [PENDING]
- **MSTAHRS** (https://mstahrs.msdh.ms.gov/): interactive query only; cells under 5 suppressed by MSTAHRS (we suppress under 11). Needed for cause-specific deaths by race/county, preterm birth, prenatal care.
- **CDC WONDER**: API is national-only; county/race queries must be run in the web interface.
- **HRSA** HPSA data (https://data.hrsa.gov/data/download), **AHRF** (https://data.hrsa.gov/topics/health-workforce/ahrf), **March of Dimes** maternity care deserts (https://www.marchofdimes.org/maternity-care-deserts-report), **CDC BRFSS Prevalence & Trends** (https://www.cdc.gov/brfss/brfssprevalence/): HPSA data-warehouse download and CDC BRFSS Prevalence & Trends not yet pulled; **AHRF and PLACES 2020 were pulled 2026-11-27 (see 4i, 4j); March of Dimes PeriStats state figures are cited in 4k.**
- Census API requires a key (not used); ACS values reach the papers through CHR and the bulk files noted in 4b.

## Tier 1d — Added 2026-11-27 (public-data-only completion of Papers 02–05)

### 4i. HRSA Area Health Resources Files (AHRF) 2024–2025 — pulled
- https://data.hrsa.gov/data/download?data=AHRF (CSV zip `AHRF_2024-2025_CSV.zip`; NCHWA; released Dec 2025). County file, Mississippi FIPS 28 (82 counties). Used: non-federal OB-GYN MDs (`md_nf_obgyn_gen_23`, AMA masterfile 2023); short-term general hospitals with obstetric care (`stgh_obstetrc_care_23`, AHA survey 2023); APN midwives with NPI (`apn_midwvs_npi_23`); 3-yr average births and preterm births 2021–2023 (`births_3yr_avg_23`, `births_pretrm_3yr_avg_23`; NCHS natality); dentists in private practice (`dent_nf_prvprac_23`, ADA masterfile) and with NPI; primary care MD+DO excl. residents (`md_nf_prim_care_pc_excl_rsdnt_23`, `do_nf_prim_care_pc_excl_rsdnt_23`); primary-care and dental HPSA codes (`hpsa_prim_care_25`, `hpsa_dent_25`; code definitions not verified in the downloaded 2023–24 technical documentation, used descriptively); Census 2023 population. Variable definitions: AHRF 2023–2024 technical documentation (https://data.hrsa.gov/DataDownload/AHRF/AHRF%202023-2024%20User%20Tech.zip). Caveat: AHRF county preterm % gives 16.9% birth-weighted vs the official NCHS state figure 14.95% (2023), so use for within-state comparison only.
- Saved: merged into `data/public/master_county_ms.csv` (`ahrf_*` columns); script `scripts/public-data/build_ahrf.py`.

### 4j. CDC PLACES 2023 release (BRFSS 2020) — pulled as sensitivity
- https://data.cdc.gov/d/h3ej-a9ec (age-adjusted prevalence, county, Mississippi): `DENTAL` (visited dentist or dental clinic in past year, 38.5–69.1%), `TEETHLOST`, `COLON_SCREEN` (ages 50–75 in this release; 45–75 in the 2025 release), `MAMMOUSE`. **Resolution of the 4g dental flag:** the 2024 (`fu4u-a9bh`) and 2025 releases both give Mississippi `DENTAL` (BRFSS 2022) of 4.9–12.9% (Hinds 7.9%), against about 39–66% in sampled counties of other states and the national estimate 63.9%; the 2020-based values are plausible. 2022-based Mississippi DENTAL remains excluded (likely a BRFSS 2022 Mississippi data issue; not confirmed by CDC); `pl20_dental` is used as a sensitivity covariate. Script: `scripts/public-data/build_places2020.py`.

### 4k. State-level birth outcome sources (published tables)
- NCHS, *Infant Mortality in the United States, 2022* (NVSR 73(5)): https://www.cdc.gov/nchs/data/nvsr/nvsr73/nvsr73-05.pdf — Mississippi 9.11 per 1,000 (highest).
- Mississippi State Department of Health, *Mississippi Child Death Review 2021 and 2022 deaths* (Feb 2025): https://msdh.ms.gov/resources/media/21025.pdf — IMR 2022 Black NH 12.1, White NH 7.2 (MSDH Vital Records; CDC WONDER).
- March of Dimes PeriStats (NCHS final natality), preterm by race, Mississippi 2022–2024 average: https://www.marchofdimes.org/peristats/data?obj=1&reg=99&slev=4&sreg=28&stop=63&top=3 — Black 18.5%, White 12.7%, Hispanic 11.0% (retrieved 2026-11-27).
- NCHS VSRR 35, *Births: Provisional Data for 2023*: https://www.cdc.gov/nchs/data/vsrr/vsrr035.pdf — US preterm Black 14.65%, White 9.45%; Mississippi 14.95%.
- NCHS DQS infant mortality by race and state (retired topic; data.cdc.gov `pjb2-jvdr`, last period 2013–2015): checked, not used.

### 4l. Checked, not usable or not scripted (2026-11-27)
- **CDC WONDER** (mortality and natality): the API accepts national queries only (https://wonder.cdc.gov/wonder/help/wonder-api.html); state/county/race queries require the web form, which was not scripted. Natality county detail is limited to counties of 100,000+ residents. Remains an optional manual follow-up.
- **MSTAHRS**: interactive; not scripted.
- **CDC PRAMStat** (data.cdc.gov): files only through 2011, no Mississippi 2012+ data.
- **State Cancer Profiles**: no oral cavity subsite (oral cavity vs oropharynx) breakdown; US Cancer Statistics subsite queries are interactive and not scripted.
- **Census API**: key required; not used. **Novelty searches** run with PubMed E-utilities (`scripts/public-data/pubmed.py`), 2026-11-27.

---

## UMMC-Internal Resources

### Patient Cohort Explorer / Research Data Warehouse (RDW) — ACCESS CONFIRMED
- **Data-use status**: Data use confirmed by Jake Harthcock 2026-11-26 per the Cohort Explorer guide. Extracted rules with page cites: [`data-use-rules.md`](data-use-rules.md). Jake runs all queries; AI tools have no direct access to the Explorer.
- **Official citation** (UMMC Center for Informatics and Analytics internal guidance, provided by Jake Harthcock 2026-11-27): University of Mississippi Medical Center, Center for Informatics and Analytics (2020): Patient Cohort Explorer. figshare. Software. https://doi.org/10.6084/m9.figshare.12252737. The DOI resolved (HTTP 302) to https://figshare.com/articles/software/Patient_Cohort_Explorer/12252737 (figshare API confirms the 2020 software record).
- **Human-protection boilerplate** (quote verbatim when a statement is required): “The data warehouse from which the information for this study is derived has been de-identified and date-shifted so that it does not include any protected health information (PHI). Pursuant to 45 CFR 46, use of this database does not meet the definition of human subjects’ research and does not require IRB review.”
- **Date-shifting**: because the warehouse is date-shifted, displayed calendar dates and windows may not correspond to true calendar dates. Do not claim that within-patient intervals are preserved unless a source states that.
- **Suppression rule (project)**: never record a UMMC RDW cell under 11 ("<11 (suppressed)"), with complementary suppression where a hidden cell could be backed out. The app itself only allows report view/export when the population is greater than 25 (guide p. 20). Public county data are unaffected.
- **Active request list (Paper 01)**: `papers/01-hearing-loss-disparities/rdw-data-requests.md`. Recorded: R0 (N = 15,612), R1 (race), R3 (unfiltered RDW base: 1,658,574 patients, 73,271,189 encounters; Black 684,322, 41.26%; White 699,367, 42.17%; other/unknown combined 274,885, 16.57%), R4 (audiology), R5 (ENT, descriptive), R9 (age-stratified audiology; MH RR 0.812, 95% CI 0.711–0.928), H-S1 (sex-stratified audiology; MH RR 0.873, 95% CI 0.765–0.997), H-S2 (crude prevalence RR 0.734, 95% CI 0.711–0.758; not age-adjusted). Pediatric Audiology window resolved 2026-11-26 (9/3/2015–9/30/2026 with race cleared; 3/2026 header with race selected was a display artifact). Still open: R7, R8; optional age-stratified unfiltered base counts.
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


## Literature sources — Paper 01 draft-v2 (2026-11-27)

Verified for `papers/01-hearing-loss-disparities/draft-v2.md`. Each peer-reviewed item was checked against PubMed E-utilities (`esummary`) and has a PMID; DOIs are listed as registered. Publisher HTML often returned 403/500 from this network; PubMed/PMC records were treated as sufficient verification. Claims not supported by a verified source were left unstated (no invented references). Nieman et al. is cited only for age- and hearing-adjusted hearing-aid ORs, not for a fully income-adjusted model. The PubMed abstract of Atherton et al. contains a corrupted insurance OR and was not quoted. Chan et al. acquisition times (rural 25.7 vs urban 19.1 years) are from the Results body, not the swapped numbers in the PubMed abstract.

| # | Citation | PMID | DOI |
|---|---|---:|---|
| 1 | Lin FR, Niparko JK, Ferrucci L. Arch Intern Med. 2011;171(20):1851-1852. | 22083573 | 10.1001/archinternmed.2011.506 |
| 2 | Agrawal Y, Platz EA, Niparko JK. Arch Intern Med. 2008;168(14):1522-1530. | 18663164 | 10.1001/archinte.168.14.1522 |
| 3 | Goman AM, Lin FR. Am J Public Health. 2016;106(10):1820-1822. | 27552261 | 10.2105/AJPH.2016.303299 |
| 4 | Rein DB, et al. Lancet Reg Health Am. 2024;30:100670. | 38405031 | 10.1016/j.lana.2023.100670 |
| 5 | Lin FR, Thorpe R, Gordon-Salant S, Ferrucci L. J Gerontol A Biol Sci Med Sci. 2011;66(5):582-590. | 21357188 | 10.1093/gerona/glr002 |
| 6 | Chien W, Lin FR. Arch Intern Med. 2012;172(3):292-293. | 22332170 | 10.1001/archinternmed.2011.1408 |
| 7 | Nieman CL, Marrone N, Szanton SL, Thorpe RJ Jr, Lin FR. J Aging Health. 2016;28(1):68-94. | 25953816 | 10.1177/0898264315585505 |
| 8 | Planey AM. Soc Sci Med. 2019;222:216-224. | 30660682 | 10.1016/j.socscimed.2019.01.015 |
| 9 | Chan S, Hixon B, Adkins M, Shinn JB, Bush ML. Laryngoscope. 2017;127(10):2362-2367. | 28144961 | 10.1002/lary.26490 |
| 10 | Atherton KM, Poupore NS, Clemmens CS, Nietert PJ, Pecha PP. Otolaryngol Head Neck Surg. 2023;168(6):1289-1300. | 36939626 | 10.1002/ohn.221 |
| 11 | Bush ML, Bianchi K, Lester C, Shinn JB, Gal TJ, Fardo DW, et al. J Pediatr. 2014;164(2):393-397. | 24183213 | 10.1016/j.jpeds.2013.09.047 |
| 12 | Bush ML, Kaufman MR, McNulty BN. Curr Opin Otolaryngol Head Neck Surg. 2017;25(5):359-364. | 28665808 | 10.1097/MOO.0000000000000388 |
| 13 | University of Mississippi Medical Center, Center for Informatics and Analytics (2020): Patient Cohort Explorer. figshare. Software. | — | 10.6084/m9.figshare.12252737 |
| 14–16 | CDC PLACES 2025; ACS 5-year 2020–2024 (B18102, B02001, B17001); County Health Rankings 2025 (already catalogued above). | — | — |

## Next Steps / Living Document Notes

- [x] Confirm RDW / Patient Cohort Explorer access.
- [x] Download latest CHR Mississippi data and PLACES county file (done 2026-11-26 for Paper 01: CHR 2025 analytic data, PLACES 2025 release; also ACS 2020–2024).
- [ ] Run sample MSTAHRS queries for diabetes / CVD / infant mortality by race and county.
- [ ] Check State Cancer Profiles for Oral Cavity & Pharynx rates in MS counties.
- [x] Run Paper 01 UMMC aggregates for R0, R1, R4, R5, R9, and H-S1 (`rdw-data-requests.md`). R3, R7, and R8 remain optional/open.
- [x] Decide primary outcome / niche for Paper 01: hearing loss (H90.3) at UMMC + county-level hearing disability context. Other niches: later papers.
- [ ] Draft specific aims once primary outcome chosen.

**File history**:  
- Created 2026-11-26 as initial catalog.  
- Updated 2026-11-26: Confirmed student RDW access; added proposed query sets and hybrid analysis option.
- 2026-11-26: Paper 01 pass: pulled CDC PLACES 2025 (HEARING), ACS 2020–2024 (B18102, B02001, B17001), CHR&R 2025 for 82 counties; linked `data-use-rules.md`; recorded Jake's data-use confirmation and the <11 suppression rule.
- Updated 2026-11-26: added Tier 1c (SCP detailed extracts, CHR March 2026 supplement, RUCC, DRA list, PLACES notes, pending sources) for Papers 02–05.
- 2026-11-26: Paper 01 R9 age-stratified audiology recorded (MH RR 0.812); see `papers/01-hearing-loss-disparities/data/r9_mh_results.md`.
- 2026-11-26: Pediatric Audiology window check: 0–17 + Audiology with race cleared spans 9/3/2015–9/30/2026 (Patients 401, Encounters 868).
- 2026-11-27: Paper 01 H-S1 sex-stratified audiology recorded (MH RR 0.873, 95% CI 0.765–0.997); see `papers/01-hearing-loss-disparities/data/hs1_sex_results.md`.
- 2026-11-27: Paper 05 merged into Paper 02 (Jake decision); no new sources. Sources for the merged paper (SCP, RUCC, AHRF, PLACES 2025 and 2023, CHR, DRA) are listed in `papers/02-oral-pharynx-cancer-disparities/README.md`. Abstract limit now ≤500 words incl. labels.
- 2026-11-27: Paper 01 draft-v2 literature sources logged (12 PubMed-verified PMIDs; see section above). Official RDW citation and boilerplate were already recorded earlier the same day.
