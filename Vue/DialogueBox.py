from PyQt5 import QtCore, QtGui, QtWidgets

from Vue.Edite_user_box import Ui_Dialog
from Vue.Edite_product_box import Ui_Dialog_Product
# from Vue.List_user import Ui_ListUser


class DialogueBox():
    def successfulBox(self):
        self.success = QtWidgets.QMessageBox()
        self.success.setWindowTitle('Successfully')
        self.success.setText('Operation effectuer avec succe')

        self.success.exec_()

    def editeDialogue(self, data):
        print('\n================================Data: ', data)
        self.dialogue = QtWidgets.QDialog()
        self.box = Ui_Dialog(data)
        self.box.setupUi(self.dialogue)
        self.dialogue.show()

    def editeBox(self,data):
        self.dialogue = QtWidgets.QDialog()
        self.box = Ui_Dialog_Product(data)
        self.box.setupUi(self.dialogue)
        self.dialogue.show()
        pass
