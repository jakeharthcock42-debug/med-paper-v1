# RDW Hearing Loss Exploration & Correlation Plan

**Paper**: 01-hearing-loss-disparities  
**Goal**: Generate the core descriptive and correlational findings needed for the abstract / paper using Patient Cohort Explorer / RDW.

---

## 1. Cohort Definition (recommended starting point)

**Primary inclusion**  
Any patient with at least one diagnosis code in the H90 range (Conductive and sensorineural hearing loss) **or** selected H91 codes (Other hearing loss).

### Key ICD-10 codes to include
**H90 – Conductive and sensorineural hearing loss** (core)
- H90.0 Conductive, bilateral
- H90.1x Conductive, unilateral
- H90.2 Conductive, unspecified
- H90.3 Sensorineural, bilateral
- H90.4x Sensorineural, unilateral
- H90.5 Unspecified sensorineural
- H90.6 Mixed, bilateral
- H90.7x Mixed, unilateral
- H90.8 Mixed, unspecified
- H90.A series (with restricted contralateral hearing) if available

**H91 – Other hearing loss** (optional expansion)
- H91.0x Ototoxic
- H91.1x Presbycusis
- H91.2x Sudden idiopathic
- H91.3 Deaf nonspeaking
- H91.8x Other specified
- H91.9x Unspecified hearing loss / deafness NOS

**Practical tip**: In the Explorer, search for “hearing loss” or the parent codes H90 / H91 and include all child codes. Start with H90 only for a cleaner “diagnosed hearing loss” cohort; expand to H91 if numbers are small.

**Time window**: All available data, or most recent 5–7 years if the tool allows easy filtering.

---

## 2. Priority Variables to Extract / Tabulate

| Variable | Why it matters | Notes |
|----------|----------------|-------|
| Unique patient count | Denominator |  |
| Age (at first diagnosis or current) | Distribution & stratification | Mean/SD or median/IQR + age bands |
| Sex | Basic demographic |  |
| Race / Ethnicity | Primary disparity axis | Black, White, Other/Unknown at minimum |
| ZIP or County of residence | Geographic / rural disparity | Critical if available in de-id data |
| First diagnosis date (shifted) | Timing |  |
| Encounter type linked to diagnosis | Context | Outpatient, ED, Inpatient |
| Any audiology specialty encounter | Care process |  |
| Any otolaryngology (ENT) specialty encounter | Care process |  |
| Relevant procedures (if coded) | Care intensity | Audiometry, hearing aid related, etc. |
| Comorbidities (optional) | Risk profile | Diabetes, hypertension, smoking if easy |

---

## 3. Core Descriptive Tables (run these first)

**Table A – Overall cohort**
- Total N with hearing-loss diagnosis
- Age, sex, race/ethnicity distribution
- % with rural ZIP/county (if available)

**Table B – Stratified by race**
- N and % for Black vs White (vs Other)
- Age and sex within each race group

**Table C – Care utilization**
- Among patients with hearing-loss diagnosis:
  - % who ever had an audiology encounter
  - % who ever had an ENT encounter
  - % who had either
- Stratify the above by race (and by rurality if possible)

These three tables alone can support a solid abstract.

---

## 4. Correlation / Association Questions to Explore

Once the basic counts are in hand, examine:

1. **Race ↔ Documentation of hearing loss**  
   Is the proportion of Black vs White patients with a hearing-loss code different from the overall RDW racial distribution? (Suggests possible under- or over-documentation.)

2. **Race ↔ Specialty care**  
   Among those with a hearing-loss diagnosis, is the rate of audiology or ENT follow-up lower for Black patients than White patients?

3. **Geography ↔ Care**  
   Do patients from rural ZIPs/counties have lower rates of specialty encounters after diagnosis?

4. **Age ↔ Type of hearing loss** (if codes allow)  
   Sensorineural vs conductive distribution by age band.

5. **Intersection**  
   Race × rurality interaction on specialty utilization (even if only descriptive).

Simple chi-square or logistic regression (race as predictor of “had specialty visit”) can be done later in Excel/R/Python once you have the stratified counts or a limited export.

---

## 5. Suggested Query Sequence in Patient Cohort Explorer

1. Build cohort: Diagnosis contains H90* (or “hearing loss”).
2. Export or view demographic summary (age, sex, race).
3. Add filter or crosstab for race.
4. Identify patients with audiology or otolaryngology department/specialty encounters (how the Explorer exposes specialty may vary — look for department, provider specialty, or clinic name).
5. Create the utilization crosstabs (hearing loss + specialty visit, stratified by race).
6. If ZIP/county is available, repeat key stratifications by rural vs non-rural.

**Output preference**: Aggregate counts and percentages. Suppress or note any cell < 10.

---

## 6. How this feeds the paper

- Tables A–C → Results section and abstract.
- Correlation findings (especially race differences in specialty follow-up) → primary disparity message.
- Optional: Compare UMMC hearing-loss documentation rates or demographic mix against CDC PLACES county-level hearing disability estimates for Mississippi to add external context.

---

## Next immediate action

Run the cohort definition (H90 ± H91) and produce Tables A, B, and C. Paste the numbers here or into `draft-v1.md` and we will immediately turn them into polished results text and an abstract draft.
