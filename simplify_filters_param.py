"""
Post-generation script to simplify filters parameter.
This script replaces complex QueryParameterDynamicFilterSchema type hints
with simple Optional[str] to allow users to pass filter strings directly.
"""

import re
import sys
from pathlib import Path


def simplify_filters_in_file(api_file):
    """Simplify filters parameter type hints in a single API file.

    Args:
        api_file: Path to the API file to fix

    Returns:
        bool: True if file was processed successfully
    """
    print(f"Processing {api_file}...")

    content = api_file.read_text()
    original_content = content

    # Pattern 1: Replace the import of QueryParameterDynamicFilterSchema
    import_pattern = r'from cloudbeds_pms\.models\.query_parameter_dynamic_filter_schema import QueryParameterDynamicFilterSchema\n'
    content = re.sub(import_pattern, '', content)

    # Pattern 2: Replace type hints in method signatures
    # Match: filters: Annotated[Optional[QueryParameterDynamicFilterSchema], ...]
    # Replace with: filters: Annotated[Optional[str], ...]
    type_hint_pattern = r'(filters:\s*Annotated\[)Optional\[QueryParameterDynamicFilterSchema\]'
    content = re.sub(type_hint_pattern, r'\1Optional[str]', content)

    # Pattern 3: Update docstrings that mention the type
    docstring_pattern = r':type filters: QueryParameterDynamicFilterSchema'
    content = re.sub(docstring_pattern, ':type filters: str', content)

    if content != original_content:
        api_file.write_text(content)
        print(f"  ✓ Simplified filters parameter in {api_file.name}")
        return True
    else:
        print(f"  No QueryParameterDynamicFilterSchema found in {api_file.name}")
        return True


def simplify_filters():
    """Simplify filters parameter in all generated API client files."""

    api_dir = Path("cloudbeds_pms/api")

    if not api_dir.exists():
        print(f"Error: {api_dir} not found")
        return False

    print(f"Scanning for API files in {api_dir}...\n")

    # Find all Python files in the api directory
    api_files = list(api_dir.glob("*_api.py"))

    if not api_files:
        print("No API files found")
        return False

    print(f"Found {len(api_files)} API file(s)\n")

    # Process each file
    success = True
    modified_count = 0

    for api_file in sorted(api_files):
        if not simplify_filters_in_file(api_file):
            success = False
        else:
            modified_count += 1

    print(f"\nProcessed {modified_count}/{len(api_files)} file(s) successfully")
    return success


def main():
    """Main function."""
    success = simplify_filters()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()