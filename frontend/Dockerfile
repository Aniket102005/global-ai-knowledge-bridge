# Stage 1: Build the React application
FROM node:18-alpine as builder
WORKDIR /app

# Copy package files for npm
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the frontend code
COPY . .
RUN npm run build

# Stage 2: Serve the app with Nginx
FROM nginx:1.25-alpine
COPY --from=builder /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
