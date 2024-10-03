import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the trained model
model = tf.keras.models.load_model("fashion_mnist_model.h5")

# Define class labels for Fashion MNIST dataset
class_labels = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]

# Streamlit app title and description
st.title("Fashion MNIST Classifier")
st.write("Upload a 28x28 grayscale image of an item from the Fashion MNIST dataset for prediction.")

# File uploader for images
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file).convert("L")  # Convert image to grayscale
    
    # Resize the image to 28x28 pixels
    image = image.resize((28, 28))
    
    # Display the image
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Preprocess the image for prediction
    image_array = np.array(image).reshape(1, 28, 28) / 255.0  # Normalize the image
    
    # Predict the class
    predictions = model.predict(image_array)
    predicted_class = np.argmax(predictions[0])
    
    # Display the prediction
    st.write(f"Predicted Class: {class_labels[predicted_class]}")
