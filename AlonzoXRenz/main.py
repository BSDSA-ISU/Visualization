import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

# STEP 1: GENERATE THE DATASET (100 Rows)
print("Generating 100 rows of Sales Data...")

# Define categories
products = ['Laptops', 'Headphones', 'Smartphones', 'Monitors', 'Keyboards', 'Mice']
channels = ['Online', 'Offline']
regions = ['North', 'South', 'East', 'West']

data = []

for i in range(100):
    product = random.choice(products)
    channel = random.choice(channels)
    region = random.choice(regions)
    
    # Assign realistic prices
    if product == 'Laptops': price = random.randint(800, 1500)
    elif product == 'Smartphones': price = random.randint(500, 1000)
    elif product == 'Monitors': price = random.randint(150, 400)
    elif product == 'Headphones': price = random.randint(50, 200)
    else: price = random.randint(20, 100)
        
    units_sold = random.randint(1, 10)
    total_revenue = price * units_sold
    
    # Calculate profit (random margin between 15% and 40%)
    margin = random.uniform(0.15, 0.40)
    total_profit = round(total_revenue * margin, 2)
    
    data.append([product, channel, region, price, units_sold, total_revenue, total_profit])

# Create DataFrame
columns = ['Product', 'Sales_Channel', 'Region', 'Unit_Price', 'Units_Sold', 'Total_Revenue', 'Total_Profit']
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv("sales_data_100_rows.csv", index=False)
print("✅ Dataset saved as 'sales_data_100_rows.csv'")

# STEP 2: CREATE 3 VISUALIZATIONS
sns.set(style="whitegrid")

# --- CHART 1: Clustered Bar Chart (Revenue by Product & Channel) ---
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Product', y='Total_Revenue', hue='Sales_Channel', estimator=sum, errorbar=None)
plt.title('Total Revenue by Product and Channel', fontsize=14, fontweight='bold')
plt.ylabel('Total Revenue ($)')
plt.tight_layout()
plt.savefig('chart1_bar_revenue.png')
print("✅ Chart 1 saved as 'chart1_bar_revenue.png'")
plt.show()

# CHART 2: Pie Chart (Sales Share by Region)
# We need to aggregate data for the pie chart
region_data = df.groupby('Region')['Total_Revenue'].sum()

plt.figure(figsize=(8, 8))
plt.pie(region_data, labels=region_data.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title('Market Share by Region', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('chart2_pie_region.png')
print("✅ Chart 2 saved as 'chart2_pie_region.png'")
plt.show()

# CHART 3: Scatter Plot (Price vs. Units Sold - "Demand Analysis")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Unit_Price', y='Units_Sold', hue='Product', s=100, alpha=0.7)
plt.title('Correlation: Unit Price vs. Volume Sold', fontsize=14, fontweight='bold')
plt.xlabel('Unit Price ($)')
plt.ylabel('Units Sold per Transaction')
plt.grid(True)
plt.tight_layout()
plt.savefig('chart3_scatter_demand.png')
print("✅ Chart 3 saved as 'chart3_scatter_demand.png'")
plt.show()
