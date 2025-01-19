import streamlit as st
import tensorflow as tf
import numpy as np
import os

# Load Model and Predict
def model_prediction(test_image):
    model = tf.keras.models.load_model('trained_crop_model.keras')
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))
    input_arr = np.array([tf.keras.preprocessing.image.img_to_array(image)])
    prediction = model.predict(input_arr)
    return np.argmax(prediction)

# Sidebar Navigation
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Species Recognition"])

# Home Page
if app_mode == "Home":
    st.header("Plant Species Recognition System")
    st.image("Garden-Plants-1024x683.jpg", use_column_width=True)
    st.markdown("Welcome to the Plant Species Recognition System! 🌿🔍")

# About Page
elif app_mode == "About":
    st.header("About")
    st.markdown("""
    ### Dataset
    - **Train**: 987 images
    - **Validation**: 211 images
    - **Test**: 212 images
    """)

# Species Recognition Page
elif app_mode == "Species Recognition":
    st.header("Species Recognition")
    test_image = st.file_uploader("Choose an Image:")
    if st.button("Show Image") and test_image:
        st.image(test_image, use_column_width=True)
    if st.button("Predict Species") and test_image:
        with st.spinner("Predicting..."):
            result_index = model_prediction(test_image)
            class_names = ["abies_concolor", "abies_nordmanniana", "acer_campestre", "acer_ginnala"]
            st.success(f"Model predicts: **{class_names[result_index]}**")
