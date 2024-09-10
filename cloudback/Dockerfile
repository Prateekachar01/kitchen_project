# # Use the official Python image from the Docker Hub
# FROM python:3.11

# # Set the working directory in the container
# WORKDIR /app

# # Copy the requirements file into the container
# COPY cloudback/requirements.txt .

# RUN pip3 install pipenv

# # RUN dnf install python3-pip
# RUN pip3 --version

# # Install dependencies
# RUN pip3 install -r requirements.txt

# # Copy the rest of the application code into the container
# COPY *.* /app/

# # Set the command to run the application
# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


# Use the official Python Alpine image from Docker Hub

FROM python:3.11-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY cloudback/requirements.txt .

# Install dependencies required to build and run Python packages
RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev


    
# Install system dependencies
# RUN apk update && apk add --no-cache \
#     mysql-client \
#     mariadb-dev \
#     gcc \
#     musl-dev \
#     libffi-dev \
#     && rm -rf /var/cache/apk/*



# Install pipenv
RUN pip install pipenv

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY *.* /app/

# Set the command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
