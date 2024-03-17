FROM python:latest 
ENV NODE_ENV=production

# Install Python
RUN apt-get update && apt-get install -y python3

# Set the working directory
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Set the entrypoint for the container
CMD ["python", "app.py"]
