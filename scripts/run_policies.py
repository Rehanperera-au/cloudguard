#!/usr/bin/env python3
"""
Run CloudGuard OPA policies against an input JSON file.

This helper script uses the OPA CLI to evaluate all policies in the opa_policies
directory against a given input. It shows how to embed policy checks into
custom tooling or local workflows.

Usage:
  python scripts/run_policies.py --input input.json
  python scripts/run_policies.py -i path/to/input.json -d path/to/policies

Requires OPA CLI installed and available in PATH.
"""

import argparse
import os
import subprocess
import sys

def run_policies(input_file: str, policies_dir: str) -> int:
    """
    Execute OPA evaluation on the input file with the policies in policies_dir.
    """
    # Build the OPA command
    cmd = [
        "opa",
        "eval",
        "-i",
        input_file,
        "-d",
        policies_dir,
        "data"
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    except FileNotFoundError:
        print("OPA executable not found. Please install OPA and ensure it is in your PATH.", file=sys.stderr)
        return 1

    # Print the evaluation results
    print(result.stdout)
    if result.stderr:
        # Print any warnings or errors
        print(result.stderr, file=sys.stderr)

    return result.returncode

def main():
    parser = argparse.ArgumentParser(description="Run OPA policies against an input JSON file.")
    parser.add_argument("-i", "--input", required=True, help="Path to the input JSON file.")
    parser.add_argument("-d", "--policies", default=os.path.join(os.path.dirname(__file__), "..", "opa_policies"),
                        help="Path to directory containing Rego policy files (default: opa_policies).")

    args = parser.parse_args()

    # Normalize paths
    input_path = os.path.abspath(args.input)
    policies_path = os.path.abspath(args.policies)

    if not os.path.isfile(input_path):
        print(f"Input file '{input_path}' does not exist.", file=sys.stderr)
        return 1

    if not os.path.isdir(policies_path):
        print(f"Policies directory '{policies_path}' does not exist.", file=sys.stderr)
        return 1

    return run_policies(input_path, policies_path)

if __name__ == "__main__":
    sys.exit(main())
