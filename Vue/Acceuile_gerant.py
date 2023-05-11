# -*- coding: utf-8 -*-
import os
# Form implementation generated from reading ui file 'PageAccueilGestBoutiqueUser.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5.QtWidgets import QDesktopWidget

sys.path.append('../Models/')

from PyQt5 import QtCore, QtGui, QtWidgets
from Models import page_loader


class Ui_PageAccueil_Gerant():


    def setupUi(self, PageAccueil):
        PageAccueil.setObjectName("PageAccueil")
        PageAccueil.resize(1248, 755)
        self.centralwidget = QtWidgets.QWidget(PageAccueil)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 1281, 801))
        self.frame.setStyleSheet("background-color: rgb(255,228,54)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_haut = QtWidgets.QFrame(self.frame)
        self.frame_haut.setGeometry(QtCore.QRect(0, 9, 1271, 71))
        self.frame_haut.setStyleSheet("border:none")
        self.frame_haut.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_haut.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_haut.setObjectName("frame_haut")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_haut)
        self.pushButton_3.setGeometry(QtCore.QRect(880, 0, 111, 51))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/feather/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(60, 80))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_haut)
        self.pushButton_2.setGeometry(QtCore.QRect(1010, 0, 111, 51))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/feather/square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 80))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_haut)
        self.pushButton.setGeometry(QtCore.QRect(1120, 0, 111, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/feather/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(40, 80))
        self.pushButton.setObjectName("pushButton")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(-1, 0, 271, 781))
        self.frame_2.setStyleSheet("background-color: rgb(220,240,200)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.user_btn = QtWidgets.QPushButton(self.frame_2)
        self.user_btn.setGeometry(QtCore.QRect(10, 260, 271, 51))
        self.user_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.user_btn.setStyleSheet("QPushButton{\n"
"background-color:rgb(61,61,61);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font:77 10pt \"metropolis\";\n"
"font-size:14px;\n"
"font-weight:bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(0,0,0);\n"
"font:77 10pt \"metropolis\";\n"
"font-size:15px;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/images/usersystem.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.user_btn.setIcon(icon3)
        self.user_btn.setIconSize(QtCore.QSize(35, 50))
        self.user_btn.setObjectName("user_btn")
        self.produit_btn = QtWidgets.QPushButton(self.frame_2)
        self.produit_btn.setGeometry(QtCore.QRect(10, 360, 291, 51))
        self.produit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.produit_btn.setStyleSheet("QPushButton{\n"
"background-color:rgb(61,61,61);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font:77 10pt \"metropolis\";\n"
"font-size:14px;\n"
"font-weight:bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(0,0,0);\n"
"font:77 10pt \"metropolis\";\n"
"font-size:15px;\n"
"font-weight:bold;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/images/product.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.produit_btn.setIcon(icon4)
        self.produit_btn.setIconSize(QtCore.QSize(35, 40))
        self.produit_btn.setObjectName("produit_btn")
        self.vente_btn = QtWidgets.QPushButton(self.frame_2)
        self.vente_btn.setGeometry(QtCore.QRect(10, 460, 261, 51))
        self.vente_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.vente_btn.setStyleSheet("QPushButton{\n"
"background-color:rgb(61,61,61);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font:77 10pt \"metropolis\";\n"
"font-size:14px;\n"
"font-weight:bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(0,0,0);\n"
"font:77 10pt \"metropolis\";\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/images/shopify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vente_btn.setIcon(icon5)
        self.vente_btn.setIconSize(QtCore.QSize(35, 50))
        self.vente_btn.setObjectName("vente_btn")
        self.acceuille_btn = QtWidgets.QPushButton(self.frame_2)
        self.acceuille_btn.setGeometry(QtCore.QRect(10, 160, 261, 51))
        self.acceuille_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.acceuille_btn.setStyleSheet("QPushButton{\n"
"background-color:rgb(61,61,61);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font:77 10pt \"metropolis\";\n"
"font-size:14px;\n"
"font-weight:bold;\n"
"cursor: pointer;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(0,0,0);\n"
"font:77 10pt \"metropolis\";\n"
"font-size:15px;\n"
"font-weight:bold;\n"
"cursor: pointer;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/images/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.acceuille_btn.setIcon(icon6)
        self.acceuille_btn.setIconSize(QtCore.QSize(35, 35))
        self.acceuille_btn.setShortcut("")
        self.acceuille_btn.setObjectName("acceuille_btn")
        self.commande_btn = QtWidgets.QPushButton(self.frame_2)
        self.commande_btn.setGeometry(QtCore.QRect(10, 560, 271, 51))
        self.commande_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commande_btn.setStyleSheet("QPushButton{\n"
"background-color:rgb(61,61,61);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font:77 10pt \"metropolis\";\n"
"font-size:14px;\n"
"font-weight:bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(0,0,0);\n"
"font:77 10pt \"metropolis\";\n"
"font-size:15px;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/images/commandes-removebg-preview .png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commande_btn.setIcon(icon7)
        self.commande_btn.setIconSize(QtCore.QSize(34, 50))
        self.commande_btn.setObjectName("commande_btn")
        self.facture_btn = QtWidgets.QPushButton(self.frame_2)
        self.facture_btn.setGeometry(QtCore.QRect(10, 660, 271, 51))
        self.facture_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.facture_btn.setStyleSheet("QPushButton{\n"
"background-color:rgb(61,61,61);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(255,255,255);\n"
"font:77 10pt \"metropolis\";\n"
"font-size:14px;\n"
"font-weight:bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:white;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"color:rgb(0,0,0);\n"
"font:77 10pt \"metropolis\";\n"
"font-size:15px;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/images/facture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.facture_btn.setIcon(icon8)
        self.facture_btn.setIconSize(QtCore.QSize(35, 50))
        self.facture_btn.setObjectName("facture_btn")
        self.widget_9 = QtWidgets.QWidget(self.frame_2)
        self.widget_9.setGeometry(QtCore.QRect(0, 0, 271, 101))
        self.widget_9.setStyleSheet("background-color:rgba(255,255,255,0.9);")
        self.widget_9.setObjectName("widget_9")
        self.label_32 = QtWidgets.QLabel(self.widget_9)
        self.label_32.setGeometry(QtCore.QRect(120, 30, 131, 41))
        self.label_32.setStyleSheet("border:none;\n"
"font:90 18pt \"metropolis\";\n"
"background-color:none;")
        self.label_32.setObjectName("label_32")
        self.connection = QtWidgets.QPushButton(self.widget_9)
        self.connection.setGeometry(QtCore.QRect(-20, 10, 151, 81))
        self.connection.setStyleSheet("background-color:none;\n"
"border:none;")
        self.connection.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/images/userIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.connection.setIcon(icon9)
        self.connection.setIconSize(QtCore.QSize(70, 110))
        self.connection.setObjectName("connection")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(300, 70, 931, 661))
        self.frame_3.setStyleSheet("background-color:rgba(0,0,0,0.7);\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.widget_2 = QtWidgets.QWidget(self.frame_3)
        self.widget_2.setGeometry(QtCore.QRect(490, 130, 391, 211))
        self.widget_2.setStyleSheet("background-color:rgba(0,0,0,0.2);\n"
"box-shodow:10px 4px 4px 4px;\n"
"border-radius:10px")
        self.widget_2.setObjectName("widget_2")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 251, 41))
        self.label_6.setStyleSheet("background-color:none;\n"
"border:none;\n"
"font:77 10pt \"metropolis\";\n"
"font-size:20px;\n"
"color:white")
        self.label_6.setObjectName("label_6")
        self.pushButton_27 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_27.setGeometry(QtCore.QRect(240, 30, 121, 131))
        self.pushButton_27.setStyleSheet("background-color:none;")
        self.pushButton_27.setText("")
        self.pushButton_27.setIcon(icon7)
        self.pushButton_27.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_27.setObjectName("pushButton_27")
        self.nb_vente = QtWidgets.QLabel(self.widget_2)
        self.nb_vente.setGeometry(QtCore.QRect(40, 100, 171, 61))
        self.nb_vente.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nb_vente.setStyleSheet("background-color: transparent;\n"
"color: #fff;\n"
"font-weidth: bold;\n"
"font-size:32px;")
        self.nb_vente.setAlignment(QtCore.Qt.AlignCenter)
        self.nb_vente.setObjectName("nb_vente")
        self.widget_4 = QtWidgets.QWidget(self.frame_3)
        self.widget_4.setGeometry(QtCore.QRect(490, 410, 391, 201))
        self.widget_4.setStyleSheet("background-color:rgba(0,0,0,0.2);\n"
"box-shodow:10px 4px 4px 4px;\n"
"border-radius:10px")
        self.widget_4.setObjectName("widget_4")
        self.label_10 = QtWidgets.QLabel(self.widget_4)
        self.label_10.setGeometry(QtCore.QRect(30, 30, 211, 41))
        self.label_10.setStyleSheet("background-color:none;\n"
"border:none;\n"
"font:77 10pt \"metropolis\";\n"
"font-size:20px;\n"
"color:white")
        self.label_10.setObjectName("label_10")
        self.label_19 = QtWidgets.QLabel(self.widget_4)
        self.label_19.setGeometry(QtCore.QRect(30, 60, 201, 41))
        self.label_19.setStyleSheet("background-color:none;\n"
"border:none;\n"
"font:77 10pt \"metropolis\";\n"
"font-size:20px;\n"
"color:white")
        self.label_19.setObjectName("label_19")
        self.pushButton_34 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_34.setGeometry(QtCore.QRect(250, 30, 131, 131))
        self.pushButton_34.setStyleSheet("background-color:none;")
        self.pushButton_34.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/images/stock-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_34.setIcon(icon10)
        self.pushButton_34.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_34.setObjectName("pushButton_34")
        self.nb_vente_3 = QtWidgets.QLabel(self.widget_4)
        self.nb_vente_3.setGeometry(QtCore.QRect(30, 110, 171, 61))
        self.nb_vente_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nb_vente_3.setStyleSheet("background-color: transparent;\n"
"color: #fff;\n"
"font-weidth: bold;\n"
"font-size:32px;")
        self.nb_vente_3.setAlignment(QtCore.Qt.AlignCenter)
        self.nb_vente_3.setObjectName("nb_vente_3")
        self.label_18 = QtWidgets.QLabel(self.frame_3)
        self.label_18.setGeometry(QtCore.QRect(370, 40, 221, 41))
        self.label_18.setStyleSheet("background-color:none;\n"
"border:none;\n"
"font:90 30pt \"metropolis\";\n"
"font-size:30px;\n"
"color:white")
        self.label_18.setObjectName("label_18")
        self.widget = QtWidgets.QWidget(self.frame_3)
        self.widget.setGeometry(QtCore.QRect(40, 130, 381, 211))
        self.widget.setStyleSheet("\n"
"background-color:rgba(0,0,0,0.2);\n"
"box-shodow:10px 4px 4px 4px;\n"
"border-radius:10px\n"
"\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 231, 41))
        self.label_4.setStyleSheet("background-color:none;\n"
"border:none;\n"
"font:77 10pt \"metropolis\";\n"
"font-size:20px;\n"
"color:white")
        self.label_4.setObjectName("label_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setGeometry(QtCore.QRect(230, 30, 121, 131))
        self.pushButton_7.setStyleSheet("background-color:none;")
        self.pushButton_7.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/images/vente-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon11)
        self.pushButton_7.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_7.setObjectName("pushButton_7")
        self.nb_vente_2 = QtWidgets.QLabel(self.widget)
        self.nb_vente_2.setGeometry(QtCore.QRect(30, 110, 171, 61))
        self.nb_vente_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nb_vente_2.setStyleSheet("background-color: transparent;\n"
"color: #fff;\n"
"font-weidth: bold;\n"
"font-size:32px;")
        self.nb_vente_2.setAlignment(QtCore.Qt.AlignCenter)
        self.nb_vente_2.setObjectName("nb_vente_2")
        self.widget_3 = QtWidgets.QWidget(self.frame_3)
        self.widget_3.setGeometry(QtCore.QRect(40, 410, 381, 201))
        self.widget_3.setStyleSheet("background-color:rgba(0,0,0,0.2);\n"
"box-shodow:10px 4px 4px 4px;\n"
"border-radius:10px")
        self.widget_3.setObjectName("widget_3")
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setGeometry(QtCore.QRect(20, 40, 261, 41))
        self.label_8.setStyleSheet("background-color:none;\n"
"border:none;\n"
"font:77 10pt \"metropolis\";\n"
"font-size:20px;\n"
"color:white")
        self.label_8.setObjectName("label_8")
        self.pushButton_21 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_21.setGeometry(QtCore.QRect(240, 40, 121, 131))
        self.pushButton_21.setStyleSheet("background-color:none;")
        self.pushButton_21.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/images/images/produit-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_21.setIcon(icon12)
        self.pushButton_21.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_21.setObjectName("pushButton_21")
        self.nb_vente_4 = QtWidgets.QLabel(self.widget_3)
        self.nb_vente_4.setGeometry(QtCore.QRect(30, 100, 171, 61))
        self.nb_vente_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nb_vente_4.setStyleSheet("background-color: transparent;\n"
"color: #fff;\n"
"font-weidth: bold;\n"
"font-size:32px;")
        self.nb_vente_4.setAlignment(QtCore.Qt.AlignCenter)
        self.nb_vente_4.setObjectName("nb_vente_4")
        PageAccueil.setCentralWidget(self.centralwidget)

        self.retranslateUi(PageAccueil)
        QtCore.QMetaObject.connectSlotsByName(PageAccueil)

    def retranslateUi(self, PageAccueil):
        _translate = QtCore.QCoreApplication.translate
        PageAccueil.setWindowTitle(_translate("PageAccueil", "MainWindow"))
        self.user_btn.setText(_translate("PageAccueil", "Gestion des comptes"))
        self.user_btn.clicked.connect(lambda: page_loader.Loader.GestionCompteUser(self))
        self.produit_btn.setText(_translate("PageAccueil", "Gestion des produits"))
        self.produit_btn.clicked.connect(lambda: page_loader.Loader.ProduitManage(self))
        self.vente_btn.setText(_translate("PageAccueil", "Gestion des ventes"))
        self.acceuille_btn.setText(_translate("PageAccueil", "Accueil"))
        self.commande_btn.setText(_translate("PageAccueil", "Enregistrer une commande"))
        self.commande_btn.clicked.connect(lambda :page_loader.Loader.GestionCommands(self))
        self.facture_btn.setText(_translate("PageAccueil", "Generer une facture"))
        self.label_32.setText(_translate("PageAccueil", "Connecter"))
        self.label_6.setText(_translate("PageAccueil", "Nombre de commande"))
        self.nb_vente.setText(_translate("PageAccueil", "50"))
        self.label_10.setText(_translate("PageAccueil", "Nombres de produits"))
        self.label_19.setText(_translate("PageAccueil", "en stock"))
        self.nb_vente_3.setText(_translate("PageAccueil", "50"))
        self.label_18.setText(_translate("PageAccueil", "DASHBOARD"))
        self.label_4.setText(_translate("PageAccueil", "Nombres de ventes"))
        self.nb_vente_2.setText(_translate("PageAccueil", "50"))
        self.label_8.setText(_translate("PageAccueil", "Nombres de produits"))
        self.nb_vente_4.setText(_translate("PageAccueil", "50"))
import ressource_rc


class test(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_PageAccueil_Gerant()
        self.ui.setupUi(self)



    def center(self):
        # récupère la taille de l'écran
        screen_size = QDesktopWidget().screenGeometry(-1)
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
    PageAccueil = QtWidgets.QMainWindow()
    ui = test()
    # ui.setupUi(PageAccueil)
    ui.center()
    ui.show()
    sys.exit(app.exec_())
