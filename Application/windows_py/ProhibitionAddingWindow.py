# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kaireen/Documents/CPr/Application/windows_ui/ProhibitionAddingWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProhibitionAddingWindow(object):
    def setupUi(self, ProhibitionAddingWindow):
        ProhibitionAddingWindow.setObjectName("ProhibitionAddingWindow")
        ProhibitionAddingWindow.resize(420, 160)
        ProhibitionAddingWindow.setMinimumSize(QtCore.QSize(420, 160))
        ProhibitionAddingWindow.setMaximumSize(QtCore.QSize(420, 160))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/kaireen/Documents/CPr/Application/windows_ui/../media/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ProhibitionAddingWindow.setWindowIcon(icon)
        ProhibitionAddingWindow.setStyleSheet("background-color: rgb(32, 178, 170);")
        self.rank_cbox = QtWidgets.QComboBox(ProhibitionAddingWindow)
        self.rank_cbox.setGeometry(QtCore.QRect(20, 80, 381, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rank_cbox.setFont(font)
        self.rank_cbox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 15px;")
        self.rank_cbox.setCurrentText("")
        self.rank_cbox.setObjectName("rank_cbox")
        self.label = QtWidgets.QLabel(ProhibitionAddingWindow)
        self.label.setGeometry(QtCore.QRect(20, 60, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.add_prohibition_btn = QtWidgets.QPushButton(ProhibitionAddingWindow)
        self.add_prohibition_btn.setGeometry(QtCore.QRect(310, 120, 93, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.add_prohibition_btn.setFont(font)
        self.add_prohibition_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 172, 172);\n"
"    color: rgb(0, 0, 0);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(105, 205, 255);\n"
"}")
        self.add_prohibition_btn.setObjectName("add_prohibition_btn")
        self.label_4 = QtWidgets.QLabel(ProhibitionAddingWindow)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.drug_id_spnbox = QtWidgets.QSpinBox(ProhibitionAddingWindow)
        self.drug_id_spnbox.setGeometry(QtCore.QRect(20, 30, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.drug_id_spnbox.setFont(font)
        self.drug_id_spnbox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 15px;")
        self.drug_id_spnbox.setMaximum(999999)
        self.drug_id_spnbox.setObjectName("drug_id_spnbox")

        self.retranslateUi(ProhibitionAddingWindow)
        QtCore.QMetaObject.connectSlotsByName(ProhibitionAddingWindow)

    def retranslateUi(self, ProhibitionAddingWindow):
        _translate = QtCore.QCoreApplication.translate
        ProhibitionAddingWindow.setWindowTitle(_translate("ProhibitionAddingWindow", "Prohibition Adding"))
        self.rank_cbox.setPlaceholderText(_translate("ProhibitionAddingWindow", "rank"))
        self.label.setText(_translate("ProhibitionAddingWindow", "Medic rank"))
        self.add_prohibition_btn.setText(_translate("ProhibitionAddingWindow", "Add"))
        self.label_4.setText(_translate("ProhibitionAddingWindow", "Drug ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProhibitionAddingWindow = QtWidgets.QDialog()
    ui = Ui_ProhibitionAddingWindow()
    ui.setupUi(ProhibitionAddingWindow)
    ProhibitionAddingWindow.show()
    sys.exit(app.exec_())