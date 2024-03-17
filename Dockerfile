# Set the base image
FROM python:alpine3.19

# Set environment variable
ENV NODE_ENV=production

# Install additional dependencies
RUN apk update && apk add --no-cache python3

# Set the working directory
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Set the entrypoint for the container
CMD ["python", "app.py"]
