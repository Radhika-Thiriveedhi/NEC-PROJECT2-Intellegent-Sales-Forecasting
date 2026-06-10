import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Headphones",
    "Smart Watch"
]

regions = [
    "North",
    "South",
    "East",
    "West"
]

prices = {
    "Laptop": 60000,
    "Mobile": 25000,
    "Tablet": 18000,
    "Headphones": 3000,
    "Smart Watch": 5000
}

start_date = datetime(2023, 1, 1)

data = []

for i in range(5000):

    date = start_date + timedelta(days=np.random.randint(0, 730))

    product = np.random.choice(products)

    region = np.random.choice(regions)

    sales = np.random.randint(10, 200)

    price = prices[product]

    revenue = sales * price

    data.append([
        date.strftime("%Y-%m-%d"),
        product,
        region,
        sales,
        price,
        revenue
    ])

df = pd.DataFrame(
    data,
    columns=[
        "Date",
        "Product",
        "Region",
        "Sales",
        "Price",
        "Revenue"
    ]
)

df.to_csv("data/sales_data.csv", index=False)

print("Dataset created successfully!")
print(df.head())