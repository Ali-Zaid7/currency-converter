import streamlit as st

# Set the page title
st.title("Unit Converter")

# Define a list of units
units = ["Meters", "Kilometers", "Miles", "Feet"]

# Select the input unit
input_unit = st.selectbox("Select the input unit:", units)

# Select the output unit
output_unit = st.selectbox("Select the output unit:", units)

# Input value from the user
value = st.number_input(f"Enter the value in {input_unit}:")

# Conversion factors dictionary
conversion_factors = {
    "Meters": {"Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084, "Meters": 1},
    "Kilometers": {"Meters": 1000, "Miles": 0.621371, "Feet": 3280.84, "Kilometers": 1},
    "Miles": {"Meters": 1609.34, "Kilometers": 1.60934, "Feet": 5280, "Miles": 1},
    "Feet": {"Meters": 0.3048, "Kilometers": 0.0003048, "Miles": 0.000189394, "Feet": 1},
}

# Perform conversion
if input_unit and output_unit:
    converted_value = value * conversion_factors[input_unit][output_unit]
    st.write(f"{value} {input_unit} is equal to {converted_value} {output_unit}.")

