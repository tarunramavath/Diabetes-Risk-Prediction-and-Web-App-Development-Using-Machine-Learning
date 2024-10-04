# imports necessary libraries. streamlit is used to create the web application
import streamlit as st
import numpy as np
import pickle

#Reading pickle file as file
with open('final_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)# Load the model from the pickle file

# Define the mean and standard deviation of the training data
mean_values = [41.885856, 0.07485, 0.03942, 27.320767, 5.527507, 138.058060]
std_values = [22.516840, 0.26315, 0.194593, 6.636783, 1.070672, 40.708136]

# Create a Streamlit app title of streamlit page
st.title('Diabetes Prediction')

# Define input sliders for user input
age = st.slider('Age', min_value=0, max_value=100, value=50)
hypertension = st.slider('Hypertension', min_value=0, max_value=1, value=0)
heart_disease = st.slider('Heart Disease', min_value=0, max_value=1, value=0)
bmi = st.slider('BMI', min_value=10.0, max_value=50.0, value=25.0, step=0.1)
HbA1c_level = st.slider('HbA1c Level', min_value=4.0, max_value=15.0, value=7.0, step=0.1)
blood_glucose_level = st.slider('Blood Glucose Level', min_value=50, max_value=400, value=100)

# Function to scale the input features manually
def scale_features(age, hypertension, heart_disease, bmi, HbA1c_level, blood_glucose_level):
    scaled_features = [(x - mean) / std for x, mean, std in zip(
        [age, hypertension, heart_disease, bmi, HbA1c_level, blood_glucose_level],
        mean_values, std_values
    )]
    return scaled_features

# Function to make predictions
def make_prediction(scaled_features):
    prediction = loaded_model.predict([scaled_features])
    return prediction

# Predict button
if st.button('Predict'):
    scaled_features = scale_features(age, hypertension, heart_disease, bmi, HbA1c_level, blood_glucose_level)
    prediction = make_prediction(scaled_features)
    st.write('Prediction:', 'Diabetic' if prediction[0] == 1 else 'Not Diabetic')
