import sys
from datetime import datetime

from Controler.Data.Models.Quantiter_Model import Quantiter

sys.path.append('../')
from peewee import *

from Controler.Data.mysql_connexion import connect
from Controler.Data.Models.Produit_Model import Produit
from Controler.Data.Models.Client_Model import Client

conn = connect()


class Command(Model):
    nom_command = CharField()
    produit_id = ForeignKeyField(Produit, backref='produit')
    quantiter_id = ForeignKeyField(Quantiter, backref='quantiter')
    montant_command = DoubleField()
    client_id = ForeignKeyField(Client, backref='client')
    debut_date = DateField(default=datetime.now)
    # fin_date = DateField()
    eta_livraison = CharField(default='Non livrer')

    class Meta:
        database = conn
        table_name = 'Command'


conn.connect()
conn.create_tables([Command])
