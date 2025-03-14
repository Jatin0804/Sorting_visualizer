# Use official Python image
FROM python:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the necessary ports (if needed)
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
