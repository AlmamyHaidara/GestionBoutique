from PyQt5 import   QtWidgets
from PyQt5.QtCore import QModelIndex

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Création du QTreeView
        self.treeview = QtWidgets.QTreeView(self)
        self.treeview.setGeometry(10, 10, 200, 200)

        # Création des items
        root_item = QtWidgets.QStandardItem('Root')
        child1_item = QtWidgets.QStandardItem('Child 1')
        child2_item = QtWidgets.QStandardItem('Child 2')

        # Ajout des items à l'index racine
        self.model = self.treeview.model()
        self.model.appendRow(root_item)
        root_index = self.model.indexFromItem(root_item)

        # Ajout des items enfants à l'index racine
        self.model.insertRow(0, child1_item, root_index)
        self.model.insertRow(1, child2_item, root_index)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
