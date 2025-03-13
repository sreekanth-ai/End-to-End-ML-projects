import streamlit as st
import joblib
import numpy as np
import pandas as pd
# Load the trained Ridge Regression model
model = joblib.load('house.pkl')

# Define feature input fields
st.title("House Price Prediction App")

lotsize = st.number_input("Lotsize")
bedrooms = st.number_input("bedrooms")
bathrms = st.number_input("bathrooms")
stories = st.number_input("stories")
garagepl = st.number_input("garagepl")

# Make prediction
if st.button("Prediction"):
    input_data = np.array([[lotsize, bedrooms, bathrms, stories, garagepl]])
    
    # Predict
    prediction = model.predict(input_data)[0]
    
    # Display result
    st.success(f"🏠 Estimated House Price: ${prediction:,.2f}")