import streamlit as st
import requests

# Streamlit app title
st.title("🧮 Simple Calculator")

# User inputs
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

operation = st.selectbox("Choose operation", ["add", "subtract", "multiply", "divide"])

# Button to calculate
if st.button("Calculate"):
    try:
        # Send request to Flask backend
        response = requests.post(
            API_URL = "https://cal-3iqk.onrender.com/calculate"
,
            json={"num1": num1, "num2": num2, "operation": operation}
        )

        if response.status_code == 200:
            result = response.json().get("result", "Error")
            st.success(f"Result: {result}")
        else:
            st.error("Error: Unable to connect to backend")

    except Exception as e:
        st.error(f"Request failed: {e}")

