# Examples

This directory contains hands‑on examples that demonstrate how to apply CloudGuard guardrails and policies in real projects. You’ll find sample infrastructure as code (IaC) projects, CI/CD pipeline configurations and end‑to‑end reference implementations.

## Structure

- `iac/` – example IaC modules that follow CloudGuard’s guardrails. Includes Terraform modules for AWS, Azure and GCP demonstrating secure defaults.
- `pipeline/` – sample CI/CD pipelines. GitHub Actions workflows and Conftest/OPA checks to enforce policies during pull requests.
- `app/` – example applications instrumented with security practices. Shows how to integrate policy checks and secrets scanning into a microservice project.

Use these examples as inspiration. Feel free to adapt them to your environment, but always remove secrets and sensitive information before committing.
