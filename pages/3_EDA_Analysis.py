import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Exploratory Data Analysis")

try:
    df = pd.read_csv("data/cleaned_sales_data.csv")

except FileNotFoundError:
    st.error("Please run Data Preprocessing first.")
    st.stop()

# Sales Trend
st.subheader("📈 Sales Trend Over Time")

sales_trend = (
    df.groupby("Date")["Sales"]
    .sum()
    .reset_index()
)

fig1 = px.line(
    sales_trend,
    x="Date",
    y="Sales",
    title="Daily Sales Trend"
)

st.plotly_chart(fig1, use_container_width=True)

# Product-wise Sales
st.subheader("📦 Product-wise Sales")

product_sales = (
    df.groupby("Product")["Sales"]
    .sum()
    .reset_index()
)

fig2 = px.bar(
    product_sales,
    x="Product",
    y="Sales",
    color="Product",
    title="Sales by Product"
)

st.plotly_chart(fig2, use_container_width=True)

# Region-wise Revenue
st.subheader("🌍 Region-wise Revenue")

region_sales = (
    df.groupby("Region")["Revenue"]
    .sum()
    .reset_index()
)

fig3 = px.pie(
    region_sales,
    names="Region",
    values="Revenue",
    title="Revenue Contribution by Region"
)

st.plotly_chart(fig3, use_container_width=True)

# Monthly Revenue
st.subheader("💰 Monthly Revenue")

revenue_trend = (
    df.groupby("Month")["Revenue"]
    .sum()
    .reset_index()
)

fig4 = px.bar(
    revenue_trend,
    x="Month",
    y="Revenue",
    title="Monthly Revenue"
)

st.plotly_chart(fig4, use_container_width=True)