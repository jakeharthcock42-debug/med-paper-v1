# Draft v1 — Hearing Loss Disparities

**Last updated**: 2026-11-26  
**Status**: Hypotheses tightened 2026-11-26 (one primary: H-U2, including persistence after age stratification). County-level public-data associations are reported as ecological context ([`county-analysis.md`](county-analysis.md)). R0–R1 and R4–R5 done (H90.3 N = 15,612; White 8,597, Black 6,176, other/unknown 839). Primary H-U2 crude: 1,730/15,612 (11.08%); Black 630/6,176 (10.20%) vs White 996/8,597 (11.59%); RD −1.38 pp (95% CI −2.40 to −0.37); RR 0.880 (0.801–0.968), p = 0.008; age-adjusted (Mantel-Haenszel) RR **[PENDING]** (R9). Otolaryngology contact 15,103/15,612 (96.74%) is a descriptive finding (retired hypotheses H-U3, H-U4): H90.3 is diagnosed almost entirely in that setting. Conference abstract v1 (300 words) below. H-S2 (formerly H-U1) partial (R3 still [PENDING]). Data use confirmed by Jake Harthcock 2026-11-26 per Cohort Explorer guide ([`../../data-use-rules.md`](../../data-use-rules.md)).

> **Numbers rule**: no number appears here unless it was obtained from a cited source. Anything not yet obtained is marked **[PENDING]**. UMMC RDW subgroup cells under 11 are never recorded; they appear as "<11 (suppressed)" (project rule). Separately, the Cohort Explorer itself only allows report view/export when the population is greater than 25 (guide p. 20).

---

## Working Title
Racial and Geographic Disparities in Documented Hearing Loss and Related Care at an Academic Medical Center in Mississippi

---

## Abstract (conference draft, v1; 300 words, body only)

**Background**: Hearing loss is common, yet disparities in diagnosis and specialty care persist by race and geography. Mississippi has a large rural population and a high disability burden, but local clinical data on hearing-loss care are limited.

**Methods**: We analyzed de-identified UMMC Research Data Warehouse / Patient Cohort Explorer counts for patients with ICD-10 H90.3 (bilateral sensorineural hearing loss). The primary hypothesis was a lower rate of ≥1 Audiology-department encounter among Black than White patients, including after age stratification (Mantel-Haenszel risk ratio; age-adjusted [PENDING]). Otolaryngology contact was treated as the diagnostic setting, not an access outcome. County data (CDC PLACES 2025, ACS 2020–2024, County Health Rankings 2025) provided ecological context, not confirmatory tests.

**Results**: Age-adjusted hearing disability was higher in rural than non-rural counties (7.54% vs 6.91%; p = 1.5e-4; rho = 0.477), higher with fewer primary care physicians (rho = −0.470) or a higher uninsured share (rho = 0.490), lower with a larger Black population share (rho = −0.321), and unassociated with poverty (rho = 0.017). The cohort included 15,612 patients with H90.3 (0.94% of the RDW; 4,244,868 encounters; 1/1/2013–9/30/2026): White 8,597 (55.1%), Black 6,176 (39.6%), and other/unknown 839 (5.4%). Nearly all (15,103/15,612, 96.74%) had ≥1 Otolaryngology encounter, consistent with diagnosis in that setting. 1,730/15,612 (11.08%) had ≥1 Audiology encounter, less often among Black than White patients (630/6,176, 10.20% vs 996/8,597, 11.59%; risk difference −1.38 percentage points, 95% CI −2.40 to −0.37; risk ratio 0.880, 95% CI 0.801–0.968; p = 0.008). Age-adjusted (Mantel-Haenszel) results, rural residence, and RDW base-population comparison remain [PENDING].

**Conclusions**: Audiology visits were uncommon and modestly less frequent among Black than White patients; whether that gap persists within age groups is [PENDING]. Otolaryngology contact was nearly universal and is not used here as an access measure. Limits include single-center data, one diagnosis code, UMMC-only capture, and Audiology data starting mid-2014.

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
1. Test whether, among UMMC patients with documented bilateral sensorineural hearing loss (ICD-10 H90.3), Black patients are less likely than White patients to have ≥1 Audiology-department encounter, and whether that difference persists after stratification by age group.
2. Secondarily, describe the cohort's race composition relative to the RDW base population, examine whether the audiology gap varies by sex, and, if a residence field can be used, compare audiology use for rural vs non-rural patients.
3. Place these findings in ecological context using county-level hearing-disability estimates (CDC PLACES, ACS, County Health Rankings), without treating those associations as confirmatory tests of the UMMC hypothesis.

### 2.2 Hypotheses (revised 2026-11-26; α = 0.05, two-sided unless noted)

**Rationale.** Audiology is the gateway to hearing aids and cochlear implant evaluation; an Otolaryngology encounter alone does not capture hearing rehabilitation. The primary contrast is therefore ≥1 Audiology-department encounter, not ENT contact.

**Primary hypothesis (H-U2).** Among UMMC patients with ICD-10 H90.3, Black patients are less likely than White patients to have ≥1 Audiology-department encounter, and the difference persists after stratifying by age group.

- **H0:** Among patients with H90.3, the proportion with ≥1 Audiology-department encounter is equal for Black and White patients overall, and the common (age-stratified) risk ratio equals 1.
- **H1:** Black patients are less likely than White patients to have ≥1 Audiology-department encounter, and the difference persists after age stratification (Mantel-Haenszel risk ratio < 1).
- **Data:** H90.3 × FirstRace (Black, White) × Department Specialty = Audiology (ever; encounter-level Data Filters); age bands from MinAge/MaxAge (request R9).
- **Tests:** Pearson χ² (2×2, uncorrected); Wald 95% CI for the risk difference (Black − White); Katz log-Wald 95% CI for the crude risk ratio; Woolf 95% CI for the odds ratio; Mantel-Haenszel risk ratio and 95% CI across age strata (R9).
- **Result:** Crude comparison **supported** (modest): 630/6,176 (10.20%) vs 996/8,597 (11.59%); RD −1.38 percentage points (95% CI −2.40 to −0.37); RR 0.880 (95% CI 0.801–0.968); Pearson χ²(1) = 7.03, p = 0.008; OR 0.867 (95% CI 0.780–0.963). Age-adjusted (Mantel-Haenszel) RR **[PENDING]** (R9). Caveats: Audiology department data from mid-2014 (window 6/26/2014–9/30/2026; 7/5/2014 start for White) while the cohort starts 1/1/2013; UMMC visits only; possible circularity (R8).

**Secondary hypotheses (few).**

| ID | Null (H0) | Alternative (H1) | Data needed | Planned test | Result |
|---|---|---|---|---|---|
| H-S1 | The Black–White difference in ≥1 Audiology-department encounter is absent within sex strata, or is explained by sex composition | The audiology gap is present after sex stratification or sex adjustment | H90.3 × sex × FirstRace × Department Specialty = Audiology (header Patients counts; do not back-calculate cells from pie-chart sex percentages) | Sex-stratified proportions; Mantel-Haenszel or logistic adjustment if counts allow | **[PENDING]** |
| H-S2 (formerly H-U1) | The share of Black patients in the H90.3 cohort equals their share of the overall RDW patient population | Differs (predicted lower, matching lower measured prevalence in Black adults; age structure must be considered) | H90.3 patients by race; all RDW patients by race (request R3) | Chi-square goodness-of-fit / two-proportion z-test; age-band stratified descriptives | **Partial**: cohort race split recorded (FirstRace; screenshots 2026-11-26): White 8,597 (55.1% of 15,612), Black 6,176 (39.6%), other/unknown combined 839 (5.4%; 15,612 − 8,597 − 6,176). Comparison to the RDW base-population race distribution remains **[PENDING]** (R3). |
| H-S3 | Among H90.3 patients, the proportion with ≥1 Audiology-department encounter is equal for rural and non-rural residents | Lower in rural residents | A residence field **if** it can classify rural vs non-rural. A State/County field has been seen on the Patient Demographics screen; exact label and usability remain to be confirmed (request R7). Otherwise not testable. | Chi-square; risk difference | **[PENDING; field seen, usability unconfirmed]** |

**Exploratory / ecological context (county-level; not confirmatory).** The former county hypotheses H-C1–H-C5 are retained as exploratory associations that set the scene. They are not confirmatory tests of the UMMC primary hypothesis. The unit is the county. PLACES estimates are model-based and use ACS inputs, so associations with race, poverty, and insurance are partly built in.

| ID | Association examined | Data source (year) | Test | Result (ecological) |
|---|---|---|---|---|
| H-C1 | Adult hearing disability higher in rural (≥50% rural) counties; positive correlation with % rural | PLACES age-adjusted % (BRFSS 2023, 2025 release); CHR&R % rural (2020 Census) | Mann-Whitney U and Welch t; Spearman rho | 7.54% vs 6.91%, p = 1.5e-4; rho = 0.477, p = 6.0e-6 |
| H-C2 | Association between county % Black and hearing disability prevalence (literature predicts negative) | PLACES; ACS 2020–2024 B02001 | Spearman rho | rho = −0.321, p = 0.0033 |
| H-C3 | Positive association between county poverty rate and hearing disability prevalence | PLACES; ACS 2020–2024 B17001 | Spearman rho | Not supported: rho = 0.017, p = 0.88 |
| H-C4 | Fewer PCPs per 100,000 associated with higher hearing disability prevalence | PLACES; CHR&R PCP (AMA 2021) | Spearman rho | rho = −0.470, p = 8.5e-6 (confounded by rurality) |
| H-C5 | Higher uninsured share (<65) associated with higher hearing disability prevalence | PLACES; CHR&R uninsured (SAHIE 2022) | Spearman rho | Partially supported (PLACES only): rho = 0.490, p = 3.0e-6; ACS direct rho = 0.178, p = 0.109 |

The five Spearman tests use PLACES age-adjusted prevalence and were Holm-corrected as one family (Holm p = 2.4e-5, 0.0066, 0.88, 2.5e-5, 1.5e-5 for H-C1 to H-C5). Exploratory: multivariable OLS with HC3 robust SE. Details: [`county-analysis.md`](county-analysis.md).

**Retired as hypotheses; retained as a descriptive finding.** H-U3 (Black patients less likely than White patients to have ≥1 Otolaryngology encounter) and H-U4 (Black patients less likely to have ≥1 audiology or ENT encounter) are retired as hypotheses. After observing near-universal Otolaryngology contact (15,103/15,612, 96.74%; Black 6,062/6,176, 98.15%; White 8,229/8,597, 95.72%), “ever ENT” and “audiology or ENT” are not useful access measures. The result is reframed as a descriptive finding: H90.3 is diagnosed almost entirely within Otolaryngology, supporting ENT as the diagnostic setting and audiology as the care-gap measure. Counts and statistics remain in §4.3 as description, not as hypothesis tests of access.

Suppression rule for all UMMC cells: counts under 11 shown as "<11 (suppressed)", with complementary suppression where a hidden cell could be recovered by subtraction.

**Hypothesis revision log**

- 2026-11-26: Hypotheses tightened with Jake Harthcock's approval. The formal list was reduced to one primary hypothesis (H-U2, expanded to include persistence after age stratification, tested with a Mantel-Haenszel risk ratio) and three secondary hypotheses (H-S1, sex-stratified or sex-adjusted audiology gap; H-S2, cohort race vs the RDW base, formerly H-U1; H-S3, rural vs non-rural audiology if a residence field can be used). County associations H-C1–H-C5 were reclassified as exploratory ecological context, not confirmatory tests, with an explicit PLACES modeling-circularity caveat. The former interaction hypothesis H-U6 was dropped from the formal list. H-U3 and H-U4 were retired as hypotheses after observing near-universal Otolaryngology contact (96.74%); they are retained only as a descriptive finding about the diagnostic setting. This change is recorded openly so the ENT outcome is not presented as if it had never been hypothesized (to avoid the appearance of HARKing). The crude audiology comparison was already pre-specified and remains the unadjusted primary result. The age-persistence clause and Mantel-Haenszel test were added as part of this tightening, before the age-stratified counts (R9) were obtained; the age-adjusted result is **[PENDING]**.

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
- Geography: a State/County field has been seen on the Patient Demographics screen; exact label and whether it can classify rural vs non-rural for the audiology analysis (H-S3) remain to be confirmed (request R7). Do not treat the field as confirmed usable until that check is done.
- Care processes: ≥1 audiology encounter and ≥1 otolaryngology (ENT) encounter, defined from **Department Specialty** (Data Filters → Admissions & Visits → Encounter Search; Current Selections label **DepartmentSpecialty**). Data Filters selections are encounter-level: the header Patients count is H90.3 patients with ≥1 encounter in the selected department specialty. Audiology uses the value **Audiology**; Otolaryngology / ENT uses the value **Otolaryngology** (both confirmed 2026-11-26). Because 15,103/15,612 (96.74%) of the H90.3 cohort had ≥1 Otolaryngology-department encounter, “ever ENT” is treated as a coding/diagnosis pattern rather than an access measure; audiology is the primary utilization outcome.
- Age: Data Filters → Patient Demographics shows “Enter Age, then Press Enter” with MinAge and MaxAge fields (seen on screen). A chart on that screen is labeled “Age at Encounter”; whether the MinAge/MaxAge filter is age at encounter versus a single patient age is unconfirmed and will be checked in request R9.
- Optional: payer (Primary Financial Class), encounter setting

### Analysis
Descriptive statistics overall and by race (and by rurality if a usable residence field is confirmed). For the primary hypothesis (H-U2, Black vs White, ≥1 Audiology-department encounter yes/no): Pearson chi-square on the 2×2 table (uncorrected); Wald 95% CI for the risk difference (Black minus White); Katz log-Wald 95% CI for the crude risk ratio; Woolf log-Wald 95% CI for the odds ratio; Mantel-Haenszel risk ratio and 95% CI across age strata (R9; age-adjusted result **[PENDING]**). Secondary: sex-stratified or sex-adjusted audiology comparison (H-S1; header Patients counts, not pie-chart percentages); two-proportion comparison of cohort vs RDW race (H-S2 / formerly H-U1; needs R3); rural vs non-rural audiology if residence is usable (H-S3; R7). Otolaryngology contact is described as the diagnostic setting, not tested as an access outcome (retired hypotheses H-U3 and H-U4). County-level associations are ecological context, not confirmatory tests of the UMMC hypothesis: Spearman correlation, Mann-Whitney/Welch rural vs non-rural comparison, Holm correction across the five tests, exploratory OLS with robust SE. PLACES estimates are model-based and use ACS inputs, so associations with race, poverty, and insurance are partly built in. Only aggregate counts are used. UMMC cells under 11 are not recorded (suppressed); public county data are unaffected. On-screen “% of RDW” figures are recorded as displayed and are not back-calculated into an RDW denominator (request R3).

### Approvals
Data use confirmed by Jake Harthcock 2026-11-26 per Cohort Explorer guide (`data-use-rules.md`). The guide does not mention IRB review; whether the target conference requires an IRB determination is **[Jake to confirm]**.

---

## 4. Results

### 4.1 County-level results (82 Mississippi counties; ecological context, not confirmatory)
These associations are ecological (county as the unit) and are not confirmatory tests of the UMMC primary hypothesis. PLACES estimates are model-based and use ACS inputs, so associations with race, poverty, and insurance are partly built in. Full tables, years, and caveats: [`county-analysis.md`](county-analysis.md).

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

Definition: H90.3 patients with ≥1 encounter in the named Department Specialty (Data Filters → Admissions & Visits → Encounter Search; Current Selections label **DepartmentSpecialty**; encounter-level). Audiology value = **Audiology**; Otolaryngology / ENT value = **Otolaryngology** (screenshots, 2026-11-26). Denominators are the R1 patient counts (overall 15,612; Black 6,176; White 8,597). Rural / non-rural columns remain **[PENDING]** (R7).

| Metric | Overall | Black | White | Rural | Non-rural |
|---|---|---|---|---|---|
| ≥1 Audiology-department encounter (primary utilization outcome) | 1,730 / 15,612 (11.08%); Encounters 3,808 (0.01% of RDW); window 6/26/2014–9/30/2026 | 630 / 6,176 (10.20%); Encounters 1,297; Sex F 62.38%, M 37.62%; window 6/26/2014–9/30/2026 | 996 / 8,597 (11.59%); Encounters 2,295; Sex F 53.41%, M 46.59%; window 7/5/2014–9/30/2026 | [PENDING] | [PENDING] |
| ≥1 Otolaryngology-department encounter | 15,103 / 15,612 (96.74%); Encounters 295,604 (0.40% of RDW); window 1/1/2013–9/30/2026 | 6,062 / 6,176 (98.15%); Encounters 116,299 (0.16%); Sex F 61.56%, M 38.44% | 8,229 / 8,597 (95.72%); Encounters 164,567 (0.22%); Sex F 51.06%, M 48.94% | [PENDING] | [PENDING] |
| ≥1 Audiology or Otolaryngology encounter | Non-informative: would be ≥15,103 / 15,612 (96.74%). Formal OR search (R6) optional. | [PENDING if R6 run] | [PENDING if R6 run] | [PENDING] | [PENDING] |

Other / unknown race combined (direct subtraction): 104 / 839 (12.40%) had ≥1 Audiology-department encounter (1,730 − 630 − 996); 812 / 839 (96.78%) had ≥1 Otolaryngology-department encounter (15,103 − 6,062 − 8,229). Not further broken out. Header “% of RDW” figures are recorded as displayed (Audiology: 0.10% of patients, 0.01% of encounters; Otolaryngology: 0.91% of patients, 0.40% of encounters; race-specific ENT 0.37% and 0.50%); the exact RDW denominator stays **[PENDING]** (R3) and is not back-calculated.

**Primary hypothesis H-U2 (Black vs White; crude).** 2×2 counts: Black 630 with and 5,546 without an Audiology-department encounter; White 996 with and 7,601 without. Risk difference (Black − White) = −1.38 percentage points (Wald 95% CI −2.40 to −0.37). Risk ratio = 0.880 (Katz log-Wald 95% CI 0.801–0.968). Pearson χ²(1) = 7.03, p = 0.008. Odds ratio = 0.867 (Woolf 95% CI 0.780–0.963). Black patients were less likely than White patients to have ≥1 Audiology-department encounter; the absolute difference is modest (1.38 percentage points). The age-adjusted (Mantel-Haenszel) risk ratio remains **[PENDING]** (R9).

**Descriptive finding (retired hypotheses H-U3 and H-U4).** 2×2 counts: Black 6,062 with and 114 without an Otolaryngology-department encounter; White 8,229 with and 368 without. Risk difference (Black − White) = +2.43 percentage points (Wald 95% CI 1.89 to 2.98). Risk ratio = 1.025 (Katz log-Wald 95% CI 1.020–1.031). Pearson χ²(1) = 67.50, p = 2.11e-16. Odds ratio = 2.378 (Woolf 95% CI 1.922–2.942). H90.3 is diagnosed almost entirely within Otolaryngology (15,103/15,612, 96.74%; window 1/1/2013–9/30/2026, the full cohort window), supporting ENT as the diagnostic setting and audiology as the care-gap measure. The former H-U3 contrast (Black patients were *more* likely than White patients to have ≥1 Otolaryngology-department encounter) is reported here for completeness and is not interpreted as an access test (circularity; request R8). The former H-U4 outcome (audiology or ENT) is non-informative: a patient-level Audiology OR Otolaryngology count would be at least 15,103/15,612 (96.74%). A formal OR search (R6) is optional and would not change this interpretation.

**Limitations specific to these comparisons.** Audiology Department Specialty data appear only from mid-2014 (encounter window 6/26/2014–9/30/2026 when Audiology is selected; 7/5/2014–9/30/2026 for White patients), while the H90.3 cohort window starts 1/1/2013, so patients whose UMMC contacts fall only in the earlier period cannot show an Audiology-department encounter in the warehouse. Otolaryngology data span the full cohort window (1/1/2013–9/30/2026). “Ever” specialty visits are UMMC only; care outside UMMC is not captured. H90.3 may be coded at specialty visits, which for Otolaryngology appears to be the rule rather than the exception (request R8).

### 4.4 Additional planned analyses
- Age-stratified audiology by race for the primary hypothesis (Mantel-Haenszel RR) **[PENDING]** (R9).
- Sex-stratified or sex-adjusted audiology gap (H-S1) **[PENDING]**; do not back-calculate 2×2 cells from pie-chart sex percentages.
- Racial distribution of the H90.3 cohort vs overall RDW population (H-S2, formerly H-U1): cohort split recorded (White 8,597, 55.1%; Black 6,176, 39.6%; other/unknown 839, 5.4%); comparison to the RDW base population remains **[PENDING]** (R3).
- Rural vs non-rural audiology (H-S3) if the State/County field on Patient Demographics is usable **[PENDING]** (R7).
- Optional: diagnosis origin / circularity check (R8); UMMC patterns beside PLACES estimates for the catchment region (needs a usable residence variable) **[PENDING]**.

---

## 5. Discussion (early framing)

**Expected contribution**  
This study provides a system-level description of documented hearing loss and related specialty care at Mississippi’s academic medical center, with explicit attention to race and geography, alongside county-level context.

**What the county data already say**  
Rural Mississippi counties have higher modeled adult hearing disability prevalence, and counties with fewer PCPs and more uninsured residents do too, while counties with larger Black populations have lower measured prevalence. These are ecological, model-based associations and are not used to confirm the UMMC hypothesis. PLACES uses ACS inputs, so associations with race, poverty, and insurance are partly built in. The pattern is consistent with the introduction's premise that lower measured prevalence among Black residents does not imply lower need or better care, which is what the UMMC cohort tests.

**What the UMMC data say**  
Almost all patients with documented H90.3 (15,103/15,612, 96.74%) had an Otolaryngology-department encounter, so “ever ENT” cannot measure disparities in access; the diagnosis appears to be assigned predominantly in that specialty. The informative utilization contrast is audiology, which was uncommon (1,730/15,612, 11.08%) and modestly less frequent among Black than White patients (10.20% vs 11.59%; RR 0.880, 95% CI 0.801–0.968; p = 0.008). Whether that gap persists after age stratification (Mantel-Haenszel RR) is **[PENDING]** (R9).

**Strengths**  
Large real-world cohort; ability to examine both diagnosis and downstream care; linkage to statewide county estimates for all 82 counties.

**Limitations**  
Single-center; reliance on one diagnosis code (H90.3 only); H90.3 appears to be assigned predominantly at Otolaryngology visits (15,103/15,612, 96.74% had an Otolaryngology-department encounter), so “ever ENT” is not a valid access measure (circularity; request R8); possible under-ascertainment of audiology care; “ever” specialty visits are UMMC only (outside care is not captured); de-identified data limit social determinants; date-shifting; specialty encounter capture depends on Department Specialty coding in the RDW, and Audiology department data appear only from mid-2014 (selected window starting 6/26/2014) while the H90.3 cohort window starts 1/1/2013 (Otolaryngology data span the full window); Data Filters Department Specialty selections are encounter-level; the age-adjusted primary test is **[PENDING]** (R9); a State/County field has been seen but is not yet confirmed as a usable rural classifier (R7); county analysis is ecological and uses model-based PLACES estimates, with mixed data years and equal-weighted counties.

**Implications**  
Otolaryngology contact should not be used as an access outcome in this cohort. The modest unadjusted audiology gap (Black patients about 12% less likely than White patients to have an Audiology-department encounter) is the result that can inform screening, referral-pathway, and outreach questions; whether that gap persists within age groups is **[PENDING]** (R9).

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
- 2026-11-26: R5 Otolaryngology (Department Specialty; screenshots). 15,103/15,612 (96.74%) with ≥1 Otolaryngology-department encounter; Black 6,062/6,176 (98.15%) vs White 8,229/8,597 (95.72%); other/unknown 812/839 (96.78%; 15,103 − 6,062 − 8,229). RD +2.43 pp (Wald 95% CI 1.89 to 2.98); RR 1.025 (Katz 95% CI 1.020–1.031); Pearson χ²(1) = 67.50, p = 2.11e-16; OR 2.378 (Woolf 95% CI 1.922–2.942). H-U3 opposite direction but not a valid access measure (near-universal; circularity). H-U4 marked non-informative (≥96.74%). H-U2 designated the primary utilization outcome. Conference abstract v1 drafted (~298 words). Next optional: R3, R8, R9.
- 2026-11-26: Hypotheses tightened with Jake's approval (see Hypothesis revision log in §2.2). One primary hypothesis (H-U2, including persistence after age stratification; Mantel-Haenszel RR). Secondary: H-S1 (sex-stratified/adjusted audiology), H-S2 (cohort vs RDW race, formerly H-U1), H-S3 (rural audiology if residence usable). County H-C1–H-C5 reclassified as exploratory ecological context, not confirmatory, with a PLACES modeling-circularity caveat. H-U3 and H-U4 retired as hypotheses after observing near-universal Otolaryngology contact (96.74%); retained as a descriptive finding about the diagnostic setting (anti-HARKing note in the revision log). H-U6 dropped from the formal list. Abstract v1 reframed (300 words, body only); numbers unchanged; age-adjusted RR [PENDING]. Next action is R9.
