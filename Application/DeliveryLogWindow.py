# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kaireen/Documents/CPr/Application/ui/DeliveryLogWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DeliveryLogWindow(object):
    def setupUi(self, DeliveryLogWindow):
        DeliveryLogWindow.setObjectName("DeliveryLogWindow")
        DeliveryLogWindow.resize(1280, 610)
        DeliveryLogWindow.setMinimumSize(QtCore.QSize(1280, 610))
        DeliveryLogWindow.setMaximumSize(QtCore.QSize(1280, 610))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/kaireen/Documents/CPr/Application/ui/../media/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DeliveryLogWindow.setWindowIcon(icon)
        DeliveryLogWindow.setStyleSheet("background-color: rgb(32, 178, 170);")
        self.tableWidget = QtWidgets.QTableWidget(DeliveryLogWindow)
        self.tableWidget.setGeometry(QtCore.QRect(0, 90, 1280, 520))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setGridStyle(QtCore.Qt.CustomDashLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0, 0))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(225)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.refresh_btn = QtWidgets.QPushButton(DeliveryLogWindow)
        self.refresh_btn.setGeometry(QtCore.QRect(898, 10, 93, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.refresh_btn.setFont(font)
        self.refresh_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(105, 205, 255);\n"
"}")
        self.refresh_btn.setObjectName("refresh_btn")
        self.search_btn = QtWidgets.QPushButton(DeliveryLogWindow)
        self.search_btn.setEnabled(True)
        self.search_btn.setGeometry(QtCore.QRect(790, 10, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.search_btn.setFont(font)
        self.search_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 172, 172);\n"
"    color: rgb(0, 0, 0);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(105, 205, 255);\n"
"}")
        self.search_btn.setObjectName("search_btn")
        self.search_drug_fld = QtWidgets.QLineEdit(DeliveryLogWindow)
        self.search_drug_fld.setGeometry(QtCore.QRect(130, 10, 651, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_drug_fld.setFont(font)
        self.search_drug_fld.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 15px;")
        self.search_drug_fld.setMaxLength(200)
        self.search_drug_fld.setObjectName("search_drug_fld")
        self.supplier_name_fld = QtWidgets.QLineEdit(DeliveryLogWindow)
        self.supplier_name_fld.setGeometry(QtCore.QRect(580, 50, 201, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.supplier_name_fld.setFont(font)
        self.supplier_name_fld.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 15px;")
        self.supplier_name_fld.setMaxLength(50)
        self.supplier_name_fld.setObjectName("supplier_name_fld")
        self.manufacturer_country_fld = QtWidgets.QLineEdit(DeliveryLogWindow)
        self.manufacturer_country_fld.setGeometry(QtCore.QRect(340, 50, 201, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.manufacturer_country_fld.setFont(font)
        self.manufacturer_country_fld.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 15px;")
        self.manufacturer_country_fld.setMaxLength(50)
        self.manufacturer_country_fld.setObjectName("manufacturer_country_fld")
        self.supplier_country_fld = QtWidgets.QLineEdit(DeliveryLogWindow)
        self.supplier_country_fld.setGeometry(QtCore.QRect(790, 50, 201, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.supplier_country_fld.setFont(font)
        self.supplier_country_fld.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 15px;")
        self.supplier_country_fld.setMaxLength(50)
        self.supplier_country_fld.setObjectName("supplier_country_fld")
        self.manufacturer_name_fld = QtWidgets.QLineEdit(DeliveryLogWindow)
        self.manufacturer_name_fld.setGeometry(QtCore.QRect(130, 50, 201, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.manufacturer_name_fld.setFont(font)
        self.manufacturer_name_fld.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 15px;")
        self.manufacturer_name_fld.setMaxLength(50)
        self.manufacturer_name_fld.setObjectName("manufacturer_name_fld")

        self.retranslateUi(DeliveryLogWindow)
        QtCore.QMetaObject.connectSlotsByName(DeliveryLogWindow)

    def retranslateUi(self, DeliveryLogWindow):
        _translate = QtCore.QCoreApplication.translate
        DeliveryLogWindow.setWindowTitle(_translate("DeliveryLogWindow", "Delivery log"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("DeliveryLogWindow", "Drug ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("DeliveryLogWindow", "Drug Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("DeliveryLogWindow", "Manuf. ID"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("DeliveryLogWindow", "Manuf. Name"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("DeliveryLogWindow", "Manuf. Country"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("DeliveryLogWindow", "Suppl. ID"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("DeliveryLogWindow", "Suppl. Name"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("DeliveryLogWindow", "Suppl. Country"))
        self.refresh_btn.setText(_translate("DeliveryLogWindow", "Refresh"))
        self.search_btn.setText(_translate("DeliveryLogWindow", "Search"))
        self.search_drug_fld.setPlaceholderText(_translate("DeliveryLogWindow", "Drug name"))
        self.supplier_name_fld.setPlaceholderText(_translate("DeliveryLogWindow", "Supplier name"))
        self.manufacturer_country_fld.setPlaceholderText(_translate("DeliveryLogWindow", "Manufacturer country"))
        self.supplier_country_fld.setPlaceholderText(_translate("DeliveryLogWindow", "Supplier country"))
        self.manufacturer_name_fld.setPlaceholderText(_translate("DeliveryLogWindow", "Manufacturer name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeliveryLogWindow = QtWidgets.QDialog()
    ui = Ui_DeliveryLogWindow()
    ui.setupUi(DeliveryLogWindow)
    DeliveryLogWindow.show()
    sys.exit(app.exec_())
