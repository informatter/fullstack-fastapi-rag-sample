FROM node:lts-alpine as build-stage

ARG VITE_AUTH0_DOMAIN
ARG VITE_AUTH0_CLIENT_ID
ARG VITE_AUTH0_CALLBACK_URL
ARG VITE_API_SERVER_URL

ENV VITE_AUTH0_DOMAIN=$VITE_AUTH0_DOMAIN
ENV VITE_AUTH0_CLIENT_ID=$VITE_AUTH0_CLIENT_ID
ENV VITE_AUTH0_CALLBACK_URL=$VITE_AUTH0_CALLBACK_URL
ENV VITE_API_SERVER_URL=$VITE_API_SERVER_URL


WORKDIR /app
COPY package.json package-lock.json /
RUN npm install

COPY . /app
# Conditionally run npm run build only if ENV is set to "production"
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

