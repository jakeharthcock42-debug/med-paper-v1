# 01 — Hearing Loss Disparities

**Working title**: Racial and Geographic Disparities in Documented Hearing Loss and Related Care at UMMC / Across Mississippi Counties  
**Status**: Hypotheses written; county-level public-data tests complete; Step 1 done (H90.3 Patients = 15,612, 0.94% of RDW; Encounters = 4,244,868, 5.79%; window 1/1/2013–9/30/2026). R1 race percentages recorded (Black or African American 47.1%; White or Caucasian 49.9%); exact counts **[PENDING]**. Next: click Black, then White, and report the header Patients counts.  
**Data use**: Data use confirmed by Jake Harthcock 2026-11-26 per Cohort Explorer guide ([`../../data-use-rules.md`](../../data-use-rules.md)). The guide does not mention IRB review; whether the target conference requires an IRB determination is open (Jake to confirm).  
**Suppression rule**: never record a UMMC RDW cell under 11; write it as "<11 (suppressed)" (project rule), and hide any other cell that could be recovered by subtraction. The Explorer itself only allows report view/export when the population is greater than 25 (guide p. 20). Public county data are unaffected.  
**Cohort**: ICD-10 **H90.3** (sensorineural, bilateral), **15,612** patients (0.94% of RDW) and **4,244,868** encounters (5.79%), confirmed from a 2026-11-26 Cohort Explorer screenshot with only H90.3 selected in **Pt Diagnosis Codes (OR)** (Current Selections: `Pt_Dx_Code ORMode H90.3`). The dataset includes encounters between **1/1/2013** and **9/30/2026**. The Explorer allows one selection per filter box, so one code is used.  
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
- [x] **Step 1**: H90.3 Patients = **15,612** (0.94% of RDW); Encounters = **4,244,868** (5.79%); window 1/1/2013–9/30/2026 (screenshot, 2026-11-26; Pt Diagnosis Codes (OR) = H90.3 only). The 0.94% figure implies an RDW patient denominator; that exact total stays **[PENDING]** until R3 (do not back-calculate it).
- [x] **Step 2 / R1 percentages** (screenshot, 2026-11-26): Race box is on the **Data Filters** page → **Patient Demographics** tab → Demographic Search list → **Race** (dropdown shows % of the current H90.3 cohort). Black or African American **47.1%**; White or Caucasian **49.9%**. Full list in [`rdw-data-requests.md`](rdw-data-requests.md) R1. Exact counts **[PENDING]** (do not back-calculate them). Sex pie chart, same screen: Female **54.84%**, Male **45.16%** (counts **[PENDING]**).
- [ ] **Next (Jake, now)**: exact Patients counts for **Black or African American** and **White or Caucasian**. Click-by-click below.
- [ ] Work through the prioritized request list in [`rdw-data-requests.md`](rdw-data-requests.md) (active; R0 to R11).
- [ ] Fill Tables 1 and 2 in `draft-v1.md`, run the H-U tests, write the abstract Results and Conclusions.
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

The Patient Filters screen shows **Diagnosis / Procedures / Medications / Labs** tabs. The **Race** box is **not** on that screen. It is on the **Data Filters** page → **Patient Demographics** tab → Demographic Search list → **Race**. The Race dropdown shows each value’s percentage of the current (H90.3) cohort.

### Step 2 / R1 — percentages recorded (2026-11-26, screenshot)
Values exactly as displayed in the Race dropdown (H90.3 cohort, N = 15,612). Exact patient counts are **[PENDING]**; do not back-calculate them from these percentages. A displayed 0.0% implies fewer than 11 patients and is treated as `<11 (suppressed)`.

- (blank/unlabeled row) 0.0% → `<11 (suppressed)`
- American Indian or Alaska Native 0.2%
- Asian 0.5%
- Asian Indian 0.0% → `<11 (suppressed)`
- Black or African American 47.1%
- Hispanic 0.2%
- MS Band Choctaw Indian 0.2%
- Multiracial 0.4%
- Native Hawaiian or Other Pacific Islander 0.0% → `<11 (suppressed)`
- Other 1.1%
- Patient Refused 0.1%
- Unknown 0.2%
- White or Caucasian 49.9%

Grayed out (no patients in this selection): Chinese, Filipino, Guamanian or Chamorro, Japanese, Korean, Native Hawaiian, Other Pacific Islander, Samoan, Vietnamese.

Sex pie chart, same Patient Demographics screen: Female **54.84%**, Male **45.16%**. Exact counts **[PENDING]**; do not back-calculate them.

### Next — exact counts for Black and White
Keep H90.3 selected. Use only what you see on screen. Never report a count under 11; write `<11 (suppressed)`.
1. Confirm you are on the **Data Filters** page, **Patient Demographics** tab, and that **Pt Diagnosis Codes (OR)** still has only **H90.3** selected (header still Patients = 15,612; Encounters = 4,244,868).
2. In the **Race** box, click **Black or African American**. Write down the **Patients** number in the header.
3. Click **White or Caucasian** (this replaces the Black selection). Write down the **Patients** number in the header.
4. Reply as `Black or African American: Patients = ____ ; White or Caucasian: Patients = ____`.

## File guide
- [`county-analysis.md`](county-analysis.md) — county-level methods, exact results, sources, caveats; data in [`data/ms_county_merged.csv`](data/ms_county_merged.csv); script [`data/build_and_analyze.py`](data/build_and_analyze.py)
- [`rdw-data-requests.md`](rdw-data-requests.md) — prioritized list of every UMMC Cohort Explorer number the paper needs (active)
- [`rdw-exploration-plan.md`](rdw-exploration-plan.md) — original cohort/variable plan (cohort and suppression updated by the banner at its top)
- `draft-v1.md` — working manuscript / abstract text, hypotheses, tables, notes
- `final.md` — polished version for submission (create when ready)
