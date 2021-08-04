# Visual Search Engine

Lets you search the internet using images (whether they are from the web or your own) as opposed to words. By sharing a specific image with your search engine, it will then go on to find others like it.

![search](https://user-images.githubusercontent.com/80465899/128132937-633843d4-eb8e-4d83-970d-7524140b1097.png)


# Demo Video



https://user-images.githubusercontent.com/80465899/127880522-4be987ae-ffff-4d47-a071-f2c4ffb4e23a.mp4


# Stats

Currently, only 8% of retailers have built-in image search into their e-commerce sites; however, recent studies in both the US and the UK have shown that 62% of millennials want visual search capabilities more than any other new technology.

# “ Big Tech ” Visual Search Engines

- Google Lens
- Pinterest Lens
- Bing Visual Search
- CamFind
- EasyJet


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

Store all the output featurea as a numpy array.

Finally iterate through all the feature numpy arrays and save as a seperate csv file.

Based on score retrieve top similar images to input images.

# Workflow

The client uploads the image

Preprocessing of an input image

Extract the visual features of the uploaded image

Calculate the similarity between extracted features and trained data

Returns the most similar image to an input query

![working](https://user-images.githubusercontent.com/80465899/128133533-335e53e1-c5df-4342-a56b-854f8eb022ee.jpg)

# What we are going to improve

We improve search engine optimization by visual search

Visual search returns the most relevant results possible based on similarities, such as color or a particular style.

This certainly helps deliver a more frictionless retail experience allowing customers to find what they want, faster.

# Things to improve

Above approach supports for single inference image, like an image to image.

But for a group of objects in a same image how it is possible ?

This is were object detection cames in.

Perform a object detection first on a input image and list all available items in the image.

Finally the user can search for product actually they are looking for.

![fashion](https://user-images.githubusercontent.com/80465899/128134640-1b088953-929f-4f98-84c5-724bf4a999a8.png)
