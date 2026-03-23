import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

# Total Revenue
total_revenue = df["Total_Sales"].sum()

# Best Selling Product
best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()

# Average Sales
average_sales = df["Total_Sales"].mean()

# Print Results
print("Sales Analysis Report")
print("---------------------")
print("Total Revenue:", total_revenue)
print("Best Product:", best_product)
print("Average Sales:", average_sales)