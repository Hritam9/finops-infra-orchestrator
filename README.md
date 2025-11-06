# finops-infra-orchestrator
A GitHub Actions → Python decision script → Terraform pipeline that right-sizes Azure capacity (e.g., a VM Scale Set or a Function App plan) from a simple demand forecast (CSV/JSON). Remote state in Azure Storage, modular Terraform with for_each, policy guardrails, and dry-run previews.

# Intelligent FinOps Infrastructure Orchestrator

Right-sizes Azure capacity from a simple demand forecast using **Python (decision)** + **Terraform (provisioning)** + **GitHub Actions (CI/CD)**.

## Architecture
- Forecast CSV → Python EWMA → writes `tf/terraform.tfvars.json`
- `plan.yml` shows change preview
- `apply.yml` deploys after approval
- Azure resources: RG + VM Scale Set (or Function App Premium)

## Quick start
```bash
pip install -r decision/requirements.txt
python decision/decide_capacity.py  # generates tf/terraform.tfvars.json
cd tf
terraform init -backend-config=backend.hcl
terraform plan
