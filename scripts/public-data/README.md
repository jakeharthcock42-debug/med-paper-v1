# Public-data pipeline (Papers 02–05)

Python 3 (pandas, numpy, scipy, statsmodels, tabulate). Run from a working directory containing `raw/` downloads.

1. Downloads (not committed; re-download): CHR `analytic_data2025_v3.csv` and `analytic_supplement_20260325[1].csv` from https://www.countyhealthrankings.org/health-data/methodology-and-sources/data-documentation → `raw/chr2025.csv`, `raw/chr_supp2026.csv`; PLACES `https://data.cdc.gov/resource/i46a-9kgh.csv?stateabbr=MS` → `raw/places_ms_2025.csv`; USDA RUCC 2023 CSV → `raw/rucc2023.csv`; State Cancer Profiles CSV exports (`output=1`) → `raw/scp/`.
2. `build_master.py` → `master_county_ms.csv` (`data/public/master_county_ms.csv` in this repo).
3. `scp_build.py` → `scp_all_long.csv` (`data/public/scp_all_long.csv`).
4. `p02.py` … `p05.py` → `results/pXX/`.

Notes: CHR rates are stored as fractions in the raw files and are scaled in `build_master.py` (PCP/dentists ×100,000; percents ×100). PLACES "dental visit" is dropped (implausible values). Delta = Delta Regional Authority-designated Mississippi counties (47). Census API was not used (key required).
