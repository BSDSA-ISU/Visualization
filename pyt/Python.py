
# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# Load your dataset (replace with your actual file path)
df = pd.read_csv("philippines_employment_restructured.csv")

# Create a Date column for plotting
df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(Day=1))

# Sort by date
df = df.sort_values('Date')

# 1. Line Chart: Employment Rate over Time
plt.figure()
sns.lineplot(data=df, x='Date', y='Employment_Rate (%)', marker='o', color='blue')
plt.title('Employment Rate (%) Over Time')
plt.xlabel('Date')
plt.ylabel('Employment Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Stacked Bar Chart: Sector Employment Distribution per Year
sector_df = df.groupby('Year')[['Services_Employed (millions)',
                                'Agriculture_Employed (millions)',
                                'Industry_Employed (millions)']].mean()

sector_df.plot(kind='bar', stacked=True, colormap='Set2')
plt.title('Average Sector Employment Distribution per Year')
plt.ylabel('Employed Persons (millions)')
plt.xlabel('Year')
plt.xticks(rotation=45)
plt.legend(title='Sector')
plt.tight_layout()
plt.show()

# 3. Combo Chart: Employment Rate vs. Employed Persons
fig, ax1 = plt.subplots()

# Bar chart for Employed Persons
ax1.bar(df['Date'], df['Employed_Persons (millions)'], color='skyblue', label='Employed Persons (millions)')
ax1.set_xlabel('Date')
ax1.set_ylabel('Employed Persons (millions)', color='skyblue')
ax1.tick_params(axis='y', labelcolor='skyblue')

# Line chart for Employment Rate
ax2 = ax1.twinx()
ax2.plot(df['Date'], df['Employment_Rate (%)'], color='darkred', marker='o', label='Employment Rate (%)')
ax2.set_ylabel('Employment Rate (%)', color='darkred')
ax2.tick_params(axis='y', labelcolor='darkred')

plt.title('Employment Rate (%) vs. Employed Persons (millions)')
fig.tight_layout()
plt.show()
