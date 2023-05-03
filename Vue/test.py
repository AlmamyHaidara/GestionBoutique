import sys
from PyQt5 import QtWidgets,QtGui,QtCore
class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(3)

        # Remplir les cellules avec des données pour tester
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                item = QtWidgets.QTableWidgetItem("Cellule {}-{}".format(row, col))
                self.tableWidget.setItem(row, col, item)

        # Connecter l'événement itemSelectionChanged
        self.tableWidget.itemSelectionChanged.connect(self.on_tableWidget_itemSelectionChanged)

        # Créer un bouton dans la cellule (0, 7)
        self.button = QtWidgets.QPushButton("Supprimer")
        self.buttonm = QtWidgets.QPushButton("modifier")
        self.tableWidget.setCellWidget(0, 6, self.button)
        self.tableWidget.setCellWidget(0, 7, self.buttonm)

        # Connecter l'événement de clic sur le bouton
        self.button.clicked.connect(lambda: self.on_button_clicked(0, 6))
        self.buttonm.clicked.connect(lambda: self.on_button_clicked(0, 7))

    def on_tableWidget_itemSelectionChanged(self):
        # Récupérer la ligne sélectionnée
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            col = selected_items[0].column()
            print("L'utilisateur a sélectionné la cellule ({}, {})".format(row, col))

    def on_button_clicked(self, row, col):
        if col == 7:
            # Modifier la cellule correspondante
            item = QtWidgets.QTableWidgetItem("Nouvelle valeur")
            self.tableWidget.setItem(row, col, item)
        elif col == 6:
            # Supprimer la ligne correspondante
            self.tableWidget.removeRow(row)
        else:
            print("Action non prise en charge")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
