'''
Image processing functions

'''
import numpy as np

from PIL import Image

import matplotlib.pyplot as plt

def importImage(image_dir):
    return Image.open(image_dir)

def displayImagePopUp(image):
    plt.imshow(image)
    plt.show()

def convertToArray(image):
    return np.array(image)

def getImageShape(image):
    if isinstance(image, np.ndarray) == False:
        image = convertToArray(image)
        return image.shape[1], image.shape[0] # X and Y coordinates in order
    else:
        return image.shape[1], image.shape[0] # X and Y coordinates in order
