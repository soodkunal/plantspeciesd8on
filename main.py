import streamlit as st
import tensorflow as tf
import numpy as np 

#tensorflow Model Prediciton
def model_prediction(test_image):
    model = tf.keras.models.load_model('trained_crop_model.keras')
    image=tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
    input_arr=tf.keras.preprocessing.image.img_to_array(image)
    input_arr=np.array([input_arr]) #convert the image into batch
    prediciton=model.predict(input_arr)
    result_index=np.argmax(prediciton)
    return result_index

#sidebar
st.sidebar.title("Dashboard")
app_mode=st.sidebar.selectbox("Select Page",["Home","About","Species Recognition"])
 
#Home Page
if(app_mode=="Home"):
    st.header("Plant Species Recognition System")
    image_path=r"Garden-Plants-1024x683.jpg"
    st.image(image_path,use_column_width=True)
    st.markdown(""" Welcome to the Plant Species Recognition System! 🌿🔍
    
    Our mission is to help in identifying plant species efficiently. Upload an image of a plant, and our system will analyze it to detect the species of plant it belongs to. Together, let's classify the plants and protect them  and contribute to a healthy ecosystem!

    ### How It Works
    1. **Upload Image:** Go to the **Species Recognition** page and upload an image of a plant whose species you want to know about.
    2. **Analysis:** Our system will process the image using advanced algorithms to identify the species tof the plant it belongs to.
    3. **Results:** View the results and recommendations for further action.

    ### Why Choose Us?
    - **Accuracy:** Our system utilizes state-of-the-art machine learning techniques for accurate species detection.
    - **User-Friendly:** Simple and intuitive interface for seamless user experience.
    - **Fast and Efficient:** Receive results in seconds, allowing for quick decision-making.

    ### Get Started
    Click on the **Species Recognition** page in the sidebar to upload an image and experience the power of our Plant Species Recognition System!

    ### About Us
    Learn more about the project, our team, and our goals on the **About** page.
    """)

#About Page
elif(app_mode=="About"):
    st.header("About")
    st.markdown("""
### About Dataset
This dataset is recreated using offline augmentation from the original dataset.The original dataset can be found on this github repo.
This dataset consists of about 987 rgb images of different plants belonging to deffeent species. The species which is categorized into 4 different classes.The total dataset is divided into 70/30 ratio of training and validation set preserving the directory structure.
A new directory containing 212 test images is created later for prediction purpose.

### Content
1. **Train**: 987 images
2. **Validation**: 211 images
3. **Test**: 212 images
""")

#Prediction Page
elif(app_mode=="Species Recognition"):
    st.header("Species Recognition")
    test_image = st.file_uploader("Choose  an Image:  ")
    if(st.button("Show Image")):
        st.image(test_image,use_column_width=True)
    if(st.button("Predict Species")):
        with st.spinner("Please Wait.."):
            st.balloons()
            st.write("Our prediction")
            result_index=model_prediction(test_image)
            #Define Class
            class_name=["abies_concolor",
    "abies_nordmanniana",
    "acer_campestre","acer_ginnala"]
            st.success(f"Model is predicting it is a {class_name[result_index]}")
