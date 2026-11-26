# Draft v1 — Hearing Loss Disparities

**Last updated**: 2026-11-26  
**Status**: Expanded outline with literature-backed background and methods. Awaiting RDW aggregate results.

---

## Working Title
Racial and Geographic Disparities in Documented Hearing Loss and Related Care at an Academic Medical Center in Mississippi

---

## Abstract (draft skeleton)

**Background**: Hearing loss is common and associated with reduced quality of life, yet disparities in diagnosis and treatment persist by race and geography. Mississippi has elevated rates of disability and large rural populations, but local clinical data on hearing-loss care are limited.

**Methods**: Retrospective analysis of de-identified data from the UMMC Research Data Warehouse / Patient Cohort Explorer. Patients with ICD-10 codes for hearing loss (primarily H90 range) were identified. Demographics, residence, and utilization of audiology or otolaryngology services were described and stratified by race and rurality. County-level context was drawn from CDC PLACES hearing-disability estimates and County Health Rankings.

**Results**: [Insert key N, demographic distribution, and stratified utilization rates once RDW queries are complete.]

**Conclusions**: [1–2 sentences on implications for equity in hearing healthcare in Mississippi.]

---

## 1. Introduction / Background

Hearing loss affects a substantial portion of the U.S. population. Approximately 11–16% of American adults report some degree of hearing difficulty, with prevalence rising sharply with age. Bilateral hearing loss is estimated at roughly 11.6% nationally, corresponding to nearly 38 million people. Rural counties consistently show higher rates than urban ones.

Mississippi ranks among the higher-burden states for disability overall. American Community Survey data indicate that roughly 4.2–4.7% of the Mississippi population reports a hearing disability, and the state has high rates of any disability. County-level model-based estimates (CDC PLACES and related small-area work) show that hearing disability prevalence increases with rurality.

Importantly, prevalence of measured or self-reported hearing loss is often **lower** among Black adults than White adults in national data. However, once hearing loss is present, Black adults and other minoritized groups show substantially lower rates of hearing-aid use and specialty care. These gaps persist after accounting for income in several studies, pointing to additional barriers related to access, trust, workforce representation, and structural factors. Pediatric data similarly show race-related delays in diagnosis and intervention after newborn screening.

Mississippi’s combination of high rurality, elevated overall disability burden, large Black population, and limited specialty workforce makes it an important setting in which to examine whether similar disparities appear in real-world documentation and care patterns at a major academic medical center.

**Gap**: Few published analyses describe the demographic profile or care utilization of patients with documented hearing loss within a Mississippi health system, or place those findings alongside county-level disability estimates.

---

## 2. Specific Aims

1. Characterize the demographic and geographic distribution of patients with documented hearing-loss diagnoses in the UMMC Research Data Warehouse.
2. Quantify disparities in utilization of audiology and/or otolaryngology services among these patients, stratified by race and (if available) rural vs non-rural residence.
3. Situate UMMC findings within the broader Mississippi context using CDC PLACES county-level hearing-disability estimates and primary-care access metrics.

---

## 3. Methods

### Data Sources
- **Primary**: UMMC Patient Cohort Explorer / Research Data Warehouse (de-identified, date-shifted Epic data; ~750k patients, ~24M encounters).
- **Contextual**: CDC PLACES county-level estimates of hearing disability; County Health Rankings & Roadmaps (primary-care supply, uninsured, rurality).

### Cohort Definition
Patients with at least one encounter carrying an ICD-10 diagnosis code in the **H90** range (Conductive and sensorineural hearing loss), with optional expansion to selected **H91** codes (other hearing loss).  
Core H90 codes include bilateral/unilateral/mixed conductive and sensorineural categories (H90.0–H90.8 and H90.A series).

### Variables
- Demographics: age, sex, race/ethnicity
- Geography: ZIP or county of residence (if available in de-identified data) → rural vs non-rural classification
- Care processes: presence of any audiology specialty encounter; presence of any otolaryngology (ENT) specialty encounter
- Optional: encounter setting (outpatient/ED/inpatient), selected comorbidities

### Analysis
Descriptive statistics overall and stratified by race and rurality. Proportions of patients with specialty follow-up compared across groups (chi-square or equivalent). Simple measures of association (e.g., risk difference or odds ratio for specialty visit by race) if sample size permits. No patient-level identifiable data will be used or reported; cells <10 will be suppressed or noted.

---

## 4. Results (placeholders — populate with RDW output)

### Table 1. Characteristics of patients with documented hearing loss (UMMC RDW)

| Characteristic              | N (%) or mean (SD) |
|-----------------------------|--------------------|
| Total patients              |                    |
| Age                         |                    |
| Female                      |                    |
| Race/ethnicity              |                    |
| &nbsp;&nbsp;Black           |                    |
| &nbsp;&nbsp;White           |                    |
| &nbsp;&nbsp;Other/Unknown   |                    |
| Rural residence (if available) |                 |

### Table 2. Specialty care utilization among patients with hearing-loss diagnosis

| Metric                          | Overall | Black | White | Rural | Non-rural |
|---------------------------------|---------|-------|-------|-------|-----------|
| ≥1 Audiology encounter          |         |       |       |       |           |
| ≥1 ENT encounter                |         |       |       |       |           |
| ≥1 Audiology or ENT encounter   |         |       |       |       |           |

### Additional planned analyses
- Comparison of racial distribution in the hearing-loss cohort vs overall RDW population.
- Optional: side-by-side view of UMMC documentation patterns against PLACES county hearing-disability estimates for the UMMC catchment region.

---

## 5. Discussion (early framing)

**Expected contribution**  
This study will provide the first system-level description of documented hearing loss and related specialty care at Mississippi’s academic medical center, with explicit attention to race and geography.

**Strengths**  
Large real-world cohort; ability to examine both diagnosis and downstream care; linkage to statewide county estimates.

**Limitations**  
Single-center; reliance on diagnosis codes (possible under-ascertainment); de-identified data limit granularity of social determinants; date-shifting; specialty encounter capture depends on how departments are coded in the RDW.

**Implications**  
Findings can inform targeted screening, referral-pathway improvement, and outreach efforts, particularly if disparities in specialty follow-up are confirmed.

---

## 6. References (seed list — expand)

- CDC PLACES / BRFSS small-area disability estimates
- National hearing-loss prevalence studies (e.g., bilateral HL ~11.6%, higher in rural areas)
- Racial disparities in hearing-aid use and pediatric hearing healthcare access literature
- Mississippi ACS disability tables
- County Health Rankings Mississippi data

---

## Version history
- 2026-11-26: Initial outline.
- 2026-11-26: Expanded with literature-backed background, refined aims/methods, and structured results placeholders. Ready for RDW numbers.
