# Heart Disease Risk Predictor

Welcome to my Heart Disease Risk Predictor project!  
This repository provides a user-facing tool that predicts the risk of heart disease based on patient data, powered by machine learning models and preprocessing pipelines developed in my companion repository: [Heart_data_preprocessing](https://github.com/AyushamMishra/Heart_data_preprocessing).

## 📋 Project Overview

This tool allows users to input relevant health and demographic details, which are processed and analyzed using ML models trained on the Heart Disease dataset.  
All data cleaning, preprocessing, feature engineering, and model training logic was built and documented in the [Heart_data_preprocessing](https://github.com/AyushamMishra/Heart_data_preprocessing) repository.

## 💡 How it Works

- **Data Input:** Users provide their health metrics (age, cholesterol, blood pressure, etc.)
- **Preprocessing:** Data is cleaned, encoded, and scaled using the same pipeline as in [Heart_data_preprocessing](https://github.com/AyushamMishra/Heart_data_preprocessing).
- **Prediction:** The trained model (e.g., Logistic Regression, Random Forest) outputs a risk score or classification.
- **Result:** Users receive an assessment of their heart disease risk.

## 🗃️ Workflow Overview

> **All data cleaning, preprocessing, and model training are detailed in [Heart_data_preprocessing](https://github.com/AyushamMishra/Heart_data_preprocessing):**

1. **Exploratory Data Analysis (EDA)**  
   - Statistical summary, distribution plots, correlation analysis, missing values.
2. **Data Cleaning & Preprocessing**  
   - Label/One-Hot Encoding, conversion to numeric, duplicate removal.
3. **Visualization**  
   - Heatmaps, countplots, histograms, pairplots.
4. **Feature Engineering**  
   - Feature selection, normalization, scaling.
5. **Model Training & Evaluation**  
   - ML model comparison and performance metrics.

## 🤖 Model Selection & Accuracy

Multiple machine learning models were trained and evaluated to find the best predictor for heart disease risk, as detailed in the [Heart_data_preprocessing](https://github.com/AyushamMishra/Heart_data_preprocessing) repo.  
The models explored included:

- **Logistic Regression**
- **Naive Bayes**
- **Support Vector Machine (SVM)**
- **K-Nearest Neighbors (KNN)**
- **Decision Tree**

After comparing model accuracy and performance using metrics such as accuracy, precision, recall, and F1-score, the **Logistic Regression** emerged as the top performer.  
**Logistic Regression** achieved the highest accuracy and generalization on the test set, outperforming the other models in terms of balanced precision and recall.  
This project uses the Logistic Regression based predictor to deliver reliable heart disease risk assessments.

## 🚀 Features in This Repo

- **User Interface** for entering patient data (CLI or notebook)
- **Model Prediction** using pre-trained models & preprocessing pipeline
- **Clear Output** of risk assessment


## 📊 Usage

- Use the interactive notebook or CLI script to enter patient details and receive a risk prediction.
- For technical details about data preprocessing and model training, see [Heart_data_preprocessing](https://github.com/AyushamMishra/Heart_data_preprocessing).

## ⚙️ Tech Stack

- **Python**
- **Pandas, NumPy**
- **Matplotlib, Seaborn**
- **Scikit-learn**

## Final Deployed app on Streamlit.
   App- https://ayushammishra-heart-disease-risk-predictor-frontend-lggnkl.streamlit.app/
   
## ⚠️ Disclaimer

This predictor is for educational and informational purposes only.  
It is **not** intended for clinical diagnosis or as a replacement for professional healthcare advice.

## 📧 Contact

Developed by **Ayusham Mishra**  
Questions, feedback, or suggestions? Connect with me on [GitHub](https://github.com/AyushamMishra).

---

Thanks for checking out my project! 😊
