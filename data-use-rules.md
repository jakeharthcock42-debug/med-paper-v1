# UMMC Patient Cohort Explorer — data-use rules

Extracted from the 24-page *Patient Cohort Explorer* user guide (PowerPoint PDF). Nothing below is inferred as a rule unless the guide states it. Quotes are exact, including original capitalization, punctuation, and grammar.

**Source file:** user-provided PDF, filename as attached by Jake Harthcock.

**PDF metadata (not printed on the slides):**

- Title: Research Data warehouse
- Author: Rhushell Moore
- Creator/Producer: Microsoft PowerPoint 2016
- Creation date: 20 August 2018, 9:46 AM CDT
- Modification date: 21 October 2022, 10:13 AM CDT
- Pages: 24
- No version number, document date, or formal policy title appears on the slides themselves.

This document is a how-to user guide, not a standalone data-use policy or IRB determination. Several topics that matter for conference abstracts are simply not addressed in the guide itself (see the lists at the end). Official citation and human-protection language from a separate UMMC internal page are recorded in the addendum below (provided by Jake Harthcock, 2026-11-27).

---

## 1. Permitted uses (feasibility vs. research vs. publication)

The guide describes the application's purpose. It does not define “feasibility,” “research,” or “publication,” and it does not say whether counts may be presented or published.

> “The Patient Cohort Explorer contains de-identified data from UMMC's Research Data Warehouse. This application is designed to support rapid querying and reporting to discover patient and encounter populations.”
>
> — page 3, under “Purpose and Overview”

> “Audience: Researchers, Providers, and Students”
>
> — page 3

> “The UMMC Patient Cohort Explorer dashboard is a constant evolution. Whether it be sheer amounts of data (patients/visits), types of data (labs/meds) or organization of data (ICD10/SNOMED), there is a constant flow of change meant to improve upon the types of research related questions that can be solved.”
>
> — page 4, under “DATA SPECIFICS”

The only place the guide distinguishes “research” from “non-research” is in the REDCap request workflow for data *outside the scope* of the Patient Cohort Explorer (not for ordinary on-screen counts). Two buttons appear in the page 23 screenshot: “REDCap Non-Research Data Request” and “REDCap Research Data Request.” See section 6.

Data domains listed on page 4: Demographic, Diagnosis, Lab, Medication, Procedure, Emergency Department, Admission & Visit Detail.

---

## 2. IRB approval or determination

**The user guide is silent.** It never mentions the IRB, an IRB determination, protocol review, or any approval required before querying, reporting, presenting, or publishing.

**Addendum (UMMC internal guidance, not from the user guide).** On 2026-11-27, Jake Harthcock provided the official citation and the suggested human-protection boilerplate from the UMMC Center for Informatics and Analytics internal Patient Cohort Explorer page. The DOI `https://doi.org/10.6084/m9.figshare.12252737` resolved (HTTP 302) to the figshare software record `https://figshare.com/articles/software/Patient_Cohort_Explorer/12252737` (figshare API: title “Patient Cohort Explorer (PCE)”; published 2020-09-15; unversioned DOI as cited below). This is the standard citation and manuscript language for any RDW / Patient Cohort Explorer paper in this project.

**Citation (use this form):**

University of Mississippi Medical Center, Center for Informatics and Analytics (2020): Patient Cohort Explorer. figshare. Software. https://doi.org/10.6084/m9.figshare.12252737

**Suggested boilerplate (quote verbatim when a human-protection statement is required):**

> The data warehouse from which the information for this study is derived has been de-identified and date-shifted so that it does not include any protected health information (PHI). Pursuant to 45 CFR 46, use of this database does not meet the definition of human subjects’ research and does not require IRB review.

The boilerplate states that the warehouse is de-identified and date-shifted and contains no PHI, and that use of the database is not human subjects’ research and does not require IRB review. Because the data are date-shifted, displayed calendar dates and windows may not correspond to true calendar dates. Do not claim that within-patient intervals are preserved unless a source states that.

---

## 3. Minimum cell size and small-number suppression

The only numeric threshold in the guide applies to *creating, viewing, and exporting reports*, not to the header patient/encounter counts that update as filters are applied.

Slide text:

> “Based on selected criteria the option to create a report will appear if the patient population is greater than 25.”
>
> — page 20, under “CREATE A REPORT”

On-screen banner in the page 20 screenshot (red box, yellow highlight):

> “Population must be greater than 25 patients to view and export reports.”
>
> — page 20, application screenshot

The guide does not say:

- whether header counts (the “Patients” / “Encounters” totals shown while filtering) are suppressed below 25;
- whether individual cells in a cross-tab (for example, a race breakdown) are suppressed;
- whether a threshold other than 25 (including 11) applies.

Pages 12–15 show header counts of 93, 97, and 77 patients as filters are applied, and they state that report creation becomes available “upon criteria completion.” Those examples are all above 25. The guide does not discuss counts at or below 25 except in the report-creation messages above.

Related how-to language (not a suppression rule):

> “The header label displays counts as the criteria is selected.”
>
> — pages 13 and 15

> “Note: Header label patient and encounter counts may increase or decrease as selections are made.”
>
> — pages 13 and 14 (page 14 punctuation: “Header label;”)

> “Upon criteria completion, report creation is available.”
>
> — pages 12 and 14

---

## 4. De-identified vs. identified / limited data

> “The Patient Cohort Explorer contains de-identified data from UMMC's Research Data Warehouse.”
>
> — page 3

The guide does not define “de-identified,” does not mention HIPAA, a limited data set, or a data-use agreement, and does not list which identifiers are removed.

The page 21 screenshot of a built report (“Patient Details”) shows row-level records with columns including **Pt. Key**, **EncounterKey**, **Age**, **Sex**, **Tobacco**, **DxGroup**, and **Med Name**. The visible keys are numeric codes, not names or medical-record numbers. The guide still calls the data de-identified and does not further classify this table.

Filter fields visible in screenshots include Sex, Ethnicity, Race, Multi-Racial, Preferred Language, Smoking Status, State, Country, Age, and (on the Admissions & Visits tab) Primary Financial Class, among others (pages 16–17). These are listed as available filters, not as a data-classification rule.

---

## 5. Exporting, printing, and report creation

Report creation, viewing, and export are offered inside the application once the patient population is greater than 25 (see section 3).

> “Print, Export, Send to Excel”
>
> — page 21, annotation pointing to printer and Excel icons on a “Patient Details” table

Page 22 is a how-to slide (“Click Create Report”) and shows “Hide Table,” “Change Selections,” and “Exit Application” controls. It states no further restriction on what may be done with a created report.

For a REDCap request for data *outside the scope* of the Explorer, the page 23 screenshot includes these on-screen instructions (not extracted by text tools; transcribed from the slide image):

> “INSTRUCTIONS”
>
> “Step 1: Export and save the table to your network drive (U: Drive). To do so, click XL in the top right of the table or right click and select Send to Excel.”
>
> “Step 2: Once the file is saved, click the appropriate REDCap data request button below and complete the required fields.”
>
> “Step 3: Upload your saved file using the Upload document link.”
>
> — page 23, application screenshot

The U: Drive instruction appears only in that data-request workflow. The guide does not state a general rule that every export, screenshot, or handwritten/pasted count must be stored on the U: Drive.

---

## 6. Data outside the scope of the Patient Cohort Explorer

> “To request data outside the scope of the Patient Cohort Explorer, submit a REDCap data request here.”
>
> — page 23, under “Data Request”

> “Select here and complete. The data request receives a priority number assigned by an Honest Broker/Analyst.”
>
> — page 23

The page 23 screenshot shows two buttons:

- “REDCap Non-Research Data Request”
- “REDCap Research Data Request”

The guide does not define “outside the scope,” and it does not say that ordinary aggregate counts taken from the Explorer itself require a REDCap request.

---

## 7. Storage

The only storage instruction is the U: Drive step in the REDCap data-request workflow on page 23 (quoted in section 5). The guide is otherwise silent on where exports, notes, or counts may be stored.

---

## 8. Screenshots

**The guide is silent.** It neither permits nor forbids screenshots. (The guide itself is built largely from application screenshots.)

---

## 9. Sharing with others, or use outside UMMC

**The guide is silent.** It does not say whether counts, exports, or reports may be shared with collaborators, students, or people outside UMMC, or placed in a repository, email, or other system off the UMMC network.

---

## 10. Use of outside or cloud tools, or AI

**The guide is silent.**

---

## 11. Citation or acknowledgment

**The user guide is silent.** It does not provide a required citation, acknowledgment, or disclaimer for abstracts, posters, or papers. The official citation and human-protection boilerplate from the UMMC internal page are in the section 2 addendum.

Developer credited on page 3 (not framed as a citation requirement):

> “Developer: Joshua Lester, Center for Informatics and Analytics”

---

## 12. Access and login

Access is described as starting on the UMMC intranet, then opening the application through the QlikView Access Point.

> “ACCESSING PATIENT COHORT EXPLORER”
>
> “UMMC INTRANET”
>
> “RESEARCH”
>
> “CENTER FOR INFORMATICS & ANALYTICS”
>
> “QLIKVIEW ACCESS POINT (LEFT COLUMN)”
>
> “PATIENT COHORT EXPLORER”
>
> — page 2

> “RECOMMENDED BROWSERS - GOOGLE CHROME OR INTERNET EXPLORER”
>
> — page 2

> “QlikView Access Point: http://ntqvcl/qlikview/index.htm”
>
> — page 24

The host `ntqvcl` is an internal name, consistent with intranet-only access. The guide does not mention VPN, off-campus access, usernames, passwords, multi-factor authentication, or who is eligible to request an account. Eligibility is implied only by the audience line on page 3 (“Researchers, Providers, and Students”).

---

## 13. Who to contact, and additional guides

> “CIA-RDWTeam@umc.edu”
>
> “Patient Cohort Explorer Team”
>
> “Center for Informatics and Analytics”
>
> “Website: https://intranet.umc.edu/Research/Centers and Institutes/Center for Informatics and Analytics/Center for Informatics and Analytics.html”
>
> “QlikView Access Point: http://ntqvcl/qlikview/index.htm”
>
> — page 24

The URL on page 24 is quoted with the spaces as printed on the slide.

The page 5 landing-page screenshot also says:

> “For additional information and training guides, please visit the Patient Cohort Explorer website.”
>
> “https://intranet.umc.edu/sites/Research/cia/Pages/Patient-Cohort-Explorer.aspx”
>
> — page 5, application screenshot (this URL was not in the PDF’s extractable text)

An Honest Broker/Analyst is named only as the person who assigns a priority number to a REDCap data request (page 23).

---

## 14. How filters work (operational, not data-use policy)

Included because the guide states what population a query actually returns.

From the page 5 landing-page screenshot, repeated in part on pages 6–8:

> “These filters allow advanced AND/OR/NOT searches at the patient level. The result is a patient population where the selections occurred for individual patients regardless of encounter or time. All encounters associated with these patients will be available for further analysis.”
>
> — pages 5 and 6, “Patient Filters”

> “These filters allow advanced AND/OR/NOT searches at the encounter level. The result is an encounter population where the selections occurred for individual encounters. All data associated with these encounters will be available for further analysis.”
>
> — pages 5 and 7, “Encounter Filters”

> “If an advanced filter is not needed at either the patient or the encounter level, please proceed directly to the standard data filters.”
>
> — pages 5 and 8

Slide explanations:

> “The Patient Level Filters returns ONLY patients for the selected criteria and ALL encounters related to those patients. (All criteria is not necessarily on the same encounter)”
>
> — page 6

> “The Encounter Level Filters return ONLY encounters for the selected criteria and ALL data related to those encounters. (All criteria is on the same encounter)”
>
> “* All information related to these encounters is still available for reporting”
>
> — page 7

> “The Data Level Filters return ONLY encounter data for the selected criteria to refine your population for specific report building. (All criteria is on the same encounter)”
>
> “* Only the ADHD Diagnosis Group is available for reporting.”
>
> — page 8 (the ADHD clause is the worked example on that slide)

Pages 9–18, 19, and 22 are navigation and report-building how-to (color scheme, wildcards, Boolean “Or,” drill-down, prefill of associated fields). They contain no additional data-use restrictions.

---

## Not addressed in the guide

The guide is silent on all of the following:

- Whether IRB approval or an IRB determination is required before querying, using, presenting, or publishing Cohort Explorer counts — **the user guide is silent; the 2026-11-27 internal-page boilerplate (section 2 addendum) states that use of this database does not meet the definition of human subjects’ research and does not require IRB review**
- Whether aggregate counts from the Explorer may appear in a conference abstract, poster, talk, or paper
- Any distinction among feasibility use, research use, and publication/presentation use of counts taken *from the Explorer itself* (the Research vs. Non-Research buttons apply only to REDCap requests for data outside its scope)
- Small-cell suppression for on-screen header counts, or for individual cells in a breakdown (race, sex, age, etc.)
- Any minimum cell size other than the “greater than 25” threshold for viewing and exporting *reports*
- A definition of “de-identified,” HIPAA classification, limited data set, or a data-use agreement
- Screenshots of the application or of counts
- Where ordinary notes, pasted counts, or exports may be stored, other than the U: Drive step in the REDCap data-request workflow
- Sharing data or counts with collaborators, people outside UMMC, or systems off the UMMC network (including email, cloud storage, or a GitHub repository)
- Use of outside computers, cloud tools, or AI assistants
- Required citation, acknowledgment, or disclaimer language — **the user guide is silent; the official citation and boilerplate are in the section 2 addendum**
- Off-campus or VPN access, account eligibility, or login/credential rules
- Whether counts or exports may leave the UMMC intranet
- A formal data-use policy, terms of use, or user attestation

---

## Open questions for UMMC research IT / IRB

Ask the Patient Cohort Explorer Team (`CIA-RDWTeam@umc.edu`) and, as needed, the UMMC IRB. This user guide alone does not answer them.

1. **Conference abstracts and papers.** May a student investigator put Patient Cohort Explorer aggregate counts (for example, an H90.3 cohort total and a race breakdown of audiology/ENT use) into a local conference abstract, poster, or paper? Is that treated as feasibility only, or as research requiring IRB review or a determination first? **Update 2026-11-27:** the internal page provides suggested human-protection language “for the manuscript” and for “the journal in which you are publishing,” which contemplates publication. It does not separately name conference abstracts. The boilerplate states that use of the database is not human subjects’ research and does not require IRB review.

2. **IRB path.** If review is required, what is the correct path (not human-subjects research; exempt; expedited; full board)? Does the “de-identified data” statement on page 3 change that? **Answered 2026-11-27 (internal page, section 2 addendum):** use of this database does not meet the definition of human subjects’ research and does not require IRB review (45 CFR 46).

3. **Cell size.** The application blocks report view/export unless the patient population is greater than 25. Does a cell-size rule also apply to header counts, to subgroup cells (race, etc.), and to numbers written into an abstract? Is there a different threshold (including 11) in a policy this guide does not include?

4. **Sharing and storage off the UMMC network.** May those aggregate counts be pasted into a private GitHub repository, a local draft, or an email? Must working notes stay on the U: Drive or another UMMC system?

5. **Outside / cloud / AI tools.** May a student share aggregate, non-row-level counts with an AI assistant running on a computer outside UMMC, solely to help draft a manuscript? The guide does not mention this. Does any other CIA or IRB policy forbid it?

6. **Row-level exports.** Page 21 shows a “Patient Details” table with Pt. Key, EncounterKey, Age, Sex, and clinical fields, which can be printed or sent to Excel when n > 25. Are those exports still considered de-identified, and may they leave the UMMC network? (The current project plan is to use aggregate counts only, not row-level exports.)

7. **Citation.** Is there required acknowledgment language for the Research Data Warehouse, Patient Cohort Explorer, or Center for Informatics and Analytics? **Answered 2026-11-27 (internal page, section 2 addendum):** University of Mississippi Medical Center, Center for Informatics and Analytics (2020): Patient Cohort Explorer. figshare. Software. https://doi.org/10.6084/m9.figshare.12252737

8. **Other policy documents.** Page 5 points to additional information and training guides on the intranet Patient Cohort Explorer site. Is there a formal data-use policy, SOP, or attestation that sits above this user guide?

9. **Access from a non-UMMC computer.** The application is reached through the UMMC intranet and `ntqvcl`. If a later plan is for anyone other than the student to log in, is that allowed, and on what network (campus, VPN, UMMC-managed device only)?
