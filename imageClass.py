'''
Image class

'''
import numpy as np

from PIL import Image
from PIL import ImageFilter

import matplotlib.pyplot as plt


class ImageClass:
    def __init__(self, img_dir):
        self.img = Image.open(img_dir)
        self.img_arr = np.array(self.img)
        self.img_X_dim = self.img_arr.shape[1]
        self.img_Y_dim = self.img_arr.shape[0]
        self.filtered_img = None
        self.cropped_img = None
        self.effects = []

# BASIC IMAGE CLASS OPERATIONS

    def displayOriginalImagePopUp(self):
        plt.imshow(self.img)
        plt.show()

    def displayAlteredImagePopUp(self):
        plt.imshow(self.filtered_img)
        plt.show()

    def displayCroppedImagePopUp(self):
        plt.imshow(self.cropped_img)
        plt.show()

    def listImageEffects(self):
        if self.filtered_img == None:
            print("No image effects currently")
        else:
            print("Current image effects present:")
            [print(effect) for effect in self.effects]

    def removeEffects(self):
        self.filtered_img = None
        self.effects = []

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


# IMAGE ALTERING FUNCTIONS

    def croppedArray(self, left, right, top, bottom):
        self.cropped_img = self.img_arr[top:bottom, left:right]

    

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#



# IMAGE FILTERING FUNCTIONS

    def gaussianFilter(self, radius):
        if self.filtered_img == None:
            self.filtered_img = self.img.filter(ImageFilter.GaussianBlur(radius=radius))
            self.effects.append(f"Gaussian Filter with radius {radius}")
        else:
            self.filtered_img = self.filtered_img.filter(ImageFilter.GaussianBlur(radius=radius))
            self.effects.append(f"Gaussian Filter with radius {radius}")

    def boxBlurFilter(self, radius):
        if self.filtered_img == None:
            self.filtered_img = self.img.filter(ImageFilter.BoxBlur(radius=radius))
            self.effects.append(f"Box Blur Filter with radius {radius}")
        else:
            self.filtered_img = self.filtered_img.filter(ImageFilter.BoxBlur(radius=radius))
            self.effects.append(f"Box Blur Filter with radius {radius}")

    def kernelFilter(self, dimension, scale=None):

        kernel_weights_3x3 = (
            1,2,1,
            1,5,1,
            1,2,1,
        )

        kernel_weights_5x5 = (
            1,2,4,2,1,
            1,3,5,3,1,
            1,5,10,5,1,
            1,3,5,3,1,
            1,2,4,2,1,
        )

        if self.filtered_img == None:
            if dimension == 3:
                self.filtered_img = self.img.filter(ImageFilter.Kernel(size=(dimension, dimension), kernel=kernel_weights_3x3, scale=scale))
                self.effects.append(f"{dimension}X{dimension} Kernel filter with scale of {scale}")

            if dimension == 5:
                self.filtered_img = self.img.filter(ImageFilter.Kernel(size=(dimension, dimension), kernel=kernel_weights_5x5, scale=scale))
                self.effects.append(f"{dimension}X{dimension} Kernel filter with scale of {scale}")

        else:
            if dimension == 3:
                self.filtered_img = self.filtered_img.filter(ImageFilter.Kernel(size=(dimension, dimension), kernel=kernel_weights_3x3, scale=scale))
                self.effects.append(f"{dimension}X{dimension} Kernel filter with scale of {scale}")

            if dimension == 5:
                self.filtered_img = self.filtered_img.filter(ImageFilter.Kernel(size=(dimension, dimension), kernel=kernel_weights_5x5, scale=scale))
                self.effects.append(f"{dimension}X{dimension} Kernel filter with scale of {scale}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


# COLOUR CONVERTION FUNCTIONS

    def convertToGrayscale(self):
        if self.filtered_img == None:
            self.filtered_img = self.img.convert("LA")
        else:
            self.filtered_img = self.filtered_img.convert("LA")



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
