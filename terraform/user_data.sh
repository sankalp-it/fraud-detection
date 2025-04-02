#!/bin/bash
sudo apt update
sudo apt install -y docker.io
sudo usermod -aG docker ubuntu
newgrp docker
docker run -d -p 8000:8000 your-docker-repo/model-inference:latest
