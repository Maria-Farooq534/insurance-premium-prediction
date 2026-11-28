import streamlit as st
import requests
import os

API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000/predict"
)

st.title("Insurance Premium Category Prediction")
st.markdown("Enter your details below:")


age = st.number_input("Age", min_value=1, max_value=120, value=30)
weight = st.number_input("Weight in Kg", min_value=1, max_value=150, value=60)
height = st.number_input("Height in meters", min_value=0.5, max_value=2.5, value=1.6)
income_lpa = st.number_input("Income in LPA", min_value=0.1, max_value=10.0, value=5.0)
smoker = st.selectbox("Are you a smoker", options=[True, False])
city = st.text_input("City", value="Karachi")
occupation = st.selectbox("Occupation", ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job'])

if st.button("Predict Premium Category"):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }
    
    try:
        response = requests.post(API_URL, json=input_data)
        response.raise_for_status()
        result = response.json()["predicted_category"]

        st.success(
            f"Predicted premium category: "
            f"{result['predicted_category']}"
        )
        st.write(f"Confidence: {result['confidence']:.0%}")
        
        st.write("📊 Class Probabilities:")

        st.json(result["class_probabilities"])

    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {e}")

        
    
