import mysql.connector
from peewee import MySQLDatabase

# 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

def connect():
    # Connection a la base de donner
    try:
        conn = MySQLDatabase(
            'shopManagement',
            user='root',
            password='root',
            host='localhost',
            port=3306,
            autocommit=True
        )
        print(f"==||==: Connexion a la base de donner:: {conn.database}")
        print(conn)
        return conn
    except mysql.connector.errors:
        print(f"Error:: {mysql.connector.errors.Error}")


