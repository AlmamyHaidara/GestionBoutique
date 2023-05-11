# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Command_admin_user.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from Models.Class.Command_management import Command_manager
from DialogueBox import DialogueBox


class Ui_Form(Command_manager):
    def __init__(self):
        self.tab = []
        # super(Ui_Form, self).__init__()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1314, 799)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1351, 801))
        self.widget.setStyleSheet("background-color: rgb(255,228,54)")
        self.widget.setObjectName("widget")
        self.command_stacke = QtWidgets.QStackedWidget(self.widget)
        self.command_stacke.setGeometry(QtCore.QRect(50, 140, 1221, 561))
        self.command_stacke.setStyleSheet("background-color:rgba(0,0,0,0.2);\n"
                                          "border-radius:20px;")
        self.command_stacke.setObjectName("command_stacke")
        self.ajout_command = QtWidgets.QWidget()
        self.ajout_command.setObjectName("ajout_command")
        self.add_command = QtWidgets.QPushButton(self.ajout_command)
        self.add_command.setGeometry(QtCore.QRect(110, 30, 221, 61))
        self.add_command.setStyleSheet("QPushButton{\n"
                                       "background-color:#fff;\n"
                                       "border-radius:5px;\n"
                                       "color:rgb(0,0,0);\n"
                                       "\n"
                                       "font:77 10pt \"metropolis\";\n"
                                       "font-size:14px;\n"
                                       "font-weight:  bold;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "background-color:rgba(0,0,0,0.3);\n"
                                       "border-tradius:5px;\n"
                                       "color:rgb(255,255,255);\n"
                                       "font:77 10pt \"metropolis\";\n"
                                       "font-size:14px;\n"
                                       "font-weight: bold;\n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/ajouter_ventes-removebg-preview.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.add_command.setIcon(icon)
        self.add_command.setIconSize(QtCore.QSize(50, 50))
        self.add_command.setObjectName("add_command")
        self.list_command_add = QtWidgets.QPushButton(self.ajout_command)
        self.list_command_add.setGeometry(QtCore.QRect(830, 30, 221, 71))
        self.list_command_add.setStyleSheet("QPushButton{\n"
                                            "background-color:rgba(0,0,0,0.3);\n"
                                            "border-radius:5px;\n"
                                            "color:rgb(0,0,0);\n"
                                            "font:77 10pt \"metropolis\";\n"
                                            "font-size:14px;\n"
                                            "font-weight:  bold;\n"
                                            "\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "background-color:white;\n"
                                            "border-radius:5px;\n"
                                            "color:rgb(0,0,0);\n"
                                            "font:77 10pt \"metropolis\";\n"
                                            "font-size:14px;\n"
                                            "font-weight:  bold;\n"
                                            "}\n"
                                            "\n"
                                            "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/images/commandes-removebg-preview .png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.list_command_add.setIcon(icon1)
        self.list_command_add.setIconSize(QtCore.QSize(60, 70))
        self.list_command_add.setObjectName("list_command_add")
        self.label = QtWidgets.QLabel(self.ajout_command)
        self.label.setGeometry(QtCore.QRect(40, 170, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#fff;\n"
                                 "background: transparent;")
        self.label.setObjectName("label")
        self.categorie_combo = QtWidgets.QComboBox(self.ajout_command)
        self.categorie_combo.setGeometry(QtCore.QRect(100, 290, 251, 41))
        self.categorie_combo.setStyleSheet("border-radius:5px;\n"
                                           "color:black;\n"
                                           "background-color:rgba(255,255,255,0.8)\n"
                                           "\n"
                                           "")
        self.categorie_combo.setObjectName("categorie_combo")
        self.categorie_combo.addItem("")
        self.prix_field = QtWidgets.QLineEdit(self.ajout_command)
        self.prix_field.setGeometry(QtCore.QRect(100, 340, 251, 41))
        self.prix_field.setStyleSheet("border-radius:5px;\n"
                                      "color:black;\n"
                                      "background-color:rgba(255,255,255,0.8)\n"
                                      "\n"
                                      "")
        self.prix_field.setObjectName("prix_field")
        self.product_field = QtWidgets.QLineEdit(self.ajout_command)
        self.product_field.setGeometry(QtCore.QRect(100, 230, 251, 41))
        self.product_field.setStyleSheet("border-radius:5px;\n"
                                         "color:black;\n"
                                         "background-color:rgba(255,255,255,0.8)\n"
                                         "\n"
                                         "")
        self.product_field.setObjectName("product_field")
        self.quantiter_field = QtWidgets.QLineEdit(self.ajout_command)
        self.quantiter_field.setGeometry(QtCore.QRect(100, 400, 251, 41))
        self.quantiter_field.setStyleSheet("border-radius:5px;\n"
                                           "color:black;\n"
                                           "background-color:rgba(255,255,255,0.8)\n"
                                           "\n"
                                           "")
        self.quantiter_field.setObjectName("quantiter_field")
        self.add_panier = QtWidgets.QPushButton(self.ajout_command)
        self.add_panier.setGeometry(QtCore.QRect(120, 480, 211, 32))
        font = QtGui.QFont()
        font.setFamily("metropolis")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.add_panier.setFont(font)
        self.add_panier.setStyleSheet("QPushButton{\n"
                                      "background-color:#FFE436;\n"
                                      "border-top-left-radius:20px;\n"
                                      "border-bottom-left-radius:20px;\n"
                                      "color:rgb(255,255,255);\n"
                                      "font:77 15pt \"metropolis\";\n"
                                      "border-radius:5px;\n"
                                      "font-weight:bold;\n"
                                      "\n"
                                      "\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color:white;\n"
                                      "border-radius:5px;\n"
                                      "color:rgb(0,0,0);\n"
                                      "font:77 15pt \"metropolis\";\n"
                                      "\n"
                                      "font-weight:bold;\n"
                                      "}\n"
                                      "")
        self.add_panier.setObjectName("add_panier")
        self.command_table = QtWidgets.QTableWidget(self.ajout_command)
        self.command_table.setGeometry(QtCore.QRect(390, 230, 801, 231))
        self.command_table.setObjectName("command_table")
        self.command_table.setColumnCount(8)
        self.command_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.command_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.command_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.command_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.command_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.command_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.command_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.command_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.command_table.setHorizontalHeaderItem(7, item)
        self.label_2 = QtWidgets.QLabel(self.ajout_command)
        self.label_2.setGeometry(QtCore.QRect(660, 160, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#fff;\n"
                                   "background: transparent;")
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setObjectName("label_2")
        self.valider = QtWidgets.QPushButton(self.ajout_command)
        self.valider.setGeometry(QtCore.QRect(970, 480, 211, 32))
        font = QtGui.QFont()
        font.setFamily("metropolis")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.valider.setFont(font)
        self.valider.setStyleSheet("QPushButton{\n"
                                   "background-color:#FFE436;\n"
                                   "border-top-left-radius:20px;\n"
                                   "border-bottom-left-radius:20px;\n"
                                   "color:rgb(255,255,255);\n"
                                   "font:77 15pt \"metropolis\";\n"
                                   "border-radius:5px;\n"
                                   "font-weight:bold;\n"
                                   "\n"
                                   "\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background-color:white;\n"
                                   "border-radius:5px;\n"
                                   "color:rgb(0,0,0);\n"
                                   "font:77 15pt \"metropolis\";\n"
                                   "\n"
                                   "font-weight:bold;\n"
                                   "}\n"
                                   "")
        self.valider.setObjectName("valider")
        self.command_stacke.addWidget(self.ajout_command)
        self.list_command = QtWidgets.QWidget()
        self.list_command.setObjectName("list_command")
        self.list_command_list = QtWidgets.QPushButton(self.list_command)
        self.list_command_list.setGeometry(QtCore.QRect(740, 30, 221, 71))
        self.list_command_list.setStyleSheet("QPushButton{\n"
                                             "background-color:#fff;\n"
                                             "border-radius:5px;\n"
                                             "color:rgb(0,0,0);\n"
                                             "font:77 10pt \"metropolis\";\n"
                                             "font-size:14px;\n"
                                             "font-weight:  bold;\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "background-color:rgba(0,0,0,0.3);\n"
                                             "border-tradius:5px;\n"
                                             "color:#fff;\n"
                                             "font:77 10pt \"metropolis\";\n"
                                             "font-size:14px;\n"
                                             "font-weight: bold;\n"
                                             "\n"
                                             "}")
        self.list_command_list.setIcon(icon1)
        self.list_command_list.setIconSize(QtCore.QSize(60, 70))
        self.list_command_list.setObjectName("list_command_list")
        self.add_command_list = QtWidgets.QPushButton(self.list_command)
        self.add_command_list.setGeometry(QtCore.QRect(170, 30, 221, 61))
        self.add_command_list.setStyleSheet("QPushButton{\n"
                                            "background-color:rgba(0,0,0,0.3);\n"
                                            "border-radius:5px;\n"
                                            "color:#fff;\n"
                                            "font:77 10pt \"metropolis\";\n"
                                            "font-size:14px;\n"
                                            "font-weight:  bold;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "background-color:white;\n"
                                            "border-radius:5px;\n"
                                            "color:rgb(0,0,0);\n"
                                            "font:77 10pt \"metropolis\";\n"
                                            "font-size:14px;\n"
                                            "font-weight:  bold;\n"
                                            "}\n"
                                            "\n"
                                            "")
        self.add_command_list.setIcon(icon)
        self.add_command_list.setIconSize(QtCore.QSize(50, 50))
        self.add_command_list.setObjectName("add_command_list")
        self.tableauListcommand = QtWidgets.QTableWidget(self.list_command)
        self.tableauListcommand.setGeometry(QtCore.QRect(190, 200, 801, 331))
        self.tableauListcommand.setObjectName("tableauListcommand")
        self.tableauListcommand.setColumnCount(8)
        self.tableauListcommand.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableauListcommand.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableauListcommand.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableauListcommand.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableauListcommand.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableauListcommand.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableauListcommand.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableauListcommand.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableauListcommand.setHorizontalHeaderItem(7, item)
        self.actualiser = QtWidgets.QPushButton(self.list_command)
        self.actualiser.setGeometry(QtCore.QRect(190, 150, 211, 32))
        font = QtGui.QFont()
        font.setFamily("metropolis")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.actualiser.setFont(font)
        self.actualiser.setStyleSheet("QPushButton{\n"
                                      "background-color:#FFE436;\n"
                                      "border-top-left-radius:20px;\n"
                                      "border-bottom-left-radius:20px;\n"
                                      "color:rgb(255,255,255);\n"
                                      "font:77 15pt \"metropolis\";\n"
                                      "border-radius:5px;\n"
                                      "font-weight:bold;\n"
                                      "\n"
                                      "\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color:white;\n"
                                      "border-radius:5px;\n"
                                      "color:rgb(0,0,0);\n"
                                      "font:77 15pt \"metropolis\";\n"
                                      "\n"
                                      "font-weight:bold;\n"
                                      "}\n"
                                      "")
        self.actualiser.setObjectName("actualiser")
        self.search = QtWidgets.QLineEdit(self.list_command)
        self.search.setGeometry(QtCore.QRect(720, 140, 251, 41))
        self.search.setStyleSheet("border-radius:5px;\n"
                                  "color:black;\n"
                                  "background-color:rgba(255,255,255,0.8)\n"
                                  "\n"
                                  "")
        self.search.setObjectName("search")
        self.command_stacke.addWidget(self.list_command)
        self.widget_9 = QtWidgets.QWidget(self.widget)
        self.widget_9.setGeometry(QtCore.QRect(-10, 0, 221, 71))
        self.widget_9.setStyleSheet("background-color:white;\n"
                                    "border:none;\n"
                                    "border-radius:5px\n"
                                    "")
        self.widget_9.setObjectName("widget_9")
        self.label_32 = QtWidgets.QLabel(self.widget_9)
        self.label_32.setGeometry(QtCore.QRect(110, 10, 101, 41))
        self.label_32.setStyleSheet("border:none;\n"
                                    "font:90 18pt \"metropolis\";")
        self.label_32.setObjectName("label_32")
        self.pushButton_12 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_12.setGeometry(QtCore.QRect(10, 0, 111, 61))
        self.pushButton_12.setStyleSheet("QPushButton{\n"
                                         "background-color:none;\n"
                                         "border-top-left-radius:20px;\n"
                                         "border-bottom-left-radius:20px;\n"
                                         "color:rgb(0,0,0);\n"
                                         "font:77 10pt \"metropolis\";\n"
                                         "font-size:14px;\n"
                                         "\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "background-color:white;\n"
                                         "border-top-left-radius:20px;\n"
                                         "border-bottom-left-radius:20px;\n"
                                         "color:rgb(0,0,0);\n"
                                         "font:77 10pt \"metropolis\";\n"
                                         "font-size:13px;\n"
                                         "\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "")
        self.pushButton_12.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/images/compte-removebg-preview.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon2)
        self.pushButton_12.setIconSize(QtCore.QSize(120, 110))
        self.pushButton_12.setObjectName("pushButton_12")

        self.retranslateUi(Form)
        self.command_stacke.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.add_command.setText(_translate("Form", "Ajouer Command"))
        self.list_command_add.setText(_translate("Form", "Liste Command"))
        self.label.setText(_translate("Form", "Ajout Produit commander"))
        self.categorie_combo.setItemText(0, _translate("Form", " Sucrerie"))
        self.prix_field.setPlaceholderText(_translate("Form", "  Prix"))
        self.product_field.setPlaceholderText(_translate("Form", "  Produit"))
        self.quantiter_field.setPlaceholderText(_translate("Form", "  Quantité"))
        self.add_panier.setText(_translate("Form", "Ajouter au panier"))
        item = self.command_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "id"))
        item = self.command_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Produit"))
        item = self.command_table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "categorie"))
        item = self.command_table.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Prix"))
        item = self.command_table.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Quantiter"))
        item = self.command_table.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Montant"))
        item = self.command_table.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Modifier"))
        item = self.command_table.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Suprimer"))
        self.label_2.setText(_translate("Form", "Liste Produit commander"))
        self.valider.setText(_translate("Form", "Valider"))
        self.list_command_list.setText(_translate("Form", "Liste Command"))
        self.add_command_list.setText(_translate("Form", "Ajouer Command"))
        item = self.tableauListcommand.horizontalHeaderItem(0)
        item.setText(_translate("Form", "id"))
        item = self.tableauListcommand.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Produit"))
        item = self.tableauListcommand.horizontalHeaderItem(2)
        item.setText(_translate("Form", "categorie"))
        item = self.tableauListcommand.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Prix"))
        item = self.tableauListcommand.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Quantiter"))
        item = self.tableauListcommand.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Montant"))
        item = self.tableauListcommand.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Modifier"))
        item = self.tableauListcommand.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Suprimer"))
        self.actualiser.setText(_translate("Form", "Actualiser"))
        self.search.setPlaceholderText(_translate("Form", "  Search"))
        self.label_32.setText(_translate("Form", "Connecté"))
        self.add_command_list.clicked.connect(lambda: self.showAdd())
        self.list_command_add.clicked.connect(lambda: self.showList())
        self.add_panier.clicked.connect(lambda: self.add_command_panier([{
            'id': 0,
            'produit': self.product_field.text(),
            'category': self.categorie_combo.currentText(),
            'prix': self.prix_field.text(),
            'quantiter': self.quantiter_field.text(),
            'montant': '0.0'
        }]))
        self.valider.clicked.connect(self.Validate_command)

    def showAdd(self):
        self.command_stacke.setCurrentWidget(self.ajout_command)

    def showList(self):
        self.command_stacke.setCurrentWidget(self.list_command)
        # self.command_table.setCurrentWidget(self.list_command)
        self.dataList = Command_manager.All_command_list(self)
        print("==>",self.dataList)
        self.command_table.setRowCount(len(self.dataList))
        self.command_table.setColumnCount(len(self.dataList) + 7)
        if self.dataList != None:
            for row in range(len(self.dataList)):
                print(len(self.dataList))
        #         for column in range(len(self.dataList[row])):
        #             # print("Data")
        #             item = QtWidgets.QTableWidgetItem(str(self.dataList[row][column]))
        #             self.command_table.setItem(row, column, item)
                    # self.update_btn = QtWidgets.QPushButton("Edite")
                    # self.delete_btn = QtWidgets.QPushButton("Delete")
                    # self.update_btn.setStyleSheet("QPushButton{\n"
                    #                               "background-color: #10e8ff;\n"
                    #                               "color:rgb(255,255,255);\n"
                    #                               "border-radius:50\n"
                    #                               "\n"
                    #                               "\n"
                    #                               "}\n")
                    # self.delete_btn.setStyleSheet("QPushButton{\n"
                    #                               "background-color:#d4820e;\n"
                    #                               "color:rgb(255,255,255);\n"
                    #                               "border-radius:50\n"
                    #                               "\n"
                    #                               "\n"
                    #                               "}\n")
                    #
                    # self.command_table.setCellWidget(row, 7, self.update_btn)
                    # self.command_table.setCellWidget(row, 8, self.delete_btn)
                    # self.delete_btn.clicked.connect(partial(self.delete_user_method, self.delete_btn))
                    # self.update_btn.clicked.connect(partial(self.update_user_method, self.update_btn))

    def add_command_panier(self, data: list):
        data[0]['id'] = self.command_table.rowCount() + 1
        if data[0]['prix'].isdigit() and data[0]['quantiter'].isdigit():
            data[0]['montant'] = str(int(data[0]['prix']) * int(data[0]['quantiter'])) + ' FCFA'
        else:
            print("Les valeurs de prix ou de quantité ne sont pas valides.")
            return False
        # print(data[0])
        self.command_table.setColumnCount(self.command_table.columnCount())

        self.tab.append(data)
        self.command_table.setRowCount(len(self.tab))
        if data is not None:

            for row, item_dict in enumerate(self.tab):
                # print(row,'||',item_dict)

                for col, (key, value) in enumerate(item_dict[0].items()):
                    item = QtWidgets.QTableWidgetItem(str(value))
                    self.command_table.setItem(row, col, item)
                    self.update_btn = QtWidgets.QPushButton("Edite")
                    self.delete_btn = QtWidgets.QPushButton("Delete")
                    #
                    self.update_btn.setStyleSheet("QPushButton{\n"
                                                  "background-color: #10e8ff;\n"
                                                  "color:rgb(255,255,255);\n"
                                                  "border-radius:50\n"
                                                  "\n"
                                                  "\n"
                                                  "}\n")
                    self.delete_btn.setStyleSheet("QPushButton{\n"
                                                  "background-color:#d4820e;\n"
                                                  "color:rgb(255,255,255);\n"
                                                  "border-radius:50\n"
                                                  "\n"
                                                  "\n"
                                                  "}\n")

                    self.command_table.setCellWidget(row, 6, self.update_btn)
                    self.command_table.setCellWidget(row, 7, self.delete_btn)
                    self.delete_btn.clicked.connect(partial(self.delete_user_method, self.delete_btn))
                    self.update_btn.clicked.connect(partial(self.update_user_method, self.update_btn))
        pass

    def delete_user_method(self, btn):
        print('delete')
        if btn:
            button = btn.sender()
            # Trouver la ligne correspondante dans le QTableWidget
            index = self.command_table.indexAt(button.pos())
            if index.isValid():
                row = index.row()
                col = index.column()
                item = self.command_table.item(row, 1)

                if item is not None:
                    produit = item.text()
                    print('=>', produit)
                    self.command_table.removeRow(row)

        pass

    def update_user_method(self, btn):
        print('update')
        if btn:
            updateBtn = btn.sender()
            update_data = []
            index = self.command_table.indexAt(updateBtn.pos())
            if index.isValid():
                row = index.row()
                col = index.column()
                for i in range(6):
                    item = self.command_table.item(row, i)
                    print('=>', item.text())
                    update_data.append(item.text())
                print(update_data)
                '''
                'produit': self.product_field.text(),
            'category': self.categorie_combo.currentText(),
            'prix': self.prix_field.text(),
            'quantiter': self.quantiter_field.text(),
            'montant': '0.0'
                '''
                self.product_field.setText(update_data[1])
                self.categorie_combo.setItemText(0, update_data[2])
                self.prix_field.setText(update_data[3])
                self.quantiter_field.setText(update_data[4])
                # self.editeBox(update_data)

        pass

    def Validate_command(self):
        print('Hello')
        donnees = []
        if (self.command_table.rowCount() != 0):
            # Parcourir chaque ligne dans le tableau
            for row in range(self.command_table.rowCount()):
                # Créer une liste pour stocker les données de cette ligne
                ligne = []
                # Parcourir chaque colonne dans la ligne actuelle
                for col in range(self.command_table.columnCount()):
                    # Ajouter la donnée de cette cellule à la liste de la ligne
                    cellule = self.command_table.item(row, col)
                    if cellule is not None:
                        ligne.append(cellule.text())
                    else:
                        ligne.append("")
                # Ajouter la ligne complète à la liste des données
                donnees.append(ligne)
            DialogueBox.clientBox(self, donnees)
            # print(donnees)
            # self.create_command(donnees)
        else:
            return False
        pass


import ressource_rc


class ui_command(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.command_stacke.setCurrentWidget(self.ui.ajout_command)
        self.center()

    def center(self):
        # récupère la taille de l'écran
        screen_size = QtWidgets.QDesktopWidget().screenGeometry(-1)
        # récupère la taille de la fenêtre
        window_size = self.geometry()
        # calcule les coordonnées pour centrer la fenêtre
        x = (screen_size.width() - window_size.width()) / 2
        y = (screen_size.height() - window_size.height()) / 2
        # définit les nouvelles coordonnées pour la fenêtre
        self.move(int(x), int(y))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AjouterCompte = QtWidgets.QMainWindow()
    ui = ui_command()
    ui.show()
    sys.exit(app.exec_())
