# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kaireen/Documents/CPr/Application/windows_ui/ManufacturerAddingWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ManufacturerAddingWindow(object):
    def setupUi(self, ManufacturerAddingWindow):
        ManufacturerAddingWindow.setObjectName("ManufacturerAddingWindow")
        ManufacturerAddingWindow.setEnabled(True)
        ManufacturerAddingWindow.resize(550, 310)
        ManufacturerAddingWindow.setMinimumSize(QtCore.QSize(550, 310))
        ManufacturerAddingWindow.setMaximumSize(QtCore.QSize(550, 310))
        font = QtGui.QFont()
        font.setPointSize(8)
        ManufacturerAddingWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/kaireen/Documents/CPr/Application/windows_ui/../media/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ManufacturerAddingWindow.setWindowIcon(icon)
        ManufacturerAddingWindow.setStyleSheet("background-color: rgb(32, 178, 170);")
        self.add_manufacturer_btn = QtWidgets.QPushButton(ManufacturerAddingWindow)
        self.add_manufacturer_btn.setGeometry(QtCore.QRect(440, 270, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.add_manufacturer_btn.setFont(font)
        self.add_manufacturer_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 172, 172);\n"
"    color: rgb(0, 0, 0);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(105, 205, 255);\n"
"}")
        self.add_manufacturer_btn.setObjectName("add_manufacturer_btn")
        self.manufacturer_name_fld = QtWidgets.QLineEdit(ManufacturerAddingWindow)
        self.manufacturer_name_fld.setGeometry(QtCore.QRect(20, 10, 311, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.manufacturer_name_fld.setFont(font)
        self.manufacturer_name_fld.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 15px;")
        self.manufacturer_name_fld.setMaxLength(200)
        self.manufacturer_name_fld.setObjectName("manufacturer_name_fld")
        self.contact_info_fld = QtWidgets.QPlainTextEdit(ManufacturerAddingWindow)
        self.contact_info_fld.setGeometry(QtCore.QRect(20, 80, 511, 181))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contact_info_fld.setFont(font)
        self.contact_info_fld.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 15px;")
        self.contact_info_fld.setMaximumBlockCount(0)
        self.contact_info_fld.setBackgroundVisible(False)
        self.contact_info_fld.setObjectName("contact_info_fld")
        self.country_fld = QtWidgets.QLineEdit(ManufacturerAddingWindow)
        self.country_fld.setGeometry(QtCore.QRect(20, 40, 311, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.country_fld.setFont(font)
        self.country_fld.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 15px;")
        self.country_fld.setMaxLength(200)
        self.country_fld.setObjectName("country_fld")

        self.retranslateUi(ManufacturerAddingWindow)
        QtCore.QMetaObject.connectSlotsByName(ManufacturerAddingWindow)

    def retranslateUi(self, ManufacturerAddingWindow):
        _translate = QtCore.QCoreApplication.translate
        ManufacturerAddingWindow.setWindowTitle(_translate("ManufacturerAddingWindow", "Manufacturer Adding"))
        self.add_manufacturer_btn.setText(_translate("ManufacturerAddingWindow", "Add"))
        self.manufacturer_name_fld.setPlaceholderText(_translate("ManufacturerAddingWindow", "Manufacturer name"))
        self.contact_info_fld.setPlaceholderText(_translate("ManufacturerAddingWindow", "Contact info"))
        self.country_fld.setPlaceholderText(_translate("ManufacturerAddingWindow", "Country"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ManufacturerAddingWindow = QtWidgets.QDialog()
    ui = Ui_ManufacturerAddingWindow()
    ui.setupUi(ManufacturerAddingWindow)
    ManufacturerAddingWindow.show()
    sys.exit(app.exec_())