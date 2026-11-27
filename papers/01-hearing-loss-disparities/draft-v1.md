# Draft v1 — Hearing Loss Disparities

**Last updated**: 2026-11-26  
**Status**: Hypotheses written; county-level public-data tests done ([`county-analysis.md`](county-analysis.md)); UMMC cohort N confirmed (H90.3 Patients = 15,612, 0.94% of RDW; Encounters = 4,244,868, 5.79%; window 1/1/2013–9/30/2026). R1 exact counts recorded (FirstRace): White 8,597 (55.1%), Black 6,176 (39.6%), other/unknown 839 (5.4%). R4 done (Department Specialty = Audiology): 1,730/15,612 (11.08%) had ≥1 Audiology-department encounter; Black 630/6,176 (10.20%) vs White 996/8,597 (11.59%); RD −1.38 pp (95% CI −2.40 to −0.37); RR 0.880 (0.801–0.968); Pearson χ²(1) = 7.03, p = 0.008. H-U2 supported (modest difference; caveats: data from mid-2014, UMMC only, possible circularity). H-U1 partial (R3 still [PENDING]). Next: R5 ENT. Data use confirmed by Jake Harthcock 2026-11-26 per Cohort Explorer guide ([`../../data-use-rules.md`](../../data-use-rules.md)).

> **Numbers rule**: no number appears here unless it was obtained from a cited source. Anything not yet obtained is marked **[PENDING]**. UMMC RDW subgroup cells under 11 are never recorded; they appear as "<11 (suppressed)" (project rule). Separately, the Cohort Explorer itself only allows report view/export when the population is greater than 25 (guide p. 20).

---

## Working Title
Racial and Geographic Disparities in Documented Hearing Loss and Related Care at an Academic Medical Center in Mississippi

---

## Abstract (draft skeleton)

**Background**: Hearing loss is common and associated with reduced quality of life, yet disparities in diagnosis and treatment persist by race and geography. Mississippi has elevated rates of disability and large rural populations, but local clinical data on hearing-loss care are limited.

**Methods**: Retrospective analysis of de-identified aggregate data from the UMMC Research Data Warehouse / Patient Cohort Explorer. Patients with ICD-10 H90.3 (bilateral sensorineural hearing loss) were identified. Race and utilization of audiology or otolaryngology services were tabulated and compared (chi-square, risk difference, odds ratio). County-level context for all 82 Mississippi counties used CDC PLACES hearing-disability estimates (2025 release, BRFSS 2023), ACS 2020–2024, and County Health Rankings 2025, analyzed with Spearman correlation and rural vs non-rural comparison.

**Results**: *County level*: age-adjusted adult hearing disability prevalence was higher in rural than non-rural counties (PLACES mean 7.54% vs 6.91%; Mann-Whitney p = 1.5e-4; n = 66 vs 16) and correlated with % rural (Spearman rho = 0.477), fewer primary care physicians (rho = −0.470), higher uninsured share (rho = 0.490) and lower county % Black (rho = −0.321); no association with county poverty (rho = 0.017). *UMMC cohort*: N = 15,612 patients (0.94% of RDW) and 4,244,868 encounters (5.79%) with ICD-10 H90.3 (Patient Cohort Explorer screenshot, 2026-11-26; data window 1/1/2013–9/30/2026). Race (FirstRace; patient counts): White or Caucasian 8,597 (55.1% of 15,612), Black or African American 6,176 (39.6%), other/unknown combined 839 (5.4%; 15,612 − 8,597 − 6,176). Black patients had more encounters per person than White patients (323.9 vs 246.5; 2,000,250 / 6,176 vs 2,119,544 / 8,597). Sex among White patients: 50.81% female; among Black patients: 61.33% female (pie chart with FirstRace selected; exact counts **[PENDING]**). Among these patients, 1,730/15,612 (11.08%) had ≥1 Audiology-department encounter (Data Filters → Admissions & Visits → Department Specialty = Audiology; encounter-level; selected encounter window 6/26/2014–9/30/2026). This was less common among Black than White patients (630/6,176, 10.20% vs 996/8,597, 11.59%; risk difference −1.38 percentage points, 95% CI −2.40 to −0.37; risk ratio 0.880, 95% CI 0.801–0.968; Pearson χ²(1) = 7.03, p = 0.008). ENT utilization **[PENDING, R5]**. Comparison of the cohort race mix to the RDW base population **[PENDING, R3]**.

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

**B. UMMC cohort hypotheses (H-U1 partial; H-U2 tested; H-U3 to H-U6 and the H-U1 test still [PENDING])**

| ID | Null (H0) | Alternative (H1) | Data needed | Planned test | Result |
|---|---|---|---|---|---|
| H-U1 | The share of Black patients in the H90.3 cohort equals their share of the overall RDW patient population | Differs (predicted lower, matching lower measured prevalence in Black adults; age structure must be considered) | H90.3 patients by race; all RDW patients by race | Chi-square goodness-of-fit / two-proportion z-test; age-band stratified descriptives | **Partial**: cohort race split recorded (FirstRace; screenshots 2026-11-26): White 8,597 (55.1% of 15,612), Black 6,176 (39.6%), other/unknown combined 839 (5.4%; 15,612 − 8,597 − 6,176). Comparison to the RDW base-population race distribution remains **[PENDING]** (request R3). |
| H-U2 | Among H90.3 patients, proportion with ≥1 audiology encounter is equal for Black and White patients | Lower in Black patients | H90.3 × race × Department Specialty = Audiology (ever; encounter-level Data Filters) | Pearson χ² (2×2, uncorrected); Wald 95% CI for risk difference (Black − White); Katz log-Wald 95% CI for risk ratio; Woolf 95% CI for odds ratio | **Supported** (modest): 630/6,176 (10.20%) vs 996/8,597 (11.59%); RD −1.38 percentage points (95% CI −2.40 to −0.37); RR 0.880 (95% CI 0.801–0.968); Pearson χ²(1) = 7.03, p = 0.008; OR 0.867 (95% CI 0.780–0.963). Caveats: Audiology department data from mid-2014 (window 6/26/2014–9/30/2026; 7/5/2014 start for White) while the cohort starts 1/1/2013; UMMC visits only; possible H90.3/audiology circularity (R8). |
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
- Demographics: age, sex, race/ethnicity. Race is the **FirstRace** field (Current Selections label), on the Data Filters page → Patient Demographics tab → Demographic Search list → Race. Patient race shares are computed from header Patients counts with H90.3 + one FirstRace value selected. The Race dropdown percentages are encounter shares of the current selection, not patient shares, and are not used as the Table 1 race distribution. Overall-cohort sex percentages are from the pie chart on that same screen with no race selected (likely patient-based; pie chart basis unconfirmed). Sex by race is from the same pie chart with one FirstRace value selected.
- Geography: ZIP or county of residence (if available in the de-identified data) → rural vs non-rural classification; the Explorer lists a State filter, others **[PENDING]**
- Care processes: ≥1 audiology encounter and ≥1 otolaryngology (ENT) encounter, defined from **Department Specialty** (Data Filters → Admissions & Visits → Encounter Search; Current Selections label **DepartmentSpecialty**). Data Filters selections are encounter-level: the header Patients count is H90.3 patients with ≥1 encounter in the selected department specialty. Audiology uses the value **Audiology** (confirmed 2026-11-26). The exact Otolaryngology / ENT label is **[PENDING, R5]**.
- Optional: payer (Primary Financial Class), encounter setting, age band

### Analysis
Descriptive statistics overall and by race (and by rurality if available). Proportions with specialty follow-up compared across groups. For H-U2 (Black vs White, ≥1 Audiology-department encounter yes/no): Pearson chi-square on the 2×2 table (uncorrected); Wald 95% CI for the risk difference (Black minus White); Katz log-Wald 95% CI for the risk ratio; Woolf log-Wald 95% CI for the odds ratio. County-level: Spearman correlation, Mann-Whitney/Welch rural vs non-rural comparison, Holm correction across the five primary tests, exploratory OLS with robust SE. Only aggregate counts are used. UMMC cells under 11 are not recorded (suppressed); public county data are unaffected. On-screen “% of RDW” figures are recorded as displayed and are not back-calculated into an RDW denominator (request R3).

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
| Encounters per patient (descriptive) | Overall 271.9 (4,244,868 / 15,612). By FirstRace: White 246.5 (2,119,544 / 8,597); Black 323.9 (2,000,250 / 6,176). |
| Data window                 | Encounters between 1/1/2013 and 9/30/2026 (same screenshot) |
| Age                         | [PENDING] |
| Sex (overall; no race selected) | Pie chart on Patient Demographics (H90.3 only). Likely patient-based; pie chart basis unconfirmed. Exact counts **[PENDING]**; not back-calculated. |
| &nbsp;&nbsp;Female          | 54.84% (exact count **[PENDING]**) |
| &nbsp;&nbsp;Male            | 45.16% (exact count **[PENDING]**) |
| Race/ethnicity (FirstRace)  | Patient counts from the header with H90.3 + one FirstRace value selected (Data Filters → Patient Demographics → Race; Current Selections: FirstRace; screenshots 2026-11-26). Percentages are patient-based (count / 15,612), rounded to one decimal (and therefore sum to 100.1%). The Race dropdown percentages (Black 47.1%, White 49.9%) are encounter shares of the 4,244,868 cohort encounters, not patient shares, and are not used here as the race distribution. Small-group dropdown percentages are encounter shares only and are not converted to patient counts. The 0.52% and 0.37% of RDW figures are recorded as displayed; the exact RDW denominator stays **[PENDING]** (R3) and is not back-calculated. |
| &nbsp;&nbsp;White or Caucasian | 8,597 (55.1% of 15,612; 0.52% of RDW). Encounters 2,119,544 (2.89% of RDW; 49.9% of 4,244,868 cohort encounters = 2,119,544 / 4,244,868). Encounters per patient 246.5 (2,119,544 / 8,597). Sex: Female 50.81%, Male 49.19% (pie chart with this FirstRace selected; exact counts **[PENDING]**). |
| &nbsp;&nbsp;Black or African American | 6,176 (39.6% of 15,612; 0.37% of RDW). Encounters 2,000,250 (2.73% of RDW; 47.1% of 4,244,868 = 2,000,250 / 4,244,868). Encounters per patient 323.9 (2,000,250 / 6,176). Sex: Female 61.33%, Male 38.67% (pie chart with this FirstRace selected; exact counts **[PENDING]**). |
| &nbsp;&nbsp;Other/unknown (combined) | 839 (5.4% of 15,612), computed as 15,612 − 8,597 − 6,176. Reported as one combined row only; not further broken into patient counts. |
| Rural residence (if available) | [PENDING] |

### 4.3 Table 2. Specialty care utilization among patients with hearing-loss diagnosis

Definition: H90.3 patients with ≥1 encounter in the named Department Specialty (Data Filters → Admissions & Visits → Encounter Search; Current Selections label **DepartmentSpecialty**; encounter-level). Audiology value = **Audiology** (screenshots, 2026-11-26). Denominators are the R1 patient counts (overall 15,612; Black 6,176; White 8,597). Rural / non-rural columns remain **[PENDING]** (R7).

| Metric | Overall | Black | White | Rural | Non-rural |
|---|---|---|---|---|---|
| ≥1 Audiology-department encounter | 1,730 / 15,612 (11.08%); Encounters 3,808 (0.01% of RDW); window 6/26/2014–9/30/2026 | 630 / 6,176 (10.20%); Encounters 1,297; Sex F 62.38%, M 37.62%; window 6/26/2014–9/30/2026 | 996 / 8,597 (11.59%); Encounters 2,295; Sex F 53.41%, M 46.59%; window 7/5/2014–9/30/2026 | [PENDING] | [PENDING] |
| ≥1 ENT-department encounter | [PENDING, R5] | [PENDING] | [PENDING] | [PENDING] | [PENDING] |
| ≥1 Audiology or ENT encounter | [PENDING, R6] | [PENDING] | [PENDING] | [PENDING] | [PENDING] |

Other / unknown race combined (direct subtraction): 104 / 839 (12.40%) had ≥1 Audiology-department encounter (1,730 − 630 − 996). Not further broken out. Header “% of RDW” figures (overall 0.10% of patients, 0.01% of encounters; Black 0.04%; White 0.06%) are recorded as displayed; the exact RDW denominator stays **[PENDING]** (R3) and is not back-calculated.

**H-U2 (Black vs White).** 2×2 counts: Black 630 with and 5,546 without an Audiology-department encounter; White 996 with and 7,601 without. Risk difference (Black − White) = −1.38 percentage points (Wald 95% CI −2.40 to −0.37). Risk ratio = 0.880 (Katz log-Wald 95% CI 0.801–0.968). Pearson χ²(1) = 7.03, p = 0.008. Odds ratio = 0.867 (Woolf 95% CI 0.780–0.963). Black patients were less likely than White patients to have ≥1 Audiology-department encounter; the absolute difference is modest (1.38 percentage points).

**Limitations specific to this comparison.** Audiology Department Specialty data appear only from mid-2014 (encounter window 6/26/2014–9/30/2026 when Audiology is selected; 7/5/2014–9/30/2026 for White patients), while the H90.3 cohort window starts 1/1/2013, so patients whose UMMC contacts fall only in the earlier period cannot show an Audiology-department encounter in the warehouse. “Ever audiology” is a UMMC visit only; care outside UMMC is not captured. H90.3 may be coded at audiology visits, so having the diagnosis and having an Audiology-department encounter can be circular (request R8).

### 4.4 Additional planned analyses
- Racial distribution of the H90.3 cohort vs overall RDW population (H-U1): cohort split recorded (White 8,597, 55.1%; Black 6,176, 39.6%; other/unknown 839, 5.4%); comparison to the RDW base population remains **[PENDING]** (R3).
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
Single-center; reliance on one diagnosis code (H90.3 only); diagnosis codes may be assigned at audiology/ENT visits, inflating utilization (circularity; request R8); possible under-ascertainment; “ever” specialty visits are UMMC only (outside care is not captured); de-identified data limit social determinants; date-shifting; specialty encounter capture depends on Department Specialty coding in the RDW, and Audiology department data appear only from mid-2014 (selected window starting 6/26/2014) while the H90.3 cohort window starts 1/1/2013; Data Filters Department Specialty selections are encounter-level; county analysis is ecological and uses model-based PLACES estimates, with mixed data years and equal-weighted counties.

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
- 2026-11-26: R1 exact counts (FirstRace; screenshots). White 8,597 (55.1% of 15,612), Black 6,176 (39.6%), other/unknown combined 839 (5.4%; 15,612 − 8,597 − 6,176). Dropdown 47.1% / 49.9% are encounter shares (2,000,250 / 4,244,868 and 2,119,544 / 4,244,868), not patient shares; small-group dropdown % not converted to patient counts; prior 0.0% → <11 reading from the dropdown withdrawn. Sex by race and encounters per patient (White 246.5; Black 323.9) added to Table 1. H-U1 marked partial (R3 still pending).
- 2026-11-26: R4 Audiology (Department Specialty; screenshots). 1,730/15,612 (11.08%) with ≥1 Audiology-department encounter; Black 630/6,176 (10.20%) vs White 996/8,597 (11.59%); other/unknown 104/839 (12.40%; 1,730 − 630 − 996). RD −1.38 pp (Wald 95% CI −2.40 to −0.37); RR 0.880 (Katz 95% CI 0.801–0.968); Pearson χ²(1) = 7.03, p = 0.008; OR 0.867 (Woolf 95% CI 0.780–0.963). H-U2 marked supported (modest; caveats: mid-2014 start, UMMC only, possible circularity). Table 2 audiology row filled. Next is R5 ENT.
