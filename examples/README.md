# Examples

This directory contains hands‑on examples that demonstrate how to apply CloudGuard guardrails and policies in real projects. You’ll find sample infrastructure as code (IaC) projects, CI/CD pipeline configurations and end‑to‑end reference implementations.

## Structure

- `iac/` – example IaC modules that follow CloudGuard’s guardrails. Includes Terraform modules for AWS, Azure and GCP demonstrating secure defaults.
- `pipeline/` – sample CI/CD pipelines. GitHub Actions workflows and Conftest/OPA checks to enforce policies during pull requests.
- `app/` – example applications instrumented with security practices. Shows how to integrate policy checks and secrets scanning into a microservice project.

Use these examples as inspiration. Feel free to adapt them to your environment, but always remove secrets and sensitive information before committing.

## Usage Examples

Below are some basic examples showing how to run CloudGuard policies in your CI pipeline and from the command line.

### Evaluate a Terraform plan using Conftest

```bash
terraform init
terraform plan -out=tfplan.binary
terraform show -json tfplan.binary > tfplan.json
conftest test tfplan.json --policy ../../opa_policies
```

### Evaluate policies with the OPA CLI

```bash
# Assuming you have an input file input.json representing your infrastructure
opa eval --format=pretty -i input.json -d ../../opa_policies "data.cloudguard.deny"
```

### Evaluate policies programmatically with Python

```python
import json
import subprocess

def evaluate_policies(input_path):
    result = subprocess.run(
        ["opa", "eval", "--format=json", "-i", input_path, "-d", "../opa_policies", "data.cloudguard.deny"],
        capture_output=True, text=True
    )
    findings = json.loads(result.stdout)
    return findings["result"]
```
