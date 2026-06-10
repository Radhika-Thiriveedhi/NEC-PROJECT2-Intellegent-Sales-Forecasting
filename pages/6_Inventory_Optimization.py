import streamlit as st

st.title("📦 Inventory Optimization")

forecast_sales = st.number_input(
    "Enter Forecasted Sales",
    min_value=1,
    value=100
)

lead_time = st.number_input(
    "Lead Time (Days)",
    min_value=1,
    value=7
)

if st.button("Calculate Inventory"):

    safety_stock = forecast_sales * 0.20

    reorder_point = forecast_sales * lead_time

    recommended_inventory = (
        forecast_sales + safety_stock
    )

    st.subheader("Inventory Recommendations")

    st.metric(
        "Safety Stock",
        int(safety_stock)
    )

    st.metric(
        "Reorder Point",
        int(reorder_point)
    )

    st.metric(
        "Recommended Inventory",
        int(recommended_inventory)
    )