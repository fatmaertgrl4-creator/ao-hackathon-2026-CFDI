# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Status

CFDI team's AO Hackathon 2026 project (`README.md`: "CFDI ekibinin projesidir").

The repository currently contains **no source code** — only `README.md`, `testgencer.txt` (a scratch file verifying Claude Code access), and GitHub's stock Python `.gitignore` template.

There are therefore no build, lint, test, or run commands to document yet, and no architecture to describe.

## Intended stack

The `.gitignore` is the unmodified GitHub Python template, so Python is the presumed language. It has not been narrowed to a specific toolchain — it still carries entries for Django, Flask, Scrapy, Streamlit, Marimo, Celery, Redis, RabbitMQ, poetry, pdm, pixi, and uv. Treat it as a default, not a statement of intent: nothing in the repo confirms which of these will actually be used.

## When code lands

Re-run `/init` once the project has real source files and a build setup, and replace this file with the actual commands and architecture. Sections worth filling in then:

- **Commands** — install/sync dependencies, run the app, run the full test suite, and run a single test.
- **Architecture** — the big-picture structure that takes reading several files to grasp, not a file listing.
