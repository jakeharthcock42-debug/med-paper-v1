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
├── data-use-rules.md                   ← Cohort Explorer user-guide rules, with page cites
├── PROJECT-HANDOFF.md                  ← this file
├── data/public/                        ← merged MS county public data + State Cancer Profiles extract (Papers 02–05)
├── scripts/public-data/                ← pipeline + analysis scripts for Papers 02–05
└── papers/
    ├── 02-oral-pharynx-cancer-disparities/     ← README, draft-v1, results/ (public data first pass done)
    ├── 03-primary-care-premature-mortality-gap/
    ├── 04-maternal-infant-outcomes/
    ├── 05-screening-gaps-cancer-stage/
    └── 01-hearing-loss-disparities/
        ├── README.md                   ← status, aims, hypotheses, next actions
        ├── draft-v1.md                 ← working manuscript (hypotheses in §2.2; abstract v2; Tables 1–3)
        ├── county-analysis.md          ← county-level public-data results (82 MS counties)
        ├── data/                       ← county files; r9_mh_analysis.py / r9_mh_results.md
        ├── rdw-data-requests.md        ← prioritized list of UMMC Explorer numbers (R0, R1, R4, R5, R9 done)
        └── rdw-exploration-plan.md     ← original query plan (cohort/suppression superseded by banner)
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
Among UMMC patients with ICD-10 H90.3, are Black patients less likely than White patients to have ≥1 Audiology-department encounter, and does that gap persist after age stratification? Otolaryngology contact is described as the diagnostic setting, not as an access measure. County-level hearing-disability estimates provide ecological context only.

### Current Cohort Definition (as of 26 Nov 2026)
- **Primary code:** ICD-10 **H90.3** (Sensorineural hearing loss, bilateral)
- **N:** **15,612 patients**, 4,244,868 encounters, window 1/1/2013–9/30/2026 (R0, screenshot 2026-11-26)
- **Why only one code?**  
  The Patient Cohort Explorer interface only allows **one selection per filter box**. It is not possible to multi-select codes within the same box (Diagnosis Codes OR, Diagnosis Name OR, etc.). H90.3 was chosen because it is the largest clean, clinically coherent single code.

Other codes explored earlier (single-select only):
- H90.5 ≈ 6,856
- H90.3 ≈ 15,612
- H90.0 ≈ 4,029

### Manuscript Status (`papers/01-hearing-loss-disparities/draft-v1.md`)
- Hypotheses tightened 2026-11-26 (Jake approved): one primary (H-U2, including persistence after age stratification); secondary H-S1, H-S2, H-S3; county associations are ecological context; ENT hypotheses H-U3/H-U4 retired after observing 96.74% Otolaryngology contact (revision log in §2.2).
- Conference abstract v2 (294 words) is in the draft. Tables 1–3 are populated for the completed UMMC pulls.
- Formal citations and the IRB question for the target conference remain [PENDING].

### Status as of 2026-11-26 (evening)
- **Data use**: Data use confirmed by Jake Harthcock 2026-11-26 per Cohort Explorer guide ([`data-use-rules.md`](data-use-rules.md)). The guide does not mention IRB; whether the target conference needs an IRB determination is open.
- **Suppression rule**: never record a UMMC RDW cell under 11 ("<11 (suppressed)"); app itself requires population >25 to view/export reports (guide p. 20). Public county data unaffected. The repo is public; committed UMMC aggregates are publicly readable.
- **Done (UMMC)**: R0 (N = 15,612; 4,244,868 encounters); R1 (FirstRace: White 8,597, Black 6,176, other/unknown 839); R4 Audiology (1,730/15,612, 11.08%; Black 630/6,176, 10.20% vs White 996/8,597, 11.59%; crude RR 0.880, 0.801–0.968, p = 0.008); R5 Otolaryngology 15,103/15,612 (96.74%), treated as a descriptive finding; R9 age-stratified Audiology (AgeKey = age at encounter). Mantel-Haenszel RR **0.812** (Greenland-Robins 95% CI 0.711–0.928; CMH p = 1.89e-5); sensitivity excluding 0–17: 0.810 (0.695–0.943). Details: `draft-v1.md` Table 3, `data/r9_mh_results.md`.
- **Done (public)**: county analysis for all 82 MS counties (PLACES 2025, ACS 2020–2024, CHR&R 2025): rural 7.54% vs 6.91%, p = 1.5e-4; see `county-analysis.md`. These are ecological context, not confirmatory.
- **Pediatric window**: resolved 2026-11-26. With race cleared, H90.3 + AgeKey 0–17 + Audiology: Patients 401 (0.02%), Encounters 868, window 9/3/2015–9/30/2026. Coding spans 2015–2026; the 3/2026 header with race selected was a display artifact. The 0–17 band stays in the primary MH estimate.
- **Still [PENDING]**: R3 (RDW base-population race, to finish H-S2); R7 (State/County field usability); R8 (diagnosis origin); formal citations; IRB for the target conference.

### Immediate Next Steps
1. Optional UMMC pulls: R3, R8, R7 field name, and H-S1 sex-stratified audiology (clicked counts, not pie-chart %).
2. Then draft-v2: Jake reviews the abstract; add formal citations; confirm IRB needs.

---

## 3b. Papers 02–05 — public-data first pass (added 2026-11-26)

Each folder has `README.md` (question, aims, hypotheses with planned tests and first-pass status, sources with years, limits, next actions, **ready-to-run UMMC RDW add-on**), `draft-v1.md` (cited intro skeleton, methods, empty results tables), and `results/` (full first-pass output + small county CSV). All numbers come from public aggregates (82 MS counties); nothing is estimated; unknowns are [PENDING]. UMMC add-ons are cleared by Jake (2026-11-26); UMMC cells under 11 are suppressed.

| # | Topic | Strongest first-pass finding (public data) |
|---|-------|--------------------------------------------|
| 02 | Oral cavity & pharynx cancer by race/rurality (ENT-adjacent) | MS Black NH incidence 9.5 vs White NH 15.6 per 100k (RR 0.61) but mortality 3.7 vs 3.5 (RR 1.06); late stage 73.1% vs 64.8%. County rural vs metro: no difference (54 of 82 counties published) |
| 03 | PCP supply, poverty, and the Black–White gap in premature mortality | Black higher than White premature mortality in 71 of 80 counties (median 742 vs 601 per 100k); PCP supply not independently associated once child poverty is in the model |
| 04 | Maternal/infant outcomes (LBW, teen births, infant mortality) | Black LBW higher than White in 77 of 77 counties (median 17.9% vs 8.8%); gap uniform across county contexts |
| 05 | Cancer screening gaps and stage (Delta/rural) | CHR Medicare mammography lower in Delta counties (40% vs 44%, p = 0.003) and higher with PCP supply; mammography inversely related to late-stage breast cancer (rho −0.331) |

Recommended order: 02 or 04 for the cleanest abstract, 03 as a primary-care-audience paper, 05 as a follow-on (see each README). Pipeline: `scripts/public-data/README.md`.

## 3c. Papers 02–05 — DECISION: public data only; draft-v1 abstracts written (2026-11-27)

**Decision (Jake, 2026-11-27):** Papers 02–05 are completed using **only publicly available data**; no UMMC/RDW pulls, because Jake is the bottleneck. Paper 01 continues with Jake separately. The UMMC add-on request lists from 3b are no longer requested; each paper README now has a **"Deferred / not used (UMMC RDW)"** section recording what was dropped and why. (They can be revived later if Jake chooses.)

Added public sources (see `data-sources.md` Tier 1d): HRSA AHRF 2024–2025 (OB-GYN, obstetric hospitals, midwives, preterm births, dentists, PCP, HPSA); CDC PLACES 2023 release (BRFSS 2020; dental visit, teeth lost, CRC screening, mammography); NCHS NVSR 73(5) infant mortality 2022; MSDH Child Death Review 2025; March of Dimes PeriStats preterm by race; NCHS VSRR 35. CDC WONDER state/county data are not available by API (national-only per CDC) and were not scripted; MSTAHRS is interactive and was not scripted (both optional manual follow-ups).

| # | Paper | Headline (public data) | Novelty (PubMed 2026-11-27) |
|---|-------|------------------------|------------------------------|
| 02 | Oral cavity & pharynx cancer by race/rurality | Black NH incidence 9.5 vs White 15.6/100k (RR 0.61) but mortality 3.7 vs 3.5 (RR 1.06), late stage 73.1% vs 64.8%; fewer dentists per 10k tracks higher late-stage share (rho −0.51, n = 34) | Moderate: no MS-specific oral cancer disparity paper found |
| 04 | Birth outcomes and obstetric access | Black LBW > White in 77/77 counties (median 17.9% vs 8.8%); 67% of counties have no obstetric hospital (37.5% of births); no adjusted association with preterm/LBW | Moderate: no county-level MS obstetric access analysis found |
| 03 | PCP supply and Black–White premature mortality | Black > White premature mortality in 71/80 counties (742 vs 601); PCP/10k −10.0 (−17.0, −2.9) for White vs +3.6 (−6.1, 13.3) for Black | **Partial overlap**: Lee 2026 (Prev Chronic Dis) covers MS county YPLL trends |
| 05 | Screening and stage (breast, CRC) | MS vs US CRC mortality 17.5 vs 12.7; Black/White breast mortality RR 1.43; county screening not associated with late stage after adjustment; PCP supply is | **Weak / low novelty**; several MS CRC and breast papers exist |

Each paper folder now has `README.md` (re-scoped aims, hypotheses with results, sources with data years, limits, Deferred section), `draft-v1.md` (conference-style abstract, intro, methods, results tables, discussion outline, verified references), and `results/` (including `*b_results.md`). All abstracts are draft-v1 for Jake's review; IRB/RDW determination still [PENDING].

---

## 4. Key Technical Constraints Discovered

**Patient Cohort Explorer (Qlik-based) limitations:**
- Only **one item can be selected at a time** in each filter box.
- Previous selections in the same box are replaced, not added.
- User can combine selections *across different boxes*, but not multiple values inside one box.
- This forced the pragmatic decision to proceed with a single high-yield code (H90.3) rather than the full H90 range.
- Cell suppression: record nothing under 11 for UMMC data ("<11 (suppressed)"); see status above.

When guiding Jake through the tool, give very concrete, sequential click-by-click instructions and ask him to report exact numbers or screenshots after each major step.

---

## 5. Important Data Sources

Full living catalog is in `data-sources.md`. Key ones currently in play:

- **UMMC Patient Cohort Explorer / RDW** (primary clinical data) — user runs all queries.
- CDC PLACES (county-level model-based hearing disability estimates; 2025 release pulled)
- County Health Rankings & Roadmaps
- American Community Survey disability tables (ACS 5-year 2020–2024 bulk files pulled; Census API needs a key)
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

## 7. Current Priority (as of 2026-11-26 evening)

**Highest priority:** Paper 01 abstract v2 is drafted with the crude and age-stratified audiology results. The pediatric Audiology coding-window check is done (9/3/2015–9/30/2026 with race cleared). Next: optional R3/R8/R7, then draft-v2 (Jake review, citations, IRB question).

Secondary priorities:
- Keep `data-sources.md` and this handoff file updated.
- Jake has not yet picked which of Papers 02–05 to start next (02, then 04, was recommended).
- Papers 02–05 draft-v1 abstracts (public data only) are ready for Jake's review (priority 02, 04; 03 has a novelty overlap; 05 is weak). See section 3c.

---

**End of handoff.**  
Any new GrokBot should treat this file + the existing files in the repository as the complete current state of the project and continue directly from the “Immediate Next Steps” listed above.
