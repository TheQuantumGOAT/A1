
# Fashion MNIST API and Web Application

This repository contains a **FastAPI** API and a **Streamlit** web application for classifying images from the **Fashion MNIST** dataset. Both services are containerized using Docker, and Docker Compose is used to orchestrate the services.

## Project Structure

```
code/
│
└───deployment/
    │
    ├── docker-compose.yml          # Docker Compose file to run both services
    │
    ├───api/                        # FastAPI app
    │     ├── app.py                # FastAPI API code
    │     └── Dockerfile            # Dockerfile for FastAPI API
    │
    └───app/                        # Streamlit web app
          ├── app.py                # Streamlit app code
          └── Dockerfile            # Dockerfile for Streamlit web app
```

### Components
1. **FastAPI API**: A RESTful API that accepts a 28x28 grayscale image of a Fashion MNIST item and returns the predicted class.
2. **Streamlit Web App**: A web interface that allows users to upload images, which are then classified by the trained model.

## Prerequisites

Before running the project, ensure that you have the following installed:
- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Usage

### 1. Clone the Repository

```bash
git clone <repository_url>
cd code/deployment
```

### 2. Build and Run the Application

To build and start both the FastAPI API and the Streamlit web application, run the following command:

```bash
docker-compose up --build
```

This will:
- Build the Docker images for both services.
- Start the containers for the **FastAPI** and **Streamlit** apps.

### 3. Access the Applications

Once the services are running, you can access them at the following URLs:

- **FastAPI API**: `http://localhost:8000/docs` (Swagger UI)
  - The API will be available at `http://localhost:8000/predict/`.

- **Streamlit Web App**: `http://localhost:8501`
  - You can upload a 28x28 grayscale image to the web app for classification.

### 4. Stopping the Services

To stop the services, press `Ctrl+C` in the terminal or run:

```bash
docker-compose down
```

### 5. Running in Detached Mode

If you want to run the services in the background, use:

```bash
docker-compose up -d
```

## API Endpoints

The FastAPI service exposes the following endpoint:

### POST `/predict/`

This endpoint accepts a JSON request containing a 28x28 grayscale image (as a 2D list of pixel values) and returns the predicted class of the Fashion MNIST item.

#### Example Request

```json
{
  "image": [
    [0, 0, 0, ..., 0, 0, 0],
    [0, 0, 0, ..., 0, 0, 0],
    ...
    [0, 0, 0, ..., 0, 0, 0]
  ]
}
```

#### Example Response

```json
{
  "predicted_class": 3
}
```

## Web Application

The Streamlit app allows users to upload an image for classification. It accepts a 28x28 grayscale image, resizes and normalizes it, and then displays the predicted class.

## Troubleshooting

- **Port conflicts**: Ensure that ports `8000` and `8501` are free. If they are in use by another process, stop the process or modify the `docker-compose.yml` file to use different ports.
  
- **Docker not starting**: Ensure Docker is installed and running. Check Docker service status if needed.

- **Model file not found**: Ensure the `fashion_mnist_model.h5` file is present in the required directory and correctly referenced in the code.

## Credits

- **FastAPI**: [FastAPI Documentation](https://fastapi.tiangolo.com/)
- **Streamlit**: [Streamlit Documentation](https://docs.streamlit.io/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
