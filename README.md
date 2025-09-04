# CloudGuard

**Opinionated IaC guardrails & policy-as-code examples**

CloudGuard provides ready-made guardrails and examples for managing secure infrastructure across AWS, Azure, and GCP. It contains policies written in [OPA](https://www.openpolicyagent.org/) and templates for common misconfiguration checks. Use these examples as starting points for your own IaC and policy-as-code pipelines.

## Repository structure

- `aws/` – guardrails and policy samples for AWS.
- `azure/` – guardrails and policy samples for Azure.
- `gcp/` – guardrails and policy samples for GCP.
- `opa_policies/` – reusable OPA (Rego) policies.
- `examples/` – sample projects demonstrating how to integrate policies in CI/CD.

Each directory contains a `README.md` describing its contents.

## Getting started

1. Clone the repo:
   ```sh
   git clone https://github.com/Rehanperera-au/cloudguard.git
   ```
2. Explore the provider-specific directories to find policies relevant to your stack.
3. Copy policies into your pipelines or use the examples to run them with OPA or Conftest.

## Security

Please report any security issues via [email](mailto:<your.email@example.com>) rather than creating public GitHub issues. See the [SECURITY.md](SECURITY.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
