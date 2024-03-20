#!/bin/bash

# Export variables from .env file excluding comments
export $(grep -v '^#' ../.env.local | xargs)

# Substitute variables in frontend.dockerfile and save as frontend.build.dockerfile
envsubst < frontend.dockerfile > frontend.build.dockerfile

# Build Docker image using frontend.build.dockerfile
docker build -t rag-app:local -f frontend.build.dockerfile .

rm frontend.build.dockerfile

# unset exported environment files from the .env.local file
# Iterate through all environment variables to unset them
for var in $(printenv | grep '^VITE_' | cut -d= -f1); do
    unset $var
done