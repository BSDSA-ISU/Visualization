import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./denguecases.csv")

print(df.head(5))

print(df.describe())

yearly_rate = (
    df.groupby("Year", as_index=False)["Dengue_Cases"]
      .mean()
)

plt.figure(figsize=(10, 5))
plt.plot(
    yearly_rate["Year"],
    yearly_rate["Dengue_Cases"],
    marker="o"
)

plt.title("Average Annual Dengue Incidence Rate in the Philippines (2008–2016)")
plt.xlabel("Year")
plt.ylabel("Dengue Cases per 100,000 Population")
plt.grid(True)

plt.tight_layout()
plt.show()


### Bar Graph ###
region_rates = (
    df.groupby("Region", as_index=False)["Dengue_Cases"]
      .mean()
      .sort_values("Dengue_Cases", ascending=False)
)


colors = plt.cm.tab20.colors  # enough distinct colors

plt.figure(figsize=(10, 5))
plt.bar(
    region_rates["Region"],
    region_rates["Dengue_Cases"],
    color=colors[:len(region_rates)],
    label=region_rates["Region"]
)

plt.title("average Dengue Cases Per 100,000 Population (2008–2016)")
plt.xlabel("Region")
plt.ylabel("Total Dengue Cases")

plt.xticks(rotation=45, ha="right")
plt.grid(axis="y")

plt.legend(title="Region", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.show()
