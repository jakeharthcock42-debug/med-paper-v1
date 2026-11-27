# Cancer Screening, Primary Care Supply, and Late-Stage Diagnosis of Breast and Colorectal Cancer Across Mississippi Counties: A Public-Data Ecological Analysis

**Status**: draft-v1 (2026-11-27). Values are published aggregates reproducible with `scripts/public-data/`. Public-data only (Jake's decision, 2026-11-27). **Weak/low-novelty flag:** see README.

## Abstract (draft-v1; ≤300 words incl. section labels; conference style)
**Background.** Mississippi has higher breast, colorectal, and cervical cancer mortality than the US. Whether county screening and primary care supply explain county differences in stage at diagnosis, and whether Black–White mortality differences reflect screening, is unclear.

**Methods.** Ecological analysis of Mississippi and its 82 counties using public aggregates: State Cancer Profiles (incidence and late-stage share 2019–2023; mortality 2020–2024), CDC PLACES model-based screening estimates (BRFSS 2022), County Health Rankings Medicare mammography (2023), and HRSA Area Health Resources File primary care physicians (2023). Black/White rate ratios came from published rates and CIs. County analyses used Spearman correlation and OLS with robust SEs for the 69 (breast) and 75 (colorectal) counties with published late-stage shares.

**Results.** Compared with the US, Mississippi colorectal incidence was 45.7 vs 36.9 per 100,000 and mortality 17.5 vs 12.7; breast mortality was 23.6 vs 18.9 despite lower incidence (125.9 vs 133.0). Black mortality exceeded White for breast (29.5 vs 20.7; rate ratio 1.43, 95% CI 1.31–1.55; incidence ratio 1.04) and colorectal cancer (21.8 vs 15.8; 1.38, 1.28–1.49), while Black and White women had similar Medicare mammography (42% vs 41%; p=0.41). County breast late-stage share correlated with Medicare mammography (rho −0.33, p=0.006) but not after adjustment for child poverty and primary care supply (−0.04 per point; 95% CI −0.35 to 0.27). Model-based screening was not associated with late-stage share. Greater primary care supply was associated with lower late-stage share (breast −0.48 points per physician/10,000, 95% CI −0.86 to −0.10; colorectal −0.91, −1.55 to −0.27).

**Conclusions.** Excess Black mortality is not matched by lower Medicare mammography, pointing to stage, treatment, and follow-up rather than screening uptake alone. County screening estimates did not explain stage, but primary care supply did, an ecological and exploratory finding.

## 1. Introduction
Colorectal cancer screening is recommended from age 45 (USPSTF 2021), and screening is generally delivered through primary care. Mississippi's Delta has long had documented gaps in breast and cervical cancer screening (Hall 2004), distinct breast cancer subtype patterns across the lower Mississippi Delta (Zahnd 2019), and high gastrointestinal cancer burden (Whatley 2014). Recent Mississippi reviews highlight colorectal cancer outcomes and screening in a rural state (Koutha 2025; Vijayakumar 2025) and gaps in breast cancer research (Barsha 2025). We did not find an analysis in PubMed (2026-11-27) that combines county-level screening, primary care supply, and late-stage share across all 82 counties; this paper is exploratory and limited by model-based screening measures.

**Aims.** (1) Compare Mississippi with the US and Black with White residents. (2) Describe county screening by Delta and rurality and its relation to primary care supply. (3) Test screening and primary care supply against county late-stage share.

**Hypotheses.** H1 Mississippi exceeds the US in mortality and late-stage share. H2 Black mortality exceeds White with similar incidence. H3 Delta and nonmetro counties have lower screening. H4 PCP supply is associated with screening. H5 Higher county screening is associated with lower late-stage share. H6 (exploratory) PCP supply is associated with lower late-stage share.

## 2. Methods
**Design.** Cross-sectional ecological analysis of public aggregate data (no patient-level or UMMC data).

**Sources.** *State Cancer Profiles*: breast, colorectal, and cervix; age-adjusted incidence 2019–2023; late-stage (regional + distant) percent 2019–2023; mortality 2020–2024; all races and (state) Black and White non-Hispanic; SCP suppresses cells with fewer than 16 cases in 5 years. *CDC PLACES 2025 release* (BRFSS 2022): colorectal screening (45–75), mammography (50–74); *PLACES 2023 release* (BRFSS 2020) for sensitivity (CRC 50–75). PLACES estimates are model-based (Greenlund 2022). *County Health Rankings* (2025; 25 March 2026 supplement): Medicare FFS mammography (women 65–74) and flu vaccination, 2023, race-specific where published; child poverty, uninsured, % Black. *HRSA AHRF 2024–2025*: MD and DO primary care physicians excluding residents (2023), per 10,000 population. USDA RUCC 2023; Delta Regional Authority list.

**Analysis.** Rate ratios and approximate CIs from published rates and CIs (log scale). County: Mann-Whitney (DRA, nonmetro), Spearman, OLS with HC3 robust SEs (WLS weighted by late-stage average annual count as sensitivity). Primary comparisons H1–H2 (state level); county tests exploratory, two-sided α=0.05, unadjusted. Python (pandas, scipy, statsmodels); scripts in `scripts/public-data/`.

**Ethics.** Published aggregates only; SCP suppression respected; no cell under 11 events reported. Confirm with UMMC IRB whether a determination letter is needed. [PENDING: IRB/RDW confirmation]

## 3. Results
**Table 1. Mississippi vs US (SCP; rates per 100,000 with 95% CI)**

| Cancer | Measure | Mississippi | US |
|---|---|---|---|
| Colorectal | Incidence | 45.7 (44.6–46.7) | 36.9 (36.9–37.0) |
| Colorectal | Mortality | 17.5 (16.9–18.1) | 12.7 (12.7–12.8) |
| Colorectal | % late stage | 63.0 | 60.2 |
| Breast | Incidence | 125.9 (123.5–128.3) | 133.0 (132.8–133.3) |
| Breast | Mortality | 23.6 (22.6–24.6) | 18.9 (18.8–19.0) |
| Breast | % late stage | 35.1 | 30.7 |
| Cervix | Incidence | 9.0 (8.4–9.7) | 7.5 (7.4–7.6) |
| Cervix | Mortality | 3.6 (3.2–4.0) | 2.1 (2.1–2.2) |
| Cervix | % late stage | 55.7 | 53.3 |

**Table 2. Mississippi Black vs White non-Hispanic (SCP)**

| Cancer | Measure | Black NH | White NH | Rate ratio (approx. 95% CI) |
|---|---|---|---|---|
| Colorectal | Incidence | 51.2 (49.3–53.2) | 44.0 (42.8–45.3) | 1.16 |
| Colorectal | Mortality | 21.8 (20.6–23.1) | 15.8 (15.1–16.6) | 1.38 (1.28–1.49) |
| Breast | Incidence | 130.6 (126.6–134.8) | 125.5 (122.5–128.6) | 1.04 |
| Breast | Mortality | 29.5 (27.6–31.5) | 20.7 (19.6–21.9) | 1.43 (1.31–1.55) |

**Table 3. County screening by Delta (DRA, n=47) vs non-DRA (n=35), median %**

| Measure | DRA | Non-DRA | p |
|---|---|---|---|
| Medicare mammography (CHR 2023) | 40 | 44 | 0.003 |
| Mammography, women 50–74 (PLACES 2022) | 72.6 | 72.4 | 0.93 |
| Colorectal screening, 45–75 (PLACES 2022) | 54.7 | 55.1 | 0.17 |

**Table 4. County late-stage share (Spearman; breast n=69, colorectal n=75)**

| Predictor | Breast % late rho (p) | Colorectal % late rho (p) |
|---|---|---|
| Medicare mammography (CHR) | −0.33 (0.006) | — |
| PLACES mammography 2022 / CRC screening 2022 | 0.10 (0.40) | −0.04 (0.75) |
| PLACES 2020 mammography / CRC screening | 0.12 (0.32) | −0.11 (0.34) |
| PCP per 10k (AHRF) | −0.37 (0.002) | −0.32 (0.005) |
| Child poverty % | 0.51 (<0.001) | −0.17 (0.15) |
| % Black NH | 0.43 (<0.001) | −0.22 (0.054) |

Adjusted (OLS, HC3): breast late-stage on Medicare mammography −0.04 (−0.35, 0.27), PCP/10k −0.48 (−0.86, −0.10), child poverty/10 +2.85 (1.19, 4.50), nonmetro −0.85 (−3.76, 2.05); R² = 0.35 (n = 69). Colorectal late-stage on PLACES screening +0.14 (−0.70, 0.99), PCP/10k −0.91 (−1.55, −0.27); R² = 0.15 (n = 75). Black vs White Medicare mammography medians 42% vs 41% (n = 81, p = 0.41). Full output: `results/p05_results.md`, `results/p05b_results.md`.

## 4. Discussion (outline)
- Principal findings: excess mortality in Mississippi and among Black residents without a corresponding screening gap in Medicare mammography; no county screening–stage association after adjustment; PCP supply associated with lower late-stage share.
- Interpretation: stage and mortality gaps likely reflect follow-up, treatment access, and biology as well as screening uptake; PLACES smoothing and Medicare-only mammography limit the ability to detect screening effects.
- Limits: model-based and narrow screening measures; ecological design; period mismatch; exploratory tests.
- Next: BRFSS state-level screening by race; registry or patient-level stage data.

## References (verified)
1. US Preventive Services Task Force. Screening for colorectal cancer: US Preventive Services Task Force recommendation statement. *JAMA.* 2021;325(19):1965–1977.
2. Hall HI, Jamison PM, Coughlin SS, Uhler RJ. Breast and cervical cancer screening among Mississippi Delta women. *J Health Care Poor Underserved.* 2004;15:375–389. doi:10.1353/hpu.2004.0042
3. Zahnd WE, Sherman RL, Klonoff-Cohen H, et al. Disparities in breast cancer subtypes among women in the lower Mississippi Delta Region states. *Cancer Causes Control.* 2019;30:591–601. doi:10.1007/s10552-019-01168-0
4. Whatley Z, Daram SR, Yousuf S, et al. Gastrointestinal cancers in Mississippi. *South Med J.* 2014;107:229–234. doi:10.1097/SMJ.0000000000000093
5. Koutha S, Vijayakumar S, Young CC. Colorectal cancer in Mississippi: how to change the tide of bad news to a success story? *Cureus.* 2025;17:e90164. doi:10.7759/cureus.90164
6. Vijayakumar S, Koutha S, Young C, et al. Current status of colorectal cancer screenings: tailoring them to Mississippi's rural geography, demographics, infrastructure and community needs. *Cureus.* 2025;17:e97517. doi:10.7759/cureus.97517
7. Barsha RAA, Miller-Kleinhenz J. Left behind: the unmet need for breast cancer research in Mississippi. *Cancers (Basel).* 2025;17(10):1652. doi:10.3390/cancers17101652
8. Greenlund KJ, Lu H, Wang Y, et al. PLACES: Local Data for Better Health. *Prev Chronic Dis.* 2022;19:210459.
9. National Cancer Institute and CDC. State Cancer Profiles. https://statecancerprofiles.cancer.gov/ (accessed 2026-11-26).
