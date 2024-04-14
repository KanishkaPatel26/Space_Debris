
import streamlit as st
import pickle
import numpy as np

def load_orbit_model():
    with open('orbitclassifier.pkl', 'rb') as file:
        orbit_data = pickle.load(file)
    return orbit_data["model"]

def load_rcs_model():
    with open('randomforestmodel.pkl', 'rb') as file:
        rcs_data = pickle.load(file)
    return rcs_data["model"]

def show_predict_page():
    st.title("Classified Orbit and RCS Size Prediction:")

    st.write("""### We need some information to predict the orbit and RCS size""")

    eccentricity = st.text_input("Eccentricity", "")
    mean_motion = st.text_input("Mean Motion", "")
    period = st.text_input("Period", "")
    object_age = st.text_input("Object Age", "")
    apoapsis = st.text_input("Apoapsis", "")
    periapsis = st.text_input("Periapsis", "")
    mean_anomaly = st.text_input("Mean Anomaly", "")
    inclination = st.text_input("Inclination", "")

    ok = st.button("Calculate Orbit and RCS Size")

    if ok:
        X_orbit = np.array([[float(eccentricity), float(mean_motion), float(period)]])
        X_rcs = np.array([[float(eccentricity), float(mean_motion), float(period), float(object_age), float(apoapsis), float(periapsis), float(mean_anomaly), float(inclination)]])

        orbit_model = load_orbit_model()
        rcs_model = load_rcs_model()

        orbit_prediction = orbit_model.predict(X_orbit)
        rcs_prediction = rcs_model.predict(X_rcs)

        st.subheader(f"The estimated orbit is {orbit_prediction[0]}")
        st.subheader(f"The estimated RCS size is {rcs_prediction[0]}")

show_predict_page()


