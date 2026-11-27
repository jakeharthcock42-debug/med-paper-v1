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
- Age: use the **Age** box to read counts for age bands (adult bands such as 18–39, 40–59, 60–74, 75 and older, or whatever the box offers; tell me the bands you used). One value or range at a time. Report Patients per band.

### R3. Denominator: all RDW patients by race — H-U1
- Filters: clear **everything** (no diagnosis). Report total Patients (and, if shown, total Encounters).
- Then Race one value at a time (same method as R1), report Patients per value. Optionally repeat with the same age bands as R2 so the comparison can be age-matched.
- Why: tests whether Black patients are over- or under-represented in the H90.3 cohort relative to the population the RDW draws from.
- Note: the R0 header shows the H90.3 cohort as **0.94%** of RDW patients (and **5.79%** of encounters). The R1 race-filtered headers show White H90.3 patients as **0.52%** of RDW and Black H90.3 patients as **0.37%**. Those percentages imply denominators exist on the unfiltered view, but the exact totals stay **[PENDING]** until you report them from the cleared-filter header. Do not back-calculate them from the percentages. H-U1 cannot be tested until this denominator (and the RDW race split) is reported.

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

### R5. ENT use among H90.3 patients — H-U3, Table 2 — **next** (exact Department Specialty label pending)
- The **Department Specialty** field is confirmed (**Data Filters** → **Admissions & Visits** → Encounter Search; Current Selections label **DepartmentSpecialty**). Data Filters selections are encounter-level. The exact Otolaryngology / ENT value label is not yet confirmed. **Do not select a value until you have sent the exact label.**
- Click-by-click:
  1. Keep H90.3 selected. Clear any **FirstRace** selection and clear **Audiology** in Department Specialty so the header returns to Patients = 15,612 and Encounters = 4,244,868 (Current Selections: `Pt_Dx_Code ORMode H90.3` only).
  2. Stay on **Data Filters** → **Admissions & Visits** → Encounter Search → **Department Specialty**.
  3. Scroll the Department Specialty list and look for Otolaryngology, ENT, or a similar label. Write down each candidate’s exact name as it appears. Leave them unselected.
  4. Reply with those exact label(s) before clicking any value. If more than one could be ENT, list them all and wait for confirmation.
  5. After the label is confirmed: keep H90.3 selected; select that exact ENT label; report header **Patients** and **Encounters** (and the encounter window if shown). Then add FirstRace = **Black or African American**, then **White or Caucasian**, reporting Patients and Encounters each time. Counts under 11 as `<11 (suppressed)`.

### R6. Audiology **or** ENT among H90.3 patients — H-U4 (primary outcome), Table 2
- The guide says the Patient Filters support advanced AND/OR/NOT searches at the patient level (pp. 5–6). If available, set Diagnosis = H90.3 AND (Audiology OR Otolaryngology). Report Patients overall and by race (Black, White, then others).
- If the OR search is not available: report R4 and R5, plus the number of H90.3 patients with **both** (select the audiology and ENT labels in two different patient-level boxes if two exist), and tell me what you did. Or report the "neither" count using a NOT search.

## Priority 2 — geography and access (needed for the rural hypothesis)

### R7. Residence variable — H-U5
- Report which of these exist in the Explorer: **State**, county, city, ZIP (look in the Demographic filters and the Admissions & Visits tab). Send only the names you find.
- If ZIP or county exists: H90.3 patients by county (or by ZIP groups) for the 82-county map, one value at a time (a Qlik list view may show all values; if counts appear next to each value without selecting, report that table). Counts under 11 suppressed.
- If only State exists: report H90.3 by State = Mississippi vs other, and stop (H-U5 is then not testable).

## Priority 3 — protects the finding from bias; do after Priority 1

### R8. Where is H90.3 diagnosed? — threat to H-U2 to H-U6
- H90.3 is often coded at an audiology/ENT visit, which would make "ever seen audiology/ENT" high for everyone. Using the **Encounter Filters** (all criteria on the same encounter), report the number of patients with H90.3 on an encounter in Audiology, in ENT, and in neither (Primary care / ED / other). Report overall and, if counts allow, for Black and White. If the Explorer cannot do this, tell me and I will note it as a limitation.

### R9. Age-stratified utilization — adjusts H-U4 for age
- For two or three age bands: H90.3 + age band + Race (Black, White) + (Audiology or ENT) as in R6. Report Patients per cell. Skip any band where a cell would be under 11.

## Priority 4 — optional covariates

### R10. Payer by race (Admissions & Visits tab)
- Primary Financial Class (Medicaid, Medicare, commercial, self-pay) × Race for the H90.3 cohort, one value at a time. Report Patients each.

### R11. Setting of care (ED vs outpatient vs inpatient)
- H90.3 patients who ever had an ED encounter, by race. Report Patients each (only if time allows).

## How the numbers get used
R0 to R3 fill Table 1 and H-U1 (race distribution vs RDW). R1 cohort race counts are in; R3 (RDW base-population race) is still needed to finish H-U1. R4 is done (H-U2). R5 and R6 fill the rest of Table 2 and H-U3 to H-U4. R7 enables H-U5 and H-U6. R8 and R9 are the main robustness checks. R10 and R11 are optional covariates. Send results as plain text, one request at a time (**R5 is next**: report the exact Department Specialty label for Otolaryngology / ENT first, before selecting a value).

## Status checklist
- [x] R0 total — Patients = 15,612 (0.94% of RDW); Encounters = 4,244,868 (5.79%); window 1/1/2013–9/30/2026 (screenshot, 2026-11-26)
- [x] R1 race exact counts — done 2026-11-26 (FirstRace): White or Caucasian Patients = 8,597 (55.1% of 15,612), Encounters = 2,119,544; Black or African American Patients = 6,176 (39.6%), Encounters = 2,000,250; other/unknown combined = 839 (15,612 − 8,597 − 6,176). Dropdown 47.1% / 49.9% are encounter shares, not patient shares.
- [x] R2 sex percentages — overall Female 54.84%, Male 45.16% (pie chart, no race selected; likely patient-based, basis unconfirmed); sex by race recorded with R1 (White F 50.81% / M 49.19%; Black F 61.33% / M 38.67%); exact counts and age **[PENDING]**
- [ ] R3 RDW race denominator (still required to finish H-U1)
- [x] R4 audiology — done 2026-11-26 (Department Specialty = Audiology): Patients 1,730/15,612 (11.08%); Black 630/6,176 (10.20%); White 996/8,597 (11.59%); other/unknown 104/839 (12.40%; 1,730 − 630 − 996). RD −1.38 pp (95% CI −2.40 to −0.37); RR 0.880 (0.801–0.968); Pearson χ²(1) = 7.03, p = 0.008
- [ ] R5 ENT — next: report the exact Department Specialty label before selecting
- [ ] R6 audiology or ENT
- [ ] R7 residence variable
- [ ] R8 diagnosis origin
- [ ] R9 age-stratified
- [ ] R10 payer
- [ ] R11 ED use
