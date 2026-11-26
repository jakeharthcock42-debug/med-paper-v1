# PROJECT HANDOFF — med-paper-v1

**Owner:** Jake Harthcock, medical student at University of Mississippi Medical Center (UMMC)  
**Date of handoff:** 26 November 2026  
**Purpose of this file:** Complete context dump so a new GrokBot (or any AI assistant) can immediately continue the project without prior conversation history.

---

## 1. Overall Goal

Jake wants to produce first-author abstracts and papers on **healthcare disparities in Mississippi**, suitable for local/regional conferences (UMMC Research Day, MAFP, ACP Mississippi chapter, etc.).

Key constraints and preferences:
- Use **existing data only** (no prospective collection).
- He has confirmed access to UMMC’s **Patient Cohort Explorer / Research Data Warehouse (RDW)** and can run any queries or exports needed.
- He cannot give the AI direct access to the RDW; he will run queries and paste aggregate results.
- He wants multiple potential papers managed cleanly as individual markdown files inside this repo, with draft → final versions (subfolders are preferred).

---

## 2. Repository Structure

**GitHub repo:** `jakeharthcock42-debug/med-paper-v1`

```
med-paper-v1/
├── README.md
├── data-sources.md                     ← living catalog of public + UMMC datasets
├── PROJECT-HANDOFF.md                  ← this file
└── papers/
    └── 01-hearing-loss-disparities/
        ├── README.md                   ← status, aims, next actions
        ├── draft-v1.md                 ← working manuscript (most developed file)
        └── rdw-exploration-plan.md     ← detailed query & analysis plan
```

Future papers should follow the same pattern:
```
papers/
  02-some-topic/
    README.md
    draft-v1.md
    final.md
```

---

## 3. Paper 01 — Hearing Loss Disparities (Currently Active)

### Working Title
Racial and Geographic Disparities in Documented Hearing Loss and Related Care at an Academic Medical Center in Mississippi

### Core Research Question
Among patients with documented hearing loss at UMMC, are there racial and/or geographic (rural) disparities in the utilization of audiology and otolaryngology (ENT) services? Place the findings in the context of Mississippi county-level hearing disability estimates.

### Current Cohort Definition (as of 26 Nov 2026)
- **Primary code:** ICD-10 **H90.3** (Sensorineural hearing loss, bilateral)
- **Approximate N:** **15,612 patients**
- **Why only one code?**  
  The Patient Cohort Explorer interface only allows **one selection per filter box**. It is not possible to multi-select codes within the same box (Diagnosis Codes OR, Diagnosis Name OR, etc.). H90.3 was chosen because it is the largest clean, clinically coherent single code.

Other codes explored earlier (single-select only):
- H90.5 ≈ 6,856
- H90.3 ≈ 15,612
- H90.0 ≈ 4,029

### Manuscript Status (`papers/01-hearing-loss-disparities/draft-v1.md`)
- Introduction is already written with solid literature backing (national prevalence, rural patterns, lower measured prevalence but lower treatment rates among Black patients, Mississippi disability context).
- Specific Aims drafted.
- Methods section drafted (includes the decision to use H90.3).
- Results section contains ready-to-populate tables.
- Early Discussion framing is present.

### Immediate Next Steps
1. With H90.3 still selected in Patient Cohort Explorer, extract the **Race** breakdown of the 15,612 patients.
2. Determine how many of these patients have ever had an **Audiology** encounter and/or an **Otolaryngology (ENT)** encounter, stratified by race.
3. Insert the numbers into `draft-v1.md`, calculate percentages, and draft the Results + Abstract.

---

## 4. Key Technical Constraints Discovered

**Patient Cohort Explorer (Qlik-based) limitations:**
- Only **one item can be selected at a time** in each filter box.
- Previous selections in the same box are replaced, not added.
- User can combine selections *across different boxes*, but not multiple values inside one box.
- This forced the pragmatic decision to proceed with a single high-yield code (H90.3) rather than the full H90 range.

When guiding Jake through the tool, give very concrete, sequential click-by-click instructions and ask him to report exact numbers or screenshots after each major step.

---

## 5. Important Data Sources

Full living catalog is in `data-sources.md`. Key ones currently in play:

- **UMMC Patient Cohort Explorer / RDW** (primary clinical data) — user runs all queries.
- CDC PLACES (county-level model-based hearing disability estimates)
- County Health Rankings & Roadmaps
- American Community Survey disability tables
- MSTAHRS (Mississippi vital statistics)
- State Cancer Profiles (for potential future papers)

---

## 6. Working Style Notes for Future GrokBots

- Jake is a busy medical student → keep instructions extremely concrete and sequential.
- Prefer updating the actual markdown files in the repo rather than only chatting.
- When he says “proceed”, advance the current paper or improve structure.
- He is happy to run RDW queries and paste aggregate counts/percentages.
- Maintain clean versioning: `draft-v1.md` → later `draft-v2.md` or move to `final.md` when ready for submission.
- Multiple papers should each live in their own numbered subfolder under `/papers`.

---

## 7. Current Priority (as of handoff)

**Highest priority:** Finish the core descriptive and disparity tables for Paper 01 (Race breakdown + Audiology/ENT utilization stratified by race) and turn them into a conference-ready abstract.

Secondary priorities:
- Keep `data-sources.md` and this handoff file updated.
- Be ready to spin up Paper 02 as soon as Jake names the next topic.

---

**End of handoff.**  
Any new GrokBot should treat this file + the existing files in the repository as the complete current state of the project and continue directly from the “Immediate Next Steps” listed above.
