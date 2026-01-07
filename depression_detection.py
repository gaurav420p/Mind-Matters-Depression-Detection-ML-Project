import streamlit as st
import pandas as pd
import joblib

# ---------------- LOAD MODEL ---------------- #
model = joblib.load("depression_model.joblib")

# ---------------- CATEGORY MAPPINGS ---------------- #

gender_map = {"Male": 0, "Female": 1}

age_group_map = {
    "18-24": 0, "25-29": 1, "30-34": 2, "35-39": 3, "40-60": 4
}

cgpa_group_map = {
    "Low CGPA": 0,
    "Below Average CGPA": 1,
    "Average CGPA": 2,
    "High CGPA": 3
}

sleep_duration_map = {
    "Less than 5 hours": 0,
    "5-6 hours": 1,
    "7-8 hours": 2,
    "More than 8 hours": 3
}

dietary_habits_map = {
    "Healthy": 0,
    "Moderate": 1,
    "Unhealthy": 2
}

yes_no_map = {"No": 0, "Yes": 1}

# ---------------- UI ---------------- #

st.title("Depression Prediction App")
st.markdown("Fill in the details below and click **Predict**")
st.divider()

# ---------------- INPUTS ---------------- #

gender = st.selectbox("Gender", list(gender_map.keys()))
age_group = st.selectbox("Age Group", list(age_group_map.keys()))
cgpa_group = st.selectbox("CGPA Group", list(cgpa_group_map.keys()))
sleep_duration = st.selectbox("Sleep Duration", list(sleep_duration_map.keys()))
dietary_habits = st.selectbox("Dietary Habits", list(dietary_habits_map.keys()))

study_hours = st.number_input(
    "Work / Study Hours per Day", 0.0, 16.0, 6.0
)

academic_pressure = st.slider("Academic Pressure (0–5)", 0, 5, 2)
study_satisfaction = st.slider("Study Satisfaction (0–5)", 0, 5, 3)
financial_stress = st.slider("Financial Stress (0–5)", 0, 5, 2)

family_history = st.selectbox(
    "Family History of Mental Illness", list(yes_no_map.keys())
)

suicidal_thoughts = st.selectbox(
    "Have you ever had suicidal thoughts ?", list(yes_no_map.keys())
)

# ---------------- PREDICTION ---------------- #

if st.button("Predict"):

    input_data = pd.DataFrame([{
        "Gender": gender_map[gender],
        "Age Group": age_group_map[age_group],
        "CGPA Group": cgpa_group_map[cgpa_group],
        "Sleep Duration": sleep_duration_map[sleep_duration],
        "Dietary Habits": dietary_habits_map[dietary_habits],
        "Work/Study Hours": study_hours,
        "Academic Pressure": academic_pressure,
        "Study Satisfaction": study_satisfaction,
        "Financial Stress": financial_stress,
        "Family History of Mental Illness": yes_no_map[family_history],
        "Have you ever had suicidal thoughts ?": yes_no_map[suicidal_thoughts]
    }])

    # 🔥 ALIGN ORDER WITH TRAINING
    input_data = input_data[model.feature_names_in_]

    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction: {int(prediction)}")

    if prediction == 1:
        st.error("⚠️ Signs indicate possible depression")
    else:
        st.success("✅ No depression detected")
