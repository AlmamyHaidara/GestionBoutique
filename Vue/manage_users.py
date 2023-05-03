import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from Models.Class.User_management import User_manager
sys.path.append('../../Controler')
from Controler.Data.Models import User_Model
from functools import partial
from Vue.DialogueBox import DialogueBox
class Ui_AjouterCompte(User_manager,DialogueBox):
    def __init__(self):
        self.users = User_Model.User()
        pass
    def setupUi(self, AjouterCompte):
        AjouterCompte.setObjectName("AjouterCompte")
        AjouterCompte.resize(1280, 800)
        self.centralwidget = QtWidgets.QWidget(AjouterCompte)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1281, 801))
        self.frame.setStyleSheet("background-color: rgb(255,228,54)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_haut = QtWidgets.QFrame(self.frame)
        self.frame_haut.setGeometry(QtCore.QRect(0, 0, 1271, 71))
        self.frame_haut.setStyleSheet("border:none")
        self.frame_haut.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_haut.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_haut.setObjectName("frame_haut")
        self.pushButton = QtWidgets.QPushButton(self.frame_haut)
        self.pushButton.setGeometry(QtCore.QRect(1120, 0, 113, 81))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Vue/Design/../fermerIcon-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(60, 80))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_haut)
        self.pushButton_2.setGeometry(QtCore.QRect(1010, 0, 113, 81))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./Vue/Design/../pngtree-fullscreen--icon-in-trendy-style-isolated-background-png-image_1566064-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(60, 80))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_haut)
        self.pushButton_3.setGeometry(QtCore.QRect(880, 0, 113, 81))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./Vue/Design/../red-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(60, 80))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_20 = QtWidgets.QPushButton(self.frame)
        self.pushButton_20.setGeometry(QtCore.QRect(-20, 750, 181, 51))
        self.pushButton_20.setStyleSheet("background-color:white;\n"
"color:black;\n"
"border-radius:8px;\n"
"font:90 18pt \"metropolis\";")
        self.pushButton_20.setObjectName("pushButton_20")
        self.widget_9 = QtWidgets.QWidget(self.frame)
        self.widget_9.setGeometry(QtCore.QRect(0, 0, 221, 80))
        self.widget_9.setStyleSheet("background-color:white;\n"
"border:none;\n"
"border-radius:8px\n"
"")
        self.widget_9.setObjectName("widget_9")
        self.label_32 = QtWidgets.QLabel(self.widget_9)
        self.label_32.setGeometry(QtCore.QRect(90, 20, 141, 41))
        self.label_32.setStyleSheet("border:none;\n"
"font:90 18pt \"metropolis\";")
        self.label_32.setObjectName("label_32")
        self.pushButton_12 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_12.setGeometry(QtCore.QRect(-10, 10, 111, 61))
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/images/userIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon3)
        self.pushButton_12.setIconSize(QtCore.QSize(60, 110))
        self.pushButton_12.setObjectName("pushButton_12")
        self.crud_user = QtWidgets.QStackedWidget(self.frame)
        self.crud_user.setGeometry(QtCore.QRect(150, 90, 991, 651))
        self.crud_user.setStyleSheet("background-color:rgba(0,0,0,0.2);\n"
"border-radius: 15px;")
        self.crud_user.setObjectName("crud_user")
        self.list_users = QtWidgets.QWidget()
        self.list_users.setObjectName("list_users")

        self.search = QtWidgets.QLineEdit(self.list_users)
        self.search.setGeometry(QtCore.QRect(710, 120, 211, 31))
        self.search.setStyleSheet("background-color:rgba(255,255,255,0.5); border-radius: 5px;")
        self.search.setObjectName("search")

        self.actualiser = QtWidgets.QPushButton(self.list_users)
        self.actualiser.setGeometry(QtCore.QRect(80, 120, 121, 31))
        self.actualiser.setStyleSheet("QPushButton{\n"
                                      "background-color:#FFE436;\n"
                                      "border-top-left-radius:20px;\n"
                                      "border-bottom-left-radius:20px;\n"
                                      "color:#000;\n"
                                      "font:77 15pt \"metropolis\";\n"
                                      "border-radius:5px\n"
                                      "\n"
                                      "\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color:white;\n"
                                      "border-radius:5px;\n"
                                      "color:rgb(0,0,0);\n"
                                      "font:77 15pt \"metropolis\";\n"
                                      "\n"
                                      "\n"
                                      "}\n"
                                      "")
        self.actualiser.setObjectName("actualiser")

        self.btn_list = QtWidgets.QPushButton(self.list_users)
        self.btn_list.setGeometry(QtCore.QRect(670, 30, 221, 71))
        self.btn_list.setStyleSheet("QPushButton{\n"
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/images/pngtree-vector-remove-user-icon-png-image_4101425-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_list.setIcon(icon4)
        self.btn_list.setIconSize(QtCore.QSize(60, 70))
        self.btn_list.setObjectName("btn_list")
        self.tableWidget = QtWidgets.QTableWidget(self.list_users)
        self.tableWidget.setGeometry(QtCore.QRect(30, 160, 931, 451))
        self.tableWidget.setStyleSheet("background-color:#fff;")
        self.tableWidget.setObjectName("tableWidget")

        font = QtGui.QFont()
        font.setBold(True)


        self.tableWidget.setHorizontalHeaderLabels(["ID", "Prenom", "Nom", "Profil", "Email", "Telephone"])
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setStyleSheet("color:#000;\n" "font-weidth:bold;\n")
        self.tableWidget.horizontalHeader().setStyleSheet("background-color: yellow;\n")

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.btn_add_list = QtWidgets.QPushButton(self.list_users)
        self.btn_add_list.setGeometry(QtCore.QRect(40, 30, 221, 61))
        self.btn_add_list.setStyleSheet("QPushButton{\n"
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/images/add_user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_list.setIcon(icon6)
        self.btn_add_list.setIconSize(QtCore.QSize(50, 50))
        self.btn_add_list.setObjectName("btn_add_list")
        self.crud_user.addWidget(self.list_users)
        self.ajout_users = QtWidgets.QWidget()
        self.ajout_users.setObjectName("ajout_users")

        self.profil = QtWidgets.QComboBox(self.ajout_users)
        self.profil.setGeometry(QtCore.QRect(340, 410, 361, 41))
        self.profil.addItem( "Caissier")
        self.profil.addItem( "Admin")
        self.profil.setStyleSheet("border-radius:8px;\n"
"color:black;\n"
"background-color:rgba(255,255,255,0.8)\n"
"\n"
"")
        self.profil.setObjectName("profil")
        self.label_3 = QtWidgets.QLabel(self.ajout_users)
        self.label_3.setGeometry(QtCore.QRect(360, 120, 341, 41))
        self.label_3.setStyleSheet("background-color:none;\n"
"border:none;\n"
"font:90 30pt \"metropolis\";\n"
"font-size:30px;\n"
"color:white")
        self.label_3.setObjectName("label_3")
        self.tel = QtWidgets.QLineEdit(self.ajout_users)
        self.tel.setGeometry(QtCore.QRect(340, 350, 361, 41))
        self.tel.setStyleSheet("border-radius:8px;\n"
"color:black;\n"
"background-color:rgba(255,255,255,0.8)\n"
"\n"
"")
        self.tel.setObjectName("tel")
        self.add_btn = QtWidgets.QPushButton(self.ajout_users)
        self.add_btn.setGeometry(QtCore.QRect(60, 30, 221, 61))
        self.add_btn.setStyleSheet("QPushButton{\n"
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
        self.add_btn.setIcon(icon6)
        self.add_btn.setIconSize(QtCore.QSize(50, 50))
        self.add_btn.setObjectName("add_btn")
        self.email = QtWidgets.QLineEdit(self.ajout_users)
        self.email.setGeometry(QtCore.QRect(340, 290, 361, 41))
        self.email.setStyleSheet("border-radius:8px;\n"
"color:black;\n"
"background-color:rgba(255,255,255,0.8)\n"
"\n"
"")
        self.email.setObjectName("email")
        self.list_btn = QtWidgets.QPushButton(self.ajout_users)
        self.list_btn.setGeometry(QtCore.QRect(690, 30, 221, 71))
        self.list_btn.setStyleSheet("QPushButton{\n"
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
        self.list_btn.setIcon(icon4)
        self.list_btn.setIconSize(QtCore.QSize(60, 70))
        self.list_btn.setObjectName("list_btn")
        self.username = QtWidgets.QLineEdit(self.ajout_users)
        self.username.setGeometry(QtCore.QRect(340, 230, 361, 41))
        self.username.setStyleSheet("border-radius:8px;\n"
"color:black;\n"
"background-color:rgba(255,255,255,0.8)\n"
"\n"
"")
        self.username.setObjectName("username")
        self.prenom = QtWidgets.QLineEdit(self.ajout_users)
        self.prenom.setGeometry(QtCore.QRect(340, 170, 171, 41))
        self.prenom.setStyleSheet("border-radius:8px;\n"
"color:black;\n"
"background-color:rgba(255,255,255,0.8)\n"
"\n"
"")
        self.prenom.setObjectName("prenom")
        self.nom = QtWidgets.QLineEdit(self.ajout_users)
        self.nom.setGeometry(QtCore.QRect(530, 170, 171, 41))
        self.nom.setStyleSheet("border-radius:8px;\n"
"color:black;\n"
"background-color:rgba(255,255,255,0.8)\n"
"\n"
"")
        self.nom.setObjectName("Nom")
        self.password = QtWidgets.QLineEdit(self.ajout_users)
        self.password.setGeometry(QtCore.QRect(340, 470, 361, 41))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setStyleSheet("border-radius:8px;\n"
"color:black;\n"
"background-color:rgba(255,255,255,0.8)\n"
"\n"
"")
        self.password.setObjectName("password")
        self.enregistrer = QtWidgets.QPushButton(self.ajout_users)
        self.enregistrer.setGeometry(QtCore.QRect(440, 560, 181, 32))
        self.enregistrer.setStyleSheet("QPushButton{\n"
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
        self.enregistrer.setObjectName("enregistrer")

        self.frame1 = QtWidgets.QFrame()
        self.label1 = QtWidgets.QLabel('Frame 1', self.frame1)
        self.button1 = QtWidgets.QPushButton('Go to Frame 2', self.frame1)

        self.frame2 = QtWidgets.QFrame()
        self.label2 = QtWidgets.QLabel('Frame 2', self.frame1)
        self.button2 = QtWidgets.QPushButton('Go to Frame 2', self.frame2)



        self.crud_user.addWidget(self.ajout_users)

        AjouterCompte.setCentralWidget(self.centralwidget)


        self.retranslateUi(AjouterCompte)
        self.crud_user.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(AjouterCompte)



    def retranslateUi(self, AjouterCompte):
        _translate = QtCore.QCoreApplication.translate
        AjouterCompte.setWindowTitle(_translate("AjouterCompte", "MainWindow"))
        self.pushButton_20.setText(_translate("AjouterCompte", "Retour"))
        self.label_32.setText(_translate("AjouterCompte", "Connecter"))
        self.btn_list.setText(_translate("AjouterCompte", "listes des utilisateurs"))

        self.search.setPlaceholderText(_translate("AjouterCompte", "Rechercher"))


        self.actualiser.setText(_translate("AjouterCompte", "Actualiser"))
        self.tableWidget.setHorizontalHeaderItem(0,QtWidgets.QTableWidgetItem("ID"))

        self.tableWidget.setHorizontalHeaderItem(1,QtWidgets.QTableWidgetItem("Nom"))
        self.tableWidget.setHorizontalHeaderItem(2,QtWidgets.QTableWidgetItem("Prenom"))
        self.tableWidget.setHorizontalHeaderItem(3,QtWidgets.QTableWidgetItem("Username"))
        self.tableWidget.setHorizontalHeaderItem(4,QtWidgets.QTableWidgetItem("Email"))
        self.tableWidget.setHorizontalHeaderItem(5,QtWidgets.QTableWidgetItem("Telephone"))
        self.tableWidget.setHorizontalHeaderItem(6,QtWidgets.QTableWidgetItem("Profil"))
        self.tableWidget.setHorizontalHeaderItem(7,QtWidgets.QTableWidgetItem("Update"))
        self.tableWidget.setHorizontalHeaderItem(8, QtWidgets.QTableWidgetItem("Delete"))
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 200)
        self.tableWidget.setColumnWidth(5, 100)
        self.tableWidget.setColumnWidth(6, 100)
        self.tableWidget.setColumnWidth(7, 80)
        self.tableWidget.setColumnWidth(8, 80)
        self.tableRow =  0


        self.btn_add_list.setText(_translate("AjouterCompte", "Ajouter un compte"))
        self.profil.setPlaceholderText(_translate("AjouterCompte", "Profile"))
        self.label_3.setText(_translate("AjouterCompte", "AJOUTER UN COMPTE"))
        self.tel.setPlaceholderText(_translate("AjouterCompte", "téléphone"))
        self.add_btn.setText(_translate("AjouterCompte", "Ajouter un compte"))
        self.crud_user.setCurrentWidget(self.ajout_users)
        self.add_btn.clicked.connect(self.showAdd)

        self.email.setPlaceholderText(_translate("AjouterCompte", "Email"))
        self.list_btn.setText(_translate("AjouterCompte", "listes des utilisateurs"))
        # self.list_btn.clicked.connect(self.showList)
        self.list_btn.clicked.connect(self.showList)
        self.username.setPlaceholderText(_translate("AjouterCompte", "Username"))
        self.prenom.setPlaceholderText(_translate("AjouterCompte", "Prenom"))
        self.nom.setPlaceholderText(_translate("AjouterCompte", "Nom"))
        self.password.setPlaceholderText(_translate("AjouterCompte", "Password"))
        self.enregistrer.setText(_translate("AjouterCompte", "Enregistrer"))



        self.actualiser.clicked.connect(self.showList)

        self.search.textChanged.connect(self.searchTable)
        # self.search.returnPressed.connect(lambda : self.showList(self.search_user( self.search.text())))

        self.btn_add_list.clicked.connect(self.showAdd)


        self.enregistrer.clicked.connect(lambda: self.create_user({
                'nom': self.nom.text(),
                'prenom': self.prenom.text(),
                'username': self.username.text(),
                'email': self.email.text(),
                'tel': self.tel.text(),
                'profil': self.profil.currentText(),
                'password': self.password.text(),
        }))


    def show_user_edit(self):
            self.crud_user.setCurrentWidget(self.frame1)


    def showAdd(self):
        print('dfghj ADD')
        self.crud_user.setCurrentWidget(self.ajout_users)

    def searchTable(self):
        # Récupération de la chaîne de recherche
        searchText = self.search.text().lower()

        # Recherche des QTableWidgetItem correspondants
        items = self.tableWidget.findItems(searchText, QtCore.Qt.MatchContains)

        # Sélection des lignes correspondantes
        self.tableWidget.clearSelection()
        for item in items:
            if item != None:
                item.setSelected(True)
            else:
                return False
    def showList(self):
        print('dfghj ADD')
        self.crud_user.setCurrentWidget(self.list_users)
        print('dfghj LIST: ', self.All_user_list())
        self.data = self.All_user_list()
        self.tableWidget.setRowCount(len( self.data ))
        self.tableWidget.setColumnCount(len( self.data )+7)
        if self.data != None:
            for row in range(len(self.data)):
                    for column in range(len(self.data[row])):
                        # pass
                            item = QtWidgets.QTableWidgetItem(str(self.data[row][column]))
                            # print('dfghj LIST: ',len(self.data), ' ', len(self.data[row]),' ', column, " => ", item.text() )
                            self.tableWidget.setItem(row, column, item)
                            # # Création d'un QPushButton pour chaque cellule
                            # # Ajout de l'objet QPushButton dans la cellule de la table
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

                            self.tableWidget.setCellWidget(row, 7, self.update_btn)
                            self.tableWidget.setCellWidget(row, 8, self.delete_btn)
                            self.delete_btn.clicked.connect(partial(self.delete_user_method, self.delete_btn))
                            self.update_btn.clicked.connect(partial(self.update_user_method, self.update_btn))
                    print('===========================================================')

    def delete_user_method(self, btn):
        if btn:
            button = btn.sender()
            # Trouver la ligne correspondante dans le QTableWidget
            index = self.tableWidget.indexAt(button.pos())
            if index.isValid():
                row = index.row()
                col = index.column()
                item = self.tableWidget.item(row, 4)

                if item is not None:
                    email = item.text()
                    # self.data_item.append(text)
                    print(email)
                    result =  self.delete_user(email)
                    if result:
                        self.tableWidget.removeRow(row)
                    else:
                        print("Voulez-vous pas suprimer davantage!!!")

        pass

    def update_user_method(self, btn):
        if btn:
            updateBtn = btn.sender()
            update_data = []
            index = self.tableWidget.indexAt(updateBtn.pos())
            if index.isValid():
                row = index.row()
                col = index.column()
                for i in range(7):
                    item = self.tableWidget.item(row, i)
                    print(item.text())
                    update_data.append(item.text())
                print(update_data)

                self.editeDialogue(update_data)

import ressource_rc


class ui_user(QtWidgets.QMainWindow):
        def __init__(self):
            QtWidgets.QMainWindow.__init__(self)
            self.ui = Ui_AjouterCompte()
            self.ui.setupUi(self)
            self.ui.crud_user.setCurrentWidget(self.ui.ajout_users)
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
    ui = ui_user()
    # ui.setupUi(AjouterCompte)
    ui.show()
    sys.exit(app.exec_())

