# FinOps Orchestrator – Runbook

This document provides operational guidance for running, troubleshooting, and maintaining the Intelligent FinOps Infrastructure Orchestrator.

---

## 1️⃣ Routine Operation

### Triggering the pipeline
- Go to **GitHub Actions → plan.yml → Run workflow**.
- Upload or specify the path to the demand CSV (optional).
- Review the generated Terraform Plan artifact.
- Once validated, trigger **apply.yml** (requires environment approval).

### Schedule (Optional)
You can configure a CRON trigger (e.g., daily at midnight UTC) to automatically generate plans.

---

## 2️⃣ Key Operational Scripts

| Script | Purpose |
|---------|----------|
| `decision/decide_capacity.py` | Computes new capacity from forecast data and writes `tf/terraform.tfvars.json`. |
| `tf/main.tf` | Entry point for Terraform configuration. |
| `.github/workflows/plan.yml` | Runs dry-run Terraform plan. |
| `.github/workflows/apply.yml` | Applies approved changes to Azure. |

---

## 3️⃣ Monitoring and Validation

- **Terraform Plan Output:** Verify no unintended resource deletions.
- **Azure Portal:** Confirm VMSS instance count matches `tfvars.json`.
- **Logs:** GitHub Actions logs show each step, including capacity computed.
- **Cost Metrics:** Optional integration with Cost Management + Azure Monitor.

---

## 4️⃣ Common Issues

| Symptom | Likely Cause | Resolution |
|----------|---------------|------------|
| `terraform init` fails | Incorrect backend storage or credentials | Verify `backend.hcl` and GitHub secrets. |
| Plan shows large-scale change | Missing or corrupted tfstate | Reinitialize backend or validate state. |
| Apply fails with 403 | Service Principal lacks permission | Assign `Contributor` role at RG/subscription. |
| No scaling detected | `CHANGE_THRESHOLD` too high | Lower threshold in environment variables. |

---

## 5️⃣ Rollback Procedure

1. Retrieve previous `terraform.tfvars.json` from last successful run.
2. Run plan again using that version.
3. Review plan output → ensure capacity reverts correctly.
4. Trigger `apply.yml`.

---

## 6️⃣ Logs & Artifacts

- All pipeline logs stored in GitHub Actions run history.
- Terraform plans and outputs uploaded as artifacts.
- Azure Activity Logs provide additional audit trail.

---

## 7️⃣ Contacts & Ownership

| Role | Name | Responsibility |
|------|------|----------------|
| **FinOps Engineer** | Hritam | Cost analysis and optimization |
| **DevOps Engineer** | Hritam | Pipeline and IaC maintenance |
