# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageEditorGUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import imageClass as IC


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
        self.checkBox = QtWidgets.QCheckBox(self.filterBox)
        self.checkBox.setGeometry(QtCore.QRect(10, 20, 81, 20))
        self.checkBox.setObjectName("checkBox")
        # Box blur
        self.checkBox_2 = QtWidgets.QCheckBox(self.filterBox)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 40, 81, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        # Kernel filter
        self.checkBox_3 = QtWidgets.QCheckBox(self.filterBox)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 60, 81, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        # ???
        self.checkBox_4 = QtWidgets.QCheckBox(self.filterBox)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 80, 81, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        # ???
        self.checkBox_5 = QtWidgets.QCheckBox(self.filterBox)
        self.checkBox_5.setGeometry(QtCore.QRect(10, 100, 81, 20))
        self.checkBox_5.setObjectName("checkBox_5")

        # Drawing tools group box (probably change to colour palette changing tools)
        self.drawBox = QtWidgets.QGroupBox(self.centralwidget)
        self.drawBox.setGeometry(QtCore.QRect(10, 400, 111, 80))
        self.drawBox.setObjectName("drawBox")

        # Label Widget for image canvas
        self.imageCanvas = QtWidgets.QLabel(self.centralwidget)
        self.imageCanvas.setGeometry(QtCore.QRect(130, 10, 861, 611))
        self.imageCanvas.setPixmap(QtGui.QPixmap("Test_image.jpg"))
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
        self.menuFile.addAction(self.actionSave_As)
        # Save image option attached to saveImage function
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionSave)
        # Exit option attached to fileExit function
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
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
        self.checkBox.setText(_translate("MainWindow", "check1"))
        self.checkBox_2.setText(_translate("MainWindow", "check2"))
        self.checkBox_3.setText(_translate("MainWindow", "check3"))
        self.checkBox_4.setText(_translate("MainWindow", "check4"))
        self.checkBox_5.setText(_translate("MainWindow", "check5"))
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
            image_object = IC.ImageClass(image_file) # Creation of image object - can apply functions from imageClass.py to object

            # Two lines below used to update the QLabel object in the GUI
            self.imageCanvas.setPixmap(QtGui.QPixmap(image_object.img_dir))
            self.imageCanvas.setScaledContents(True)
        else:
            pass


    def fileExit(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
