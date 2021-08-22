'''

Image filter functions

'''

from PIL import ImageFilter


# Image filters
def gaussianFilter(image, radius):
    return image.filter(ImageFilter.GaussianBlur(radius=radius))

def boxBlurFilter(image, radius):
    return image.filter(ImageFilter.BoxBlur(radius=radius))

def kernelFilter(image, dimension):

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

    if dimension == 3:
        return image.filter(ImageFilter.Kernel(size=(dimension, dimension), kernel=kernel_weights_3x3))

    if dimension == 5:
        return image.filter(ImageFilter.Kernel(size=(dimension, dimension), kernel=kernel_weights_5x5))



# Colour palette functions
def convertToGrayscale(image):
    return image.convert("LA")
