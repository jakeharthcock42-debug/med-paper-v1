# Abstract review against the writing guide

**Date:** 2026-11-27  
**Scope:** Review dated 2026-11-27. Fixes below were applied the same day (Jake approved). Abstracts now live in Paper 01 `draft-v2.md` and Papers 02–04 `draft-v1.md`. No AAO-HNSF short version was written (**on hold per Jake 2026-11-27**).  
**Revised word counts (same method):** Paper 01 **391**; Paper 02 **370**; Paper 03 **299**; Paper 04 **312**. All ≤500 words including labels.  
**Guide:** [`guides/abstract-writing-guide.md`](abstract-writing-guide.md)  
**Versions scored:** Paper 01 conference abstract v2 in `papers/01-hearing-loss-disparities/draft-v2.md` (same text also appears in `draft-v1.md`; v2 is the latest file). Papers 02–04 draft-v1 abstracts in their paper folders (no later draft exists).

**Word-count method:** Whitespace-separated tokens after stripping markdown bold markers, including section labels, excluding the title. Character counts are the same text with whitespace collapsed to single spaces, including labels and spaces, for comparison with AAO-HNSF (1,800 characters for the four sections combined) and SGIM 2027 (3,000 characters including spaces for Background–Conclusions; [official page](https://annualmeeting.sgim.org/present/scientific-abstracts/), confirmed 2026-11-27). Paper 01’s draft header previously said 449 words; a direct token count of the pre-revision text was 378. The revised header uses the counted total.

All four abstracts are within the project standard of ≤500 words including labels. None currently fits AAO-HNSF’s 1,800-character limit without cutting. Paper 01 fits SGIM’s 3,000-character limit (2,673 characters) if no table or figure is added.

---

## Paper 01 — Hearing loss disparities

**Source:** `papers/01-hearing-loss-disparities/draft-v2.md`  
**Title (18 words):** Racial and Geographic Disparities in Documented Hearing Loss and Related Care at an Academic Medical Center in Mississippi  
**Words:** 378 (Background 37 / 10%; Methods 70 / 19%; Results 189 / 50%; Conclusions 82 / 22%)  
**Characters:** 2,673 (over AAO-HNSF by 873; under SGIM by 327)  
**Overall grade:** Needs minor fixes

### Strengths
- Results are densely quantified: denominators, RRs, risk difference, and 95% CIs for the primary Audiology contrast and the crude prevalence contrast; the Mantel-Haenszel estimates are reported after age and sex stratification.
- Conclusions stay with association language (“modestly less frequent”), refuse to treat Otolaryngology contact as an access measure, and list concrete limitations.
- County data are correctly labeled “ecological, not confirmatory,” and the primary hypothesis is stated in Methods.

### Fixes
1. **Pending result in a submission draft.** Phrase: “Rural residence remains [PENDING].” The guide forbids pending results in a submitted abstract. Cut this sentence until the pull is done, or complete R7/H-S3 first and then report the number.  
   **Applied 2026-11-27:** Sentence cut. Rural residence remains open as a paper-level gap (R7/H-S3), not in the abstract.
2. **Design is not named (STROBE 1(a)).** Phrase: “We analyzed de-identified UMMC Patient Cohort Explorer counts…” Suggested: “In this cross-sectional analysis of routinely collected data, we used de-identified [source] counts…” Move the window “1/1/2013–9/30/2026” from Results into Methods (RECORD 1.2).  
   **Applied 2026-11-27:** Design named; window moved into Methods. “UMMC” kept in the main version.
3. **Results lead with secondary county findings, not the primary Audiology hypothesis.** Phrase: “Age-adjusted hearing disability was higher in rural than non-rural counties (7.54% vs 6.91%; p = 1.5e-4; rho = 0.477)…” Open Results with the H90.3 cohort N and the Audiology contrast (already well reported later). Keep the county sentences as brief ecological context, and do not lead a contrast with a P value; add a 95% CI only if it is already in `county-analysis.md`.  
   **Applied 2026-11-27:** Results now open with the RDW and H90.3 cohort, then the Audiology contrast. County findings moved to the end and report the already-computed Welch 95% CI (difference 0.63 points, 0.28 to 0.98) instead of leading with p = 1.5e-4. No new CI was computed.
4. **“RDW” is never spelled out.** Phrase: “The unfiltered RDW included…” Suggested: “The unfiltered research data warehouse (RDW) included…”  
   **Applied 2026-11-27:** Spelled out at first use.
5. **Venue-specific, if submitting to SGIM or AAO-HNSF.** SGIM disqualifies abstracts that identify the institution; “UMMC Patient Cohort Explorer” and “UMMC-only capture” should become something like “an academic medical center in the Southern region.” AAO-HNSF needs the title cut from 18 words to 15 and the body cut from 2,673 to ≤1,800 characters.  
   **Applied in part 2026-11-27:** A SGIM note was added that a submission must remove institution identifiers; “UMMC” is kept in the main abstract. No separate AAO-HNSF 1,800-character short version was written (**on hold per Jake 2026-11-27**).

### [PENDING] gaps
Rural residence (in the abstract itself). Still open in the paper, not all in the abstract: R7/H-S3, R8 (diagnosis origin), male all-patients count, and an age-adjusted prevalence comparison.

---

## Paper 02 — Oral cavity and pharynx, breast, and colorectal cancer (merged)

**Source:** `papers/02-oral-pharynx-cancer-disparities/draft-v1.md`  
**Title (17 words):** Racial Disparities in Oral Cavity and Pharynx, Breast, and Colorectal Cancer in Mississippi: A Public-Data Ecological Analysis  
**Words:** 358 (Background 33 / 9%; Methods 85 / 24%; Results 186 / 52%; Conclusions 54 / 15%) — matches the draft’s own 358-word note  
**Characters:** 2,479 (over AAO-HNSF by 679; under SGIM by 521)  
**Overall grade:** Needs minor fixes

### Strengths
- The title names the design (“public-data ecological analysis”); Methods name sources, years, geography (Mississippi, 82 counties), and the analysis.
- Results carry rate ratios with intervals for the main oral-cavity and breast/colorectal mortality contrasts, and the conclusions include the ecological, hypothesis-generating caveat.
- The abstract uses the available room under 500 words to cover the merged cancer pair without feeling empty.

### Fixes
1. **Several contrasts are reported with a P value and no interval.** Phrases: “more late-stage diagnosis (73.1% vs 64.8%; approximate p<0.001)”; “median 14.6 vs 13.9; p=0.31”; “42% vs 41%; p=0.41.” Keep the two rates or medians; add a 95% CI only if it is already in the results tables; otherwise drop the isolated P value. The same applies to “incidence ratio 1.04,” which has no interval at all.  
   **Applied 2026-11-27:** Isolated p-values dropped; the two rates or medians were kept. An approximate 95% CI for the breast incidence ratio was computed from published rate CIs (130.6, 126.6–134.8 vs 125.5, 122.5–128.6) with the paper’s existing log-normal method: **1.04 (1.00–1.08)**. Calculation: [`papers/02-oral-pharynx-cancer-disparities/results/abstract-ci-breast-incidence-rr.md`](../papers/02-oral-pharynx-cancer-disparities/results/abstract-ci-breast-incidence-rr.md). No CI was added for late-stage percentages (only rounded reconstructed counts), metro/nonmetro medians, or Medicare mammography (no CI or usable counts in the repo).
2. **Conclusions reach past the data.** Phrase: “pointing to stage, treatment, and follow-up.” Treatment and follow-up were not measured. Suggested: “…is diagnosed later in Black residents despite lower incidence. Treatment and follow-up were not measured. County dental and primary care supply tracked stage.”  
   **Applied 2026-11-27:** Wording updated as suggested.
3. **Too many abbreviations** (NPCR, NCHS, USDA, HRSA, CDC, plus US). Spell out the first use of NPCR and NCHS, or drop the less essential acronyms.  
   **Applied 2026-11-27:** NPCR, NCHS, USDA, and HRSA spelled out at first use.
4. **Venue-specific:** over AAO-HNSF’s 1,800-character and 15-word-title limits if the oral-cavity half is submitted there. Live State Cancer Profiles values should be re-checked before submission (noted in the draft; not a wording defect).  
   **Not applied (venue version):** No AAO-HNSF short version was written (on hold per Jake 2026-11-27). SCP re-verification remains a pre-submission note, not a wording fix.

### [PENDING] gaps
None inside the abstract. Before submission: re-verify State Cancer Profiles on the live site (draft status).

---

## Paper 03 — Primary care supply and the Black–White premature-mortality gap

**Source:** `papers/03-primary-care-premature-mortality-gap/draft-v1.md`  
**Title (18 words):** Primary Care Physician Supply and the Black–White Gap in Premature Mortality Across Mississippi Counties: A Public-Data Ecological Analysis  
**Words:** 282 (Background 45 / 16%; Methods 80 / 28%; Results 122 / 43%; Conclusions 35 / 12%)  
**Characters:** 1,909 (over AAO-HNSF by 109; under SGIM by 1,091)  
**Overall grade:** Needs minor fixes

### Strengths
- Clear gap in Background, design named in the title, all 82 counties and data years in Methods, and adjustment variables listed.
- The headline regression results include 95% CIs and are framed as associations (“was associated with,” “strongest correlate”).
- Section balance is close to the guide’s practical allocation, and the ecological caveat is present. There is still room under 500 words to add intervals where they are missing.

### Fixes
1. **Descriptive contrasts lean on a P value or a ratio without an interval.** Phrase: “median 742 vs 601 per 100,000; p<0.001); statewide rates were 715 vs 550 (ratio 1.30).” Keep the 71-of-80 count and the medians; add a 95% CI for the ratio only if it is already computed in the results files.  
   **Applied 2026-11-27:** Kept “71 of 80 counties” and the medians 742 vs 601; kept statewide rates 715 vs 550; dropped p<0.001 and ratio 1.30 (no 95% CI or counts were in the repo).
2. **Conclusions overstate what an ecological model can say.** Phrase: “is not closed by greater physician supply.” Suggested: “was not narrower in counties with greater physician supply, which tracked White but not Black mortality.”  
   **Applied 2026-11-27:** Wording updated as suggested.
3. **Spell out or reduce abbreviations** (NCHS, HRSA, MD+DO, CDC, USDA). “US” and “PCP” if used should be clear on first mention (the abstract says “primary care physicians” in Methods, which is good).  
   **Applied 2026-11-27:** NCHS, HRSA, MD+DO, and USDA spelled out at first use.

### [PENDING] gaps
None in the abstract. The manuscript Methods still contain “[PENDING: IRB/RDW confirmation]”; that is outside the abstract, and Jake has already recorded that this database does not require IRB review.

---

## Paper 04 — Birth outcomes and obstetric access

**Source:** `papers/04-maternal-infant-outcomes/draft-v1.md`  
**Title (16 words):** Black–White Differences in Birth Outcomes and Obstetric Care Access Across Mississippi Counties: A Public-Data Ecological Analysis  
**Words:** 297 (Background 42 / 14%; Methods 67 / 23%; Results 136 / 46%; Conclusions 52 / 18%)  
**Characters:** 2,001 (over AAO-HNSF by 201; under SGIM by 999)  
**Overall grade:** Needs minor fixes

### Strengths
- Background opens with a specific, sourced fact (9.11 per 1,000 in 2022) and a clear gap.
- Results combine statewide rates, a 77-of-77 county contrast, and access denominators (55/82 counties, 37.5% of births) with adjusted estimates and 95% CIs for the obstetric-hospital tests.
- Conclusions stay cautious on the null hospital finding and include the ecological caveat.

### Fixes
1. **Some headline ratios and P values lack intervals.** Phrases: “infant mortality in 2022 was 12.1 vs 7.2 per 1,000 (rate ratio 1.68)”; “preterm birth in 2022–2024 was 18.5% vs 12.7%”; “median 17.9% vs 8.8%, p<0.001.” Keep the two rates; add 95% CIs only if they are already in the results tables.  
   **Applied 2026-11-27:** Kept the two rates and the county medians; dropped rate ratio 1.68 and p<0.001 (no 95% CIs or counts were in the repo).
2. **“Unrelated” is stronger than an R² of 0.04 really allows.** Phrase: “a gap of about 9 percentage points unrelated to county poverty, segregation, primary care supply, or rurality (R²=0.04).” Suggested: “a gap of about 9 percentage points that was not associated with county poverty, segregation, primary care supply, or rurality (R²=0.04).”  
   **Applied 2026-11-27:** Wording updated as suggested.
3. **Spell out OLS and SEs**, and expand OB-GYN at first use if the venue limits abbreviations.  
   **Applied 2026-11-27:** NCHS, HRSA, ordinary least squares (OLS), standard errors, and obstetrician-gynecologist (OB-GYN) spelled out at first use.

### [PENDING] gaps
None in the abstract. Same manuscript-level IRB note as Paper 03, outside the abstract.

---

## Cross-cutting notes

- All four already meet the project’s ≤500-word cap and, for Papers 02–04, already name an ecological design and include an individual-level-confirmation caveat.
- Papers 03 and 04 were drafted to an older ≤300-word target (282 and 297 words). They can take more of the 500-word allowance to add intervals and spell out abbreviations without new unsourced numbers.
- AAO-HNSF is mainly relevant to Papers 01 and 02 (hearing / head and neck). Both would still need a shorter title and a substantially shorter body to meet 1,800 characters. **Bookmarked, on hold (Jake 2026-11-27):** AAO-HNSF 1,800-character short version of Paper 01 (deadline Dec 16, 2026). Paper 01 keeps “UMMC” in the main abstract and now has a SGIM note that a submission must remove institution identifiers.
- Nothing was submitted. Jake submits after choosing a venue and applying that venue’s instructions.
