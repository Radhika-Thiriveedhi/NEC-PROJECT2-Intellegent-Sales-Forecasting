import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

st.title("🤖 Model Training")

try:
    df = pd.read_csv("data/cleaned_sales_data.csv")

except FileNotFoundError:
    st.error("Please run Data Preprocessing first.")
    st.stop()

# Encode categorical columns
df["Product"] = df["Product"].astype("category").cat.codes
df["Region"] = df["Region"].astype("category").cat.codes

# Features (Revenue removed to avoid data leakage)
X = df[
    [
        "Product",
        "Region",
        "Price",
        "Year",
        "Month",
        "Day"
    ]
]

# Target
y = df["Sales"]

# Dataset Information
st.subheader("Dataset Information")

col1, col2 = st.columns(2)

with col1:
    st.metric("Rows", len(df))

with col2:
    st.metric("Features", len(X.columns))

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Training
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

st.success("✅ Model Trained Successfully!")

# Metrics Display
st.subheader("Model Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("MAE", round(mae, 2))

with col2:
    st.metric("MSE", round(mse, 2))

with col3:
    st.metric("R² Score", round(r2, 2))

# Feature Importance
st.subheader("📊 Feature Importance")

importance_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

fig = px.bar(
    importance_df,
    x="Feature",
    y="Importance",
    title="Feature Importance Analysis"
)

st.plotly_chart(fig, use_container_width=True)

# Save Model
joblib.dump(
    model,
    "models/sales_model.pkl"
)

st.success("💾 Model Saved as sales_model.pkl")