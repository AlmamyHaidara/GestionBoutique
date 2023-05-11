import sys
sys.path.append('../')
from peewee import *

from Controler.Data.mysql_connexion import connect
from Controler.Data.Models.Role import Role

conn = connect()


class Profile(Model):
    nom_profile = CharField()
    # role = ForeignKeyField(Role, backref='roles')

    class Meta:
        database = conn
        table_name = 'Profile'


conn.connect()
conn.create_tables([Profile])