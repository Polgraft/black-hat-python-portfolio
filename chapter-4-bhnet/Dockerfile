# Dockerfile

# Use a lean, official Python 3.10 image as the base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file (even if it's empty, it's good practice)
COPY requirements.txt .

# Copy the main script into the container
COPY bhnet.py .

# Expose a common port for network tools (for documentation/testing clarity)
EXPOSE 9999

# Set the default command to execute the script. 
# This allows users to pass arguments directly when running the container (e.g., -l -c).
ENTRYPOINT ["python", "bhnet.py"]

# Optional: Add author metadata
LABEL maintainer="[Your Name] <[your.email@example.com]>"
