# 01 — Hearing Loss Disparities

**Working title**: Racial and Geographic Disparities in Documented Hearing Loss and Related Care at UMMC / Across Mississippi Counties  
**Status**: Hypotheses written; county-level public-data tests complete; Step 1 done (H90.3 Patients = 15,612). Next: Step 2 / R1 race breakdown. Encounters **[PENDING]**.  
**Data use**: Data use confirmed by Jake Harthcock 2026-11-26 per Cohort Explorer guide ([`../../data-use-rules.md`](../../data-use-rules.md)). The guide does not mention IRB review; whether the target conference requires an IRB determination is open (Jake to confirm).  
**Suppression rule**: never record a UMMC RDW cell under 11; write it as "<11 (suppressed)" (project rule), and hide any other cell that could be recovered by subtraction. The Explorer itself only allows report view/export when the population is greater than 25 (guide p. 20). Public county data are unaffected.  
**Cohort**: ICD-10 **H90.3** (sensorineural, bilateral), **15,612** patients (confirmed 2026-11-26, Diagnosis Codes = H90.3 only). Encounters **[PENDING]**. The Explorer allows one selection per filter box, so one code is used.  
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

**UMMC cohort (need remaining RDW numbers; H-U1 to H-U6 still [PENDING])**

| ID | Hypothesis | Test |
|---|---|---|
| H-U1 | Black share of H90.3 cohort differs from Black share of overall RDW population (lower predicted) | chi-square / two-proportion test |
| H-U2 | Black patients less likely than White to have ≥1 audiology encounter | chi-square, risk difference, odds ratio |
| H-U3 | Black patients less likely than White to have ≥1 ENT encounter | same |
| H-U4 (primary) | Black patients less likely than White to have ≥1 audiology or ENT encounter | same |
| H-U5 | Rural patients less likely than non-rural to have ≥1 audiology or ENT encounter (only if a residence variable exists) | chi-square, risk difference |
| H-U6 | Race × rurality interaction (exploratory) | stratified proportions |

Caution: H90.3 is often coded at an audiology/ENT visit, so "ever seen audiology/ENT" may be high for everyone by construction. See requests R8 and R9 in [`rdw-data-requests.md`](rdw-data-requests.md).

## Next actions
- [x] **Step 1**: H90.3 Patients = **15,612** (Jake, 2026-11-26, Diagnosis Codes = H90.3 only). Encounters **[PENDING]**.
- [ ] **Step 2 (Jake, now)**: race breakdown of the H90.3 cohort (R1). Click-by-click below and in [`rdw-data-requests.md`](rdw-data-requests.md).
- [ ] Work through the prioritized request list in [`rdw-data-requests.md`](rdw-data-requests.md) (active; R0 to R11).
- [ ] Fill Tables 1 and 2 in `draft-v1.md`, run the H-U tests, write the abstract Results and Conclusions.
- [ ] Add formal citations for the Introduction (currently seed claims) and confirm whether an IRB determination is needed for the target conference.
- [x] Write hypotheses and map each to a data source and test (2026-11-26).
- [x] Pull and test public county data (PLACES, ACS, CHR&R; 82 counties) (2026-11-26).
- [x] Replace the old H90 ± H91 plan with H90.3 (the older plan text in `rdw-exploration-plan.md` is superseded by the banner at its top).

### Step 1 — done (2026-11-26)
Patients = **15,612** with Diagnosis Codes = H90.3 only. Encounters **[PENDING]** (optional; report the Encounters number from the same header if you still have the selection up).

### Step 2 — race breakdown (R1; do this next)
Keep H90.3 selected. Use only what you see on screen; if a box is named differently, tell me the name you see. Never report a count under 11; write `<11 (suppressed)`.
1. Confirm **Diagnosis Codes** still has only **H90.3** selected, and that the header still shows Patients = 15,612. Clear every other box.
2. In the **Race** box, select the first value (use the exact label shown, for example Black or African American). Read **Patients** in the header. Write down the label and the number.
3. Clear only the Race selection (H90.3 stays). Select the next Race value and read **Patients**. Repeat for every value listed in the Race box, including Unknown / Declined if shown.
4. Clear Race. Do the same once in the **Ethnicity** box (Hispanic or Latino / not), one value at a time.
5. Note whether **Multi-Racial** is a separate box and, if it is, its Patients count when selected (one value at a time).
6. Reply as lines like `Race value: Patients = ____`.

## File guide
- [`county-analysis.md`](county-analysis.md) — county-level methods, exact results, sources, caveats; data in [`data/ms_county_merged.csv`](data/ms_county_merged.csv); script [`data/build_and_analyze.py`](data/build_and_analyze.py)
- [`rdw-data-requests.md`](rdw-data-requests.md) — prioritized list of every UMMC Cohort Explorer number the paper needs (active)
- [`rdw-exploration-plan.md`](rdw-exploration-plan.md) — original cohort/variable plan (cohort and suppression updated by the banner at its top)
- `draft-v1.md` — working manuscript / abstract text, hypotheses, tables, notes
- `final.md` — polished version for submission (create when ready)
