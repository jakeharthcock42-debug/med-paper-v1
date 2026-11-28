# Approximate 95% CI for the Black/White breast cancer incidence rate ratio

Computed 2026-11-27 to support the Paper 02 abstract revision. No new source rates were introduced. The method is the same log-normal approximation already described in `draft-v1.md` Methods (“rate ratios and approximate 95% CIs were derived from published CIs”).

## Inputs (already in Table 5)

From State Cancer Profiles, age-adjusted incidence per 100,000 (2019–2023), non-Hispanic:

- Black: 130.6 (95% CI 126.6–134.8)
- White: 125.5 (95% CI 122.5–128.6)
- Point ratio reported in Table 5: 1.04 (130.6 / 125.5 = 1.0406)

## Method

For a published rate with 95% CI (L, U), the standard error of the log rate is approximated as

SE(ln R) = (ln U − ln L) / (2 × 1.96)

The standard error of the log rate ratio is

SE(ln RR) = sqrt( SE(ln R_B)^2 + SE(ln R_W)^2 )

and the approximate 95% CI is

exp( ln RR ± 1.96 × SE(ln RR) )

## Result

- RR = 1.0406
- Approximate 95% CI = 1.0001 to 1.0828, reported in the abstract and Table 5 as **1.04 (1.00–1.08)** (two-decimal style used for the other Paper 02 ratios).

## Method check against ratios already in the draft

The same formula recovers the intervals already reported (to two decimals):

- Breast mortality 29.5 (27.6–31.5) / 20.7 (19.6–21.9) → 1.43 (1.31–1.55)
- Colorectal mortality 21.8 (20.6–23.1) / 15.8 (15.1–16.6) → 1.38 (1.28–1.49)
- Oral cavity and pharynx incidence 9.5 (8.8–10.4) / 15.6 (14.9–16.4) → 0.61 (0.55–0.67)

Calculation: Python 3, `math.log` / `math.exp`.
