FROM node:18-alpine as build

WORKDIR /app
COPY . .
RUN npm install && npm run build

