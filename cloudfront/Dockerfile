# Stage 1: Build the React app
# FROM node:18 as build

# # Set working directory
# WORKDIR /app

# # Copy package.json and package-lock.json
# COPY cloudfront/package*.json ./

# # Install dependencies
# RUN npm install

# # Copy the rest of the application code
# COPY cloudfront/ .

# # Build the application
# RUN npm run build

# # Stage 2: Serve the app with Nginx
# FROM nginx:alpine

# # Copy built files from the previous stage
# COPY --from=build /app/build /usr/share/nginx/html

# # Expose port 80
# EXPOSE 80

# # Start Nginx
# CMD ["nginx", "-g", "daemon off;"]


# Stage 1: Build the React app

FROM node:18-alpine as build

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY cloudfront/package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY cloudfront/ .

# Build the application
RUN npm run build

# Stage 2: Serve the app with Nginx
FROM nginx:alpine

# Copy built files from the previous stage
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
