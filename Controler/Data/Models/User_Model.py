import sys
sys.path.append('../')
from peewee import *

from Controler.Data.mysql_connexion import connect
from Controler.Data.Models.Profile_Model import Profile
from Controler.Data.Models.Command_Model import Command
from Controler.Data.Models.Vente_Model import Vente


conn = connect()


# User model
class User(Model):
    nom = CharField()
    prenom = CharField()
    username = CharField()
    email = CharField()
    tel = CharField()
    password = CharField()
    profile = ForeignKeyField(Profile, backref='profiles')
    command = ForeignKeyField(Command, backref='commands')
    vente = ForeignKeyField(Vente, backref='ventes')


    class Meta:
        database = conn
        table_name = 'User'


conn.connect()
conn.create_tables([User])

