import streamlit as st
import pandas as pd

st.title("🧹 Data Preprocessing")

# Load uploaded dataset
try:
    df = pd.read_csv("data/uploaded_sales_data.csv")

except FileNotFoundError:
    st.error("Please upload dataset first.")
    st.stop()

# Original shape
st.subheader("Original Dataset Shape")
st.write(df.shape)

# Remove duplicates
duplicates = df.duplicated().sum()

if duplicates > 0:
    df = df.drop_duplicates()

st.write(f"Duplicates Removed: {duplicates}")

# Missing values
missing_values = df.isnull().sum()

st.subheader("Missing Values")
st.dataframe(missing_values)

# Fill missing values
df = df.fillna(0)

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Feature Engineering
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day

# Preview
st.subheader("Processed Dataset Preview")
st.dataframe(df.head())

# Updated shape
st.subheader("Updated Dataset Shape")
st.write(df.shape)

# Save cleaned dataset
df.to_csv("data/cleaned_sales_data.csv", index=False)

st.success("Cleaned dataset saved successfully!")