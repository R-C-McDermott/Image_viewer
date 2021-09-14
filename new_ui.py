# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageEditorGUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1008, 721)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.editBox = QtWidgets.QGroupBox(self.centralwidget)
        self.editBox.setGeometry(QtCore.QRect(10, 10, 111, 181))
        self.editBox.setObjectName("editBox")
        self.cropButton = QtWidgets.QPushButton(self.editBox)
        self.cropButton.setGeometry(QtCore.QRect(10, 20, 93, 28))
        self.cropButton.setObjectName("cropButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(850, 630, 91, 21))
        self.label.setObjectName("label")
        self.filterBox = QtWidgets.QGroupBox(self.centralwidget)
        self.filterBox.setGeometry(QtCore.QRect(10, 190, 111, 211))
        self.filterBox.setObjectName("filterBox")
        self.gaussian = QtWidgets.QPushButton(self.filterBox)
        self.gaussian.setGeometry(QtCore.QRect(10, 20, 93, 28))
        self.gaussian.setMouseTracking(False)
        self.gaussian.setObjectName("gaussian")
        self.boxBlur = QtWidgets.QPushButton(self.filterBox)
        self.boxBlur.setGeometry(QtCore.QRect(10, 50, 93, 28))
        self.boxBlur.setObjectName("boxBlur")
        self.kernelFilt = QtWidgets.QPushButton(self.filterBox)
        self.kernelFilt.setGeometry(QtCore.QRect(10, 80, 93, 28))
        self.kernelFilt.setObjectName("kernelFilt")
        self.pushButton_4 = QtWidgets.QPushButton(self.filterBox)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 110, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.drawBox = QtWidgets.QGroupBox(self.centralwidget)
        self.drawBox.setGeometry(QtCore.QRect(10, 400, 111, 80))
        self.drawBox.setObjectName("drawBox")
        self.imageCanvas = QtWidgets.QLabel(self.centralwidget)
        self.imageCanvas.setGeometry(QtCore.QRect(130, 10, 861, 611))
        self.imageCanvas.setText("")
        self.imageCanvas.setPixmap(QtGui.QPixmap("Test_image.jpg"))
        self.imageCanvas.setScaledContents(True)
        self.imageCanvas.setObjectName("imageCanvas")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1008, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

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
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.drawBox.setTitle(_translate("MainWindow", "Draw"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))