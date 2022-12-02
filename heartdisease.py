import pickle
import streamlit as st

# load save model
model = pickle.load(open('heart_disease.sav', 'rb'))

# judul web
st.title('Predict Your Heart Disease')

col1, col2, col3 = st.columns(3)
with col1:
    Age = st.text_input('Age')
with col2:
    RestingBP = st.text_input("RestingBP")
with col3:
    Cholesterol = st.text_input('Cholesterol')
with col1:
    MaxHR = st.text_input('MaxHR')
with col2:
    FastingBS = st.text_input('FastingBS')

# code for prediction
heart_diagnosis = ''

# membuat tombol prediksi
if st.button('predict heart disease'):
    heart_prediction = model.predict([[Age, RestingBP, Cholesterol, MaxHR, FastingBS]])

    if(heart_prediction[0]==1):
        heart_diagnosis = 'Sorry, you have heart disease'
    else:
        heart_diagnosis = 'Congratulation, you are healthy!'
st.success(heart_diagnosis)