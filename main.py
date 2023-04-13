import sys
import os

from PyQt5.QtWidgets import QApplication

# from PySide2.QtWidgets import QApplication

import Vue

os.environ["QT_QPA_PLATFORM"] = "wayland"
sys.path.append('./Vue')
from Custom_Widgets.Widgets import QMainWindow
from Custom_Widgets.components.python.ui_interface import Ui_MainWindow



from Vue.LoginBoutique   import *

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.ui = Vue.LoginBoutique.Ui_Form()
        self.ui.setupUi(self)

        self.show()


if __name__ == '__main__':
    app =  QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())