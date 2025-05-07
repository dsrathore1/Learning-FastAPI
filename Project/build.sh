#!/bin/bash

#? Optional : Clear previous Docker build cache
docker builder prune -f

#? Remove if there any image exists by same name
docker rmi fastapi_app:latest

#? Build Docker image 
docker build -t fastapi_app:latest .

#? Optional : Clean up again after build
docker builder prune -f

#? Remove if there any container exists by same name
docker rm myapp

#? Activate the container
docker run --name myapp -d -p 8000:8000 fastapi_app:latest