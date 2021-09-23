# RCM Image editor by Ryan C. McDermott
#
# GUI built using the PyQt5 library in Python
#
# Imports image editing functions and image class from ImageClass.py
#
# GitHub: https://github.com/R-C-McDermott/Image_editor.git

# Library imports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import imageClass as IC
import os


# GUI Class
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1008, 721)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        # Image editing tools group box properties
        self.editBox = QtWidgets.QGroupBox(self.centralwidget)
        self.editBox.setGeometry(QtCore.QRect(10, 10, 111, 181))
        self.editBox.setObjectName("editBox")
        # Image editing tools (buttons)
        # Crop image
        self.cropButton = QtWidgets.QPushButton(self.editBox)
        self.cropButton.setGeometry(QtCore.QRect(10, 20, 93, 28))
        self.cropButton.setObjectName("cropButton")
        # Rotate image clockwise
        self.clockwiseButton = QtWidgets.QPushButton(self.editBox)
        self.clockwiseButton.setGeometry(QtCore.QRect(10, 50, 93, 56))
        self.clockwiseButton.setObjectName("clockwiseButton")
        self.clockwiseButton.clicked.connect(self.rotateImageClockwise)
        # Rotate image anti-clockwise
        self.antiClockwiseButton = QtWidgets.QPushButton(self.editBox)
        self.antiClockwiseButton.setGeometry(QtCore.QRect(10, 108, 93, 56))
        self.antiClockwiseButton.setObjectName("clockwiseButton")
        self.antiClockwiseButton.clicked.connect(self.rotateImageAntiClockwise)
        # Image filter group box properties
        self.filterBox = QtWidgets.QGroupBox(self.centralwidget)
        self.filterBox.setGeometry(QtCore.QRect(10, 190, 111, 331))
        self.filterBox.setObjectName("filterBox")
        # Check boxes for filters (may change)
        # Gaussian filter
        self.gaussian = QtWidgets.QPushButton(self.filterBox)
        self.gaussian.setGeometry(QtCore.QRect(10, 20, 93, 28))
        self.gaussian.setObjectName("gaussian")
        self.gaussian.clicked.connect(self.filterGaussian)
        # Box blur
        self.boxBlur = QtWidgets.QPushButton(self.filterBox)
        self.boxBlur.setGeometry(QtCore.QRect(10, 50, 93, 28))
        self.boxBlur.setObjectName("boxBlur")
        self.boxBlur.clicked.connect(self.filterBoxBlur)
        # Kernel filter
        self.kernelFilt = QtWidgets.QPushButton(self.filterBox)
        self.kernelFilt.setGeometry(QtCore.QRect(10, 80, 93, 28))
        self.kernelFilt.setObjectName("kernelFilt")
        self.kernelFilt.clicked.connect(self.filterKernel)
        # Image Negative
        self.negative = QtWidgets.QPushButton(self.filterBox)
        self.negative.setGeometry(QtCore.QRect(10, 110, 93, 28))
        self.negative.setObjectName("negativeButton")
        self.negative.clicked.connect(self.filterImageNegative)
        # Grayscale
        self.grayScale = QtWidgets.QPushButton(self.filterBox)
        self.grayScale.setGeometry(QtCore.QRect(10, 140, 93, 28))
        self.grayScale.setObjectName("grayscaleButton")
        self.grayScale.clicked.connect(self.filterGrayScale)
        # Remove filters
        self.removeFilters = QtWidgets.QPushButton(self.filterBox)
        self.removeFilters.setGeometry(QtCore.QRect(10, 260, 93, 56))
        self.removeFilters.setObjectName("removeFilters")
        self.removeFilters.clicked.connect(self.revertOriginal)

        # Drawing tools group box (probably change to colour palette changing tools)
        self.drawBox = QtWidgets.QGroupBox(self.centralwidget)
        self.drawBox.setGeometry(QtCore.QRect(10, 519, 111, 80))
        self.drawBox.setObjectName("drawBox")

        # Label Widget for image canvas
        self.imageCanvas = QtWidgets.QLabel(self.centralwidget)
        self.imageCanvas.setGeometry(QtCore.QRect(130, 10, 861, 611))
        self.imageCanvas.setScaledContents(True)
        self.imageCanvas.setObjectName("imageCanvas")

        # Menu bar creation
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1008, 26))
        self.menubar.setObjectName("menubar")
        # Create 'File' drop down
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menubar.addAction(self.menuFile.menuAction())
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # Open image option attached to openImage function
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.openImage)
        self.menuFile.addAction(self.actionOpen)
        # Save image option attached to saveAsImage function
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSave_As.triggered.connect(self.imageSaveAs)
        self.menuFile.addAction(self.actionSave_As)
        # Save image option attached to saveImage function
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(self.imageSave)
        self.menuFile.addAction(self.actionSave)
        # Exit option attached to fileExit function
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(self.fileExit)
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RCM Image Editor"))
        self.editBox.setTitle(_translate("MainWindow", "Edit"))
        self.cropButton.setText(_translate("MainWindow", "Crop"))
        self.clockwiseButton.setText(_translate("MainWindow", "Rotate\nClockwise"))
        self.antiClockwiseButton.setText(_translate("MainWindow", "Rotate\nAnti-Clockwise"))
        self.grayScale.setText(_translate("MainWindow", "Grayscale"))
        self.negative.setText(_translate("MainWindow", "Negative"))
        self.filterBox.setTitle(_translate("MainWindow", "Filter"))
        self.gaussian.setText(_translate("MainWindow", "Gaussian Filter"))
        self.boxBlur.setText(_translate("MainWindow", "Box Blur"))
        self.kernelFilt.setText(_translate("MainWindow", "Kernel Filter"))
        self.removeFilters.setText(_translate("MainWindow", "Remove\nEffects"))
        self.drawBox.setTitle(_translate("MainWindow", "Draw"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def openImage(self):
        image_file, _ = QFileDialog.getOpenFileName(self.imageCanvas, "Image Selector",
                                                    "", "Images (*.png *.xpm *.jpg)")
        # If user presses cancel, the function will pass and the image object will not be created
        if image_file != "":
            global image_object
            # Creation of image object - can apply functions from imageClass.py to object
            image_object = IC.ImageClass(image_file)
            max_dimension = image_object.getMaximumImageDimension()
            image_object.img_read.save(os.path.dirname(__file__) + "/temp/ORIGINAL.jpg")
            # Two lines below used to update the QLabel object in the GUI
            self.imageCanvas.setPixmap(QtGui.QPixmap().fromImage(QImage(image_object.img_directory)))
            self.imageCanvas.setGeometry(QtCore.QRect(130, 10, image_object.img_X_dim, image_object.img_Y_dim))
            # MainWindow.resize(160+max_dimension, 80+max_dimension)
            MainWindow.resize(160+image_object.img_X_dim, 80+image_object.img_Y_dim)


            self.imageCanvas.setScaledContents(False)
        else:
            pass

    def imageSaveAs(self):
        save_name, _ = QFileDialog.getSaveFileName(self.imageCanvas, 'Save File',
                                           "", "Images (*.png *.xpm *.jpg)")
        image_object.img_directory = save_name
        if image_object.altered_img is None:
            image_object.img_read.save(save_name)
        else:
            image_object.altered_img.save(save_name)

    def imageSave(self):
        if image_object.altered_img is None:
            image_object.img_read.save(image_object.img_directory)
        else:
            image_object.altered_img.save(image_object.img_directory)

    def filterGaussian(self):
        image_object.gaussianFilter(5)
        image_object.altered_img.save(os.path.dirname(__file__) + "/temp/ALTERED.jpg")
        self.imageCanvas.setPixmap(QtGui.QPixmap().fromImage(QImage(os.path.dirname(__file__) + "/temp/ALTERED.jpg")))
        self.imageCanvas.setScaledContents(True)

    def filterBoxBlur(self):
        image_object.boxBlurFilter(5)
        image_object.altered_img.save(os.path.dirname(__file__) + "/temp/ALTERED.jpg")
        self.imageCanvas.setPixmap(QtGui.QPixmap().fromImage(QImage(os.path.dirname(__file__) + "/temp/ALTERED.jpg")))
        self.imageCanvas.setScaledContents(True)

    def filterKernel(self):
        image_object.kernelFilter(5)
        image_object.altered_img.save(os.path.dirname(__file__) + "/temp/ALTERED.jpg")
        self.imageCanvas.setPixmap(QtGui.QPixmap().fromImage(QImage(os.path.dirname(__file__) + "/temp/ALTERED.jpg")))
        self.imageCanvas.setScaledContents(True)

    def revertOriginal(self):
        image_object.removeEffects()
        self.imageCanvas.setPixmap(QtGui.QPixmap().fromImage(QImage(os.path.dirname(__file__) + "/temp/ORIGINAL.jpg")))
        self.imageCanvas.setGeometry(QtCore.QRect(130, 10, image_object.img_X_dim, image_object.img_Y_dim))
        self.imageCanvas.setScaledContents(False)

    def fileExit(self):
        sys.exit(app.exec_())

    def filterGrayScale(self):
        image_object.convertToGrayscale()
        image_object.altered_img.save(os.path.dirname(__file__) + "/temp/ALTERED.jpg")
        self.imageCanvas.setPixmap(QtGui.QPixmap().fromImage(QImage(os.path.dirname(__file__) + "/temp/ALTERED.jpg")))
        self.imageCanvas.setScaledContents(True)

    def filterImageNegative(self):
        image_object.imageNegative()
        image_object.altered_img.save(os.path.dirname(__file__) + "/temp/ALTERED.jpg")
        self.imageCanvas.setPixmap(QtGui.QPixmap().fromImage(QImage(os.path.dirname(__file__) + "/temp/ALTERED.jpg")))
        self.imageCanvas.setScaledContents(True)

    def rotateImageClockwise(self):
        image_object.rotateClockwise()
        image_object.altered_img.save(os.path.dirname(__file__) + "/temp/ALTERED.jpg")
        self.imageCanvas.setPixmap(QtGui.QPixmap().fromImage(QImage(os.path.dirname(__file__) + "/temp/ALTERED.jpg")))
        self.imageCanvas.setGeometry(QtCore.QRect(130, 10, image_object.altered_img_X_dim, image_object.altered_img_Y_dim))
        MainWindow.resize(160 + image_object.altered_img_X_dim, 80 + image_object.altered_img_Y_dim)
        self.imageCanvas.setScaledContents(False)

    def rotateImageAntiClockwise(self):
        image_object.rotateAntiClockwise()
        image_object.altered_img.save(os.path.dirname(__file__) + "/temp/ALTERED.jpg")
        self.imageCanvas.setPixmap(QtGui.QPixmap().fromImage(QImage(os.path.dirname(__file__) + "/temp/ALTERED.jpg")))
        self.imageCanvas.setGeometry(QtCore.QRect(130, 10, image_object.altered_img_X_dim, image_object.altered_img_Y_dim))
        MainWindow.resize(160 + image_object.altered_img_X_dim, 80 + image_object.altered_img_Y_dim)
        self.imageCanvas.setScaledContents(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
