import requests
import numpy as np
# Example 28x28 grayscale image (random values in this example)
image = np.random.randint(0, 255, size=(28, 28)).tolist()

# Send the POST request
response = requests.post("http://localhost:8000/predict/", json={"image": image})

# Print the predicted class
print(response.json())