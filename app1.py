import streamlit as st
import pandas as pd

st.title("BMI Calculator")

height=st.slider("Enter your heigt in centimeters",100,250,150)
weight=st.slider("Enter your weight in KiloGrams",10,150,40)
age=st.slider("Enter age in years",1,100,20)


bmi=weight/((height/100)**2)
if st.button('My BMI'):
    st.write(f"your BMI is {bmi:.2f}")
st.write("### BMI Categories")
st.write("--Underweight:BMI less than 18.5")
st.write("--Normal:BMI between 18.5and 24.9")
st.write("--Overweight:BMI between 25and 29.9")
st.write("--Obesity:BMI greater than 30")