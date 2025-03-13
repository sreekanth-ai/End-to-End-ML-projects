import streamlit as st
import numpy as np
import joblib

# sved model
model = joblib.load("diabetes.pkl")

# App title
st.title("🩺 Diabetes Prediction App")

# Define feature input fields
Pregnancies = st.number_input("Pregnancies")
Glucose = st.number_input("Glucose")
BloodPressure = st.number_input("BloodPressure")
SkinThickness = st.number_input("SkinThickness")
Insulin = st.number_input("Insulin")
BMI = st.number_input("BMI")
DiabetesPedigreeFunction = st.number_input("DPF")
Age = st.number_input("Age")

# make prediction 
if st.button("Prediction"):
    input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
    # predctiction
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.error("⚠️ The patient is likely to have diabetes.")
    else:
        st.success("✅ The patient doesn't have diabetes.")