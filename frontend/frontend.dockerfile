FROM node:lts-alpine as build-stage

ARG VITE_AUTH0_DOMAIN
ARG VITE_AUTH0_CLIENT_ID
ARG VITE_AUTH0_CALLBACK_URL
ARG VITE_API_SERVER_URL

# We need to set the needed env variables when the image is being built. We need
# to do this because when bundling for production, the env variables are baked in the 
# final boundle
ENV VITE_AUTH0_DOMAIN=$VITE_AUTH0_DOMAIN
ENV VITE_AUTH0_CLIENT_ID=$VITE_AUTH0_CLIENT_ID
ENV VITE_AUTH0_CALLBACK_URL=$VITE_AUTH0_CALLBACK_URL
ENV VITE_API_SERVER_URL=$VITE_API_SERVER_URL


WORKDIR /app
COPY package.json package-lock.json /
RUN npm install

COPY . /app
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage

# All bundled files will be copied over to the html dir in Nginx to be so Nginx
# can serve them as static content
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

