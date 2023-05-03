import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget

import Vue

# from PySide2.QtWidgets import QApplication

# os.environ["QT_QPA_PLATFORM"] = "X11"
sys.path.append('./Vue')
# from Custom_Widgets.Widgets import QMainWindow
# from Custom_Widgets.components.python.ui_interface import Ui_MainWindow


<<<<<<< HEAD
from Vue.LoginBoutique import *
=======
from Vue import Login_UI
>>>>>>> f3f9d25 (la version avec les interface utilisateur)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
<<<<<<< HEAD
        self.ui = Vue.LoginBoutique.Ui_Form()
        self.ui.setupUi(self)
        self.center()  # centre la fenêtre
        self.show()
=======
        self.ui = Login_UI.Ui_file1()
        self.ui.setupUi(self)
        self.center()  # centre la fenêtre
        # self.show()
>>>>>>> f3f9d25 (la version avec les interface utilisateur)

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

<<<<<<< HEAD
=======
    def winClose(self):
        self.close()
>>>>>>> f3f9d25 (la version avec les interface utilisateur)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())
