import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import os
from PIL import Image

st.set_page_config(page_title="Health Assistant", page_icon=":heart:", layout="wide")

# Custom CSS to change sidebar background and font styles
st.markdown("""
<style>
    /* Sidebar background */
    .st-emotion-cache-vk3377, .st-emotion-cache-1pxazr8 {
        background-color: #f0f2f6; /* Light gray background */
    }

    /* Sidebar header/title font */
    .st-emotion-cache-16txt4v, .st-emotion-cache-10q70j5 {
        color: #0e1117; /* Darker font color for better contrast */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* Custom font */
    }

    /* Sidebar menu item font */
    .st-emotion-cache-1kyxreq  {
        color: #4a4a4a; /* Medium dark font color */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* Custom font */
    }
</style>
""", unsafe_allow_html=True)

# getting the working directory of the main script
working_dir = os.path.dirname(os.path.abspath(__file__))

heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Disease Prediction System',
                           ['Heart Disease Prediction'],
                           menu_icon='hospital-fill',
                           icons=['heart', 'activity', 'person'],
                           default_index=0)
#Heart Disease Prediction page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    # Add header image
    try:
        # Use the user-provided image path directly
        header_image_path = '/content/Signs of Heart Disease in Women – A Silent Killer - Med Transport Center.jfif'
        if os.path.exists(header_image_path):
            st.image(header_image_path, width=400) # Added width parameter
        else:
            st.warning("Header image not found. Please ensure the path is correct.")
    except Exception as e:
        st.error(f"Error loading header image: {e}")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age', key='age_input')
    with col2:
        sex_option = st.selectbox('Sex', ['Male', 'Female'], key='sex_input_select')
        sex_val = 1 if sex_option == 'Male' else 0
    with col3:
        cp_val = st.selectbox('Chest Pain Type', [0, 1, 2, 3], key='cp_input_select')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure', key='trestbps_input')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl', key='chol_input')
    with col3:
        fbs_val = st.selectbox('Fasting Blood Sugar > 120 mg/dl (0 = False; 1 = True)', [0, 1], key='fbs_input_select')

    with col1:
        restecg_val = st.selectbox('Resting Electrocardiographic results', [0, 1, 2], key='restecg_input_select')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved', key='thalach_input')
    with col3:
        exang_val = st.selectbox('Exercise Induced Angina (0 = No; 1 = Yes)', [0, 1], key='exang_input_select')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise relative to rest', key='oldpeak_input')
    with col2:
        slope_val = st.selectbox('Slope of the peak exercise ST segment', [0, 1, 2], key='slope_input_select')
    with col3:
        ca_val = st.selectbox('Major vessels colored by fluoroscopy', [0, 1, 2, 3, 4], key='ca_input_select')

    with col1:
        thal_val = st.selectbox('Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect', [0, 1, 2, 3], key='thal_input_select')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        # Check if any text_input field is empty
        text_inputs_to_check = [age, trestbps, chol, thalach, oldpeak]
        if any(val == '' for val in text_inputs_to_check):
            st.warning("Please fill in all numerical input fields.")
        else:
            try:
                input_data_for_model = [
                    float(age),
                    sex_val,
                    cp_val,
                    float(trestbps),
                    float(chol),
                    fbs_val,
                    restecg_val,
                    float(thalach),
                    exang_val,
                    float(oldpeak),
                    slope_val,
                    ca_val,
                    thal_val
                ]

                heart_prediction = heart_disease_model.predict([input_data_for_model])
                heart_diagnosis = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does NOT have any heart disease'
                st.success(heart_diagnosis)
            except ValueError:
                st.error("Please ensure all numerical fields contain valid numbers.")

    # Footer
    st.markdown("""
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f0f2f6; /* Light gray background */
            color: #4a4a4a; /* Medium dark font color */
            text-align: center;
            padding: 10px;
            font-size: 0.8em;
        }
    </style>
    <div class="footer">
        <p>Developed by Nafisat Musa| <a href="mailto:your.email@example.com">musanafisat59@gmail.com</a></p>
    </div>
    """, unsafe_allow_html=True)
