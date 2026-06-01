import streamlit as st
import pickle
import pandas as pd
import numpy as np


# Load model
model = pickle.load(open("model.pkl", "rb"))
df=pd.read_csv('final.csv')

# Load columns
data_columns=(df.columns).to_list()
locs=set(df['location'].to_list())
# Extract location names
locations = []
for val in locs:
    locations.append(val)
locations.sort()

area_types = sorted(list(set(df['area_type'].to_list())))

st.title("🏠 Bengaluru House Price Predictor")

location = st.selectbox(
    "Location",
    sorted(locations)
)
area_type = st.selectbox("area_type", area_types)

sqft = st.number_input(
    "Total Sqft",
    min_value=300.0,
    value=1200.0
)

bath = st.number_input(
    "Bathrooms",
    min_value=1,
    value=2
)

size = st.number_input(
    "size",
    min_value=1,
    value=2
)

availability = st.selectbox(
    "Availability",
    [0, 1]
)

balcony = st.number_input(
    "Balcony",
    min_value=0,
    value=1
)


if st.button("Predict Price"):

    #x = np.zeros(len(data_columns))

    #x=[area_type,availability,location,sqft,bath,balcony,size]
    input_df = pd.DataFrame({
        'area_type': [area_type],
        'availability': [availability],
        'location': [location],
        'total_sqft': [sqft],
        'bath': [bath],
        'balcony': [balcony],
        'bhk': [size]
    })

    prediction = model.predict(input_df)[0]
    # Adjust indexes according to your X.columns order
    #x[data_columns.index('availability')] = availability
    #x[data_columns.index('size')] = size
    #x[data_columns.index('total_sqft')] = sqft
    #x[data_columns.index('bath')] = bath
    #x[data_columns.index('balcony')] = balcony


    st.success(
        f"Estimated Price: ₹ {prediction:.2f} Lakhs"
    )

