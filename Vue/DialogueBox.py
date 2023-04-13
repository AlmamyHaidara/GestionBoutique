from PyQt5 import QtCore, QtGui, QtWidgets


class DialogueBox():
    def successfulBox(self):
        self.success = QtWidgets.QMessageBox()
        self.success.setWindowTitle('Successfully')
        self.success.setText('Operation effectuer avec succe')

        self.success.exec_()

