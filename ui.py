# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import subprocess
import pandas as pd
import scraper


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.maxst = False
        self.mst = False
        self.from_building = None
        self.to_building = None
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(801, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 0, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(27)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 90, 261, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(12)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 250, 181, 71))
        self.pushButton.clicked.connect(self.openExternal)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 250, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox.stateChanged.connect(self.checkbox_changed)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_2.stateChanged.connect(self.checkbox_changed2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(580, 169, 160, 291))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemClicked.connect(self.on_selection_changed)
        self.verticalLayout_2.addWidget(self.listWidget)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.listWidget_2 = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_2.itemClicked.connect(self.on_selection_changed_2)
        self.verticalLayout_2.addWidget(self.listWidget_2)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(240, 470, 321, 71))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.on_button_clicked)
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        try:
            self.data = pd.read_csv("building.csv",sep=',')
            for ind,item in self.data.iterrows():
                self.listWidget.addItem(item.at["Building"])
                self.listWidget_2.addItem(item.at["Building"])
        except:
            pass
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Unipath"))
        self.label.setText(_translate("MainWindow", "Unipath"))
        self.label_2.setText(_translate("MainWindow", "College Campus Mapper"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.label_3.setText(_translate("MainWindow", "Visualization"))
        self.checkBox.setText(_translate("MainWindow", "MinST"))
        self.checkBox_2.setText(_translate("MainWindow", "MaxST"))
        self.label_5.setText(_translate("MainWindow", "Singular Path"))
        self.label_6.setText(_translate("MainWindow", "From"))
        self.label_4.setText(_translate("MainWindow", "to"))
        self.label_7.setText(_translate("MainWindow", "Format: \"Wikipedia Link of Buildings, Other Identifiers (City, State, etc.)\""))
        self.pushButton_2.setText(_translate("MainWindow", "Enter"))
    
    def checkbox_changed(self, state):
        self.mst = state == QtCore.Qt.Checked
        self.listWidget.clearSelection()
        self.listWidget_2.clearSelection()
        self.from_building = None
        self.to_building = None
        if state == QtCore.Qt.Checked:
            self.checkBox_2.setChecked(False)

    def checkbox_changed2(self, state):
        self.maxst = state == QtCore.Qt.Checked
        self.listWidget.clearSelection()
        self.listWidget_2.clearSelection()
        self.from_building = None
        self.to_building = None
        if state == QtCore.Qt.Checked:
            self.checkBox.setChecked(False)
    
    def on_selection_changed(self):
        self.from_building = self.listWidget.currentItem().text()
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        if (self.from_building == self.to_building):
            self.to_building = None
            self.listWidget_2.clearSelection()

    
    def on_selection_changed_2(self):
        self.to_building = self.listWidget_2.currentItem().text()
        self.checkBox.setChecked(False)
        self.checkBox_2.setChecked(False)
        if (self.from_building == self.to_building):
            self.from_building = None
            self.listWidget.clearSelection()

    def on_button_clicked(self):
        userInput = self.textEdit.text()
        userInput = userInput.split(", ")
        for item in userInput:
            print(item)
        if (len(userInput) > 1):
            city = userInput[1]
        else:
            city = ""
        success = scraper.scrape(userInput[0],city)
        if success:
            self.data = pd.read_csv("building.csv",sep=',',encoding='windows-1252')
            self.listWidget.clear()
            self.listWidget_2.clear()
            for ind,item in self.data.iterrows():
                self.listWidget.addItem(item.at["Building"])
                self.listWidget_2.addItem(item.at["Building"])
        else:
            self.textEdit.setText("Invalid Wikipedia link")
        
        
    def openExternal(self):
        if self.from_building is not None and self.to_building is not None:
            subprocess.run(['python', 'main.py', self.from_building, self.to_building])
        else:
            if self.mst:
                subprocess.run(['python', 'main.py', 'mst'])
            elif self.maxst:
                subprocess.run(['python', 'main.py', 'maxst'])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


