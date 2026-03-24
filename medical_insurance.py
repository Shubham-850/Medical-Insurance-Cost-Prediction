import streamlit as st
import joblib
import pandas as pd

# Load model and columns
model = joblib.load("insurance_model.pkl")
columns = joblib.load("columns.pkl")

# Title
st.title("💰 Medical Insurance Cost Predictor")

st.write("Enter your details below:")

# User Inputs
age = st.slider("Age", 18, 65)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0)
children = st.number_input("Number of Children", 0, 5)

sex = st.selectbox("Sex", ["male", "female"])
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox(
    "Region",
    ["northeast", "northwest", "southeast", "southwest"]
)

# Predict Button
if st.button("Predict Insurance Cost"):

    # Create input dictionary
    input_dict = {
        "age": age,
        "bmi": bmi,
        "children": children,
        "sex_male": 1 if sex == "male" else 0,
        "smoker_yes": 1 if smoker == "yes" else 0,
        "region_northwest": 0,
        "region_southeast": 0,
        "region_southwest": 0
    }

    # Set region encoding
    if region == "northwest":
        input_dict["region_northwest"] = 1
    elif region == "southeast":
        input_dict["region_southeast"] = 1
    elif region == "southwest":
        input_dict["region_southwest"] = 1

    # Convert to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Match column order
    input_df = input_df.reindex(columns=columns, fill_value=0)

    # Prediction
    prediction = model.predict(input_df)

    # Output
    st.success(f"💵 Estimated Insurance Cost: ₹ {prediction[0]:,.2f}")