import streamlit as st
import joblib
import pandas as pd

# Load Model
model = joblib.load('gold_price_forecasting_model.pkl')

st.title("📈 Global Supply Chain Commodity Price Forecasting")
st.markdown("---")
st.subheader("Gold Price Prediction System")

st.write("Enter Commodity Details")

open_price = st.number_input("Open Price")
high_price = st.number_input("High Price")
low_price = st.number_input("Low Price")
volume = st.number_input("Volume")

year = st.number_input("Year", min_value=2000, max_value=2100)
month = st.number_input("Month", min_value=1, max_value=12)
day = st.number_input("Day", min_value=1, max_value=31)

if st.button("Predict Gold Price"):

    data = pd.DataFrame({
        'Open':[open_price],
        'High':[high_price],
        'Low':[low_price],
        'Volume':[volume],
        'Year':[year],
        'Month':[month],
        'Day':[day]
    })

    prediction = model.predict(data)

    st.success(f"💰 Predicted Gold Close Price: {prediction[0]:.2f}")