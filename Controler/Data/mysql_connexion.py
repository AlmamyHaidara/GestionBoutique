import mysql.connector
# from PyQt5.QtCore.QUrl import query

class Mysql_connection():
    def __init__(self):
        pass
    def connect(self):
        # Connection a la base de donner
        try:
            self.conn = mysql.connector.connect(user='root', password='',host='localhost', database='boutique')
            print(f"==||==: Connexion a la base de donner:: {self.conn.database}")

            return self.conn
        except mysql.connector.errors:
            print(f"Error:: {mysql.connector.errors.Error}")
