import sys
from datetime import datetime

sys.path.append('../')
from peewee import *

from Controler.Data.mysql_connexion import connect
from Controler.Data.Models.Produit_Model import Produit
from Controler.Data.Models.User_Model import User

conn = connect()


class Command(Model):
    nom_command = CharField()
    produit = ForeignKeyField(Produit, backref='produit')
    montant_command = DoubleField()
    user = ForeignKeyField(User, backref='users')
    debut_date = DateField(default=datetime.now)
    fin_date = DateField()

    class Meta:
        database = conn
        table_name = 'Command'


conn.connect()
conn.create_tables([Command])
