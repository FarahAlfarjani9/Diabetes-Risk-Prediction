import joblib
import streamlit as st
import numpy as np

model= joblib.load("model.joblib")

st.title("Diabetes Risk Prediction")
#_________
gender = st.selectbox("Gender",["Female", "Male"], index=None,
   placeholder="Select gender...")

gender_code = None
if gender is not None:
  gender_code = 0 if gender == "Female" else 1
#____________
age= st.number_input("Age",   min_value=1,max_value=100,
     placeholder="Enter Your Age...")
#____________
hypertension= st.selectbox("Hypertension", ["Yes", "No"] ,index=None)
hypertension_code= None
if hypertension is not None:
    hypertension_code=0 if hypertension=="No" else 1
#____________
heart_disease = st.selectbox("Heart Disease",  ["Yes", "No"] ,index=None)
heart_disease_code= None
if heart_disease is not None:
    heart_disease_code= 0 if heart_disease=="No" else 1
#____________
smoking_history= st.selectbox("Smoking History", ["never","current","former","ever","not current"] ,index=None)
code_map = {
    "No Info": 0,
    "never": 4,
    "current": 1,
    "former": 3,
    "ever": 2,
    "not current": 5,
}
smoking_history_code = code_map.get(smoking_history)
#____________
bmi= st.number_input("BMI")
#____________
HbA1c_level=st.number_input("HbA1c Level")     
#____________
blood_glucose_level = st.number_input("Blood Glucose Level")
#____________
#diabetes
if st.button("Risk Prediction"):
    if None in [gender_code,age, hypertension_code, heart_disease_code, smoking_history_code,bmi,HbA1c_level,blood_glucose_level]:
        st.warning("Please fill in all required fields")
    else:
        features=np.array([gender_code,age,hypertension_code,heart_disease_code,smoking_history_code,bmi,HbA1c_level,blood_glucose_level]).reshape(1,-1)
        prediction= model.predict(features)[0]
     
        result="Diabetic (Positive)" if prediction==1 else "Not Diabetic (Negative)"
        st.success(result)
#____________
