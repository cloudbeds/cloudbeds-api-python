#!/usr/bin/env python3
"""Patch the OpenAPI spec with temporary overrides before code generation.

Reads spec_overrides.yaml and applies each override to the OpenAPI spec
defined in openapitools.json. This allows releasing SDK versions with type
fixes while waiting for the upstream spec to be updated.

Usage:
    python scripts/patch_openapi_spec.py

The script is a no-op (exits 0) if spec_overrides.yaml doesn't exist or
has no overrides defined.
"""

import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
OVERRIDES_FILE = ROOT / "spec_overrides.yaml"
OPENAPITOOLS_FILE = ROOT / "openapitools.json"


def load_overrides():
    if not OVERRIDES_FILE.exists():
        return []
    with open(OVERRIDES_FILE) as f:
        data = yaml.safe_load(f)
    if not data or not data.get("overrides"):
        return []
    return data["overrides"]


def get_spec_path():
    with open(OPENAPITOOLS_FILE) as f:
        config = json.load(f)
    return ROOT / config["inputSpec"]


def set_nested(doc, dotted_path, value):
    """Set a value in a nested dict using a dot-separated path, creating intermediate keys as needed."""
    keys = dotted_path.split(".")
    current = doc
    for key in keys[:-1]:
        if key not in current:
            current[key] = {}
        current = current[key]
    current[keys[-1]] = value


def apply_overrides(spec, overrides):
    applied = 0
    for override in overrides:
        path = override["path"]
        schema = override["schema"]
        set_nested(spec, path, schema)
        print(f"  Patched: {path}")
        applied += 1
    return applied


def main():
    overrides = load_overrides()
    if not overrides:
        print("No spec overrides found, skipping patch step.")
        return

    spec_path = get_spec_path()
    if not spec_path.exists():
        print(f"Error: spec file not found at {spec_path}", file=sys.stderr)
        sys.exit(1)

    with open(spec_path) as f:
        spec = yaml.safe_load(f)

    print(f"Applying {len(overrides)} override(s) to {spec_path.name}:")
    applied = apply_overrides(spec, overrides)

    with open(spec_path, "w") as f:
        yaml.dump(spec, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    print(f"Done. {applied} override(s) applied.")


if __name__ == "__main__":
    main()
