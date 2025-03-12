import streamlit as st

# Function to convert units
def convert_units(value, unit_from, unit_to):
    conversions = {
        # Length Conversions
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "meters_centimeters": 100,
        "centimeters_meters": 0.01,
        "meters_millimeters": 1000,
        "millimeters_meters": 0.001,
        "meters_miles": 0.000621371,
        "miles_meters": 1609.34,
        "meters_inches": 39.3701,
        "inches_meters": 0.0254,
        "meters_feet": 3.28084,
        "feet_meters": 0.3048,
        
        # Mass Conversions
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000,
        "grams_milligrams": 1000,
        "milligrams_grams": 0.001,
        "kilograms_pounds": 2.20462,
        "pounds_kilograms": 0.453592,
        "grams_ounces": 0.035274,
        "ounces_grams": 28.3495,
    }
    
    # Temperature conversion
    if unit_from == "Celsius" and unit_to == "Fahrenheit":
        return (value * 9/5) + 32
    elif unit_from == "Fahrenheit" and unit_to == "Celsius":
        return (value - 32) * 5/9
    
    # Regular unit conversion
    key = f"{unit_from}_{unit_to}"
    if key in conversions:
        return value * conversions[key]
    else:
        return "Conversion not supported"

# Streamlit UI
st.title("Advanced Unit Converter")

# User input
value = st.number_input("Enter value:", min_value=0.0, step=0.1)

# Unit categories
unit_categories = {
    "Length": ["meters", "kilometers", "centimeters", "millimeters", "miles", "inches", "feet"],
    "Mass": ["grams", "kilograms", "milligrams", "pounds", "ounces"],
    "Temperature": ["Celsius", "Fahrenheit"]
}
#select category
category_options = ["Length", "Mass", "Temperature"]  # List of categories
category = st.selectbox("Select Category:", category_options)  # Dropdown to select category


# Select units
unit_from = st.selectbox("Convert from:", unit_categories[category])
unit_to = st.selectbox("Convert to:", unit_categories[category])

# Convert button
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted Value: {result} {unit_to}")
