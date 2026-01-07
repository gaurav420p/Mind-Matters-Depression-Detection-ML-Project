# Mind Matters: Depression Risk Prediction using Machine Learning

## 📌 Project Overview
Mind Matters is an end-to-end machine learning project designed to predict depression risk levels based on structured survey data collected from students. The project applies multiple classification algorithms, compares their performance, and deploys the best-performing model for inference.

This project is academic and exploratory in nature and is intended to demonstrate applied machine learning skills, including data preprocessing, model evaluation, and deployment readiness.

---

## 🎯 Problem Statement
Mental health challenges among students are increasing globally. Early identification of potential depression risk can help in initiating timely support mechanisms.

The objective of this project is to:
- Analyze student survey data
- Build predictive machine learning models
- Identify patterns associated with depression risk

⚠️ **Important Disclaimer**  
This system does **NOT** provide medical diagnosis and must not be used for clinical or therapeutic decision-making.

---

## 📂 Dataset Description
- **Source**: Student Depression Dataset (CSV)
- **Type**: Structured tabular data
- **Features include**:
  - Academic pressure
  - Sleep duration
  - Study hours
  - Stress levels
  - Lifestyle-related attributes
- **Target Variable**: Depression (Binary classification)

---

## ⚙️ Machine Learning Pipeline
The project follows a production-style ML pipeline:

1. Data Cleaning & Exploration  
2. Feature Engineering  
3. Train–Test Split  
4. Preprocessing using `ColumnTransformer`
   - Numerical feature scaling
   - Categorical feature encoding  
5. Model Training using `Pipeline`  
6. Model Evaluation & Comparison  
7. Model Serialization using `joblib`  
8. Inference via Python script / Streamlit app  

---

## 🧠 Models Implemented

| Model | Purpose |
|------|--------|
| Logistic Regression | Baseline linear classifier |
| K-Nearest Neighbors | Distance-based learning |
| Decision Tree | Rule-based classification |
| Random Forest | Ensemble learning |
| Naive Bayes | Probabilistic classifier |
| AdaBoost | Boosting-based ensemble |

The best-performing model was selected based on accuracy and generalization performance.

---

## 📊 Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-score

---

## 🚀 Deployment
- Trained model saved using `joblib`
- Integrated into a Streamlit web application
- Accepts user inputs and returns depression risk prediction

---

## 🛠️ Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Joblib
- Git & GitHub

---

## ⚠️ Limitations
- Dataset size is limited
- Model predictions depend entirely on self-reported survey data
- Not suitable for real-world medical diagnosis


---

## 👨‍💻 Author
**Gaurav Patel**  
B.Tech Computer Science Engineering  
Machine Learning & Backend Enthusiast
