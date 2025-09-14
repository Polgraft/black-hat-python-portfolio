# This command specifies the base image we're using.
# We're starting with a lightweight official Python 3.10 image.
FROM python:3.10-slim

# This sets the working directory inside the container.
# All subsequent commands will be run from this directory.
WORKDIR /app

# We copy the requirements file first to take advantage of Docker's layer caching.
# This makes subsequent builds faster if dependencies haven't changed.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# This command copies your Python script into the container.
COPY tcp_client.py .

# This specifies the default command to run when the container starts.
# We're setting it to display the help message by default.
CMD ["python", "tcp_client.py", "--help"]
