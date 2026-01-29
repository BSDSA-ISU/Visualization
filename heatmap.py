import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("./denguecases.csv")

# Ensure correct month order
month_order = ["Jan","Feb","Mar","Apr","May","Jun",
               "Jul","Aug","Sep","Oct","Nov","Dec"]
df["Month"] = pd.Categorical(df["Month"], categories=month_order, ordered=True)

# Pivot table: average dengue cases per month per year
heatmap_data = df.pivot_table(
    values="Dengue_Cases",
    index="Month",
    columns="Year",
    aggfunc="mean"
)

# Plot heatmap
plt.figure(figsize=(14, 6))
plt.imshow(heatmap_data, aspect="auto")
plt.colorbar(label="Average Dengue Cases")

plt.xticks(range(len(heatmap_data.columns)), heatmap_data.columns)
plt.yticks(range(len(heatmap_data.index)), heatmap_data.index)

plt.xlabel("Year")
plt.ylabel("Month")
plt.title("Heatmap of Average Dengue Cases by Month and Year")

plt.tight_layout()
plt.show()
