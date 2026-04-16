import google.generativeai as genai
import streamlit as st

genai.configure(api_key="AIzaSyDuI2XIIzTwmg2pLn0nTPJmg0JktOd9nLA")
model=genai.GenerativeModel("gemini-2.5-flash")

st.title("AI based BMI calculator- know your health!")
name=st.text_input("Enter your name")
weight=st.number_input("Enter your weight in kg")
height=st.slider("Enter your height in cm",50,300)
age=st.number_input("Enter your age")
gender=st.text_input("Enter your gender")

bmi=round((weight/(height/100)**2),2)

st.write(f"{name}, your BMI is{bmi}")

prompt=f"act like nutritionist and comment on bmi with the following data:height as {height},weight as {weight},age as {age}"

response=model.generate_content(prompt)
st.markdown(response.text)




