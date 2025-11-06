import json, math, os
import pandas as pd

INPUT = os.getenv("DEMAND_FILE", "decision/demand_sample.csv")
OUTPUT = "tf/terraform.tfvars.json"

# tuning knobs (safe guardrails)
MIN_CAP = int(os.getenv("MIN_CAP", "1"))
MAX_CAP = int(os.getenv("MAX_CAP", "10"))
UNITS_PER_INSTANCE = float(os.getenv("UNITS_PER_INSTANCE", "25"))  # how much demand one instance can handle
SMOOTHING = float(os.getenv("SMOOTHING", "0.6"))  # EWMA smoothing for near-future bias
CHANGE_THRESHOLD = int(os.getenv("CHANGE_THRESHOLD", "1"))  # skip changes smaller than this

df = pd.read_csv(INPUT, parse_dates=["date"]).sort_values("date")
# simple EWMA of demand to bias towards the latest days
series = df["demand"].ewm(alpha=SMOOTHING).mean()
forecast = series.iloc[-1]
raw_capacity = forecast / UNITS_PER_INSTANCE
desired = max(MIN_CAP, min(MAX_CAP, math.ceil(raw_capacity)))

# previous desired (if any) to avoid noisy churn
prev = None
try:
    with open(OUTPUT, "r") as f:
        prev = json.load(f).get("vmss_capacity")
except Exception:
    pass

if prev is not None and abs(desired - prev) < CHANGE_THRESHOLD:
    desired = prev

vars_payload = {
    # if you switch to Function App EP1, expose a different var (e.g., "plan_worker_count")
    "vmss_capacity": desired,
    "tags": {"project": "finops-orchestrator", "env": "dev"}
}

os.makedirs("tf", exist_ok=True)
with open(OUTPUT, "w") as f:
    json.dump(vars_payload, f, indent=2)

print(f"Desired VMSS capacity -> {desired}. Wrote {OUTPUT}")
