import requests
import streamlit as st

API_URL = "https://cal-3iqk.onrender.com/calculate"   # your backend Render URL

st.title("🧮 Simple Calculator")

num1 = st.number_input("Enter first number", value=0.0, format="%.2f")
num2 = st.number_input("Enter second number", value=0.0, format="%.2f")
operation = st.selectbox("Choose operation", ["add", "subtract", "multiply", "divide"])

if st.button("Calculate"):
    try:
        response = requests.post(API_URL, json={"num1": num1, "num2": num2, "operation": operation})
        if response.status_code == 200:
            result = response.json().get("result")
            st.success(f"Result: {result}")
        else:
            st.error(f"Error: {response.text}")
    except Exception as e:
        st.error(f"Request failed: {e}")
