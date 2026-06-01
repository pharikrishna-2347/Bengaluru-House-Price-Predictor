# 🏠 Bengaluru House Price Predictor

A Machine Learning-based web application that predicts house prices in Bengaluru based on various property features. The project leverages data preprocessing, feature engineering, and Linear Regression to provide accurate house price predictions through an interactive Streamlit interface.

---

## 🚀 Live Demo

https://phk-bengaluru-house-price-predictor-b9jmvsmdmgfqxmntmgprnz.streamlit.app/#bengaluru-house-price-predictor
```text
https://your-app-name.streamlit.app
```

---

## 📌 Project Overview

The real estate market involves numerous factors that influence property prices. This project aims to predict house prices in Bengaluru using machine learning techniques and a carefully preprocessed dataset.

The application allows users to enter property details such as location, area type, square footage, number of bathrooms, balconies, and BHK configuration, and then predicts the estimated house price.

---

## 📊 Dataset

Dataset Used: Bengaluru House Prices Dataset

The dataset contains information about thousands of residential properties in Bengaluru, including:

* Location
* Area Type
* Availability
* Total Square Feet
* Number of Bathrooms
* Number of Balconies
* BHK Configuration
* Price

---

## 🧹 Data Preprocessing

Extensive preprocessing was performed to improve data quality and model performance.

### Data Cleaning

* Removed unnecessary columns with excessive missing values.
* Dropped the **society** column because it contained a large number of missing values and contributed little to prediction performance.
* Handled missing and inconsistent values across multiple columns.

### Feature Engineering

Created a new feature:

**Price Per Square Foot**

This helped identify and remove unrealistic property records and improve model accuracy.

### Outlier Removal

Applied efficient outlier detection and removal techniques based on:

* Price per square foot
* BHK configuration
* Property characteristics

This significantly improved the reliability of predictions.

---

## 🔄 Feature Encoding

Categorical features were converted into machine-readable numerical representations.

### Label Encoding

Applied to:

* Availability

### One-Hot Encoding

Applied to:

* Area Type
* Location

These transformations allowed the model to effectively learn patterns from categorical data.

---

## 🤖 Machine Learning Model

The final model was trained using:

### Linear Regression

Linear Regression was chosen due to its simplicity, interpretability, and strong performance on the processed dataset.

The trained model was serialized and stored using Pickle for deployment.

---

## 📥 Input Features

The application accepts the following inputs from users:

```python
input_df = pd.DataFrame({
    'area_type': [area_type],
    'availability': [availability],
    'location': [location],
    'total_sqft': [sqft],
    'bath': [bath],
    'balcony': [balcony],
    'bhk': [size]
})
```

### User Inputs

* Area Type
* Availability Status
* Location
* Total Square Feet
* Number of Bathrooms
* Number of Balconies
* BHK Size

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Pickle

### Machine Learning

* Linear Regression

### Deployment

* GitHub
* Streamlit Community Cloud

---

## 📂 Project Structure

```text
HousePricePredictor/
│
├── app.py
├── model.pkl
├── Final.csv
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ✨ Features

✅ Interactive Streamlit Interface

✅ Real-Time House Price Prediction

✅ Data Cleaning and Feature Engineering

✅ Outlier Detection and Removal

✅ One-Hot Encoding and Label Encoding

✅ Linear Regression-Based Prediction

✅ Cloud Deployment Ready

---

## 🔮 Future Improvements

* Experiment with advanced models such as Random Forest and XGBoost
* Add interactive visualizations and analytics
* Incorporate market trends and location-based insights
* Improve prediction accuracy using ensemble methods
* Deploy using Docker and cloud platforms

---

## 👨‍💻 Author

**Hari Krishna**

Computer Science Engineering Student | AI/ML Enthusiast | Python Developer

Feel free to connect and explore the project!
