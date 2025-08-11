import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title='Home_price_prediction', page_icon='home_icon.png')
st.header('Welcome to Bengaluru Home Price Predictor')

# Load data
df = pd.read_csv('copied.csv')

# Load trained model
with open('RFmodel.pkl', 'rb') as file:
    model = pickle.load(file)

# Sorted unique locations
locations = sorted(df['location'].unique())

with st.container(border=True):
    col1, col2 = st.columns(2)
    loc = col1.selectbox('Locations', options=locations)
    sqft = col2.number_input('Sqft', min_value=300)
    bath = col1.number_input('Bathroom', min_value=1)
    bhk = col2.number_input('Bedrooms', min_value=1)

    # Prepare input for prediction
    input_values = [(locations.index(loc), sqft, bath, bhk)]

    c1, c2, c3 = st.columns([1.6, 1.5, 1])
    if c2.button('predict_price'):
        out = model.predict(input_values)
        st.subheader(f'Total Price 💰: {out[0]*100000:.2f}')
