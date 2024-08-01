# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 16:45:27 2024

@author: rutvi
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/rutvi/OneDrive/Documents/ML_Practice/trained_model.sav','rb'))

#creating a function for prediction

def heart_disease_prediction(input_data):
   
    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    #print(prediction)

    if(prediction[0]==1):
      return'The Person has heart disease'
    else:
      return 'The person is good'
  
    
def main():
    
    # giving a title
    st.title('Heart Disease Prediction Web APP')
    
    #getting the input data from the user
    
    Age = st.text_input('Age of the person')
    sex = st.text_input('Sex')
    cp = st.text_input('Chest Pain Type')
    bp = st.text_input('What is the Blood pressure')
    Cholesterol = st.text_input('What is the cholestrol level')
    fbs = st.text_input('FBS over 120')
    restecg = st.text_input('ECG results')
    thalach = st.text_input('Max HR')
    exang  = st.text_input('Exercise angina')
    oldpeak = st.text_input('ST depression')
    slope = st.text_input('Slope of ST')
    ca = st.text_input('Number of vessels fluro')
    thal = st.text_input('Thallium')
    
    #code for diagnosis
    
    diagnosis = ''
    
    #creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        input_data = [float(Age), float(sex), float(cp), float(bp), float(Cholesterol), float(fbs), 
                          float(restecg), float(thalach), float(exang), float(oldpeak), float(slope), 
                          float(ca), float(thal)]
        diagnosis = heart_disease_prediction(input_data)
    
    st.success(diagnosis)
    
    
if __name__ == '__main__':
    main()