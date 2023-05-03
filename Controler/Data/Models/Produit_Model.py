import sys

from Controler.Data.Models.Quantiter_Model import Quantiter

sys.path.append('../')
from peewee import *

from Controler.Data.mysql_connexion import connect

conn = connect()


class Produit(Model):
    nom_produit = CharField()
    categorie = CharField()
    quantiter = ForeignKeyField(Quantiter, backref='quantiters')
    prix_produit = DoubleField()
    quantiter_id = ForeignKeyField(Quantiter, backref='quantiters')
    prix_produit = DoubleField()
    etat = CharField()
    montant = DoubleField()

    class Meta:
        database = conn
        table_name = 'Produit'


conn.connect()
conn.create_tables([Produit])
