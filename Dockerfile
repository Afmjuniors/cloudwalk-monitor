# Use the official Ubuntu 20.04 base image
FROM ubuntu:20.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    postgresql \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Set environment variables from .env file
ARG env_file
ENV ENV_FILE=$env_file
RUN echo "source $ENV_FILE" >> /root/.bashrc

# Expose the port for the application
EXPOSE 5000

# Run the server and monitoring script
CMD ["sh", "-c", "source /root/.bashrc && python3 app.py & python3 realtime_monitor.py"]
