# finops-infra-orchestrator
A GitHub Actions → Python decision script → Terraform pipeline that right-sizes Azure capacity (e.g., a VM Scale Set or a Function App plan) from a simple demand forecast (CSV/JSON). Remote state in Azure Storage, modular Terraform with for_each, policy guardrails, and dry-run previews.
