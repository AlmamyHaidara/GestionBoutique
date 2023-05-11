import sys
from datetime import datetime

sys.path.append('../')
from peewee import *

from Controler.Data.mysql_connexion import connect

conn = connect()


class Client(Model):
    nom= CharField()
    prenom = CharField()
    telephone = CharField()
    quartier = CharField()


    class Meta:
        database = conn
        table_name = 'Client'


conn.connect()
conn.create_tables([Client])
