# **Student Well-being Index Prediction**

**Project Overview**  
This project utilizes **machine learning** to predict a student **mental health index** based on behavioral and lifestyle indicators. It represents a foundational entry into applied ML, focusing on **model integrity** and **practical feature engineering**.

---

## **Model Evolution**

- **The 92% Accuracy Trap**  
  Initial iterations achieved ~92% accuracy but relied on **clinical symptoms** (`stress_level`, `anxiety_score`), leading to significant **data leakage**.

- **The Strategic Shift**  
  Clinical scores were intentionally removed to force the model to rely on **controllable lifestyle factors**.

- **Feature Engineering**  
  Custom metrics were developed, including:  
  - `Outdoors` → Physical Activity + Social Support  
  - `Social_Ratio` → Social Support vs. Depression Symptoms

- **Dimensionality Reduction**  
  Applied **PCA** to condense academic variables into a single `academic_factors` component.

---

## **Performance**

- **Model**: `Random Forest Regressor` (50 estimators, max depth 10)  
- **Result**: Achieved a **scientifically honest R² score of 65%**  
- **Key Findings**:  
  - `Depression symptoms` remain the primary predictor (**84.29% importance**)  
  - Followed by **social support** and **sleep patterns**

---

## **Repository Structure**

- `app.py` → **Streamlit frontend** for real-time model inference  
- `wellbeing_model.pkl` → **Serialized Random Forest model**  
- `notebooks/` → Full **EDA** and **model training history**  
- `requirements.txt` → **Environment dependencies**

---

## **Installation & Usage**

1. **Clone the repository**  
   ```bash
   https://github.com/parinaB/studentwellbeing_ml.git
2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
3.**Run the app**
   ```bash
     streamlit run app.py

