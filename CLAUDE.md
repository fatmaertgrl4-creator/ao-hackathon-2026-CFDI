# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Status

Team **CFDI**'s entry for AO Hackathon 2026. The repository currently contains **no source code** — only the mandatory submission scaffolding, all of it in draft (`TODO`) state. There are no build, lint, test, or run commands yet; do not invent them.

`testgencer.txt` and `test_dogukan.txt` are leftover access-check artifacts, not project files.

## Repository layout is mandated, not chosen

The hackathon rules fix this structure. Do not rename, relocate, or "tidy" these paths:

```
README.md            AI_JURI.md         submission.json    .env.example
CLAUDE.md            docs/              prompts/           demo/            src/
```

`docs/` must contain `plan.md`, `fazlar.md`, `mimari.md`. Documentation is written in **Turkish** — match that when editing docs; this file stays in English.

## The evidence rule

Scoring rejects unevidenced claims: every assertion in `AI_JURI.md` must cite a real path, and section 3 (X-Factor) requires line-level precision (`src/<file>:<line-range>`).

Two consequences when editing:

- **Never write a claim without a path that resolves.** A citation to a nonexistent file is worse than no citation — it discredits the claim.
- **Refactors can silently break scoring.** Moving or reformatting a file that `AI_JURI.md` cites by line range invalidates the evidence. Grep `AI_JURI.md` for the path before restructuring `src/`.

## Cross-file invariants

The same fact is duplicated across files by design, so these must be updated together:

| Fact | Lives in |
|---|---|
| Run command | `AI_JURI.md` §4 · `submission.json` → `calistirma.komut` · `README.md` |
| Demo flow steps | `submission.json` → `sunum.demo_akisi` · `demo/README.md` |
| Metrics | `AI_JURI.md` §2 · `submission.json` → `cozum.olctugumuz_metrikler` |
| X-Factor | `AI_JURI.md` §3 · `submission.json` → `cozum.x_factor` |

`submission.json` is machine-read; its key names come from the official spec. Keep the keys exactly as-is (ASCII, no Turkish characters) and change only values.

## Secrets

`.env` is gitignored and must never be committed. Every new variable used in code must also be added to `.env.example` with an **empty** value. If a real secret ever lands in a commit, rotate the key at the provider — removing it from history is not sufficient.

## prompts/ is a deliverable

`prompts/` is scored evidence for `AI_JURI.md` §1, not a scratch folder. When a prompt meaningfully shapes the code, record it there using `prompts/_SABLON.md`, including the human decision that accepted or rejected the output. Write it as the work happens — reconstructing prompts afterwards is both unreliable and visible to the jury.

## When code lands

Fill in the run/test commands and replace `docs/mimari.md` and `src/README.md` with the real architecture. Re-run `/init` at that point to regenerate this file's command and architecture sections.
