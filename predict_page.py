import streamlit as st
import pickle
import numpy as np

def load_models():
    with open('orbitclassifier.pkl', 'rb') as file:
        orbit_data = pickle.load(file)
    with open('randomforestmodel.pkl', 'rb') as file:
        rcs_data = pickle.load(file)
    return orbit_data["model"], rcs_data["model"]

def show_predict_page():
    st.title("Orbit Classification and RCS Prediction")

    st.write("""### Input Information:""")

    # Input fields for both Orbit Classification and RCS Size Prediction
    eccentricity = st.text_input("Eccentricity", "")
    mean_motion = st.text_input("Mean Motion", "")
    period = st.text_input("Period", "")
    object_age = st.text_input("Object Age", "")
    apoapsis = st.text_input("Apoapsis", "")
    periapsis = st.text_input("Periapsis", "")
    mean_anomaly = st.text_input("Mean Anomaly", "")
    inclination = st.text_input("Inclination", "")
    # eccentricity_rcs = st.text_input("Eccentricity (RCS)", "")

    # print("eccentricity:",eccentricity)
    # print("eccentricity_rcs",eccentricity)
    predict = st.button("Predict")

    if predict:
        # Prepare input data for both models
        X_orbit = np.array([[eccentricity, mean_motion, period]])
        X_rcs = np.array([[object_age, apoapsis, periapsis, mean_anomaly, mean_motion, inclination, period,eccentricity]])

        # Load models
        orbit_model, rcs_model = load_models()

        # Make predictions
        orbit_prediction = orbit_model.predict(X_orbit)
        rcs_prediction = rcs_model.predict(X_rcs)

        orbit_type_map = {0: 'Other', 1: 'HEO', 2: 'LEO', 3: 'GEO', 4: 'MEO'}
        predicted_orbit_type = orbit_type_map[orbit_prediction[0]]

        size_mapping = {1: 'SMALL', 2: 'MEDIUM', 3: 'LARGE'}
        predicted_rcs_size = size_mapping[rcs_prediction[0]]

        # Display predictions
        st.subheader(f"The estimated orbit is {predicted_orbit_type}")
        st.subheader(f"The estimated RCS size is {predicted_rcs_size}")

        

if __name__ == '__main__':
    show_predict_page()