# Draft v1 — Hearing Loss Disparities

**Last updated**: 2026-11-26  
**Status**: Hypotheses written; county-level public-data tests done ([`county-analysis.md`](county-analysis.md)); UMMC cohort N and encounter total confirmed (H90.3 Patients = 15,612, 0.94% of RDW; Encounters = 4,244,868, 5.79%; window 1/1/2013–9/30/2026). R1 race percentages recorded (Black or African American 47.1%; White or Caucasian 49.9%; screenshot 2026-11-26); exact race and sex counts **[PENDING]** (next: click Black, then White). Data use confirmed by Jake Harthcock 2026-11-26 per Cohort Explorer guide ([`../../data-use-rules.md`](../../data-use-rules.md)).

> **Numbers rule**: no number appears here unless it was obtained from a cited source. Anything not yet obtained is marked **[PENDING]**. UMMC RDW subgroup cells under 11 are never recorded; they appear as "<11 (suppressed)" (project rule). Separately, the Cohort Explorer itself only allows report view/export when the population is greater than 25 (guide p. 20).

---

## Working Title
Racial and Geographic Disparities in Documented Hearing Loss and Related Care at an Academic Medical Center in Mississippi

---

## Abstract (draft skeleton)

**Background**: Hearing loss is common and associated with reduced quality of life, yet disparities in diagnosis and treatment persist by race and geography. Mississippi has elevated rates of disability and large rural populations, but local clinical data on hearing-loss care are limited.

**Methods**: Retrospective analysis of de-identified aggregate data from the UMMC Research Data Warehouse / Patient Cohort Explorer. Patients with ICD-10 H90.3 (bilateral sensorineural hearing loss) were identified. Race and utilization of audiology or otolaryngology services were tabulated and compared (chi-square, risk difference, odds ratio). County-level context for all 82 Mississippi counties used CDC PLACES hearing-disability estimates (2025 release, BRFSS 2023), ACS 2020–2024, and County Health Rankings 2025, analyzed with Spearman correlation and rural vs non-rural comparison.

**Results**: *County level*: age-adjusted adult hearing disability prevalence was higher in rural than non-rural counties (PLACES mean 7.54% vs 6.91%; Mann-Whitney p = 1.5e-4; n = 66 vs 16) and correlated with % rural (Spearman rho = 0.477), fewer primary care physicians (rho = −0.470), higher uninsured share (rho = 0.490) and lower county % Black (rho = −0.321); no association with county poverty (rho = 0.017). *UMMC cohort*: N = 15,612 patients (0.94% of RDW) and 4,244,868 encounters (5.79%) with ICD-10 H90.3 (Patient Cohort Explorer screenshot, 2026-11-26; data window 1/1/2013–9/30/2026). Race (dropdown % of cohort): Black or African American 47.1%, White or Caucasian 49.9% (exact counts **[PENDING]**). Utilization by race **[PENDING]**.

**Conclusions**: **[PENDING; write after RDW results]**.

---

## 1. Introduction / Background

Hearing loss affects a substantial portion of the U.S. population. Approximately 11–16% of American adults report some degree of hearing difficulty, with prevalence rising sharply with age. Bilateral hearing loss is estimated at roughly 11.6% nationally, corresponding to nearly 38 million people. Rural counties consistently show higher rates than urban ones.

Mississippi ranks among the higher-burden states for disability overall. American Community Survey data indicate that roughly 4.2–4.7% of the Mississippi population reports a hearing disability, and the state has high rates of any disability. (Checked against ACS 5-year 2020–2024, table B18102: 124,867 of 2,883,649 civilian noninstitutionalized residents, or 4.33%, summed across the 82 counties.) County-level model-based estimates (CDC PLACES and related small-area work) show that hearing disability prevalence increases with rurality.

Importantly, prevalence of measured or self-reported hearing loss is often **lower** among Black adults than White adults in national data. However, once hearing loss is present, Black adults and other minoritized groups show substantially lower rates of hearing-aid use and specialty care. These gaps persist after accounting for income in several studies, pointing to additional barriers related to access, trust, workforce representation, and structural factors. Pediatric data similarly show race-related delays in diagnosis and intervention after newborn screening.

Mississippi’s combination of high rurality, elevated overall disability burden, large Black population, and limited specialty workforce makes it an important setting in which to examine whether similar disparities appear in real-world documentation and care patterns at a major academic medical center.

**Gap**: Few published analyses describe the demographic profile or care utilization of patients with documented hearing loss within a Mississippi health system, or place those findings alongside county-level disability estimates.

*Note: the literature statements above were carried over from the seed draft and still need formal citations [PENDING].*

---

## 2. Specific Aims and Hypotheses

### 2.1 Aims
1. Characterize the demographic and geographic distribution of patients with documented bilateral sensorineural hearing loss (ICD-10 H90.3) in the UMMC Research Data Warehouse.
2. Quantify disparities in utilization of audiology and/or otolaryngology services among these patients, stratified by race and (if available) rural vs non-rural residence.
3. Situate UMMC findings within the Mississippi context using CDC PLACES county-level hearing-disability estimates and primary-care access metrics.

### 2.2 Hypotheses (pre-specified; α = 0.05, two-sided unless noted)

**A. County-level hypotheses (public data; tested, see [`county-analysis.md`](county-analysis.md))**

| ID | Null (H0) | Alternative (H1) | Data source (year) | Planned test | Result |
|---|---|---|---|---|---|
| H-C1 | Adult hearing disability prevalence does not differ between rural (≥50% rural) and non-rural Mississippi counties, and is uncorrelated with % rural | Higher in rural counties; positive correlation with % rural | PLACES age-adjusted % (BRFSS 2023, 2025 release); CHR&R % rural (2020 Census) | Mann-Whitney U and Welch t; Spearman rho | **Supported**: 7.54% vs 6.91%, p = 1.5e-4; rho = 0.477, p = 6.0e-6 |
| H-C2 | No association between county % Black and hearing disability prevalence | Association exists (literature predicts negative) | PLACES; ACS 2020–2024 B02001 | Spearman rho | **Supported, negative**: rho = −0.321, p = 0.0033 |
| H-C3 | No association between county poverty rate and hearing disability prevalence | Positive association | PLACES; ACS 2020–2024 B17001 | Spearman rho | **Not supported**: rho = 0.017, p = 0.88 |
| H-C4 | No association between PCP supply and hearing disability prevalence | Fewer PCPs per 100,000 associated with higher prevalence | PLACES; CHR&R PCP (AMA 2021) | Spearman rho | **Supported** (confounded by rurality): rho = −0.470, p = 8.5e-6 |
| H-C5 | No association between uninsured share and hearing disability prevalence | Higher uninsured share (<65) associated with higher prevalence | PLACES; CHR&R uninsured (SAHIE 2022) | Spearman rho | **Partially supported** (PLACES only): rho = 0.490, p = 3.0e-6; ACS direct rho = 0.178, p = 0.109 |

The five primary Spearman tests use PLACES age-adjusted prevalence and are Holm-corrected as one family (Holm p = 2.4e-5, 0.0066, 0.88, 2.5e-5, 1.5e-5 for H-C1 to H-C5). Exploratory: multivariable OLS with HC3 robust SE. Caveat: PLACES is model-based and uses ACS inputs, so associations with race, poverty, and insurance are partly built in.

**B. UMMC cohort hypotheses (need RDW aggregates; all results [PENDING])**

| ID | Null (H0) | Alternative (H1) | Data needed | Planned test | Result |
|---|---|---|---|---|---|
| H-U1 | The share of Black patients in the H90.3 cohort equals their share of the overall RDW patient population | Differs (predicted lower, matching lower measured prevalence in Black adults; age structure must be considered) | H90.3 patients by race; all RDW patients by race | Chi-square goodness-of-fit / two-proportion z-test; age-band stratified descriptives | **[PENDING]** |
| H-U2 | Among H90.3 patients, proportion with ≥1 audiology encounter is equal for Black and White patients | Lower in Black patients | H90.3 × race × audiology (ever) | Chi-square; risk difference with 95% CI; odds ratio | **[PENDING]** |
| H-U3 | Proportion with ≥1 ENT encounter is equal for Black and White patients | Lower in Black patients | H90.3 × race × ENT (ever) | Same as H-U2 | **[PENDING]** |
| H-U4 (primary) | Proportion with ≥1 audiology **or** ENT encounter is equal for Black and White patients | Lower in Black patients | H90.3 × race × (audiology or ENT) | Same as H-U2 | **[PENDING]** |
| H-U5 | Proportion with ≥1 audiology or ENT encounter is equal for rural and non-rural residents | Lower in rural residents | Residence variable (ZIP/county) **if** the Explorer has one; otherwise not testable | Chi-square; risk difference | **[PENDING; residence variable availability unknown]** |
| H-U6 (exploratory) | No race × rurality interaction on specialty-visit use | Interaction present | Race × rurality × utilization | Descriptive stratified proportions; Breslow-Day/logistic only if counts allow | **[PENDING]** |

Known threat to H-U2 to H-U6: H90.3 is often assigned **at** an audiology or ENT visit, so "ever seen audiology/ENT" may be high for everyone by construction and mask real differences. Mitigations are in `rdw-data-requests.md` (diagnosis-origin and age-stratified requests). Suppression rule for all UMMC cells: counts under 11 shown as "<11 (suppressed)", with complementary suppression where a hidden cell could be recovered by subtraction.

---

## 3. Methods

### Data Sources
- **Primary**: UMMC Patient Cohort Explorer / Research Data Warehouse (de-identified, date-shifted Epic data). Jake runs all queries and reports aggregates; AI tools have no direct access to the Explorer. Exact RDW patient and encounter denominators are **[PENDING]** (request R3) and will not be back-calculated from on-screen percentages.
- **County context (public)**: CDC PLACES County Data, 2025 release (BRFSS 2023); ACS 5-year 2020–2024 (B18102, B02001, B17001); County Health Rankings & Roadmaps 2025 analytic data (PCP 2021, uninsured 2022, % rural 2020). URLs and variable definitions in [`county-analysis.md`](county-analysis.md).

### Cohort Definition
Patients with at least one encounter carrying ICD-10 diagnosis **H90.3** (sensorineural hearing loss, bilateral): **15,612** patients (0.94% of RDW) and **4,244,868** encounters (5.79%), confirmed from a 2026-11-26 Patient Cohort Explorer screenshot with only H90.3 selected in **Pt Diagnosis Codes (OR)** (Current Selections: `Pt_Dx_Code ORMode H90.3`; Step 1 in [`README.md`](README.md)). The 0.94% figure implies an RDW patient denominator; that exact total is **[PENDING]** until reported in request R3 and is not back-calculated here. The Explorer permits one selection per filter box, so a single code was chosen over the broader H90 range; this is a limitation (unilateral, mixed, and conductive loss are excluded). Other single-code counts seen earlier: H90.5 ≈ 6,856; H90.0 ≈ 4,029.

### Data window
The Explorer header states that the dataset includes encounters between **January 1, 2013** and **September 30, 2026** (same 2026-11-26 screenshot).

### Variables
- Demographics: age, sex, race/ethnicity. Race is on the Data Filters page → Patient Demographics tab → Demographic Search list → Race (dropdown shows % of the current cohort). Sex percentages below are from the pie chart on that same screen.
- Geography: ZIP or county of residence (if available in the de-identified data) → rural vs non-rural classification; the Explorer lists a State filter, others **[PENDING]**
- Care processes: ≥1 audiology encounter; ≥1 otolaryngology (ENT) encounter; either
- Optional: payer (Primary Financial Class), encounter setting, age band

### Analysis
Descriptive statistics overall and by race (and by rurality if available). Proportions with specialty follow-up compared across groups (chi-square, risk difference, odds ratio with 95% CI). County-level: Spearman correlation, Mann-Whitney/Welch rural vs non-rural comparison, Holm correction across the five primary tests, exploratory OLS with robust SE. Only aggregate counts are used. UMMC cells under 11 are not recorded (suppressed); public county data are unaffected.

### Approvals
Data use confirmed by Jake Harthcock 2026-11-26 per Cohort Explorer guide (`data-use-rules.md`). The guide does not mention IRB review; whether the target conference requires an IRB determination is **[Jake to confirm]**.

---

## 4. Results

### 4.1 County-level results (82 Mississippi counties; public data)
Full tables, years, and caveats: [`county-analysis.md`](county-analysis.md).

| Hypothesis | Primary statistic (PLACES age-adjusted, 2025 release, BRFSS 2023) | Verdict |
|---|---|---|
| H-C1 rural | rural 7.54% (SD 0.42, n = 66) vs non-rural 6.91% (SD 0.64, n = 16); Mann-Whitney p = 1.5e-4; rho (% rural) = 0.477 | Supported |
| H-C2 % Black | rho = −0.321, p = 0.0033 | Supported (negative) |
| H-C3 poverty | rho = 0.017, p = 0.88 | Not supported |
| H-C4 PCP supply | rho = −0.470, p = 8.5e-6 | Supported |
| H-C5 uninsured | rho = 0.490, p = 3.0e-6 (ACS direct: rho = 0.178, p = 0.109) | Partially supported |

### 4.2 Table 1. Characteristics of patients with documented hearing loss (UMMC RDW, ICD-10 H90.3)

| Characteristic              | N (%) or mean (SD) |
|-----------------------------|--------------------|
| Total patients              | 15,612 (0.94% of RDW; Patient Cohort Explorer, Pt Diagnosis Codes (OR) = H90.3 only; Current Selections: `Pt_Dx_Code ORMode H90.3`; screenshot 2026-11-26) |
| Encounters                  | 4,244,868 (5.79% of RDW encounters; same screenshot) |
| Data window                 | Encounters between 1/1/2013 and 9/30/2026 (same screenshot) |
| Age                         | [PENDING] |
| Sex                         | Pie chart on Patient Demographics (same screenshot). Exact counts **[PENDING]**; not back-calculated. |
| &nbsp;&nbsp;Female          | 54.84% (exact count **[PENDING]**) |
| &nbsp;&nbsp;Male            | 45.16% (exact count **[PENDING]**) |
| Race/ethnicity              | % of H90.3 cohort from the Race dropdown (Data Filters → Patient Demographics → Demographic Search). Exact counts **[PENDING]**; not back-calculated. |
| &nbsp;&nbsp;Black or African American | 47.1% (exact count **[PENDING]**) |
| &nbsp;&nbsp;White or Caucasian | 49.9% (exact count **[PENDING]**) |
| &nbsp;&nbsp;Other/multiple/unknown | Other 1.1%; Asian 0.5%; Multiracial 0.4%; American Indian or Alaska Native 0.2%; Hispanic 0.2%; MS Band Choctaw Indian 0.2%; Unknown 0.2%; Patient Refused 0.1% (exact counts **[PENDING]**). Blank/unlabeled row, Asian Indian, and Native Hawaiian or Other Pacific Islander each displayed as 0.0% and are shown as <11 (suppressed). Component percentages are listed as displayed and are not summed. |
| Rural residence (if available) | [PENDING] |

### 4.3 Table 2. Specialty care utilization among patients with hearing-loss diagnosis

| Metric                          | Overall | Black | White | Rural | Non-rural |
|---------------------------------|---------|-------|-------|-------|-----------|
| ≥1 Audiology encounter          | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] |
| ≥1 ENT encounter                | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] |
| ≥1 Audiology or ENT encounter   | [PENDING] | [PENDING] | [PENDING] | [PENDING] | [PENDING] |

### 4.4 Additional planned analyses
- Racial distribution of the H90.3 cohort vs overall RDW population (H-U1) **[PENDING]**.
- Optional: UMMC patterns beside PLACES estimates for the UMMC catchment region (needs a residence variable) **[PENDING]**.

---

## 5. Discussion (early framing)

**Expected contribution**  
This study will provide a system-level description of documented hearing loss and related specialty care at Mississippi’s academic medical center, with explicit attention to race and geography, alongside county-level context.

**What the county data already say**  
Rural Mississippi counties have higher modeled adult hearing disability prevalence, and counties with fewer PCPs and more uninsured residents do too, while counties with larger Black populations have lower measured prevalence. That pattern matches the introduction's premise: lower measured prevalence among Black residents does not imply lower need or better care, which is what the UMMC cohort tests.

**Strengths**  
Large real-world cohort; ability to examine both diagnosis and downstream care; linkage to statewide county estimates for all 82 counties.

**Limitations**  
Single-center; reliance on one diagnosis code (H90.3 only); diagnosis codes may be assigned at audiology/ENT visits, inflating utilization; possible under-ascertainment; de-identified data limit social determinants; date-shifting; specialty encounter capture depends on department coding in the RDW; county analysis is ecological and uses model-based PLACES estimates, with mixed data years and equal-weighted counties.

**Implications**  
Findings can inform targeted screening, referral-pathway improvement, and outreach efforts, particularly if disparities in specialty follow-up are confirmed.

---

## 6. References (seed list — expand)

- CDC PLACES, County Data, 2025 release (BRFSS 2023): https://data.cdc.gov/500-Cities-Places/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb
- U.S. Census Bureau, ACS 5-year 2020–2024 Table-Based Summary File, tables B18102, B02001, B17001: https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/
- County Health Rankings & Roadmaps, 2025 analytic data: https://www.countyhealthrankings.org/sites/default/files/media/document/analytic_data2025_v3.csv
- National hearing-loss prevalence studies (e.g., bilateral HL ~11.6%, higher in rural areas) **[full citation PENDING]**
- Racial disparities in hearing-aid use and pediatric hearing healthcare access literature **[full citations PENDING]**

---

## Version history
- 2026-11-26: Initial outline.
- 2026-11-26: Expanded with literature-backed background, refined aims/methods, and structured results placeholders.
- 2026-11-26: Added pre-specified hypotheses (county-level and UMMC), switched cohort to H90.3, <11 suppression rule, county-level results (82 counties), RDW placeholders marked [PENDING].
- 2026-11-26: Step 1 confirmed: H90.3 Patients = 15,612. Encounters still [PENDING]. Table 1 total and cohort definition updated.
- 2026-11-26: Screenshot added Encounters = 4,244,868 (5.79%), patients as 0.94% of RDW, and data window 1/1/2013–9/30/2026. RDW denominators left [PENDING] (not back-calculated).
- 2026-11-26: R1 race percentages from Data Filters → Patient Demographics → Race dropdown (Black or African American 47.1%; White or Caucasian 49.9%); sex pie chart Female 54.84%, Male 45.16%. Exact counts left [PENDING] (not back-calculated). 0.0% rows treated as <11 (suppressed).
