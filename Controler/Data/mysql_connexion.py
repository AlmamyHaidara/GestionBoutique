from peewee import *
import mysql.connector
from peewee import MySQLDatabase


# from PyQt5.QtCore.QUrl import query
def connect():
    # Connection a la base de donner
    try:
        conn = db = MySQLDatabase(
            'shopManagement',
            user='root',
            password='',
            host='localhost',
            port=3306,
            autocommit=True
        )
        print(f"==||==: Connexion a la base de donner:: {conn.database}")

        return conn
    except mysql.connector.errors:
        print(f"Error:: {mysql.connector.errors.Error}")


