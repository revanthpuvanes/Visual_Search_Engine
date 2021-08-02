# Visual Search Engine

Lets you search the internet using images (whether they are from the web or your own) as opposed to words. By sharing a specific image with your search engine, it will then go on to find others like it.

# Demo Video



https://user-images.githubusercontent.com/80465899/127880522-4be987ae-ffff-4d47-a071-f2c4ffb4e23a.mp4

# Requirements

- pandas
- numpy
- matplotlib
- pillow
- keras
- tensorflow
- flask
- flask_ngrok
- werkzeug

# Goal

- Make a better convenience search for users.
- Applicable on any e-commerce sites.
- Brings most similar outputs to our input query.

# Datasets

We are going to solve this problem using the [Flipkart](https://www.kaggle.com/PromptCloudHQ/flipkart-products) images dataset.

# Process

We extract the images features using a pretrained VGG16 on the imagenet dataset, and also calculate the euclidean distance between the images and any desired picture to find the similar ones.

Here we are interested on the output of the fully connected layer, where we can find all the imnage features.

![](images/vgg16.png)

