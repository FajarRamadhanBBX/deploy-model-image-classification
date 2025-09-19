# Build Docker image for image classification
This repository contains the code to build a Docker Image, which will then be deployed to IBM Cloud. Model can predict cattle disease from image.

# Prerequisites
Make sure you have installed Docker on your local machine.

# Steps
1. Clone the repository
  ```sh
  git clone https://github.com/FajarRamadhanBBX/deploy-model-image-classification
  ```
2. Build te Image
  ```sh
    docker build -t image-classification:latest .
  ```  
3. Verify the Image
   ```sh
    docker images
   You should see image-classification with the tag `latest` in the list.```
