# RDW / Patient Cohort Explorer data requests — Paper 01

**For**: Jake Harthcock (runs all queries; pastes aggregate numbers back).  
**Status**: **ACTIVE.** Data use confirmed by Jake Harthcock 2026-11-26 per Cohort Explorer guide ([`../../data-use-rules.md`](../../data-use-rules.md)).  
**Cohort**: ICD-10 **H90.3** (sensorineural hearing loss, bilateral), approximately 15,612 patients.  
**Last updated**: 2026-11-26.

## Rules for every request
1. **One selection per box.** Selecting a second value in the same box replaces the first. Different boxes can combine (AND). To get counts for several values of one box (for example each Race value), select one value, read the count, clear that box, then select the next.
2. **Keep H90.3 in Diagnosis Codes** for every cohort request unless the request says otherwise. Clear all other boxes before starting each request.
3. **What to report**: the **Patients** number in the header label. Say the Encounters number only when asked. Type numbers exactly; do not round.
4. **Suppression (project rule)**: never report or record a count under 11; write "<11 (suppressed)". Also note any category total you could not read directly so a hidden small cell cannot be recovered by subtraction. The app itself only allows report view/export when the population is greater than 25 (guide p. 20); if the app hides the report, the header counts are still enough for this list.
5. **Patient-level vs encounter-level**: the guide says the Patient Filters return patients where each criterion occurred for the patient on any encounter (not necessarily the same one), and the Encounter Filters require all criteria on the same encounter (guide pp. 6–7). For "ever had an audiology/ENT visit" use the **patient-level** filters. If you cannot tell which kind a box is, tell me what the box is called and where it sits.
6. If a box named below is not where expected, send the exact names of the filter boxes you see (the guide lists Sex, Ethnicity, Race, Multi-Racial, Preferred Language, Smoking Status, State, Country, Age, and on the Admissions & Visits tab Primary Financial Class; pp. 16–17). Do not guess.

## Priority 1 — core Tables 1 and 2 (needed for the abstract)

### R0. Cohort total (Step 1) — H-U1, Table 1
- Filters: Diagnosis Codes = H90.3 only.
- Report: Patients; Encounters.

### R1. Race breakdown of the H90.3 cohort (Step 2) — H-U1, Table 1
1. Keep H90.3 selected in Diagnosis Codes. Clear every other box.
2. In the **Race** box, select the first value (for example Black or African American, using the exact label shown). Read **Patients** in the header. Write down the label and the number.
3. Clear only the Race selection (H90.3 stays). Select the next Race value and read **Patients**. Repeat for every value listed in the Race box, including Unknown / Declined if shown.
4. Do the same once in the **Ethnicity** box (Hispanic or Latino / not), with Race cleared.
5. Note whether **Multi-Racial** is a separate box and its count when selected (one value at a time).
6. Report as `Race value: Patients`. Counts under 11 as "<11 (suppressed)".

### R2. Sex and age of the H90.3 cohort — Table 1
- Filters: H90.3 + **Sex** (Female, then Male; one at a time). Report Patients each.
- Age: use the **Age** box to read counts for age bands (adult bands such as 18–39, 40–59, 60–74, 75 and older, or whatever the box offers; tell me the bands you used). One value or range at a time. Report Patients per band.

### R3. Denominator: all RDW patients by race — H-U1
- Filters: clear **everything** (no diagnosis). Report total Patients.
- Then Race one value at a time (same method as R1), report Patients per value. Optionally repeat with the same age bands as R2 so the comparison can be age-matched.
- Why: tests whether Black patients are over- or under-represented in the H90.3 cohort relative to the population the RDW draws from.

### R4. Audiology use among H90.3 patients — H-U2, Table 2
- Find the box that holds the clinic, department, or provider specialty (look under Patient Filters, Encounter Filters, and the standard data filters; send me the box names you see). Select **Audiology** (use the exact label; if there are several audiology labels, report each one separately, never combined by guesswork).
- Filters: H90.3 + Audiology (patient-level). Report Patients overall.
- Then add **Race**, one value at a time (at least Black, White; then every other value that is not suppressed). Report Patients each.

### R5. ENT use among H90.3 patients — H-U3, Table 2
- Same as R4 with **Otolaryngology / ENT** (exact label).

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
R0 to R3 fill Table 1 and H-U1 (race distribution vs RDW). R4 to R6 fill Table 2 and H-U2 to H-U4. R7 enables H-U5 and H-U6. R8 and R9 are the main robustness checks. R10 and R11 are optional covariates. Send results as plain text, one request at a time (R0 first).

## Status checklist
- [ ] R0 total
- [ ] R1 race
- [ ] R2 sex and age
- [ ] R3 RDW race denominator
- [ ] R4 audiology
- [ ] R5 ENT
- [ ] R6 audiology or ENT
- [ ] R7 residence variable
- [ ] R8 diagnosis origin
- [ ] R9 age-stratified
- [ ] R10 payer
- [ ] R11 ED use
