# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GestionComptelqzNGP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ressource_rc

class Ui_AjouterCompte(object):
    def setupUi(self, AjouterCompte):
        if not AjouterCompte.objectName():
            AjouterCompte.setObjectName(u"AjouterCompte")
        AjouterCompte.resize(1280, 800)
        self.centralwidget = QWidget(AjouterCompte)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1281, 801))
        self.frame.setStyleSheet(u"background-color: rgb(255,228,54)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_haut = QFrame(self.frame)
        self.frame_haut.setObjectName(u"frame_haut")
        self.frame_haut.setGeometry(QRect(0, 0, 1271, 71))
        self.frame_haut.setStyleSheet(u"border:none")
        self.frame_haut.setFrameShape(QFrame.StyledPanel)
        self.frame_haut.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_haut)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1120, 0, 113, 81))
        icon = QIcon()
        icon.addFile(u"../fermerIcon-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(60, 80))
        self.pushButton_2 = QPushButton(self.frame_haut)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1010, 0, 113, 81))
        icon1 = QIcon()
        icon1.addFile(u"../pngtree-fullscreen--icon-in-trendy-style-isolated-background-png-image_1566064-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(60, 80))
        self.pushButton_3 = QPushButton(self.frame_haut)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(880, 0, 113, 81))
        self.pushButton_3.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"../red-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(60, 80))
        self.pushButton_20 = QPushButton(self.frame)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(-20, 750, 181, 51))
        self.pushButton_20.setStyleSheet(u"background-color:white;\n"
"color:black;\n"
"border-radius:8px;\n"
"font:90 18pt \"metropolis\";")
        self.widget_9 = QWidget(self.frame)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(0, 0, 221, 80))
        self.widget_9.setStyleSheet(u"background-color:white;\n"
"border:none;\n"
"border-radius:8px\n"
"")
        self.label_32 = QLabel(self.widget_9)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(90, 20, 141, 41))
        self.label_32.setStyleSheet(u"border:none;\n"
"font:90 18pt \"metropolis\";")
        self.pushButton_12 = QPushButton(self.widget_9)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(-10, 10, 111, 61))
        self.pushButton_12.setStyleSheet(u"QPushButton{\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/images/images/userIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon3)
        self.pushButton_12.setIconSize(QSize(60, 110))
        self.crud_user = QStackedWidget(self.frame)
        self.crud_user.setObjectName(u"crud_user")
        self.crud_user.setGeometry(QRect(150, 90, 991, 651))
        self.crud_user.setStyleSheet(u"background-color:rgba(0,0,0,0.2);\n"
"border-radius: 15px;")
        self.list_users = QWidget()
        self.list_users.setObjectName(u"list_users")
        self.pushButton_28 = QPushButton(self.list_users)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setGeometry(QRect(670, 30, 221, 71))
        self.pushButton_28.setStyleSheet(u"QPushButton{\n"
"background-color:#fff;\n"
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
"}\n"
"\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/images/images/pngtree-vector-remove-user-icon-png-image_4101425-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_28.setIcon(icon4)
        self.pushButton_28.setIconSize(QSize(60, 70))
        self.treeWidget_3 = QTreeWidget(self.list_users)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(6, font);
        __qtreewidgetitem.setFont(5, font);
        __qtreewidgetitem.setFont(4, font);
        __qtreewidgetitem.setFont(3, font);
        __qtreewidgetitem.setFont(2, font);
        __qtreewidgetitem.setFont(1, font);
        __qtreewidgetitem.setFont(0, font);
        self.treeWidget_3.setHeaderItem(__qtreewidgetitem)
        self.treeWidget_3.setObjectName(u"treeWidget_3")
        self.treeWidget_3.setGeometry(QRect(30, 130, 931, 501))
        self.treeWidget_3.setStyleSheet(u"background-color:#fff;")
        self.pushButton_29 = QPushButton(self.list_users)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setGeometry(QRect(370, 30, 221, 61))
        self.pushButton_29.setStyleSheet(u"QPushButton{\n"
"background-color:transparent;\n"
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
"\n"
"font-size:13px;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/images/images/editer-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_29.setIcon(icon5)
        self.pushButton_29.setIconSize(QSize(70, 70))
        self.pushButton_30 = QPushButton(self.list_users)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setGeometry(QRect(40, 30, 221, 61))
        self.pushButton_30.setStyleSheet(u"QPushButton{\n"
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
        icon6 = QIcon()
        icon6.addFile(u":/images/images/add_user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_30.setIcon(icon6)
        self.pushButton_30.setIconSize(QSize(50, 50))
        self.crud_user.addWidget(self.list_users)
        self.ajout_users = QWidget()
        self.ajout_users.setObjectName(u"ajout_users")
        self.comboBox_2 = QComboBox(self.ajout_users)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(340, 410, 361, 41))
        self.comboBox_2.setStyleSheet(u"border-radius:8px;\n"
"color:black;\n"
"background-color:rgba(255,255,255,0.8)\n"
"\n"
"")
        self.label_3 = QLabel(self.ajout_users)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(360, 120, 341, 41))
        self.label_3.setStyleSheet(u"background-color:none;\n"
"border:none;\n"
"font:90 30pt \"metropolis\";\n"
"font-size:30px;\n"
"color:white")
        self.lineEdit_6 = QLineEdit(self.ajout_users)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(340, 350, 361, 41))
        self.lineEdit_6.setStyleSheet(u"border-radius:8px;\n"
"color:black;\n"
"background-color:rgba(255,255,255,0.8)\n"
"\n"
"")
        self.pushButton_24 = QPushButton(self.ajout_users)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setGeometry(QRect(60, 30, 221, 61))
        self.pushButton_24.setStyleSheet(u"QPushButton{\n"
"background-color:#fff;\n"
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
        self.pushButton_24.setIcon(icon6)
        self.pushButton_24.setIconSize(QSize(50, 50))
        self.lineEdit_7 = QLineEdit(self.ajout_users)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(340, 290, 361, 41))
        self.lineEdit_7.setStyleSheet(u"border-radius:8px;\n"
"color:black;\n"
"background-color:rgba(255,255,255,0.8)\n"
"\n"
"")
        self.pushButton_25 = QPushButton(self.ajout_users)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setGeometry(QRect(690, 30, 221, 71))
        self.pushButton_25.setStyleSheet(u"QPushButton{\n"
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
"}\n"
"\n"
"\n"
"")
        self.pushButton_25.setIcon(icon4)
        self.pushButton_25.setIconSize(QSize(60, 70))
        self.lineEdit_8 = QLineEdit(self.ajout_users)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(340, 230, 361, 41))
        self.lineEdit_8.setStyleSheet(u"border-radius:8px;\n"
"color:black;\n"
"background-color:rgba(255,255,255,0.8)\n"
"\n"
"")
        self.lineEdit_9 = QLineEdit(self.ajout_users)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(340, 170, 171, 41))
        self.lineEdit_9.setStyleSheet(u"border-radius:8px;\n"
"color:black;\n"
"background-color:rgba(255,255,255,0.8)\n"
"\n"
"")
        self.lineEdit_10 = QLineEdit(self.ajout_users)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(530, 170, 171, 41))
        self.lineEdit_10.setStyleSheet(u"border-radius:8px;\n"
"color:black;\n"
"background-color:rgba(255,255,255,0.8)\n"
"\n"
"")
        self.lineEdit_73 = QLineEdit(self.ajout_users)
        self.lineEdit_73.setObjectName(u"lineEdit_73")
        self.lineEdit_73.setGeometry(QRect(340, 470, 361, 41))
        self.lineEdit_73.setStyleSheet(u"border-radius:8px;\n"
"color:black;\n"
"background-color:rgba(255,255,255,0.8)\n"
"\n"
"")
        self.pushButton_26 = QPushButton(self.ajout_users)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setGeometry(QRect(390, 30, 221, 61))
        self.pushButton_26.setStyleSheet(u"QPushButton{\n"
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
"\n"
"font-size:13px;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_26.setIcon(icon5)
        self.pushButton_26.setIconSize(QSize(70, 70))
        self.pushButton_27 = QPushButton(self.ajout_users)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setGeometry(QRect(440, 560, 181, 32))
        self.pushButton_27.setStyleSheet(u"QPushButton{\n"
"background-color:#FFE436;\n"
"border-top-left-radius:8px;\n"
"border-bottom-left-radius:8px;\n"
"color:rgb(255,255,255);\n"
"font:77 21pt \"metropolis\";\n"
"border-radius:8px\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:white;\n"
"border-radius:8px;\n"
"color:rgb(0,0,0);\n"
"font:77 18pt \"metropolis\";\n"
"\n"
"\n"
"}\n"
"")
        self.crud_user.addWidget(self.ajout_users)
        self.edite_users = QWidget()
        self.edite_users.setObjectName(u"edite_users")
        self.lineEdit_26 = QLineEdit(self.edite_users)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setGeometry(QRect(530, 170, 171, 41))
        self.lineEdit_26.setStyleSheet(u"border-radius:8px;\n"
"color:black;\n"
"background-color:rgba(255,255,255,0.8)\n"
"\n"
"")
        self.label_7 = QLabel(self.edite_users)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(360, 120, 341, 41))
        self.label_7.setStyleSheet(u"background-color:none;\n"
"border:none;\n"
"font:90 30pt \"metropolis\";\n"
"font-size:30px;\n"
"color:white")
        self.lineEdit_77 = QLineEdit(self.edite_users)
        self.lineEdit_77.setObjectName(u"lineEdit_77")
        self.lineEdit_77.setGeometry(QRect(340, 470, 361, 41))
        self.lineEdit_77.setStyleSheet(u"border-radius:8px;\n"
"color:black;\n"
"background-color:rgba(255,255,255,0.8)\n"
"\n"
"")
        self.pushButton_45 = QPushButton(self.edite_users)
        self.pushButton_45.setObjectName(u"pushButton_45")
        self.pushButton_45.setGeometry(QRect(430, 550, 181, 32))
        self.pushButton_45.setStyleSheet(u"QPushButton{\n"
"background-color:#FFE436;\n"
"border-top-left-radius:8px;\n"
"border-bottom-left-radius:8px;\n"
"color:rgb(255,255,255);\n"
"font:77 21pt \"metropolis\";\n"
"border-radius:8px\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:white;\n"
"border-radius:8px;\n"
"color:rgb(0,0,0);\n"
"font:77 18pt \"metropolis\";\n"
"\n"
"\n"
"}\n"
"")
        self.lineEdit_27 = QLineEdit(self.edite_users)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setGeometry(QRect(340, 170, 171, 41))
        self.lineEdit_27.setStyleSheet(u"border-radius:8px;\n"
"color:black;\n"
"background-color:rgba(255,255,255,0.8)\n"
"\n"
"")
        self.lineEdit_28 = QLineEdit(self.edite_users)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setGeometry(QRect(340, 290, 361, 41))
        self.lineEdit_28.setStyleSheet(u"border-radius:8px;\n"
"color:black;\n"
"background-color:rgba(255,255,255,0.8)\n"
"\n"
"")
        self.pushButton_46 = QPushButton(self.edite_users)
        self.pushButton_46.setObjectName(u"pushButton_46")
        self.pushButton_46.setGeometry(QRect(690, 30, 221, 71))
        self.pushButton_46.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
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
"}\n"
"\n"
"\n"
"")
        self.pushButton_46.setIcon(icon4)
        self.pushButton_46.setIconSize(QSize(60, 70))
        self.lineEdit_29 = QLineEdit(self.edite_users)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setGeometry(QRect(340, 230, 361, 41))
        self.lineEdit_29.setStyleSheet(u"border-radius:8px;\n"
"color:black;\n"
"background-color:rgba(255,255,255,0.8)\n"
"\n"
"")
        self.lineEdit_30 = QLineEdit(self.edite_users)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        self.lineEdit_30.setGeometry(QRect(340, 350, 361, 41))
        self.lineEdit_30.setStyleSheet(u"border-radius:8px;\n"
"color:black;\n"
"background-color:rgba(255,255,255,0.8)\n"
"\n"
"")
        self.pushButton_47 = QPushButton(self.edite_users)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setGeometry(QRect(390, 30, 221, 61))
        self.pushButton_47.setStyleSheet(u"QPushButton{\n"
"background-color:#fff;\n"
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
"\n"
"font-size:13px;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_47.setIcon(icon5)
        self.pushButton_47.setIconSize(QSize(70, 70))
        self.comboBox_6 = QComboBox(self.edite_users)
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setGeometry(QRect(340, 410, 361, 41))
        self.comboBox_6.setStyleSheet(u"border-radius:8px;\n"
"color:black;\n"
"background-color:rgba(255,255,255,0.8)\n"
"\n"
"")
        self.pushButton_48 = QPushButton(self.edite_users)
        self.pushButton_48.setObjectName(u"pushButton_48")
        self.pushButton_48.setGeometry(QRect(60, 30, 221, 61))
        self.pushButton_48.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_48.setIcon(icon6)
        self.pushButton_48.setIconSize(QSize(50, 50))
        self.crud_user.addWidget(self.edite_users)
        AjouterCompte.setCentralWidget(self.centralwidget)

        self.retranslateUi(AjouterCompte)

        self.crud_user.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AjouterCompte)
    # setupUi

    def retranslateUi(self, AjouterCompte):
        AjouterCompte.setWindowTitle(QCoreApplication.translate("AjouterCompte", u"MainWindow", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_20.setText(QCoreApplication.translate("AjouterCompte", u"Retour", None))
        self.label_32.setText(QCoreApplication.translate("AjouterCompte", u"Connecter", None))
        self.pushButton_12.setText("")
        self.pushButton_28.setText(QCoreApplication.translate("AjouterCompte", u"listes des utilisateurs", None))
        ___qtreewidgetitem = self.treeWidget_3.headerItem()
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("AjouterCompte", u"Profile", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("AjouterCompte", u"Telephone", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("AjouterCompte", u"Email", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("AjouterCompte", u"Username", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("AjouterCompte", u"Prenom", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("AjouterCompte", u"Nom", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("AjouterCompte", u"ID", None));
        self.pushButton_29.setText(QCoreApplication.translate("AjouterCompte", u"Editer un compte", None))
        self.pushButton_30.setText(QCoreApplication.translate("AjouterCompte", u"Ajouter un compte", None))
        self.comboBox_2.setPlaceholderText(QCoreApplication.translate("AjouterCompte", u"Profile", None))
        self.label_3.setText(QCoreApplication.translate("AjouterCompte", u"AJOUTER UN COMPTE", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("AjouterCompte", u"t\u00e9l\u00e9phone", None))
        self.pushButton_24.setText(QCoreApplication.translate("AjouterCompte", u"Ajouter un compte", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("AjouterCompte", u"email", None))
        self.pushButton_25.setText(QCoreApplication.translate("AjouterCompte", u"listes des utilisateurs", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("AjouterCompte", u"Prenom", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("AjouterCompte", u"id", None))
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("AjouterCompte", u"Nom", None))
        self.lineEdit_73.setPlaceholderText(QCoreApplication.translate("AjouterCompte", u"Password", None))
        self.pushButton_26.setText(QCoreApplication.translate("AjouterCompte", u"Editer un compte", None))
        self.pushButton_27.setText(QCoreApplication.translate("AjouterCompte", u"Enregistrer", None))
        self.lineEdit_26.setPlaceholderText(QCoreApplication.translate("AjouterCompte", u"Nom", None))
        self.label_7.setText(QCoreApplication.translate("AjouterCompte", u"EDITER UN COMPTE", None))
        self.lineEdit_77.setPlaceholderText(QCoreApplication.translate("AjouterCompte", u"Password", None))
        self.pushButton_45.setText(QCoreApplication.translate("AjouterCompte", u"Enregistrer", None))
        self.lineEdit_27.setPlaceholderText(QCoreApplication.translate("AjouterCompte", u"id", None))
        self.lineEdit_28.setPlaceholderText(QCoreApplication.translate("AjouterCompte", u"email", None))
        self.pushButton_46.setText(QCoreApplication.translate("AjouterCompte", u"listes des utilisateurs", None))
        self.lineEdit_29.setPlaceholderText(QCoreApplication.translate("AjouterCompte", u"Prenom", None))
        self.lineEdit_30.setPlaceholderText(QCoreApplication.translate("AjouterCompte", u"t\u00e9l\u00e9phone", None))
        self.pushButton_47.setText(QCoreApplication.translate("AjouterCompte", u"Editer un compte", None))
        self.comboBox_6.setPlaceholderText(QCoreApplication.translate("AjouterCompte", u"Profile", None))
        self.pushButton_48.setText(QCoreApplication.translate("AjouterCompte", u"Ajouter un compte", None))
    # retranslateUi

