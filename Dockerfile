# #-----------------------------------------------to here
# FROM node:alpine AS development
# ENV NODE_ENV development
# WORKDIR /react-app

# # Installing dependencies
# COPY cloudfront/package*.json /react-app/
# RUN npm install

# # Copying all the files in our project
# COPY cloudfront /react-app/

# EXPOSE 3000

# # Starting our application
# CMD ["npm", "start"]


#----------------------------modify to add backend code 
# # Stage 1: ReactJS
# FROM node:alpine AS react-build
# ENV NODE_ENV development
# WORKDIR /react-app

# # Installing dependencies for ReactJS
# COPY cloudfront/package*.json /react-app/
# RUN npm install

# # Copying all ReactJS files
# COPY cloudfront /react-app/

# # Building ReactJS app
# RUN npm run build

# # Stage 2: Django
# FROM python:alpine AS django-build
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# WORKDIR /djangoback

# # Installing dependencies for Django
# COPY cloudback/requirements.txt /djangoback/
# RUN pip3 install -r requirements.txt 

# # Copying all Django files
# COPY cloudback /djangoback/

# # Exposing port 8000 for Django
# EXPOSE 8000

# # Copy ReactJS build files to Django static directory
# # RUN mkdir -p /djangoback/static && cp -r /react-app/build /djangoback/static

# # Final stage: Combine both environments
# FROM python:alpine

# # Copy React build and Django files from previous stages
# COPY --from=react-build /react-app/build /app/react-build
# COPY --from=django-build /djangoback /app/djangoback
# WORKDIR /app/djangoback

# # Install Django dependencies again to ensure they're available in the final image
# RUN pip install -r requirements.txt

# # Expose the ports
# EXPOSE 3000
# EXPOSE 8000

# # Start both applications
# CMD ["sh", "-c", "npm start & python manage.py runserver 0.0.0.0:8000"]


#_---------------------------------------------------------


    # Stage 1: ReactJS
FROM node:alpine AS react-build
ENV NODE_ENV development
WORKDIR /react-app

# Installing dependencies for ReactJS
COPY cloudfront/package*.json /react-app/
RUN npm install

# Copying all ReactJS files
COPY cloudfront /react-app/

# Building ReactJS app
RUN npm run build

# Stage 2: Django
FROM python:alpine AS django-build
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /djangoback

# Installing dependencies for Django
COPY cloudback/requirements.txt /djangoback/
RUN pip3 install -r requirements.txt 

# Copying all Django files
COPY cloudback /djangoback

# Exposing port 8000 for Django
EXPOSE 8000

# Final stage: Combine both environments
FROM python:alpine

# Create the app directory structure
RUN mkdir -p /app/reactfront /app/djangoback

# Copy React build and Django files from previous stages
COPY --from=react-build /react-app/build /app/reactfront/static
COPY --from=django-build /djangoback /app/djangoback

# Set the working directory
WORKDIR /app/djangoback

# Install Django dependencies again to ensure they're available in the final image
RUN pip3 install -r requirements.txt

# Expose the ports
EXPOSE 3000
EXPOSE 8000

# Start both applications
CMD ["ls"]
CMD ["sh", "-c", "npm start & python manage.py runserver 0.0.0.0:8000"]
