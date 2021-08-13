'''
Image processing functions

'''
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


import skimage.io
from skimage.color import rgb2gray, rgba2rgb, lab2rgb, rgb2lab
import cv2


def test(x):
    print(x)

def importImage(image_dir):
    return skimage.io.imread(image_dir)

def displayImage(image):
    plt.imshow(image)
    plt.show()

def convertToArray(image):
    return np.array(image)

def convertToGrayscale(image):
    return rgb2gray(image)

def getImageShape(image):
    return image.shape
