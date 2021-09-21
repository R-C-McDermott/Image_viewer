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

        # Label Widget for image position
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(850, 630, 91, 21))
        self.label.setObjectName("label")

        # Image editing tools group box properties
        self.editBox = QtWidgets.QGroupBox(self.centralwidget)
        self.editBox.setGeometry(QtCore.QRect(10, 10, 111, 181))
        self.editBox.setObjectName("editBox")
        # Image editing tools (buttons)
        self.cropButton = QtWidgets.QPushButton(self.editBox)
        self.cropButton.setGeometry(QtCore.QRect(10, 20, 93, 28))
        self.cropButton.setObjectName("cropButton")

        # Image filter group box properties
        self.filterBox = QtWidgets.QGroupBox(self.centralwidget)
        self.filterBox.setGeometry(QtCore.QRect(10, 190, 111, 211))
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
        # Remove filters
        self.removeFilters = QtWidgets.QPushButton(self.filterBox)
        self.removeFilters.setGeometry(QtCore.QRect(10, 110, 93, 28))
        self.removeFilters.setObjectName("removeFilters")
        self.removeFilters.clicked.connect(self.revertOriginal)
        # Undo filter - UNUSED
        # self.undoFilterButton = QtWidgets.QPushButton(self.filterBox)
        # self.undoFilterButton.setGeometry(QtCore.QRect(10, 140, 93, 28))
        # self.undoFilterButton.setObjectName("undoFilterButton")
        # self.undoFilterButton.clicked.connect(self.undoFilter)

        # Drawing tools group box (probably change to colour palette changing tools)
        self.drawBox = QtWidgets.QGroupBox(self.centralwidget)
        self.drawBox.setGeometry(QtCore.QRect(10, 400, 111, 80))
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
        self.actionSave_As.triggered.connect(self.imageSave)
        self.menuFile.addAction(self.actionSave_As)
        # Save image option attached to saveImage function
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
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
        self.label.setText(_translate("MainWindow", "Position:"))
        self.filterBox.setTitle(_translate("MainWindow", "Filter"))
        self.gaussian.setText(_translate("MainWindow", "Gaussian Filter"))
        self.boxBlur.setText(_translate("MainWindow", "Box Blur"))
        self.kernelFilt.setText(_translate("MainWindow", "Kernel Filter"))
        self.removeFilters.setText(_translate("MainWindow", "Remove Filters"))
        # self.undoFilterButton.setText(_translate("MainWindow", "Undo Filter"))
        self.drawBox.setTitle(_translate("MainWindow", "Draw"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def openImage(self):
        image_file, _ = QFileDialog.getOpenFileName(self.imageCanvas, "Image Selector",
                                                    "hello", "Images (*.png *.xpm *.jpg)")
        # If user presses cancel, the function will pass and the image object will not be created
        if image_file != "":
            global image_object
            # Creation of image object - can apply functions from imageClass.py to object
            image_object = IC.ImageClass(image_file)
            image_object.img_read.save(os.path.dirname(__file__) + "/temp/ORIGINAL.jpg")
            # Two lines below used to update the QLabel object in the GUI
            self.imageCanvas.setPixmap(QtGui.QPixmap().fromImage(image_object.img))
            self.imageCanvas.setScaledContents(True)
        else:
            pass

    def imageSave(self):
        pass
        # name = QFileDialog.getSaveFileName(self, 'Save File')
        # print(name)
        # file = open(name, 'w')
        # text = self.textEdit.toPlainText()
        # file.write(text)
        # file.close()

    def filterGaussian(self):
        image_object.gaussianFilter(5)
        image_object.filtered_img.save(os.path.dirname(__file__) + "/temp/FILTERED.jpg")
        self.imageCanvas.setPixmap(QtGui.QPixmap().fromImage(QImage(os.path.dirname(__file__) + "/temp/FILTERED.jpg")))
        self.imageCanvas.setScaledContents(True)

    def filterBoxBlur(self):
        image_object.boxBlurFilter(5)
        image_object.filtered_img.save(os.path.dirname(__file__) + "/temp/FILTERED.jpg")
        self.imageCanvas.setPixmap(QtGui.QPixmap().fromImage(QImage(os.path.dirname(__file__) + "/temp/FILTERED.jpg")))
        self.imageCanvas.setScaledContents(True)

    def filterKernel(self):
        image_object.kernelFilter(5)
        image_object.filtered_img.save(os.path.dirname(__file__) + "/temp/FILTERED.jpg")
        self.imageCanvas.setPixmap(QtGui.QPixmap().fromImage(QImage(os.path.dirname(__file__) + "/temp/FILTERED.jpg")))
        self.imageCanvas.setScaledContents(True)

    def revertOriginal(self):
        image_object.filtered_img = None
        image_object.effects = []
        self.imageCanvas.setPixmap(QtGui.QPixmap().fromImage(QImage(os.path.dirname(__file__) + "/temp/ORIGINAL.jpg")))
        self.imageCanvas.setScaledContents(True)

    def fileExit(self):
        sys.exit(app.exec_())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
