# studentwellbeing_ml
Student Well-being Index Prediction
Project Overview
This repository contains a comprehensive machine learning analysis and deployment of a Student Well-being Index predictor. The objective is to utilize behavioral and lifestyle indicators—such as sleep patterns, physical activity, and social support—to estimate a quantitative mental health index.

This project represents a foundational entry into applied machine learning, moving beyond standard tutorials to address real-world data challenges such as data leakage, overfitting, and feature engineering.

Model Evolution: From "High-Accuracy Leak" to Behavioral Insight
A critical component of this project was the intentional transition from a descriptive model to a predictive, actionable one.

1. Initial State: The 92% Accuracy Trap
Initial model iterations achieved an accuracy of approximately 92%. However, exploratory data analysis revealed that the model was primarily utilizing clinical symptoms—stress_level and anxiety_score—as its strongest predictors.

The Problem: This represented significant Data Leakage. The model was essentially predicting a mental health index using mental health symptoms, leading to an overfitted state with no real-world utility.

2. The Strategic Shift
To create a robust model, stress_level and anxiety_score were intentionally removed from the feature set. This forced the model to rely on controllable lifestyle factors, making the output actionable for student well-being improvements.

3. Feature Engineering & Dimensionality Reduction
To recapture predictive power lost by removing clinical scores, the following methodologies were applied:

Dimensionality Reduction: Principal Component Analysis (PCA) condensed multiple variables (study_hours_per_day, exam_pressure, and academic_performance) into a single academic_factors component.

Behavioral Engineering: Custom metrics were developed to capture holistic wellness, including an Outdoors feature (sum of Physical Activity and Social Support) and a Social_Ratio (Social Support relative to Depression symptoms).

Model Performance
The final model utilizes a Random Forest Regressor with 50 estimators and a maximum depth of 10.

R² Score: ~0.65 (65%).

Conclusion: While the numeric score is lower than the initial 92%, this 65% represents a scientifically honest and robust correlation between controllable lifestyle behaviors and mental health outcomes.

Repository Structure
app.py: Streamlit-based web interface for real-time model inference using serialized data.

wellbeing_model.pkl: The serialized Random Forest model.

notebooks/: Full exploratory data analysis (EDA) and the journey from overfitted clinical modeling to behavioral prediction.

requirements.txt: Necessary Python dependencies for environment replication.

Local Deployment
To execute the prediction interface locally, install the dependencies and run the Streamlit application:

Bash
pip install -r requirements.txt
streamlit run app.py
Significance
As one of the initial forays into professional machine learning, this project demonstrates the transition from chasing high accuracy to ensuring model integrity. It serves as a practical application of predictive modeling in the domain of student health and behavioral science.
