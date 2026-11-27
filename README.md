# med-paper-v1

Mississippi county-level / UMMC health disparities research project (medical student abstracts & papers).

## Structure

```
med-paper-v1/
├── README.md                 # this file
├── data-sources.md           # living catalog of public + UMMC datasets
├── data/public/              # merged MS county public data + State Cancer Profiles extract
├── scripts/public-data/      # pipeline + analysis scripts (Papers 02–05)
└── papers/                   # one subfolder per potential paper
    ├── 01-hearing-loss-disparities/
    │   ├── README.md         # status, aims, notes
    │   ├── draft-v1.md       # working draft
    │   └── final.md          # (when ready)
    ├── 02-oral-pharynx-cancer-disparities/   # README, draft-v1, results/
    ├── 03-primary-care-premature-mortality-gap/
    ├── 04-maternal-infant-outcomes/
    ├── 05-screening-gaps-cancer-stage/
    └── (future papers...)
```

## Active papers

| # | Working title | Status | Folder |
|---|---------------|--------|--------|
| 01 | Hearing loss disparities (UMMC + county context) | Ideation / early draft | [papers/01-hearing-loss-disparities](papers/01-hearing-loss-disparities) |
| 02 | Oral cavity & pharynx cancer by race and rurality | **Public-data only; analysis complete; draft-v1 abstract (2026-11-27)** | [papers/02-oral-pharynx-cancer-disparities](papers/02-oral-pharynx-cancer-disparities) |
| 03 | Primary care supply, poverty, Black–White gap in premature mortality | **Public-data only; analysis complete; draft-v1 abstract; partial novelty overlap (Lee 2026)** | [papers/03-primary-care-premature-mortality-gap](papers/03-primary-care-premature-mortality-gap) |
| 04 | Maternal/infant outcomes (LBW, teen births, infant mortality) | **Public-data only; analysis complete; draft-v1 abstract (2026-11-27)** | [papers/04-maternal-infant-outcomes](papers/04-maternal-infant-outcomes) |
| 05 | Cancer screening gaps and stage (Delta/rural) | **Public-data only; draft-v1 abstract; weak / low novelty** | [papers/05-screening-gaps-cancer-stage](papers/05-screening-gaps-cancer-stage) |

**Decision (2026-11-27):** Papers 02–05 use public data only (no UMMC/RDW pulls); Paper 01 continues with UMMC data. See `PROJECT-HANDOFF.md` section 3c.

## Key shared resources

- **[data-sources.md](data-sources.md)** — Datasets (CHR, MSTAHRS, PLACES, State Cancer Profiles, RDW, etc.) with access notes and ENT relevance.
