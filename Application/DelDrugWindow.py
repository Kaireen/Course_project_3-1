# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kaireen/Documents/CPr/Application/ui/DelDrugWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DrugDelWindow(object):
    def setupUi(self, DrugDelWindow):
        DrugDelWindow.setObjectName("DrugDelWindow")
        DrugDelWindow.resize(200, 100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DrugDelWindow.sizePolicy().hasHeightForWidth())
        DrugDelWindow.setSizePolicy(sizePolicy)
        DrugDelWindow.setMinimumSize(QtCore.QSize(200, 100))
        DrugDelWindow.setMaximumSize(QtCore.QSize(200, 100))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/kaireen/Documents/CPr/Application/ui/../media/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DrugDelWindow.setWindowIcon(icon)
        DrugDelWindow.setStyleSheet("background-color: rgb(32, 178, 170);")
        self.del_drug_btn = QtWidgets.QPushButton(DrugDelWindow)
        self.del_drug_btn.setGeometry(QtCore.QRect(50, 60, 93, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.del_drug_btn.setFont(font)
        self.del_drug_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 172, 172);\n"
"    color: rgb(0, 0, 0);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(105, 205, 255);\n"
"}")
        self.del_drug_btn.setObjectName("del_drug_btn")
        self.label_4 = QtWidgets.QLabel(DrugDelWindow)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.drug_id_spnbox = QtWidgets.QSpinBox(DrugDelWindow)
        self.drug_id_spnbox.setGeometry(QtCore.QRect(90, 20, 91, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.drug_id_spnbox.setFont(font)
        self.drug_id_spnbox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 15px;")
        self.drug_id_spnbox.setMaximum(999999)
        self.drug_id_spnbox.setObjectName("drug_id_spnbox")

        self.retranslateUi(DrugDelWindow)
        QtCore.QMetaObject.connectSlotsByName(DrugDelWindow)

    def retranslateUi(self, DrugDelWindow):
        _translate = QtCore.QCoreApplication.translate
        DrugDelWindow.setWindowTitle(_translate("DrugDelWindow", "Delete Drug"))
        self.del_drug_btn.setText(_translate("DrugDelWindow", "Delete drug"))
        self.label_4.setText(_translate("DrugDelWindow", "Drug ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DrugDelWindow = QtWidgets.QDialog()
    ui = Ui_DrugDelWindow()
    ui.setupUi(DrugDelWindow)
    DrugDelWindow.show()
    sys.exit(app.exec_())
