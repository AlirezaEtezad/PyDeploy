# Use a lightweight Python image
FROM python

# Set the working directory inside the container
WORKDIR /app

# Copy app code into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
