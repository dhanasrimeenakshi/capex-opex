CapEx vs OpEx Cost-Benefit Analyzer (Cloud vs On-Premises)
Project Overview

This project analyzes and compares Capital Expenditure (CapEx) and Operational Expenditure (OpEx) for IT infrastructure deployment options: Cloud vs On-Premises.
It calculates the Total Cost of Ownership (TCO) for 1–5 years, provides summary statistics, and visualizes the costs for easy decision-making.

This tool helps organizations understand the cost trade-offs between Cloud and On-Prem deployments for budgeting and planning.

Features

Generate a synthetic dataset of Cloud and On-Prem costs.

Compute TCO for 1–5 years.

Compare average CapEx, OpEx, and total costs.

Perform a breakeven cost analysis.

Visualize results using:

Bar chart for 5-year total cost comparison

Line chart for yearly total cost trend

Export dataset as CSV (capex_opex_dataset.csv) for further analysis.

Technologies Used

Python 3.12.11

Libraries:

pandas – data manipulation and CSV export

numpy – random synthetic data generation

matplotlib – data visualization

streamlit (optional) – for interactive dashboards

Installation

Clone or download the project folder:

cd "C:\Users\YourUsername\Desktop"
git clone <project-repo-url>  # optional if using Git
cd capex_opex_analyzer


Create a virtual environment:

python -m venv .venv


Activate the virtual environment:

.venv\Scripts\activate


Install required libraries:

pip install --upgrade pip
pip install pandas numpy matplotlib streamlit

How to Run
python capex_opex_analyzer.py


Output:

Console prints summary of average costs and breakeven analysis.

Bar chart: compares 5-year TCO (Cloud vs On-Prem).

Line chart: shows yearly TCO trend over 5 years.

CSV file: capex_opex_dataset.csv is saved in the project folder.

Sample Output

Console Summary Example:

===== Average Cost Summary =====
               CapEx  OpEx_per_month    TCO_5yr  Total_Avg_Cost
Infrastructure
Cloud             0.0         4150.0   249000.0        249000.0
On-Prem       72000.0         2800.0   240000.0        240000.0

💡 On-Prem is more cost-effective over 5 years.

✅ Dataset and analysis saved to 'capex_opex_dataset.csv'


Graphs Generated:

Bar Chart – 5-year TCO comparison

Line Chart – yearly cost trend (1–5 years)

Insights

Cloud: Lower upfront CapEx, higher OpEx → ideal for short-term or scalable workloads.

On-Prem: Higher CapEx, lower OpEx → cost-effective for long-term fixed workloads.

Organizations can make informed budgeting and infrastructure decisions using these analyses.

Notes

Synthetic dataset is randomly generated; you can replace it with real cost data if available.

Can be extended to include interactive dashboards using Streamlit for dynamic comparisons.
