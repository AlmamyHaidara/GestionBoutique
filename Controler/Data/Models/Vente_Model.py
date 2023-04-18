import sys
from datetime import datetime

from Controler.Data.Models.Produit_Model import Produit
from Controler.Data.Models.Quantiter_Model import Quantiter
from Controler.Data.Models.User_Model import User

sys.path.append('../')
from peewee import *

from Controler.Data.mysql_connexion import connect

conn = connect()


class Vente(Model):
    produit = ForeignKeyField(Produit, backref='produits')
    quantiter = ForeignKeyField(Quantiter, backref='quantiter')
    user = ForeignKeyField(User, backref='users')
    debut_date = DateField(default=datetime.now)

    class Meta:
        database = conn
        table_name = 'Vente'


conn.connect()
conn.create_tables([Vente])
