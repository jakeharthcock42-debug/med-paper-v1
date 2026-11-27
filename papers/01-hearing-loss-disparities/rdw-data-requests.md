# RDW / Patient Cohort Explorer data requests — Paper 01

**For**: Jake Harthcock (runs all queries; pastes aggregate numbers back).  
**Status**: **ACTIVE.** Data use confirmed by Jake Harthcock 2026-11-26 per Cohort Explorer guide ([`../../data-use-rules.md`](../../data-use-rules.md)).  
**Cohort**: ICD-10 **H90.3** (sensorineural hearing loss, bilateral), **15,612** patients (0.94% of RDW) and **4,244,868** encounters (5.79%), confirmed from a 2026-11-26 screenshot (Pt Diagnosis Codes (OR) = H90.3 only; Current Selections: `Pt_Dx_Code ORMode H90.3`). Data window: encounters between **1/1/2013** and **9/30/2026**. Race uses the **FirstRace** field (Data Filters → Patient Demographics → Race). Audiology/ENT use uses **Department Specialty** (Data Filters → Admissions & Visits → Encounter Search; Current Selections label **DepartmentSpecialty**); Data Filters selections are encounter-level.  
**Last updated**: 2026-11-26.

## Rules for every request
1. **One selection per box.** Selecting a second value in the same box replaces the first. Different boxes can combine (AND). To get counts for several values of one box (for example each Race value), select one value, read the count, clear that box, then select the next.
2. **Keep H90.3 in Diagnosis Codes** for every cohort request unless the request says otherwise. Clear all other boxes before starting each request.
3. **What to report**: the **Patients** number in the header label. Say the Encounters number only when asked. Type numbers exactly; do not round.
4. **Suppression (project rule)**: never report or record a count under 11; write "<11 (suppressed)". Also note any category total you could not read directly so a hidden small cell cannot be recovered by subtraction. The app itself only allows report view/export when the population is greater than 25 (guide p. 20); if the app hides the report, the header counts are still enough for this list.
5. **Patient-level vs encounter-level**: the guide says the Patient Filters return patients where each criterion occurred for the patient on any encounter (not necessarily the same one), and the Encounter Filters require all criteria on the same encounter (guide pp. 6–7). For "ever had an audiology/ENT visit" use the **patient-level** filters. If you cannot tell which kind a box is, tell me what the box is called and where it sits.
6. If a box named below is not where expected, send the exact names of the filter boxes you see (the guide lists Sex, Ethnicity, Race, Multi-Racial, Preferred Language, Smoking Status, State, Country, Age, and on the Admissions & Visits tab Primary Financial Class; pp. 16–17). Do not guess.

## Priority 1 — core Tables 1 and 2 (needed for the abstract)

### R0. Cohort total (Step 1) — H-U1, Table 1 — **DONE** (2026-11-26, screenshot)
- Filters: **Pt Diagnosis Codes (OR)** = H90.3 only. Current Selections: `Pt_Dx_Code ORMode H90.3`.
- Report: Patients; Encounters.
- **Result**: Patients = **15,612** (0.94% of RDW). Encounters = **4,244,868** (5.79%). Data window: encounters between **1/1/2013** and **9/30/2026**.

### R1. Race breakdown of the H90.3 cohort (Step 2) — H-U1, Table 1 — **DONE** (exact counts, 2026-11-26, screenshots)
- Location confirmed: **Data Filters** page → **Patient Demographics** tab → Demographic Search list → **Race**. Current Selections label: **FirstRace**. Race is not on the Patient Filters (Diagnosis / Procedures / Medications / Labs) screen.
- **Result — patient counts** (header totals with H90.3 + one FirstRace value selected):
  - White or Caucasian: Patients = **8,597** (0.52% of RDW; **55.1%** of 15,612 = 8,597 / 15,612); Encounters = **2,119,544** (2.89% of RDW; **49.9%** of 4,244,868 cohort encounters = 2,119,544 / 4,244,868); encounters per patient = **246.5** (2,119,544 / 8,597). Sex (pie chart with this FirstRace selected): Female **50.81%**, Male **49.19%**.
  - Black or African American: Patients = **6,176** (0.37% of RDW; **39.6%** of 15,612 = 6,176 / 15,612); Encounters = **2,000,250** (2.73% of RDW; **47.1%** of 4,244,868 = 2,000,250 / 4,244,868); encounters per patient = **323.9** (2,000,250 / 6,176). Sex: Female **61.33%**, Male **38.67%**.
  - Other / unknown combined: Patients = **839** (**5.4%** of 15,612), computed as 15,612 − 8,597 − 6,176. Reported as one combined row only.
- Patient-share percentages are rounded to one decimal and sum to 100.1% because of that rounding. The 0.52% and 0.37% of RDW figures are recorded as displayed; do not back-calculate an RDW denominator from them (that total stays **[PENDING]** until R3). Exact sex counts **[PENDING]**; do not back-calculate them from the pie-chart percentages.
- **Encounter shares vs patient shares.** The Race dropdown percentages are encounter shares of the 4,244,868 H90.3 encounters, not patient shares (Black 47.1% matches 2,000,250 / 4,244,868; White 49.9% matches 2,119,544 / 4,244,868). They are kept as encounter-share notes only and are **not** converted to patient counts. A displayed 0.0% encounter share is not treated as a patient count and is not recorded as `<11 (suppressed)` from the dropdown alone.
  - (blank/unlabeled row) 0.0%
  - American Indian or Alaska Native 0.2%
  - Asian 0.5%
  - Asian Indian 0.0%
  - Black or African American 47.1%
  - Hispanic 0.2%
  - MS Band Choctaw Indian 0.2%
  - Multiracial 0.4%
  - Native Hawaiian or Other Pacific Islander 0.0%
  - Other 1.1%
  - Patient Refused 0.1%
  - Unknown 0.2%
  - White or Caucasian 49.9%
- Grayed out (no patients in this selection, as previously observed): Chinese, Filipino, Guamanian or Chamorro, Japanese, Korean, Native Hawaiian, Other Pacific Islander, Samoan, Vietnamese.
- Ethnicity (Hispanic or Latino / not) as a separate box, if present, remains **[PENDING]** (Hispanic also appears as a Race-list value at 0.2% encounter share).

### R2. Sex and age of the H90.3 cohort — Table 1 — **sex percentages recorded** (2026-11-26, screenshot); exact counts and age **[PENDING]**
- Overall-cohort sex pie chart on the Patient Demographics screen (H90.3, no race selected): Female **54.84%**, Male **45.16%**. This is likely patient-based; the pie chart basis is unconfirmed. Exact Patients counts **[PENDING]**; do not back-calculate them. If needed later, click Female, then Male, and report the header Patients number for each.
- Sex by race was captured with the R1 FirstRace clicks (pie chart with one race selected): White Female **50.81%**, Male **49.19%**; Black Female **61.33%**, Male **38.67%**. Exact by-race sex counts **[PENDING]**; not back-calculated.
- Age: Data Filters → Patient Demographics, **“Enter Age, then Press Enter”** (Current Selections **AgeKey**). R9 confirmed this is age at encounter. Band totals (0–17: 2,185; 18–44: 2,692; 45–64: 6,956; 65+: 8,991) are recorded with R9; they sum to more than 15,612 because a patient can appear in more than one band.

### R3. Denominator: all RDW patients by race — H-S2 (formerly H-U1)
- Filters: clear **everything** (no diagnosis). Report total Patients (and, if shown, total Encounters).
- Then Race one value at a time (same method as R1), report Patients per value. Optionally repeat with the same age bands as R2 so the comparison can be age-matched.
- Why: tests whether Black patients are over- or under-represented in the H90.3 cohort relative to the population the RDW draws from.
- Note: the R0 header shows the H90.3 cohort as **0.94%** of RDW patients (and **5.79%** of encounters). The R1 race-filtered headers show White H90.3 patients as **0.52%** of RDW and Black H90.3 patients as **0.37%**. Those percentages imply denominators exist on the unfiltered view, but the exact totals stay **[PENDING]** until you report them from the cleared-filter header. Do not back-calculate them from the percentages. H-S2 (formerly H-U1) cannot be tested until this denominator (and the RDW race split) is reported.

### R4. Audiology use among H90.3 patients — H-U2, Table 2 — **DONE** (2026-11-26, screenshots)
- Field confirmed: **Data Filters** → **Admissions & Visits** → Encounter Search → **Department Specialty** (Current Selections label **DepartmentSpecialty**), value **Audiology**. Data Filters selections are encounter-level: header Patients = H90.3 patients with ≥1 Audiology-department encounter.
- **Result**
  - H90.3 + Audiology: Patients = **1,730** (0.10% of RDW; 1,730 / 15,612 = **11.08%**), Encounters = **3,808** (0.01%); encounter window **6/26/2014–9/30/2026**.
  - + FirstRace Black or African American: Patients = **630** (0.04%; 630 / 6,176 = **10.20%**), Encounters = **1,297**; Sex Female **62.38%**, Male **37.62%**; window **6/26/2014–9/30/2026**.
  - + FirstRace White or Caucasian: Patients = **996** (0.06%; 996 / 8,597 = **11.59%**), Encounters = **2,295**; Sex Female **53.41%**, Male **46.59%**; window **7/5/2014–9/30/2026**.
  - Other / unknown combined with audiology: Patients = **104** of 839 (**12.40%**), computed as 1,730 − 630 − 996. Reported as one combined row only.
- Black vs White (2×2: Black 630 with / 5,546 without; White 996 with / 7,601 without). Risk difference (Black − White) = **−1.38** percentage points (Wald 95% CI **−2.40 to −0.37**). Risk ratio = **0.880** (Katz log-Wald 95% CI **0.801–0.968**). Pearson χ²(1) = **7.03**, p = **0.008**. Odds ratio = **0.867** (Woolf 95% CI **0.780–0.963**). H-U2 supported (modest absolute difference).
- The 0.10%, 0.04%, 0.06%, and 0.01% of RDW figures are recorded as displayed; do not back-calculate an RDW denominator from them.
- Caveats: Audiology department data appear only from mid-2014 (selected-window start 6/26/2014; 7/5/2014 for White), while the H90.3 cohort window starts 1/1/2013; “ever” audiology is a UMMC visit only; H90.3 may be coded at audiology visits (circularity; R8).

### R5. ENT use among H90.3 patients — descriptive finding (retired hypotheses H-U3 / H-U4), Table 2 — **DONE** (2026-11-26, screenshots)
- Field confirmed: **Data Filters** → **Admissions & Visits** → Encounter Search → **Department Specialty** (Current Selections label **DepartmentSpecialty**), value **Otolaryngology**. Data Filters selections are encounter-level: header Patients = H90.3 patients with ≥1 Otolaryngology-department encounter. Encounter window with this selection: **1/1/2013–9/30/2026** (the full cohort window).
- **Result**
  - H90.3 + Otolaryngology: Patients = **15,103** (0.91% of RDW; 15,103 / 15,612 = **96.74%**), Encounters = **295,604** (0.40%).
  - + FirstRace Black or African American: Patients = **6,062** (0.37%; 6,062 / 6,176 = **98.15%**), Encounters = **116,299** (0.16%); Sex Female **61.56%**, Male **38.44%**.
  - + FirstRace White or Caucasian: Patients = **8,229** (0.50%; 8,229 / 8,597 = **95.72%**), Encounters = **164,567** (0.22%); Sex Female **51.06%**, Male **48.94%**.
  - Other / unknown combined with Otolaryngology: Patients = **812** of 839 (**96.78%**), computed as 15,103 − 6,062 − 8,229. Reported as one combined row only.
- Black vs White (2×2: Black 6,062 with / 114 without; White 8,229 with / 368 without). Risk difference (Black − White) = **+2.43** percentage points (Wald 95% CI **1.89 to 2.98**). Risk ratio = **1.025** (Katz log-Wald 95% CI **1.020–1.031**). Pearson χ²(1) = **67.50**, p = **2.11e-16**. Odds ratio = **2.378** (Woolf 95% CI **1.922–2.942**). The pre-specified alternative (lower in Black patients) is not supported (direction is opposite). This is **not a valid access measure**: 96.74% had ≥1 Otolaryngology encounter, so “ever ENT” is near-universal by construction (H90.3 predominantly coded or diagnosed within Otolaryngology; circularity; R8). H-U3 and H-U4 were retired as hypotheses on 2026-11-26 after this result was observed (see the Hypothesis revision log in `draft-v1.md`); the counts are retained as a descriptive finding that H90.3 is diagnosed almost entirely within Otolaryngology, supporting ENT as the diagnostic setting and audiology as the care-gap measure. Audiology (H-U2) is the primary utilization outcome.
- The 0.91%, 0.37%, 0.50%, 0.40%, 0.16%, and 0.22% of RDW figures are recorded as displayed; do not back-calculate an RDW denominator from them.

### R6. Audiology **or** ENT among H90.3 patients — retired hypothesis H-U4 — **optional / non-informative**
- The former H-U4 hypothesis is retired and is non-informative without a new query: 15,103/15,612 (96.74%) already had ≥1 Otolaryngology encounter, so a patient-level Audiology OR Otolaryngology count would be **≥96.74%** (and at most 100%) and is not a useful access measure. H-U2 (audiology) is the primary utilization outcome.
- A formal OR search remains optional if a precise combined count is wanted. The guide says the Patient Filters support advanced AND/OR/NOT searches at the patient level (pp. 5–6). If used, set Diagnosis = H90.3 AND (Audiology OR Otolaryngology) and report Patients overall and by race.

## Priority 2 — geography and access (needed for secondary hypothesis H-S3)

### R7. Residence variable — H-S3
- A State/County field has been seen on the **Patient Demographics** screen. Confirm the exact field name(s) and send only the names you find (State, County, city, ZIP — Demographic filters and the Admissions & Visits tab). Do not treat the field as confirmed usable for rural vs non-rural classification until this check is done.
- If ZIP or county exists and can be used: H90.3 patients by county (or by ZIP groups) for the 82-county map, one value at a time (a Qlik list view may show all values; if counts appear next to each value without selecting, report that table). Counts under 11 suppressed. Then, if a rural classifier is agreed, repeat audiology counts (Department Specialty = Audiology) for rural vs non-rural, overall and by race if counts allow (H-S3).
- If only State exists, or County cannot support a rural classifier: report H90.3 by State = Mississippi vs other if useful, and stop (H-S3 is then not testable).

## Priority 3 — protects the finding from bias; do after Priority 1

### R8. Where is H90.3 diagnosed? — threat to the primary (and secondary) audiology comparisons
- H90.3 is often coded at an audiology/ENT visit, which would make "ever seen audiology/ENT" high for everyone. Using the **Encounter Filters** (all criteria on the same encounter), report the number of patients with H90.3 on an encounter in Audiology, in ENT, and in neither (Primary care / ED / other). Report overall and, if counts allow, for Black and White. If the Explorer cannot do this, tell me and I will note it as a limitation.

### R9. Age-stratified audiology by race — primary hypothesis (H-U2, Mantel-Haenszel RR) — **DONE** (2026-11-26, screenshots)
Field: Data Filters → Patient Demographics → “Enter Age, then Press Enter” (Current Selections **AgeKey**). This is age at encounter (chart label “Age at Encounter”); a patient can fall into more than one band. 65+ used MinAge 65 with MaxAge left blank. Department Specialty = **Audiology** as in R4. All reported cells ≥11 (no suppression).

| Age band | All | Black | Black, ≥1 Audiology | White | White, ≥1 Audiology |
|---|---:|---:|---:|---:|---:|
| 0–17 | 2,185 | 1,042 | 168 | 926 | 182 |
| 18–44 | 2,692 | 1,261 | 82 | 1,266 | 89 |
| 45–64 | 6,956 | 3,128 | 143 | 3,543 | 178 |
| 65+ | 8,991 | 3,225 | 243 | 5,428 | 550 |

Black vs White RR (Katz 95% CI): 0–17 0.820 (0.678–0.992); 18–44 0.925 (0.692–1.236); 45–64 0.910 (0.734–1.128); 65+ 0.744 (0.644–0.859). Mantel-Haenszel RR = **0.812** (Greenland-Robins 95% CI **0.711–0.928**; CMH χ² = 18.29, p = 1.89e-5). Homogeneity (Breslow-Day / Tarone) p = 0.31. Sensitivity excluding 0–17: MH RR **0.810** (0.695–0.943). Band totals sum to 20,824 vs unique N = 15,612. The 0–17 Audiology encounter window was 3/2026–9/30/2026 (Black 3/26/2026, White 3/16/2026); adult Audiology windows begin mid/late 2014. Whether pediatric Audiology-department coding begins only in 2026 is **[PENDING]** verification. Computations: `data/r9_mh_analysis.py`.

## Priority 4 — optional covariates

### R10. Payer by race (Admissions & Visits tab)
- Primary Financial Class (Medicaid, Medicare, commercial, self-pay) × Race for the H90.3 cohort, one value at a time. Report Patients each.

### R11. Setting of care (ED vs outpatient vs inpatient)
- H90.3 patients who ever had an ED encounter, by race. Report Patients each (only if time allows).

## How the numbers get used
R9 is done (age-stratified audiology; MH RR 0.812, 95% CI 0.711–0.928). R0 to R3 fill Table 1 and H-S2 (formerly H-U1; race distribution vs RDW). R1 cohort race counts are in; R3 (RDW base-population race) is still needed to finish H-S2. R4 is done (H-U2, crude primary result). R5 is done and is retained as a descriptive finding (retired hypotheses H-U3 / H-U4; 96.74% had an Otolaryngology encounter). R6 is non-informative (≥96.74%) and optional. R7 enables H-S3 if the State/County field can classify rural vs non-rural. R8 (diagnosis origin / circularity) remains an important limitation check. R10 and R11 are optional covariates. A conference abstract v2 is in `draft-v1.md`. Next non-optional UMMC check: verify the pediatric Audiology coding window.

## Status checklist
- [x] R0 total — Patients = 15,612 (0.94% of RDW); Encounters = 4,244,868 (5.79%); window 1/1/2013–9/30/2026 (screenshot, 2026-11-26)
- [x] R1 race exact counts — done 2026-11-26 (FirstRace): White or Caucasian Patients = 8,597 (55.1% of 15,612), Encounters = 2,119,544; Black or African American Patients = 6,176 (39.6%), Encounters = 2,000,250; other/unknown combined = 839 (15,612 − 8,597 − 6,176). Dropdown 47.1% / 49.9% are encounter shares, not patient shares.
- [x] R2 sex percentages — overall Female 54.84%, Male 45.16% (pie chart, no race selected; likely patient-based, basis unconfirmed); sex by race recorded with R1 (White F 50.81% / M 49.19%; Black F 61.33% / M 38.67%); exact counts and age **[PENDING]**
- [ ] R3 RDW race denominator (still required to finish H-S2 / formerly H-U1)
- [x] R4 audiology — done 2026-11-26 (Department Specialty = Audiology): Patients 1,730/15,612 (11.08%); Black 630/6,176 (10.20%); White 996/8,597 (11.59%); other/unknown 104/839 (12.40%; 1,730 − 630 − 996). RD −1.38 pp (95% CI −2.40 to −0.37); RR 0.880 (0.801–0.968); Pearson χ²(1) = 7.03, p = 0.008. Crude primary result; age-stratified MH RR 0.812 (0.711–0.928) recorded in R9.
- [x] R5 ENT — done 2026-11-26 (Department Specialty = Otolaryngology): Patients 15,103/15,612 (96.74%); Black 6,062/6,176 (98.15%); White 8,229/8,597 (95.72%); other/unknown 812/839 (96.78%; 15,103 − 6,062 − 8,229). RD +2.43 pp (95% CI 1.89 to 2.98); RR 1.025 (1.020–1.031); Pearson χ²(1) = 67.50, p = 2.11e-16. Descriptive finding (retired hypotheses H-U3 / H-U4): H90.3 is diagnosed almost entirely in Otolaryngology.
- [ ] R6 audiology or ENT — optional / non-informative (would be ≥96.74%)
- [ ] R7 residence variable (State/County field seen; confirm name and usability for H-S3)
- [ ] R8 diagnosis origin — circularity check
- [x] R9 age-stratified audiology — done 2026-11-26 (AgeKey = age at encounter): MH RR 0.812 (0.711–0.928; CMH p = 1.89e-5); sensitivity excluding 0–17: 0.810 (0.695–0.943). Pediatric Audiology window 3/2026–9/30/2026 remains [PENDING] verification.
- [ ] R10 payer
- [ ] R11 ED use
