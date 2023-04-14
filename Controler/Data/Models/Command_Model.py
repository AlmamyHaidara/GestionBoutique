import sys

from Controler.Data.Models.User_Model import User

sys.path.append('../')
from peewee import *

from Controler.Data.mysql_connexion import connect
from Controler.Data.Models.Produit_Model import Produit

conn = connect()


class Command(Model):
    nom_command = CharField()
    montant_command = DoubleField()
    produit = ForeignKeyField(Produit, backref='produit')
    user = ForeignKeyField(User, backref='users')

    class Meta:
        database = conn
        table_name = 'Command'


conn.connect()
conn.create_tables([Command])
