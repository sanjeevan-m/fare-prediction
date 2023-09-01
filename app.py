import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained regression model
model_path = 'C:\\Users\\Vaidees\\last\\fare_prediction\\data\\model.pkl'

with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

st.title("Total Fare Calculator")

# Section for user input
st.header("Fill Following Details :")

# Input fields for user input
trip_duration_minutes = st.number_input("Trip Duration (minutes)", 1, 3000, 30)
trip_duration_seconds = trip_duration_minutes * 60  # Convert minutes to seconds

distance_traveled = st.number_input("Distance Traveled (miles)", 0.1, 50.0, 5.0)
num_of_passengers = st.number_input("Number of Passengers", 1, 6, 1)
surge_applied = st.selectbox("Surge Applied", ["No", "Yes"])
surge_applied = 1 if surge_applied == "Yes" else 0

tip = st.number_input("Tip ($)", 0.0, 100.0, 2.0)
miscellaneous_fees = st.number_input("Miscellaneous Fees ($)", 0.0, 200.0, 0.0)

# "Calculate Total Fare" button to trigger fare prediction and total fare calculation
if st.button("Calculate Total Fare"):
    # Predict fare using the loaded regression model
    input_data = [[trip_duration_seconds, distance_traveled, num_of_passengers, surge_applied]]
    predicted_fare = model.predict(input_data)[0]

    # Calculate total fare
    total_fare = predicted_fare + tip + miscellaneous_fees

    st.header("Total Fare Results")
    st.text(f"Predicted Fare: {predicted_fare:.2f}")
    st.text(f"Total Fare: {total_fare:.2f}")
