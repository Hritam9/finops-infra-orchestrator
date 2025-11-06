# Intelligent FinOps Infrastructure Orchestrator – Architecture

## 1️⃣ Overview
The Intelligent FinOps Infrastructure Orchestrator is an automation system that dynamically adjusts Azure compute capacity based on predicted workload demand. It combines **Python (decision logic)**, **Terraform (infrastructure as code)**, and **GitHub Actions (CI/CD automation)**.

---

## 2️⃣ System Components

| Component | Description |
|------------|--------------|
| **Python Decision Module** | Analyzes demand forecast data and outputs the optimal desired capacity (VM count or Function App instances). |
| **Terraform Infrastructure** | Defines and provisions Azure infrastructure (Resource Group, VM Scale Set, Storage Account, Function App). |
| **GitHub Actions Pipelines** | Automates planning and deployment workflows. Generates Terraform plans and applies them with manual approvals. |
| **Azure Backend Storage** | Stores Terraform state files for consistent, shared state management. |
| **Guardrails** | Min/max capacity limits and change-threshold filters prevent excessive scaling and cost spikes. |

---

## 3️⃣ Data Flow Diagram

[Forecast CSV/JSON]
↓
[Python Decision Script]
↓ generates tfvars.json
[Terraform Plan & Apply via GitHub Actions]
↓
[Azure Infrastructure Updated]


---

## 4️⃣ Deployment Flow

1. Commit demand forecast or trigger pipeline manually in GitHub Actions.
2. The **decision module** computes required capacity → writes `tf/terraform.tfvars.json`.
3. **Terraform Plan** runs (safe dry-run).
4. After approval, **Terraform Apply** provisions updates.
5. Azure resources are scaled up or down accordingly.

---

## 5️⃣ Key Azure Resources

- Resource Group  
- VM Scale Set (Linux) or Function App (EP1 Plan)  
- Azure Storage Account for remote tfstate  
- Optional: Log Analytics Workspace for telemetry

---

## 6️⃣ Security & Governance

- Uses **Azure Service Principal** credentials stored in GitHub Secrets.  
- Manual approval step in GitHub environment before deployment.  
- Supports policy enforcement (Terraform policy checks can be added later).

---

## 7️⃣ Scalability and Extension

Future roadmap:
- Integrate real telemetry from Azure Monitor / Log Analytics  
- Add forecast ML model (ARIMA / Prophet) instead of CSV  
- Auto-generate cost reports post-deployment  
