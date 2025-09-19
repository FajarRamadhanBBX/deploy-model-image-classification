# Build Docker image for diseases classification from image
This repository contains the code to build a Docker Image, which will then be deployed to IBM Cloud. Model can predict cattle disease from image.

# Prerequisites
Make sure you have installed Docker on your local machine.

# Steps
- Clone the repository
  ```sh
  git clone https://github.com/FajarRamadhanBBX/deploy-model-image-classification
  ```
- Build te Image
  ```sh
    docker build -t disease-classification-from-image:latest .
  ```  
- Verify the Image
   ```sh
    docker images
   ```
   You should see disease-classification-from-image with the tag latest in the list.
