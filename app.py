import streamlit as st
import pandas as pd
import joblib

# 1. SETUP & STYLING (The "Less AI" Academic Look)
st.set_page_config(page_title="Well-being Predictor", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #fdfdfc; }
    h1 { font-family: 'Georgia', serif; color: #2c2c2c; border-bottom: 2px solid #2c2c2c; padding-bottom: 10px; }
    .stButton>button { background-color: #2c2c2c; color: white; border-radius: 0px; width: 100%; border: none; height: 3em;}
    .result-card { padding: 30px; background-color: #ffffff; border: 1px solid #2c2c2c; text-align: center; margin-top: 20px; }
    .score-text { font-size: 54px; font-family: 'Georgia', serif; color: #3d5a52; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 2. LOAD THE BRAIN
# Ensure 'wellbeing_model.pkl' is in the same folder as this app.py
@st.cache_resource
def load_model():
    return joblib.load('wellbeing_model.pkl')

model = load_model()

st.title("Mental Health Index Analysis")
st.write("Behavioral prediction engine utilizing a Random Forest Regressor (65% R²).")

# 3. USER INPUTS
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", 15, 35, 21)
        academic_year = st.slider("Academic Year", 1, 5, 2)
        sleep = st.number_input("Sleep Hours", 0.0, 15.0, 7.0)
        physical = st.slider("Physical Activity (1-10)", 1, 10, 5)
        depression = st.slider("Depression Score (0-10)", 0, 10, 2)
    with col2:
        support = st.slider("Social Support (1-10)", 1, 10, 5)
        acad_factors = st.number_input("Academic Factors (PCA)", -25.0, 25.0, 0.0)
        gender = st.selectbox("Gender Identity", ["Female", "Male", "Other"])

# 4. PREDICTION LOGIC
if st.button("EXECUTE ANALYSIS"):
    # Recreate the exact feature vector from cell 66
    # Note: Column names must match X_sample exactly!
    input_data = pd.DataFrame({
        'age': [age],
        'academic_year': [academic_year],
        'depression_score': [depression],
        'sleep_hours': [sleep],
        'physical_activity': [physical],
        'social_support': [support],
        'gender_Female': [1 if gender == "Female" else 0],
        'gender_Male': [1 if gender == "Male" else 0],
        'gender_Other': [1 if gender == "Other" else 0],
        'academic_factors': [acad_factors],
        'Outdoors': [physical + support], #
        'Social_Ratio': [support / (depression + 1)] #
    })
    
    # Run Inference
    prediction = model.predict(input_data)[0]
    
    # Display Result
    st.markdown("---")
    st.markdown(f"""
        <div class="result-card">
            <p style="text-transform: uppercase; letter-spacing: 2px; font-size: 14px;">Calculated Well-being Index</p>
            <div class="score-text">{round(prediction, 2)}</div>

        </div>
    """, unsafe_allow_html=True)
    
    # Contextual insight based on your high feature importance for depression
    if depression > 5:
        st.warning("Analysis: High depression score is heavily weighting the index downward.")
        
    outdoors = physical + support
    if outdoors < 8:
        st.info("Recommendation: Increasing 'Outdoors' activities (Physical Activity + Social Support) may positively influence this index.")
        