import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Intelligent Sales Dashboard")

try:
    df = pd.read_csv("data/cleaned_sales_data.csv")

except FileNotFoundError:
    st.error("Please run Data Preprocessing first.")
    st.stop()

# =========================
# KPI SECTION
# =========================

total_sales = df["Sales"].sum()
total_revenue = df["Revenue"].sum()
avg_sales = round(df["Sales"].mean(), 2)
total_products = df["Product"].nunique()

st.subheader("📌 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"{total_sales:,}")
col2.metric("Total Revenue", f"₹{total_revenue:,}")
col3.metric("Average Sales", avg_sales)
col4.metric("Products", total_products)

# =========================
# SALES TREND
# =========================

st.subheader("📈 Sales Trend")

sales_trend = (
    df.groupby("Date")["Sales"]
    .sum()
    .reset_index()
)

fig1 = px.line(
    sales_trend,
    x="Date",
    y="Sales",
    title="Sales Trend"
)

st.plotly_chart(fig1, use_container_width=True)

# =========================
# PRODUCT PERFORMANCE
# =========================

st.subheader("📦 Product Performance")

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
    title="Product-wise Sales"
)

st.plotly_chart(fig2, use_container_width=True)

# =========================
# REGION PERFORMANCE
# =========================

st.subheader("🌍 Region Performance")

region_sales = (
    df.groupby("Region")["Revenue"]
    .sum()
    .reset_index()
)

fig3 = px.pie(
    region_sales,
    names="Region",
    values="Revenue",
    title="Region-wise Revenue"
)

st.plotly_chart(fig3, use_container_width=True)

# =========================
# TOP PRODUCT
# =========================

top_product = (
    df.groupby("Product")["Sales"]
    .sum()
    .idxmax()
)

st.success(f"🏆 Top Selling Product: {top_product}")

# =========================
# BUSINESS INSIGHTS
# =========================

st.subheader("💡 Business Insights")

st.info(
    """
    • Monitor high-demand products closely.
    
    • Maintain safety stock to avoid stockouts.
    
    • Use sales forecasts for inventory planning.
    
    • Focus marketing efforts on top-performing products.
    """
)