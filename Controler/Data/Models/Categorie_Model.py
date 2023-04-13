import sys
sys.path.append('../')
from peewee import *

from Controler.Data.mysql_connexion import connect

conn = connect()


class Categorie(Model):
    nom_categorie = CharField()

    class Meta:
        database = conn
        table_name = 'Categorie'

conn.connect()
conn.create_tables([Categorie])