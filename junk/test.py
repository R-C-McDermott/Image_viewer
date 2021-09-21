'''
Image editor programme - by Ryan C. McDermott

Written using Python 3.6.1

Packages used:
- NumPy
- Pillow
- matplotlib

'''


import matplotlib.pyplot as plt
import imageClass as im
import sys
import os

img_dir = "Test_image.jpg"

def main():

    print(sys.executable)
    print(os.getcwd())
    # CURRENTLY TESTING FUNCTIONS
    # img = im.ImageClass(img_dir)
    # print(img.img_X_dim)
    # print(img.img_Y_dim)
    #
    # # img.boxBlurFilter(20)
    # img.gaussianFilter(5)
    # img.kernelFilter(5, scale=30)
    # img.displayOriginalImagePopUp()
    # img.displayAlteredImagePopUp()
    # img.croppedArray(200, 740, 200, 550)
    # img.displayCroppedImagePopUp()
    # img.listImageEffects()
    # img = ipf.importImage(img_dir)
    # img = functions.convertToArray(img)

    # print(ipf.getImageShape(img))

    # img = iff.convertToGrayscale(img)
    # img = iff.gaussianFilter(img, 4)
    # img = iff.boxBlurFilter(img, 8)
    # img = iff.kernelFilter(img, 5)

    # ipf.displayImagePopUp(img)


if __name__ == '__main__':
    main()
