# Base image with Python and necessary tools
FROM python:3.8-slim

# Set working directory
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the model code and ONNX file
COPY Fomo_based_CNN.ipynb ./model_code/
COPY model.onnx ./model/

# Set the entrypoint script
COPY entrypoint.py .

# Set the default command to run the entrypoint script
ENTRYPOINT ["python", "entrypoint.py"]
