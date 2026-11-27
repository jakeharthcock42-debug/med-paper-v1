# 01 — Hearing Loss Disparities

**Working title**: Racial and Geographic Disparities in Documented Hearing Loss and Related Care at UMMC / Across Mississippi Counties  
**Status**: Hypotheses written; county-level public-data tests complete; Step 1 done (H90.3 Patients = 15,612, 0.94% of RDW; Encounters = 4,244,868, 5.79%; window 1/1/2013–9/30/2026). R1 exact counts recorded (FirstRace): White or Caucasian 8,597 (55.1% of 15,612); Black or African American 6,176 (39.6%); other/unknown combined 839 (5.4%; 15,612 − 8,597 − 6,176). The Race dropdown percentages (Black 47.1%, White 49.9%) are encounter shares, not patient shares. Next: R4/R5 — find the department/specialty field (report exact names before selecting), then audiology and ENT counts by race.  
**Data use**: Data use confirmed by Jake Harthcock 2026-11-26 per Cohort Explorer guide ([`../../data-use-rules.md`](../../data-use-rules.md)). The guide does not mention IRB review; whether the target conference requires an IRB determination is open (Jake to confirm).  
**Suppression rule**: never record a UMMC RDW cell under 11; write it as "<11 (suppressed)" (project rule), and hide any other cell that could be recovered by subtraction. The Explorer itself only allows report view/export when the population is greater than 25 (guide p. 20). Public county data are unaffected.  
**Cohort**: ICD-10 **H90.3** (sensorineural, bilateral), **15,612** patients (0.94% of RDW) and **4,244,868** encounters (5.79%), confirmed from a 2026-11-26 Cohort Explorer screenshot with only H90.3 selected in **Pt Diagnosis Codes (OR)** (Current Selections: `Pt_Dx_Code ORMode H90.3`). The dataset includes encounters between **1/1/2013** and **9/30/2026**. Race uses the **FirstRace** field (Data Filters → Patient Demographics → Race). The Explorer allows one selection per filter box, so one code is used.  
**Primary data**: UMMC Patient Cohort Explorer / RDW (Jake runs all queries and pastes aggregates) + public county data (CDC PLACES, ACS, County Health Rankings)  
**Target**: Local/regional conference abstract (MAFP, ACP MS chapter, UMMC Research Day) → possible full paper later

## Specific aims
1. Describe the demographic distribution (race, age, sex, residence) of patients with documented H90.3 bilateral sensorineural hearing loss in the UMMC RDW.
2. Examine disparities in audiology/ENT utilization among those patients, by race and (if available) rural vs non-rural residence.
3. Place UMMC findings in the context of county-level hearing disability estimates (CDC PLACES) and primary-care access metrics across Mississippi.

## Hypotheses (full null/alternative table, data sources, and tests in [`draft-v1.md`](draft-v1.md) §2.2)

**County-level (public data) — tested 2026-11-26, details in [`county-analysis.md`](county-analysis.md)**

| ID | Hypothesis | Result (PLACES age-adjusted % hearing disability, 82 counties) |
|---|---|---|
| H-C1 | Higher in rural counties | **Supported**: 7.54% (n = 66) vs 6.91% (n = 16), Mann-Whitney p = 1.5e-4; Spearman rho vs % rural = 0.477 |
| H-C2 | Associated with county % Black (negative expected) | **Supported, negative**: rho = −0.321, p = 0.0033 |
| H-C3 | Higher with county poverty | **Not supported**: rho = 0.017, p = 0.88 |
| H-C4 | Higher with fewer PCPs per 100,000 | **Supported** (confounded by rurality): rho = −0.470, p = 8.5e-6 |
| H-C5 | Higher with more uninsured (<65) | **Partially supported**: PLACES rho = 0.490, p = 3.0e-6; ACS direct rho = 0.178, p = 0.109 |

**UMMC cohort (H-U1 partial; H-U2 to H-U6 and the H-U1 test still [PENDING])**

| ID | Hypothesis | Test |
|---|---|---|
| H-U1 | Black share of H90.3 cohort differs from Black share of overall RDW population (lower predicted) | chi-square / two-proportion test. **Partial**: cohort split recorded (FirstRace): White 8,597 (55.1%), Black 6,176 (39.6%), other/unknown 839 (5.4%). RDW base-population race (R3) still **[PENDING]**. |
| H-U2 | Black patients less likely than White to have ≥1 audiology encounter | chi-square, risk difference, odds ratio |
| H-U3 | Black patients less likely than White to have ≥1 ENT encounter | same |
| H-U4 (primary) | Black patients less likely than White to have ≥1 audiology or ENT encounter | same |
| H-U5 | Rural patients less likely than non-rural to have ≥1 audiology or ENT encounter (only if a residence variable exists) | chi-square, risk difference |
| H-U6 | Race × rurality interaction (exploratory) | stratified proportions |

Caution: H90.3 is often coded at an audiology/ENT visit, so "ever seen audiology/ENT" may be high for everyone by construction. See requests R8 and R9 in [`rdw-data-requests.md`](rdw-data-requests.md).

## Next actions
- [x] **Step 1**: H90.3 Patients = **15,612** (0.94% of RDW); Encounters = **4,244,868** (5.79%); window 1/1/2013–9/30/2026 (screenshot, 2026-11-26; Pt Diagnosis Codes (OR) = H90.3 only). The 0.94% figure implies an RDW patient denominator; that exact total stays **[PENDING]** until R3 (do not back-calculate it).
- [x] **Step 2 / R1 exact counts** (screenshots, 2026-11-26): Race box is on the **Data Filters** page → **Patient Demographics** tab → Demographic Search list → **Race**; Current Selections label is **FirstRace**. With H90.3 + one FirstRace value: White or Caucasian Patients = **8,597** (0.52% of RDW; 55.1% of 15,612), Encounters = **2,119,544** (2.89%); Black or African American Patients = **6,176** (0.37% of RDW; 39.6% of 15,612), Encounters = **2,000,250** (2.73%). Other/unknown combined = **839** (5.4%; 15,612 − 8,597 − 6,176). The Race dropdown percentages (Black 47.1%, White 49.9%) are encounter shares of the 4,244,868 cohort encounters (2,000,250 / 4,244,868 = 47.1%; 2,119,544 / 4,244,868 = 49.9%), not patient shares; small-group dropdown percentages are encounter shares only and are not converted to patient counts. Sex by race (pie chart with FirstRace selected): White Female 50.81%, Male 49.19%; Black Female 61.33%, Male 38.67%. Overall-cohort sex (no race selected): Female **54.84%**, Male **45.16%** (likely patient-based; pie chart basis unconfirmed). Exact overall and by-race sex counts **[PENDING]** (not back-calculated). The 0.52% and 0.37% figures imply RDW denominators; those exact totals stay **[PENDING]** until R3 (do not back-calculate them).
- [ ] **Next (Jake, now): R4, then R5** — look on **Admissions & Visits** for a department/specialty/provider-specialty field and report the exact names before selecting any value; then audiology (R4) and ENT (R5) Patients counts overall and by race. Click-by-click below.
- [ ] Work through the remaining requests in [`rdw-data-requests.md`](rdw-data-requests.md) (active; R3 and R4 to R11 still open). R3 is still needed to finish H-U1.
- [ ] Fill remaining cells in Tables 1 and 2 in `draft-v1.md`, run the H-U tests, write the abstract Results and Conclusions.
- [ ] Add formal citations for the Introduction (currently seed claims) and confirm whether an IRB determination is needed for the target conference.
- [x] Write hypotheses and map each to a data source and test (2026-11-26).
- [x] Pull and test public county data (PLACES, ACS, CHR&R; 82 counties) (2026-11-26).
- [x] Replace the old H90 ± H91 plan with H90.3 (the older plan text in `rdw-exploration-plan.md` is superseded by the banner at its top).

### Step 1 — done (2026-11-26, screenshot)
- Patients = **15,612** (0.94% of RDW).
- Encounters = **4,244,868** (5.79%).
- Selection: only H90.3 in **Pt Diagnosis Codes (OR)**; Current Selections showed `Pt_Dx_Code ORMode H90.3`.
- Data window shown on screen: encounters between **1/1/2013** and **9/30/2026**.
- The 0.94% (and 5.79%) figures imply RDW denominators; the exact unfiltered totals stay **[PENDING]** until Jake reports them in R3. Do not back-calculate them.

The Patient Filters screen shows **Diagnosis / Procedures / Medications / Labs** tabs. The **Race** box is **not** on that screen. It is on the **Data Filters** page → **Patient Demographics** tab → Demographic Search list → **Race**. The Current Selections label for that field is **FirstRace**. The Race dropdown percentages are encounter shares of the current selection, not patient shares.

### Step 2 / R1 — done (2026-11-26, screenshots)
Field: **FirstRace** (Data Filters → Patient Demographics → Race). Counts are header totals with H90.3 + one FirstRace value selected.

- White or Caucasian: Patients = **8,597** (0.52% of RDW; **55.1%** of 15,612 = 8,597 / 15,612); Encounters = **2,119,544** (2.89% of RDW; **49.9%** of 4,244,868 cohort encounters = 2,119,544 / 4,244,868); encounters per patient = **246.5** (2,119,544 / 8,597). Sex (pie chart with this FirstRace selected): Female **50.81%**, Male **49.19%**.
- Black or African American: Patients = **6,176** (0.37% of RDW; **39.6%** of 15,612 = 6,176 / 15,612); Encounters = **2,000,250** (2.73% of RDW; **47.1%** of 4,244,868 = 2,000,250 / 4,244,868); encounters per patient = **323.9** (2,000,250 / 6,176). Sex: Female **61.33%**, Male **38.67%**.
- Other / unknown combined: Patients = **839** (**5.4%** of 15,612), computed as 15,612 − 8,597 − 6,176. This is a direct subtraction of reported counts, reported as one combined row only.

Patient-share percentages are rounded to one decimal (8,597 / 15,612 = 55.1%; 6,176 / 15,612 = 39.6%; 839 / 15,612 = 5.4%) and sum to 100.1% because of that rounding. The 0.52% and 0.37% of RDW figures are recorded as displayed; do not back-calculate an RDW denominator from them. Exact sex counts are **[PENDING]**; do not back-calculate them from the pie-chart percentages. Overall-cohort sex with no race selected (Female 54.84%, Male 45.16%) is likely patient-based; the pie chart basis is unconfirmed.

**Encounter shares vs patient shares.** The Race dropdown percentages recorded earlier (Black or African American 47.1%; White or Caucasian 49.9%; and the smaller rows below) are encounter shares of the 4,244,868 H90.3 encounters, not patient shares. They are kept as encounter-share notes only and are **not** converted to patient counts:

- (blank/unlabeled row) 0.0%
- American Indian or Alaska Native 0.2%
- Asian 0.5%
- Asian Indian 0.0%
- Black or African American 47.1% (matches 2,000,250 / 4,244,868)
- Hispanic 0.2%
- MS Band Choctaw Indian 0.2%
- Multiracial 0.4%
- Native Hawaiian or Other Pacific Islander 0.0%
- Other 1.1%
- Patient Refused 0.1%
- Unknown 0.2%
- White or Caucasian 49.9% (matches 2,119,544 / 4,244,868)

Grayed out (no patients in this selection, as previously observed): Chinese, Filipino, Guamanian or Chamorro, Japanese, Korean, Native Hawaiian, Other Pacific Islander, Samoan, Vietnamese.

A displayed 0.0% encounter share is not treated as a patient count and is not recorded as `<11 (suppressed)` from the dropdown alone.

### Next — R4 (then R5): find the department or specialty field, then audiology / ENT counts by race
Keep H90.3 selected. Use only what you see on screen. Never report a count under 11; write `<11 (suppressed)`. Clear any Race / FirstRace selection first so the header returns to Patients = 15,612 and Encounters = 4,244,868.

The department or specialty filter location is not yet confirmed. **Do not select a value until you have sent the exact field names.**

1. Confirm you are on the **Data Filters** page and that only **H90.3** is selected in diagnosis (Current Selections: `Pt_Dx_Code ORMode H90.3`; header Patients = 15,612; Encounters = 4,244,868).
2. The Data Filters page has these tabs: **Patient Demographics**, **Admissions & Visits**, **ED Visits**, **Procedures**, **Medications**, **Labs**, **Diagnosis**. Open **Admissions & Visits** and look for a department, clinic, specialty, or provider-specialty field. Write down each field’s exact label and leave it unselected.
3. If you do not see such a field on Admissions & Visits, check the other Data Filters tabs, the Patient Filters page, and the page reached by **Proceed to Encounter Filters**. Send the exact names and locations of any candidate fields you find.
4. Reply with those exact field names (and which tab or page each is on) before clicking any value. If more than one field could be audiology or ENT, list them all and wait for confirmation.
5. After the field is confirmed, the counts to get are: H90.3 + the exact Audiology label, header **Patients** (and Encounters if shown); then the same with FirstRace = **Black or African American**, then FirstRace = **White or Caucasian**. R5 repeats this with the Otolaryngology / ENT label.

## File guide
- [`county-analysis.md`](county-analysis.md) — county-level methods, exact results, sources, caveats; data in [`data/ms_county_merged.csv`](data/ms_county_merged.csv); script [`data/build_and_analyze.py`](data/build_and_analyze.py)
- [`rdw-data-requests.md`](rdw-data-requests.md) — prioritized list of every UMMC Cohort Explorer number the paper needs (active)
- [`rdw-exploration-plan.md`](rdw-exploration-plan.md) — original cohort/variable plan (cohort and suppression updated by the banner at its top)
- `draft-v1.md` — working manuscript / abstract text, hypotheses, tables, notes
- `final.md` — polished version for submission (create when ready)
