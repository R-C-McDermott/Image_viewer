'''
Image editor programme - by Ryan C. McDermott

Written using Python 3.6.1

Packages used:
- NumPy
- Scikit-Image
- Pillow
- Open-CV

'''


import functions
import matplotlib.pyplot as plt


img_dir = "Test_image.jpg"

def main():
    img = functions.importImage(img_dir)
    img = functions.convertToArray(img)
    print(functions.getImageShape(img))

    img = functions.convertToGrayscale(img)
    print(functions.getImageShape(img))
    functions.displayImage(img)


if __name__ == '__main__':
    main()
