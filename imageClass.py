'''
Image class

'''
import numpy as np

from PIL import Image, ImageOps, ImageFilter

import matplotlib.pyplot as plt


class ImageClass:
    def __init__(self, img_dir):
        self.img_directory = img_dir
        self.img_read = Image.open(img_dir)
        self.img_arr = np.array(self.img_read)
        self.img_X_dim = self.img_arr.shape[1]
        self.img_Y_dim = self.img_arr.shape[0]
        self.altered_img = None
        self.altered_img_arr = None
        self.altered_img_X_dim = None
        self.altered_img_Y_dim = None
        self.cropped_img = None
        self.effects = []

# BASIC IMAGE CLASS OPERATIONS

    def getMaximumImageDimension(self):
        if self.img_X_dim > self.img_Y_dim:
            return self.img_X_dim
        else:
            return self.img_Y_dim

    def displayOriginalImagePopUp(self):
        plt.imshow(self.img_read)
        plt.show()

    def displayAlteredImagePopUp(self):
        plt.imshow(self.altered_img)
        plt.show()

    def displayCroppedImagePopUp(self):
        plt.imshow(self.cropped_img)
        plt.show()

    def listImageEffects(self):
        if self.altered_img == None:
            print("No image effects currently")
        else:
            print("Current image effects present:")
            [print(effect) for effect in self.effects]

    def removeEffects(self):
        self.altered_img = None
        self.effects = []


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


# IMAGE ALTERING FUNCTIONS

    def croppedArray(self, left, right, top, bottom):
        self.cropped_img = self.img_arr[top:bottom, left:right]

    def rotateClockwise(self):
        if self.altered_img is None:
            self.altered_img = self.img_read.rotate(-90, expand=True)
        else:
            self.altered_img = self.altered_img.rotate(-90, expand=True)
        self.altered_img_arr = np.array(self.altered_img)
        self.altered_img_X_dim = self.altered_img_arr.shape[1]
        self.altered_img_Y_dim = self.altered_img_arr.shape[0]

    def rotateAntiClockwise(self):
        if self.altered_img is None:
            self.altered_img = self.img_read.rotate(90, expand=True)
        else:
            self.altered_img = self.altered_img.rotate(90, expand=True)
        self.altered_img_arr = np.array(self.altered_img)
        self.altered_img_X_dim = self.altered_img_arr.shape[1]
        self.altered_img_Y_dim = self.altered_img_arr.shape[0]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#



# IMAGE FILTERING FUNCTIONS

    def gaussianFilter(self, radius):
        if self.altered_img == None:
            self.altered_img = self.img_read.filter(ImageFilter.GaussianBlur(radius=radius))
            self.effects.append(f"Gaussian Filter with radius {radius}")
        else:
            self.altered_img = self.altered_img.filter(ImageFilter.GaussianBlur(radius=radius))
            self.effects.append(f"Gaussian Filter with radius {radius}")

    def boxBlurFilter(self, radius):
        if self.altered_img == None:
            self.altered_img = self.img_read.filter(ImageFilter.BoxBlur(radius=radius))
            self.effects.append(f"Box Blur Filter with radius {radius}")
        else:
            self.altered_img = self.altered_img.filter(ImageFilter.BoxBlur(radius=radius))
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

        if self.altered_img == None:
            if dimension == 3:
                self.altered_img = self.img_read.filter(ImageFilter.Kernel(size=(dimension, dimension), kernel=kernel_weights_3x3, scale=scale))
                self.effects.append(f"{dimension}X{dimension} Kernel filter with scale of {scale}")

            if dimension == 5:
                self.altered_img = self.img_read.filter(ImageFilter.Kernel(size=(dimension, dimension), kernel=kernel_weights_5x5, scale=scale))
                self.effects.append(f"{dimension}X{dimension} Kernel filter with scale of {scale}")

        else:
            if dimension == 3:
                self.altered_img = self.altered_img.filter(ImageFilter.Kernel(size=(dimension, dimension), kernel=kernel_weights_3x3, scale=scale))
                self.effects.append(f"{dimension}X{dimension} Kernel filter with scale of {scale}")

            if dimension == 5:
                self.altered_img = self.altered_img.filter(ImageFilter.Kernel(size=(dimension, dimension), kernel=kernel_weights_5x5, scale=scale))
                self.effects.append(f"{dimension}X{dimension} Kernel filter with scale of {scale}")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


# COLOUR CONVERTION FUNCTIONS

    def convertToGrayscale(self):
        if self.altered_img is None:
            self.altered_img = self.img_read.convert("L")
        else:
            self.altered_img = self.altered_img.convert("L")

    def imageNegative(self):
        if self.altered_img is None:
            self.altered_img = ImageOps.invert(self.img_read)
        else:
            self.altered_img = ImageOps.invert(self.altered_img)



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
