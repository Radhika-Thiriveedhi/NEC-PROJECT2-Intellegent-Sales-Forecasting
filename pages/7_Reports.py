import streamlit as st
import pandas as pd

st.title("📄 Reports")

try:
    df = pd.read_csv("data/cleaned_sales_data.csv")

except FileNotFoundError:
    st.error("Please run Data Preprocessing first.")
    st.stop()

# Dataset Preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Summary Statistics
st.subheader("Summary Statistics")
st.dataframe(df.describe())

# Business Summary
st.subheader("Business Summary")

total_sales = int(df["Sales"].sum())
total_revenue = int(df["Revenue"].sum())
top_product = df.groupby("Product")["Sales"].sum().idxmax()
top_region = df.groupby("Region")["Revenue"].sum().idxmax()

st.write(f"**Total Sales:** {total_sales:,}")
st.write(f"**Total Revenue:** ₹{total_revenue:,}")
st.write(f"**Top Product:** {top_product}")
st.write(f"**Best Region:** {top_region}")

# Download Report
csv = df.to_csv(index=False)

st.download_button(
    label="📥 Download Report",
    data=csv,
    file_name="sales_report.csv",
    mime="text/csv"
)

st.success("Report Ready!")