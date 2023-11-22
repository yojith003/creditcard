# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st
from sklearn.preprocessing import StandardScaler
# Loading saved model
loaded_model = pickle.load(open('creditcard_trained.sav', 'rb'))
# Creating prediction
def credit_card_prediction(input_data):
    # Converting input data to numeric values
    input_data = [float(x) for x in input_data]
    # Changing the input_data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    scaler = StandardScaler()
    scaler.fit(input_data_reshaped)
    std_data=scaler.transform(input_data_reshaped)
    prediction = loaded_model.predict(std_data)
    if prediction== 0:
        return 'The user is a Valid User'
    else:
        return 'The user is an Invalid User'

def main():
    
    # Giving title
    st.title('Valid Credit Card User Prediction')
    # Getting input data from the user
   
    V1 = st.text_input('V1 Value')
    V2 = st.text_input('V2 Value')
    V3 = st.text_input('V3 Value')
    V4 = st.text_input('V4 Value')
    V5 = st.text_input('V5 Value')
    V6 = st.text_input('V6 Value')
    V7 = st.text_input('V7 Value')
    V8 = st.text_input('V8 Value')
    V9 = st.text_input('V9 Value')
    V10 = st.text_input('V10 Value')
    V11 = st.text_input('V11 Value')
    V12 = st.text_input('V12 Value')
    V13 = st.text_input('V13 Value')
    V14 = st.text_input('V14 Value')
    V15 = st.text_input('V15 Value')
    V16 = st.text_input('V16 Value')
    V17 = st.text_input('V17 Value')
    V18 = st.text_input('V18 Value')
    V19 = st.text_input('V19 Value')
    V20 = st.text_input('V20 Value')
    V21 = st.text_input('V21 Value')
    V22 = st.text_input('V22 Value')
    V23 = st.text_input('V23 Value')
    V24 = st.text_input('V24 Value')
    V25 = st.text_input('V25 Value')
    V26 = st.text_input('V26 Value')
    V27 = st.text_input('V27 Value')
    V28 = st.text_input('V28 Value')
    Amount = st.text_input('Amount')
    # Code for prediction
    diagnosis = ""
    if st.button("User Result"):
        input_data = [V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, 
        V14, V15, V16, V17, V18, V19, V20, V21,
        V22, V23, V24, V25, V26, V27, V28, Amount]
        diagnosis = credit_card_prediction(input_data)
    
    st.success(diagnosis)

if __name__ == '__main__':
    main()
