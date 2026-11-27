# Public-data pipeline (Papers 02–05)

Python 3 (pandas, numpy, scipy, statsmodels, tabulate, openpyxl, requests). Run from a working directory containing `raw/` downloads. All inputs are public; no UMMC data.

1. Downloads (not committed; re-download):
   - CHR `analytic_data2025_v3.csv` and `analytic_supplement_20260325[1].csv` from https://www.countyhealthrankings.org/health-data/methodology-and-sources/data-documentation → `raw/chr2025.csv`, `raw/chr_supp2026.csv`
   - PLACES 2025 `https://data.cdc.gov/resource/i46a-9kgh.csv?stateabbr=MS` → `raw/places_ms_2025.csv`
   - USDA RUCC 2023 CSV → `raw/rucc2023.csv`; State Cancer Profiles CSV exports (`output=1`) → `raw/scp/`
   - HRSA AHRF 2024–2025 CSV zip https://data.hrsa.gov/DataDownload/AHRF/AHRF_2024-2025_CSV.zip → unzip to `raw/ahrf/`
2. `build_master.py` → `master_county_ms.csv` (`data/public/master_county_ms.csv` in this repo).
3. `build_ahrf.py` adds AHRF columns (`ahrf_*`, `obgyn_per10k_fem`, `dent_per10k`, `preterm_pct`, `ob_hospital_any`) to the master file.
4. `build_places2020.py` adds PLACES 2023-release (BRFSS 2020) dental visit, all-teeth-lost, colorectal screening and mammography (`pl20_*`) via the data.cdc.gov API (dataset `h3ej-a9ec`).
5. `scp_build.py` → `scp_all_long.csv` (`data/public/scp_all_long.csv`).
6. `p02.py`, `p03.py`, `p04.py`, `p05.py` (first pass) and `p02b.py`, `p03b.py`, `p04b.py`, `p05b.py` (AHRF/PLACES-2020 additions) → `results/pXX/`.
7. `pubmed.py "<query>"` runs the PubMed E-utilities novelty searches (NCBI esearch/esummary).

Notes: CHR rates are stored as fractions in the raw files and are scaled in `build_master.py` (PCP/dentists ×100,000; percents ×100). The PLACES 2024/2025 releases give Mississippi dental-visit values of 4.9–12.9% (BRFSS 2022), implausible versus other states (about 39–66%) and the national estimate (63.9%); the 2022-based `DENTAL` measure is dropped and the 2020-based measure (`pl20_dental`) is used as a sensitivity covariate. Delta = Delta Regional Authority-designated Mississippi counties (47). AHRF HPSA codes (0/1/2) are used descriptively only (definitions not in the downloaded documentation). The Census API was not used (key required). CDC WONDER state/county mortality and natality cannot be queried by API (national-only), so they are not scripted.
