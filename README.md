# Torrent_to_Drive

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1pO6CaIFIdJ_4Rc4X3vpBxQdnXMm0zhJ5#scrollTo=s4TwJU-pVNC9)

**Automatic Image Captioning**, using Deep Learning and Flickr-8k Dataset.
Also made a comparison between Xception Model and Inception Model.

This is the easiest way to generate captions and alt text for all kind of images using
Convolutional Neural Networks and a type of Recurrent Neural Network (LSTM).

## About

The image features will be extracted from CNN models trained on the imagenet dataset (see below)
and then the features are fed into the LSTM model which will be responsible for generating the image captions.

This Repo revolves around 2 Models provided by Keras.

- [Inception](https://keras.io/api/applications/inceptionv3/)
- [Xception](https://keras.io/api/applications/xception/)

1. Features Extracted can be found [here](Features)
1. Dataset used can be found [here](Dataset)
1. Jupyter Notebooks can be found [here](Notebook)
1. Models Trained can be found [here](Model)
1. Requirements and dependencies can be found [here](requirements.txt)
1. Caption generator can be found [here](generator.py)

Want to contribute? Suggestions, Error reporting, Bug Solving are highly
appreciated, please open an Issue and/or PR
[here](https://github.com/vybhav72954/Automated_Image_Captioning)

## Setup 

- Setup a Virtual Environment (HIGHLY RECOMMENDED)
- Activate the Environment.
- Install Requirements, use `pip3 install -r requirements.txt`
  - NOTE: A GPU accelerated hardware is recommended, after `TF v2.1`,
    _there is no need to install GPU separately._ So no need to use `pip3 install tensorflow-gpu`
    For GPU, separate Guidelines are provided [here](#GPU).
- TODO    

### GPU

It is recommended to train these Neural Networks using GPU accelerated hardware.
User first need to have a CUDA enabled Graphics Card, if this condition is met, Download CUDA toolkit and cuDNN library.

For installation and help, these links are helpful:

LINK1
LINK2
LINK3

## Usage

TODO

#### Author
Made by [Vybhav Chaturvedi](https://www.linkedin.com/in/vybhav-chaturvedi-0ba82614a/)

## Disclaimer

Using GPU for training these networks can lead to Memory overflow errors,
long sessions can lead to overheating issues and can cause similar problems related to GPU computing.

Carefully read the CUDA guidelines to avoid any problems.
