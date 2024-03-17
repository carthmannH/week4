# Set the base image
FROM python:3.8-slim

# Set environment variable
ENV NODE_ENV=production

# Install Flask
RUN python -m pip install flask

# Set the working directory
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Set the entrypoint for the container
CMD ["python", "app.py"]
