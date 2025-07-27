import streamlit as st
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder,OneHotEncoder
import pickle

model=tf.keras.models.load_model('model.h5')
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f) 
with open('one_hot_encoder.pkl', 'rb') as f:
    encoder = pickle.load(f)    
with open('label_encoder_gender.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

# streamlit app
st.title('Customer Churn Prediction')


geography = st.selectbox('Geography', encoder.categories_[0])   
gender = st.selectbox('Gender',label_encoder.classes_)
age=st.slider('Age', min_value=18, max_value=100, value=30, step=1)
balance = st.number_input('Balance')
credit_score=st.number_input('Credit Score')
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure', min_value=0, max_value=10, value=5, step=1)
number_of_products = st.slider('Number of Products', min_value=1, max_value=4, value=2, step=1) 
has_cr_card = st.selectbox('Has Credit Card', ['Yes', 'No'])
is_active_member = st.selectbox('Is Active Member', ['Yes', 'No'])

# prepare input data
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [1 if gender == 'Male' else 0],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [number_of_products],
    'HasCrCard': [1 if has_cr_card == 'Yes' else 0],
    'IsActiveMember': [1 if is_active_member == 'Yes' else 0],
    'EstimatedSalary': [estimated_salary], 
})

st.write(input_data)
st.write(input_data.dtypes)

# ...existing code...

# onehot encode geography
geography_encoded = encoder.transform([[geography]]).toarray()
geography_df = pd.DataFrame(geography_encoded, columns=encoder.get_feature_names_out(['Geography']))

# concatenate all features
input_data = pd.concat([input_data.reset_index(drop=True), geography_df], axis=1)

# Ensure column order matches training
expected_columns = [
    'CreditScore', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts',
    'HasCrCard', 'IsActiveMember', 'EstimatedSalary',
    'Geography_France', 'Geography_Germany', 'Geography_Spain'
]
input_data = input_data[expected_columns]

# scaling
input_data_scaled = scaler.transform(input_data)

# prediction churn
prediction = model.predict(input_data_scaled)
prediction_proba = prediction[0][0]

if prediction_proba > 0.5:
    st.write(f"**Churn Probability:** {prediction_proba:.2f} - The customer is likely to churn.")
else:
    st.write(f"**Churn Probability:** {prediction_proba:.2f} - The customer is likely to stay.")