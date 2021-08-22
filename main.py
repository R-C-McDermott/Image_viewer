'''
Image editor programme - by Ryan C. McDermott

Written using Python 3.6.1

Packages used:
- NumPy
- Pillow
- matplotlib

'''

import imagePropertyFunctions as ipf
import imageFilterFunctions as iff
import matplotlib.pyplot as plt


img_dir = "Test_image.jpg"

def main():

    # CURRENTLY TESTING FUNCTIONS

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
