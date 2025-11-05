import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("sales_data_sample.csv", encoding='latin1')

# Keep relevant columns
df = df[['ORDERNUMBER', 'QUANTITYORDERED', 'PRICEEACH', 'ORDERDATE', 'PRODUCTLINE', 'STATUS', 'COUNTRY']]

df['REVENUE'] = df['QUANTITYORDERED'] * df['PRICEEACH']


df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce')


df = df.dropna(subset=['ORDERDATE'])

#KPIs
total_revenue = df['REVENUE'].sum()
best_product_line = df.groupby('PRODUCTLINE')['REVENUE'].sum().idxmax()
daily_sales = df.groupby(df['ORDERDATE'].dt.date)['REVENUE'].sum()

print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Best-Selling Product Line: {best_product_line}")
print("\nDaily Sales Sample:")
print(daily_sales.head())

# Plot daily revenue trend
plt.figure(figsize=(8,4))
plt.plot(daily_sales.index, daily_sales.values, marker='o', linewidth=1)
plt.title("Daily Revenue Trend")
plt.xlabel("Date")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.show()
