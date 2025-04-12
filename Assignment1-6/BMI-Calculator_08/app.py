import streamlit as st

# Set Page Title (No Icon)
st.set_page_config(page_title="BMI Calculator")

# Title
st.title("BMI Calculator")

# User Input
height = st.slider("Enter your height (in cm):", 100, 250, 170)
weight = st.slider("Enter your weight (in kg):", 40, 200, 70)

# BMI Calculation
bmi = weight / ((height / 100) ** 2)

# Display BMI
st.subheader(f"Your BMI: {bmi:.2f}")

# BMI Categories
st.write("### BMI Categories:")
if bmi < 18.5:
    st.warning("Underweight: BMI less than 18.5")
elif 18.5 <= bmi < 24.9:
    st.success("Normal weight: BMI between 18.5 and 24.9")
elif 25 <= bmi < 29.9:
    st.warning("Overweight: BMI between 25 and 29.9")
else:
    st.error("Obesity: BMI 30 or greater")
