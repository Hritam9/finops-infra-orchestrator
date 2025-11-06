# Design Decisions

## 1️⃣ Why Terraform?
Terraform provides consistent, version-controlled IaC for Azure. It supports modular design and integration with GitHub Actions seamlessly.

## 2️⃣ Why Python Decision Module?
Python enables data-driven scaling logic (using Pandas, smoothing, forecasting). This logic can evolve into ML models later.

## 3️⃣ Why GitHub Actions (CI/CD)?
- Native integration with GitHub repo
- Easy artifact upload and environment approvals
- Cost-free for public repositories

## 4️⃣ Backend Choice
Azure Storage backend provides:
- Centralized remote state management
- Locking and concurrent execution prevention
- Compliance with enterprise-grade FinOps policies

## 5️⃣ Guardrails
To prevent uncontrolled scaling:
- **MIN_CAP / MAX_CAP:** ensure capacity stays within safe limits.
- **CHANGE_THRESHOLD:** ignores noise or small fluctuations.

## 6️⃣ Extensibility
Future enhancements:
- Add forecasting (Prophet / ARIMA)
- Integrate with Cost Management API
- Replace VMSS with Function App EP1 or AKS autoscaler
