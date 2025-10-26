# CapEx vs OpEx Cost-Benefit Analyzer
# Author: Dhanasri M Project – Cloud vs On-Premises TCO Comparison

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1️⃣ Generate Synthetic Dataset
# -----------------------------
np.random.seed(42)

n = 50  # number of samples
infra_types = np.random.choice(["Cloud", "On-Prem"], size=n)

data = []
for infra in infra_types:
    if infra == "On-Prem":
        capex = np.random.randint(30000, 120000)
        opex = np.random.randint(1500, 4000)
    else:  # Cloud
        capex = 0
        opex = np.random.randint(2500, 6000)

    storage = np.random.randint(10, 200)  # in TB
    compute = np.random.randint(4, 64)    # vCPU
    network = np.random.uniform(1, 20)    # TB/month

    data.append([infra, capex, opex, storage, compute, network])

df = pd.DataFrame(data, columns=["Infrastructure", "CapEx", "OpEx_per_month", "Storage_TB", "Compute_vCPU", "Network_TB"])

# -----------------------------
# 2️⃣ Calculate TCO for 1–5 Years
# -----------------------------
for year in range(1, 6):
    df[f"TCO_{year}yr"] = df["CapEx"] + df["OpEx_per_month"] * 12 * year

# -----------------------------
# 3️⃣ Summary Analysis
# -----------------------------
summary = df.groupby("Infrastructure")[["CapEx", "OpEx_per_month", "TCO_5yr"]].mean().round(2)
summary["Total_Avg_Cost"] = summary["CapEx"] + summary["OpEx_per_month"] * 12 * 5

print("===== Average Cost Summary =====")
print(summary, "\n")

# Breakeven Analysis
avg_onprem_5yr = summary.loc["On-Prem", "Total_Avg_Cost"]
avg_cloud_5yr = summary.loc["Cloud", "Total_Avg_Cost"]

if avg_cloud_5yr < avg_onprem_5yr:
    print("💡 Cloud is more cost-effective over 5 years.")
else:
    print("💡 On-Prem is more cost-effective over 5 years.")
print("\n")

# -----------------------------
# 4️⃣ Visualization
# -----------------------------

# Bar Chart: 5-year TCO comparison
plt.figure(figsize=(8, 5))
summary["Total_Avg_Cost"].plot(kind='bar', color=['green', 'blue'])
plt.title("Average 5-Year Total Cost (Cloud vs On-Prem)")
plt.ylabel("Cost ($)")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# Line Graph: Yearly cost comparison
plt.figure(figsize=(8, 5))
for infra in ["Cloud", "On-Prem"]:
    avg_costs = [df[df["Infrastructure"] == infra][f"TCO_{y}yr"].mean() for y in range(1, 6)]
    plt.plot(range(1, 6), avg_costs, marker='o', label=infra)

plt.title("Yearly Total Cost Trend (Cloud vs On-Prem)")
plt.xlabel("Years")
plt.ylabel("Average Total Cost ($)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

# -----------------------------
# 5️⃣ Export Results
# -----------------------------
df.to_csv("capex_opex_dataset.csv", index=False)
print("✅ Dataset and analysis saved to 'capex_opex_dataset.csv'")
