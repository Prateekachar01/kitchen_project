# # Use the official Node.js image as the base image
# FROM node:20

# # Set the working directory inside the container
# WORKDIR /app

# # Copy the package.json and package-lock.json from the cloudfront directory
# COPY cloudfront/package*.json ./cloudfront/

# # Install the project dependencies directly from the correct directory
# RUN npm install 

# # Copy the rest of the application code from the cloudfront directory
# COPY cloudfront/ ./cloudfront/

# # Expose the port that the React app will run on
# EXPOSE 3000

# # Start the React application
# CMD ["npm", "start", "--prefix", "cloudfront"]


FROM node:alpine AS development
ENV NODE_ENV development
WORKDIR /react-app

# Installing dependencies
# COPY ./package*.json /react-app
COPY ./package*.json /react-app

RUN npm install
# RUN cd cloudfront && npm install

# Copying all the files in our project
COPY . .

EXPOSE 3000

# Starting our application
CMD ["npm","start"]
