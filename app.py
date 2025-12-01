import streamlit as st 
import numpy as np 
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input  # corrected import

st.title("Aerial Object Classification and Detection")
st.write("Upload an image and the model will predict whether the object is Bird or a Drone")

uploaded_file = st.file_uploader('Choose an Image...',type=['jpg','jpeg','png','webp'])

if uploaded_file is not None:
    st.image(uploaded_file,caption="Uploaded Image",use_column_width=True)

    model = load_model('MobileNetV2.h5')

    img = image.load_img(uploaded_file, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    predictions = model.predict(img_array)
    predicted_idx = np.argmax(predictions, axis=1)[0]
    confidence = np.max(predictions) * 100

    class_names = ['bird', 'drone']
    predicted_class = class_names[predicted_idx]
    
    st.subheader("Prediction Results")
    st.write(f"Predicted Class: **{predicted_class}**")
    st.write(f"Confidence Score: **{confidence:.2f}%**")
