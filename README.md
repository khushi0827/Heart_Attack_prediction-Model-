Heart Attack Risk Prediction using Logistic Regression
📌 Overview
Heart disease is one of the leading causes of death worldwide. Early prediction can help in timely medical intervention and save lives.
This project uses Logistic Regression, a simple yet powerful machine learning algorithm, to predict the likelihood of a heart attack based on patient health parameters.
📊Dataset
Source: UCI Heart Disease Dataset
Features used:
Age
Sex
Chest Pain Type (cp)
Resting Blood Pressure (trestbps)
Cholesterol (chol)
Fasting Blood Sugar (fbs)
Resting ECG (restecg)
Maximum Heart Rate (thalach)
Exercise Induced Angina (exang)
ST Depression (oldpeak)
Slope of ST Segment (slope)
Number of Major Vessels (ca)
Thalassemia (thal)
⚙️ Workflow
🔹 Data Preprocessing
Handling missing values
Encoding categorical variables
Feature scaling
Outlier detection and removal using IQR and Z‑Score methods
Z‑Score method gave better accuracy compared to IQR.
Standard deviation check using heatmap to visualize feature distributions and detect anomalies.
These techniques reduced noise and improved test prediction accuracy.

🔹 Model Training
Logistic Regression classifier

🔹 Evaluation
Accuracy, Precision, Recall, F1-score
Confusion Matrix

🔹 Deployment
Built a website interface with black + neon theme for user inputs.
Connected the trained Logistic Regression model to the website for real‑time predictions.

Outputs include:
Risk prediction (⚠️ High Risk / ✅ Low Risk)
Probability pie chart (Yes vs No)

🚀 Results
Logistic Regression achieved higher accuracy after Z‑Score preprocessing.
Heatmap analysis confirmed reduced variance and better feature stability.
Interactive web app allows users to test predictions with custom inputs
