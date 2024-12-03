# Use a lightweight Python image
FROM python

# Set the working directory inside the container
WORKDIR /app

# Copy into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the ONNX service runs on
EXPOSE 8000

# Command to run the ONNX service
CMD ["python", "onnx_service.py"]
