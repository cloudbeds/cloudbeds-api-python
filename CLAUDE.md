# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Auto-generated Python SDK for the Cloudbeds PMS v1.3 API, produced by OpenAPI Generator 7.11.0. Nearly all code under `cloudbeds_pms_v1_3/` is generated — do not manually edit generated files.

## Commands

- **Install dependencies**: `uv sync` (dev) or `uv sync --locked --no-dev` (prod)
- **Run all tests**: `pytest`
- **Run a single test**: `pytest cloudbeds_pms_v1_3/test/test_<name>.py`
- **Build**: `uv build`

## Code Generation

The SDK is regenerated from an OpenAPI spec using the config in `openapitools.json`:
- Generator: `python` (OpenAPI Generator CLI 7.11.0)
- Input spec: sourced from Cloudbeds MFD repository (fetched during CI)
- Custom Mustache templates in `templates/` (`model_enum.mustache`, `model_generic.mustache`)
- Key setting: `enumUnknownDefaultCase: true` — enums include an unknown default case

To regenerate: the CI workflow in `.github/workflows/publish.yaml` handles spec fetching, generation, version bumping, and publishing to PyPI.

## Architecture

```
cloudbeds_pms_v1_3/
├── api/              # 21 API endpoint classes (one per resource domain)
├── models/           # ~318 Pydantic v2 models (from OpenAPI schemas)
├── test/             # Unittest stubs (one per model, auto-generated)
├── docs/             # Markdown docs (one per model/endpoint)
├── api_client.py     # Core HTTP client (request building, serialization)
├── configuration.py  # Auth config: API key (x-api-key header) and OAuth2
├── exceptions.py     # Exception hierarchy
└── rest.py           # REST layer using urllib3
```

API classes use `@validate_call` from Pydantic and return typed model instances. Auth is configured via `Configuration` with either API key or OAuth2 bearer token.

## Version

Current version: `1.9.0` (tracked in `VERSION` file and `openapitools.json`). Version bumps happen automatically during the publish workflow.