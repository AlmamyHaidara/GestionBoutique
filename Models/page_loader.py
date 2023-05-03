import sys

import Vue.Gestion_user
from Vue import Login_UI

sys.path.append('../Vue')

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget

from Vue.Acceuile_cassier import Ui_PageAccueil
from Vue.Acceuile_gerant import Ui_PageAccueil_Gerant,test
from Vue.manage_users import Ui_AjouterCompte
from Vue.GestionProduitAdmin import ui_user
from Vue.Login_UI import *
from main import MainWindow
from Vue import  manage_users
from Vue.Edite_user_box import Ui_Dialog

class Loader(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # self.center()
        pass
    def testMethode(self):
        Ui_AjouterCompte.showList()
    def acceuile_cassier(self):
        self.PageAccueil = QtWidgets.QMainWindow()
        self.ui = Ui_PageAccueil()
        self.ui.setupUi(self.PageAccueil)
        # Vue.Login_UI.Ui_file1.closeWindow(self)
        self.center()
        self.PageAccueil.show()

        pass

    def acceuile_gerant(self):
        self.ui = test()
        self.ui.center()
        main = MainWindow()
        main.close()
        self.ui.show()
        pass

    def GestionCompteUser(self):
        print("Gestion users")
        self.ui = manage_users.ui_user()
        self.ui.center()

        self.ui.show()

    def editeDialogue(self):
        self.dialogue = QtWidgets.QDialog()
        self.box = Ui_Dialog()
        self.box.setupUi(self.dialogue)
        self.dialogue.show()

    # def ListVenteUser(self):
    #     self.window2 = QtWidgets.QMainWindow()
    #     self.ui = Ui_ListVente()
    #     self.ui.setupUi(self.window2)
    #     self.window2.show()
    #
    # def GestionVenteUser(self):
    #     self.window2 = QtWidgets.QMainWindow()
    #     self.ui = Ui_AjouterVente()
    #     self.ui.setupUi(self.window2)
    #     self.window2.show()

    def ProduitManage(self):
        self.ui = ui_user()
        self.ui.show()
    pass
