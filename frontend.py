import streamlit as st
import pandas as pd
import joblib

# Load saved files
model = joblib.load("Logistic_reg_pred.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("COLUMNS.pkl")  # list of all feature columns used in training

st.title("Heart Stroke Prediction")
st.markdown("Enter the details below:")

# --- User Inputs ---
age = st.slider("Age", 18, 120, 40)
sex = st.selectbox("Sex", ['M', 'F'])
chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA"])
resting_bp = st.number_input("Resting Blood Pressure (mm/Hg)", 80, 200, 120)
cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar (>120 mg/dL)", [1, 0])
resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST"])
max_hr = st.slider("Maximum Heart Rate", 60, 220, 150)
exercise_angina = st.selectbox("Exercise Angina", ["Y", "N"])
oldpeak = st.number_input("Oldpeak (ST Depression)", 0.0, 6.0, 0.0, 0.1)
st_slope = st.selectbox("ST Slope", ["Flat", "Up"])

if st.button("PREDICT"):
    # --- Initialize DataFrame with all columns 0 ---
    user_input = pd.DataFrame(0, index=[0], columns=columns)

    # --- Fill numeric features ---
    numeric_cols = ['Age','RestingBP','Cholesterol','Oldpeak','MaxHR']
    user_input.loc[0, 'Age'] = age
    user_input.loc[0, 'RestingBP'] = resting_bp
    user_input.loc[0, 'Cholesterol'] = cholesterol
    user_input.loc[0, 'Oldpeak'] = oldpeak
    user_input.loc[0, 'MaxHR'] = max_hr

    # --- Fill binary features ---
    user_input.loc[0, 'Sex'] = 1 if sex == 'M' else 0
    user_input.loc[0, 'ExerciseAngina'] = 1 if exercise_angina == 'Y' else 0
    user_input.loc[0, 'FastingBS'] = fasting_bs

    # --- Fill one-hot encoded features ---
    chest_col = f"ChestPainType_{chest_pain}"
    if chest_col in columns:
        user_input.loc[0, chest_col] = 1

    st_slope_col = f"ST_Slope_{st_slope}"
    if st_slope_col in columns:
        user_input.loc[0, st_slope_col] = 1

    ecg_col = f"RestingECG_{resting_ecg}"
    if ecg_col in columns:
        user_input.loc[0, ecg_col] = 1

    # --- Scale numeric columns only ---
    user_input[numeric_cols] = scaler.transform(user_input[numeric_cols])

    # --- Make prediction ---
    prediction = model.predict(user_input)[0]
    probability = model.predict_proba(user_input)[0][1]

    # --- Show result ---
    st.subheader("Prediction Result")
    if prediction == 1:
        st.error(f"⚠️ High chance of Heart Disease (Probability: {probability:.2f})")
    else:
        st.success(f"✅ Low chance of Heart Disease (Probability: {probability:.2f})")

    st.subheader("Processed Input for Model")
    st.write(user_input)
