from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import tensorflow as tf

# Load the pre-trained model
model = tf.keras.models.load_model("fashion_mnist_model.h5")

# Initialize FastAPI app
app = FastAPI()

# Define input structure
class ImageRequest(BaseModel):
    image: list  # A 2D list representing the image (28x28 pixel grayscale)

@app.post("/predict/")
async def predict_image(request: ImageRequest):
    # Convert list to numpy array
    image = np.array(request.image)
    
    # Check if the image has the correct shape
    if image.shape != (28, 28):
        return {"error": "Image must be 28x28 pixels"}
    
    # Reshape and normalize the image
    image = image.reshape(1, 28, 28)  # Add batch dimension
    image = image / 255.0  # Normalize

    # Perform the prediction
    predictions = model.predict(image)
    predicted_class = np.argmax(predictions[0])

    # Return the predicted class
    return {"predicted_class": int(predicted_class)}