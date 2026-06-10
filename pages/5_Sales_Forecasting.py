import streamlit as st
import pandas as pd
import joblib

st.title("📈 Sales Forecasting")

try:
    model = joblib.load("models/sales_model.pkl")

except:
    st.error("Please train the model first.")
    st.stop()

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

product = st.selectbox(
    "Select Product",
    products
)

region = st.selectbox(
    "Select Region",
    regions
)

price = st.number_input(
    "Enter Price",
    min_value=1
)

year = st.number_input(
    "Year",
    value=2025
)

month = st.number_input(
    "Month",
    min_value=1,
    max_value=12,
    value=1
)

day = st.number_input(
    "Day",
    min_value=1,
    max_value=31,
    value=1
)

if st.button("Predict Sales"):

    product_code = products.index(product)
    region_code = regions.index(region)


    input_data = pd.DataFrame(
    [[
        product_code,
        region_code,
        price,
        year,
        month,
        day
    ]],
    columns=[
        "Product",
        "Region",
        "Price",
        "Year",
        "Month",
        "Day"
    ]
)

    prediction = model.predict(input_data)[0]

    st.success(
        f"Predicted Sales: {int(prediction)} Units"
    )