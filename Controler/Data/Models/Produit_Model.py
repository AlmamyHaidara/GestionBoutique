import sys

from Controler.Data.Models.Categorie_Model import Categorie
from Controler.Data.Models.Quantiter_Model import Quantiter

sys.path.append('../')
from peewee import *

from Controler.Data.mysql_connexion import connect

conn = connect()


class Produit(Model):
    nom_produit = CharField()
    prix_produit = DoubleField()
    categorie = ForeignKeyField(Categorie, backref='categories')
    quantiter = ForeignKeyField(Quantiter, backref='quantiters')

    class Meta:
        database = conn
        table_name = 'Produit'

conn.connect()
conn.create_tables([Produit])