import streamlit as st
import pandas as pd

st.title("📂 Data Upload")

uploaded_file = st.file_uploader(
    "Upload Sales Dataset",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)
    df.to_csv("data/uploaded_sales_data.csv", index=False)

    st.success("Dataset Uploaded Successfully!")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Shape")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    st.subheader("Column Names")

    st.write(df.columns.tolist())

    st.subheader("Data Types")

    st.dataframe(df.dtypes.astype(str))

    st.subheader("Summary Statistics")

    st.dataframe(df.describe())

else:
    st.info("Please upload a CSV file.")