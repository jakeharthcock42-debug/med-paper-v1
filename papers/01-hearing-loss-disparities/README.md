# 01 — Hearing Loss Disparities

**Working title**: Racial and Geographic Disparities in Documented Hearing Loss and Related Care at UMMC / Across Mississippi Counties  
**Status**: Hypotheses tightened 2026-11-26 (one primary: H-U2, including persistence after age stratification). County-level public-data associations are ecological context, not confirmatory. R0–R1 and R4–R5 done (H90.3 N = 15,612; White 8,597, Black 6,176, other/unknown 839). Primary H-U2 crude: 1,730/15,612 (11.08%); Black 630/6,176 (10.20%) vs White 996/8,597 (11.59%); RD −1.38 pp (95% CI −2.40 to −0.37); RR 0.880 (0.801–0.968), p = 0.008; age-adjusted (Mantel-Haenszel) RR **[PENDING]** (R9). Otolaryngology 15,103/15,612 (96.74%) is a descriptive finding (retired hypotheses H-U3, H-U4): H90.3 is diagnosed almost entirely in that setting. Conference abstract v1 (300 words) in [`draft-v1.md`](draft-v1.md). Next: **R9** (age-stratified audiology by race).  
**Data use**: Data use confirmed by Jake Harthcock 2026-11-26 per Cohort Explorer guide ([`../../data-use-rules.md`](../../data-use-rules.md)). The guide does not mention IRB review; whether the target conference requires an IRB determination is open (Jake to confirm).  
**Suppression rule**: never record a UMMC RDW cell under 11; write it as "<11 (suppressed)" (project rule), and hide any other cell that could be recovered by subtraction. The Explorer itself only allows report view/export when the population is greater than 25 (guide p. 20). Public county data are unaffected.  
**Cohort**: ICD-10 **H90.3** (sensorineural, bilateral), **15,612** patients (0.94% of RDW) and **4,244,868** encounters (5.79%), confirmed from a 2026-11-26 Cohort Explorer screenshot with only H90.3 selected in **Pt Diagnosis Codes (OR)** (Current Selections: `Pt_Dx_Code ORMode H90.3`). The dataset includes encounters between **1/1/2013** and **9/30/2026**. Race uses the **FirstRace** field (Data Filters → Patient Demographics → Race). Specialty use uses **Department Specialty** (Data Filters → Admissions & Visits → Encounter Search; Current Selections label **DepartmentSpecialty**; values **Audiology** and **Otolaryngology**); Data Filters selections are encounter-level (header Patients = H90.3 patients with ≥1 encounter in the selected department specialty). Age uses MinAge/MaxAge on Data Filters → Patient Demographics (“Enter Age, then Press Enter”; a chart is labeled “Age at Encounter” — confirm whether the filter is age at encounter). A State/County field has been seen on Patient Demographics; usability for rural classification is unconfirmed (R7). The Explorer allows one selection per filter box, so one code is used.  
**Primary data**: UMMC Patient Cohort Explorer / RDW (Jake runs all queries and pastes aggregates) + public county data (CDC PLACES, ACS, County Health Rankings)  
**Target**: Local/regional conference abstract (MAFP, ACP MS chapter, UMMC Research Day) → possible full paper later

## Specific aims
1. Test whether, among UMMC patients with documented H90.3, Black patients are less likely than White patients to have ≥1 Audiology-department encounter, and whether that difference persists after stratification by age group.
2. Secondarily, describe the cohort's race composition relative to the RDW base population, examine whether the audiology gap varies by sex, and, if a residence field can be used, compare audiology use for rural vs non-rural patients.
3. Place these findings in ecological context using county-level hearing-disability estimates (CDC PLACES, ACS, County Health Rankings), without treating those associations as confirmatory.

## Hypotheses (full null/alternative table, data sources, and tests in [`draft-v1.md`](draft-v1.md) §2.2)

**Primary (H-U2).** Among UMMC patients with ICD-10 H90.3, Black patients are less likely than White patients to have ≥1 Audiology-department encounter, and the difference persists after stratifying by age group (Mantel-Haenszel RR). **H0:** equal proportions overall and common RR = 1 after age stratification. **H1:** lower in Black patients, and the difference persists (MH RR < 1). **Rationale:** audiology is the gateway to hearing aids and cochlear implant evaluation; ENT contact alone does not capture hearing rehabilitation. Crude result **supported** (modest): 630/6,176 (10.20%) vs 996/8,597 (11.59%); RD −1.38 pp (95% CI −2.40 to −0.37); RR 0.880 (0.801–0.968); Pearson χ²(1) = 7.03, p = 0.008. Age-adjusted (Mantel-Haenszel) RR **[PENDING]** (R9).

**Secondary**

| ID | Hypothesis | Test / status |
|---|---|---|
| H-S1 | Sex-stratified or sex-adjusted audiology gap | **[PENDING]**; use header Patients counts, not pie-chart sex percentages. |
| H-S2 (formerly H-U1) | Black share of the H90.3 cohort differs from the Black share of the overall RDW population (lower predicted) | chi-square / two-proportion test. **Partial**: cohort split recorded (FirstRace): White 8,597 (55.1%), Black 6,176 (39.6%), other/unknown 839 (5.4%). RDW base-population race (R3) still **[PENDING]**. |
| H-S3 | Rural patients less likely than non-rural to have ≥1 Audiology-department encounter, only if a residence field can classify rural vs non-rural | chi-square, risk difference. A State/County field has been seen on Patient Demographics; exact label and usability **[PENDING]** (R7). |

**Exploratory / ecological context (public data; not confirmatory) — details in [`county-analysis.md`](county-analysis.md).** PLACES estimates are model-based and use ACS inputs, so associations with race, poverty, and insurance are partly built in.

| ID | Association | Result (PLACES age-adjusted % hearing disability, 82 counties) |
|---|---|---|
| H-C1 | Higher in rural counties | 7.54% (n = 66) vs 6.91% (n = 16), Mann-Whitney p = 1.5e-4; Spearman rho vs % rural = 0.477 |
| H-C2 | Associated with county % Black (negative expected) | rho = −0.321, p = 0.0033 |
| H-C3 | Higher with county poverty | Not supported: rho = 0.017, p = 0.88 |
| H-C4 | Higher with fewer PCPs per 100,000 | rho = −0.470, p = 8.5e-6 (confounded by rurality) |
| H-C5 | Higher with more uninsured (<65) | Partially supported: PLACES rho = 0.490, p = 3.0e-6; ACS direct rho = 0.178, p = 0.109 |

**Retired as hypotheses; retained as a descriptive finding.** H-U3 and H-U4 were retired after observing near-universal Otolaryngology contact (15,103/15,612, 96.74%; Black 6,062/6,176, 98.15%; White 8,229/8,597, 95.72%). H90.3 is diagnosed almost entirely within Otolaryngology, supporting ENT as the diagnostic setting and audiology as the care-gap measure. See the Hypothesis revision log in [`draft-v1.md`](draft-v1.md) §2.2 (records that the ENT outcome was dropped as a hypothesis after observing near-universal contact, to avoid the appearance of HARKing).

## Next actions
- [x] **Step 1**: H90.3 Patients = **15,612** (0.94% of RDW); Encounters = **4,244,868** (5.79%); window 1/1/2013–9/30/2026 (screenshot, 2026-11-26; Pt Diagnosis Codes (OR) = H90.3 only). The 0.94% figure implies an RDW patient denominator; that exact total stays **[PENDING]** until R3 (do not back-calculate it).
- [x] **Step 2 / R1 exact counts** (screenshots, 2026-11-26): Race box is on the **Data Filters** page → **Patient Demographics** tab → Demographic Search list → **Race**; Current Selections label is **FirstRace**. With H90.3 + one FirstRace value: White or Caucasian Patients = **8,597** (0.52% of RDW; 55.1% of 15,612), Encounters = **2,119,544** (2.89%); Black or African American Patients = **6,176** (0.37% of RDW; 39.6% of 15,612), Encounters = **2,000,250** (2.73%). Other/unknown combined = **839** (5.4%; 15,612 − 8,597 − 6,176). The Race dropdown percentages (Black 47.1%, White 49.9%) are encounter shares of the 4,244,868 cohort encounters (2,000,250 / 4,244,868 = 47.1%; 2,119,544 / 4,244,868 = 49.9%), not patient shares; small-group dropdown percentages are encounter shares only and are not converted to patient counts. Sex by race (pie chart with FirstRace selected): White Female 50.81%, Male 49.19%; Black Female 61.33%, Male 38.67%. Overall-cohort sex (no race selected): Female **54.84%**, Male **45.16%** (likely patient-based; pie chart basis unconfirmed). Exact overall and by-race sex counts **[PENDING]** (not back-calculated). The 0.52% and 0.37% figures imply RDW denominators; those exact totals stay **[PENDING]** until R3 (do not back-calculate them).
- [x] **R4 audiology** (screenshots, 2026-11-26): Field is **Data Filters** → **Admissions & Visits** → Encounter Search → **Department Specialty** (Current Selections: **DepartmentSpecialty**), value **Audiology**. Data Filters selections are encounter-level: header Patients = H90.3 patients with ≥1 Audiology-department encounter. H90.3 + Audiology: Patients = **1,730** (0.10% of RDW; **11.08%** of 15,612 = 1,730 / 15,612), Encounters = **3,808** (0.01%); window **6/26/2014–9/30/2026**. + FirstRace Black: Patients = **630** (0.04%; **10.20%** of 6,176 = 630 / 6,176), Encounters = **1,297**; Sex F 62.38%, M 37.62%; window 6/26/2014–9/30/2026. + FirstRace White: Patients = **996** (0.06%; **11.59%** of 8,597 = 996 / 8,597), Encounters = **2,295**; Sex F 53.41%, M 46.59%; window 7/5/2014–9/30/2026. Other/unknown combined with audiology = **104** of 839 (**12.40%**), computed as 1,730 − 630 − 996. Black vs White: RD (Black − White) **−1.38** percentage points (Wald 95% CI **−2.40 to −0.37**); RR **0.880** (Katz log-Wald 95% CI **0.801–0.968**); Pearson χ²(1) = **7.03**, p = **0.008**; OR **0.867** (95% CI **0.780–0.963**). The 0.10%, 0.04%, 0.06%, and 0.01% of RDW figures are recorded as displayed; do not back-calculate an RDW denominator from them. Caveats: Audiology department data appear only from mid-2014 while the cohort window starts 1/1/2013; “ever” audiology is UMMC only; H90.3 may be coded at audiology visits (R8).
- [x] **R5 ENT** (screenshots, 2026-11-26): Department Specialty value **Otolaryngology**; window **1/1/2013–9/30/2026**. H90.3 + Otolaryngology: Patients = **15,103** (0.91% of RDW; **96.74%** of 15,612 = 15,103 / 15,612), Encounters = **295,604** (0.40%). + FirstRace Black: Patients = **6,062** (0.37%; **98.15%** of 6,176 = 6,062 / 6,176), Encounters = **116,299** (0.16%); Sex F 61.56%, M 38.44%. + FirstRace White: Patients = **8,229** (0.50%; **95.72%** of 8,597 = 8,229 / 8,597), Encounters = **164,567** (0.22%); Sex F 51.06%, M 48.94%. Other/unknown combined with Otolaryngology = **812** of 839 (**96.78%**), computed as 15,103 − 6,062 − 8,229. Black vs White: RD (Black − White) **+2.43** percentage points (Wald 95% CI **1.89 to 2.98**); RR **1.025** (Katz log-Wald 95% CI **1.020–1.031**); Pearson χ²(1) = **67.50**, p = **2.11e-16**; OR **2.378** (Woolf 95% CI **1.922–2.942**). Direction is opposite the pre-specified alternative, but “ever ENT” is near-universal by construction and is not a valid access measure (circularity; R8). The 0.91%, 0.37%, 0.50%, 0.40%, 0.16%, and 0.22% of RDW figures are recorded as displayed; do not back-calculate an RDW denominator from them.
- [x] **Conference abstract v1** drafted in [`draft-v1.md`](draft-v1.md) (300 words, body only) using only reported counts and computed stats; reframed 2026-11-26 to match the tightened hypotheses (age-adjusted RR [PENDING]).
- [x] **Hypotheses tightened** 2026-11-26 (Jake approved): one primary (H-U2 + age stratification); ENT hypotheses retired as hypotheses after observing near-universal contact (revision log in `draft-v1.md`).
- [ ] **Next: R9** — age-stratified audiology by race (Mantel-Haenszel RR for the primary hypothesis). Click-by-click below and in [`rdw-data-requests.md`](rdw-data-requests.md).
- [ ] Later / optional: R3 (RDW base-population race, needed to finish H-S2); R8 (diagnosis origin); H-S1 sex-stratified audiology (clicked sex counts, not pie-chart %); R7 (confirm State/County usability); R6, R10, R11.
- [ ] Add formal citations for the Introduction (currently seed claims), review the conference abstract in `draft-v1.md`, and confirm whether an IRB determination is needed for the target conference.
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

### R4 — done (2026-11-26, screenshots)
Field: **Data Filters** → **Admissions & Visits** → Encounter Search → **Department Specialty** (Current Selections label **DepartmentSpecialty**), value **Audiology**. Data Filters selections are encounter-level: the header Patients count is H90.3 patients with ≥1 Audiology-department encounter.

- H90.3 + Audiology: Patients = **1,730** (0.10% of RDW; 1,730 / 15,612 = **11.08%**), Encounters = **3,808** (0.01%); encounter window **6/26/2014–9/30/2026**.
- + FirstRace Black or African American: Patients = **630** (0.04%; 630 / 6,176 = **10.20%**), Encounters = **1,297**; Sex Female **62.38%**, Male **37.62%**; window **6/26/2014–9/30/2026**.
- + FirstRace White or Caucasian: Patients = **996** (0.06%; 996 / 8,597 = **11.59%**), Encounters = **2,295**; Sex Female **53.41%**, Male **46.59%**; window **7/5/2014–9/30/2026**.
- Other / unknown combined with audiology: Patients = **104** of 839 (**12.40%**), computed as 1,730 − 630 − 996. Reported as one combined row only.

Black vs White (2×2: 630 vs 5,546 without; 996 vs 7,601 without). Risk difference (Black − White) = **−1.38** percentage points (Wald 95% CI **−2.40 to −0.37**). Risk ratio = **0.880** (Katz log-Wald 95% CI **0.801–0.968**). Pearson χ²(1) = **7.03**, p = **0.008**. Odds ratio = **0.867** (Woolf 95% CI **0.780–0.963**). H-U2 is supported (Black patients less likely to have ≥1 Audiology-department encounter); the absolute difference is modest. Caveats: Audiology department data appear only from mid-2014, while the H90.3 cohort window starts 1/1/2013; “ever” audiology is a UMMC visit only (outside care is not captured); H90.3 may be coded at audiology visits (circularity; request R8). The 0.10%, 0.04%, 0.06%, and 0.01% of RDW figures are recorded as displayed; do not back-calculate an RDW denominator from them.

### R5 — done (2026-11-26, screenshots)
Field: **Data Filters** → **Admissions & Visits** → Encounter Search → **Department Specialty** (Current Selections label **DepartmentSpecialty**), value **Otolaryngology**. Data Filters selections are encounter-level: the header Patients count is H90.3 patients with ≥1 Otolaryngology-department encounter. Encounter window with this selection: **1/1/2013–9/30/2026** (the full cohort window).

- H90.3 + Otolaryngology: Patients = **15,103** (0.91% of RDW; 15,103 / 15,612 = **96.74%**), Encounters = **295,604** (0.40%).
- + FirstRace Black or African American: Patients = **6,062** (0.37%; 6,062 / 6,176 = **98.15%**), Encounters = **116,299** (0.16%); Sex Female **61.56%**, Male **38.44%**.
- + FirstRace White or Caucasian: Patients = **8,229** (0.50%; 8,229 / 8,597 = **95.72%**), Encounters = **164,567** (0.22%); Sex Female **51.06%**, Male **48.94%**.
- Other / unknown combined with Otolaryngology: Patients = **812** of 839 (**96.78%**), computed as 15,103 − 6,062 − 8,229. Reported as one combined row only.

Black vs White (2×2: 6,062 vs 114 without; 8,229 vs 368 without). Risk difference (Black − White) = **+2.43** percentage points (Wald 95% CI **1.89 to 2.98**). Risk ratio = **1.025** (Katz log-Wald 95% CI **1.020–1.031**). Pearson χ²(1) = **67.50**, p = **2.11e-16**. Odds ratio = **2.378** (Woolf 95% CI **1.922–2.942**). The pre-specified alternative (lower in Black patients) is not supported; the difference runs in the opposite direction. This is **not a valid access measure**: 15,103/15,612 (96.74%) had ≥1 Otolaryngology-department encounter, so “ever ENT” is near-universal by construction and indicates that H90.3 is predominantly coded or diagnosed within Otolaryngology (circularity; request R8). H-U3 and H-U4 were later retired as hypotheses (2026-11-26 revision log); this Otolaryngology result is retained as a descriptive finding about the diagnostic setting. Audiology (H-U2) is the primary utilization outcome. The 0.91%, 0.37%, 0.50%, 0.40%, 0.16%, and 0.22% of RDW figures are recorded as displayed; do not back-calculate an RDW denominator from them.

### Next — R9: age-stratified audiology by race (primary hypothesis)

Needed for the age-adjusted (Mantel-Haenszel) risk ratio. Keep H90.3 selected throughout. Do not use audiology-or-ENT. Full click-by-click is also in [`rdw-data-requests.md`](rdw-data-requests.md).

1. Keep H90.3 selected in Diagnosis Codes. Clear Race and Department Specialty so the header returns to 15,612 patients.
2. Go to **Data Filters → Patient Demographics**. Find the control labeled **“Enter Age, then Press Enter”** with **MinAge** and **MaxAge** fields (seen on this screen).
3. Confirm, and tell me, whether Age on this screen is age at encounter. A chart on the same screen is labeled **“Age at Encounter”**; if the filter uses encounter age, a patient could fall into more than one band. Note what you observe (do not assume).
4. Use these bands, entering MinAge and MaxAge and pressing Enter for each:
   - **0–17:** MinAge 0, MaxAge 17
   - **18–44:** MinAge 18, MaxAge 44
   - **45–64:** MinAge 45, MaxAge 64
   - **65+:** MinAge 65. If a MaxAge is required, enter a high upper bound (for example 120) and tell me exactly what you entered.
5. For each band, record the header **Patients** number for all six combinations (24 counts total):
   - (a) no Race and no Department Specialty
   - (b) FirstRace = **Black or African American**, no Department Specialty
   - (c) FirstRace = **White or Caucasian**, no Department Specialty
   - (d) no Race + Department Specialty = **Audiology** (Admissions & Visits tab)
   - (e) FirstRace = Black + Department Specialty = Audiology
   - (f) FirstRace = White + Department Specialty = Audiology
6. One selection per box. After each band, clear MinAge/MaxAge (and Race / Department Specialty) before the next band. Keep H90.3 throughout.
7. If any Patients count is under 11, write “under 11” (do not report the number). If a complementary cell could be recovered by subtraction, also suppress that cell.
8. Reply as a compact table: band, setting, Patients.

If convenient, also send the exact name of the State/County field on Patient Demographics (for later R7); do not start pulling county counts yet.

Later / optional: **R3** (clear all filters; total RDW Patients and Encounters, then FirstRace = Black and White; needed to finish H-S2; do not back-calculate from percentages); **R8** (diagnosis origin / circularity); **H-S1** sex-stratified audiology (clicked sex counts, not pie-chart %).

## File guide
- [`county-analysis.md`](county-analysis.md) — county-level methods, exact results, sources, caveats; data in [`data/ms_county_merged.csv`](data/ms_county_merged.csv); script [`data/build_and_analyze.py`](data/build_and_analyze.py)
- [`rdw-data-requests.md`](rdw-data-requests.md) — prioritized list of every UMMC Cohort Explorer number the paper needs (active)
- [`rdw-exploration-plan.md`](rdw-exploration-plan.md) — original cohort/variable plan (cohort and suppression updated by the banner at its top)
- `draft-v1.md` — working manuscript / abstract text, hypotheses, tables, notes
- `final.md` — polished version for submission (create when ready)
