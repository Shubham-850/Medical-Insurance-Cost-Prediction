# 💰 Medical Insurance Cost Prediction

An end-to-end Machine Learning project that predicts individual medical insurance costs based on demographic and health-related features such as age, BMI, smoking status, and region.

---

## 🚀 Project Overview

This project demonstrates a complete ML pipeline:

- Data Cleaning & Preprocessing  
- Exploratory Data Analysis (EDA)  
- Feature Engineering  
- Model Training (Multiple Regression Models)  
- Model Evaluation  
- Experiment Tracking using MLflow  
- Deployment using Streamlit  

---

## 📂 Dataset

The dataset contains the following features:

- **age**: Age of the individual  
- **sex**: Gender (male/female)  
- **bmi**: Body Mass Index  
- **children**: Number of dependents  
- **smoker**: Smoking status  
- **region**: Residential area  
- **charges**: Medical insurance cost (target)  

---

## 📊 Exploratory Data Analysis

Key insights:

- Smokers have significantly higher insurance charges  
- Charges increase with age  
- BMI has moderate impact on cost  
- Region and gender have smaller effects  

---

## 🤖 Models Used

- Linear Regression  
- Ridge Regression  
- Decision Tree Regressor  
- Random Forest Regressor ✅ (Best Performing)  
- XGBoost Regressor  

---

## 📈 Model Evaluation Metrics

- Mean Absolute Error (MAE)  
- Root Mean Squared Error (RMSE)  
- R² Score  

---

## 🧪 MLflow Tracking

- Logged model parameters and metrics  
- Compared multiple models  
- Registered best-performing model  

---

## 🌐 Streamlit App

An interactive web application where users can:

- Enter personal details  
- Get real-time insurance cost prediction  
- Explore insights from the dataset  

### ▶️ Run the app locally

```bash
streamlit run medical_insurance.py
