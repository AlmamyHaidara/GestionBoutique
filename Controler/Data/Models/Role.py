import sys
sys.path.append('../')
from peewee import *

from Controler.Data.mysql_connexion import connect

conn = connect()


class Role(Model):
    nom_Role = CharField()

    class Meta:
        database = conn
        table_name = 'Role'

conn.connect()
conn.create_tables([Role])