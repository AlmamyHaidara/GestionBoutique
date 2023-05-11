import sys

sys.path.append('../Controler/Data')
sys.path.append('../Vue')
# import mysql.connector
from Controler.Data import mysql_connexion
from Vue.DialogueBox import DialogueBox


class Btn_method(mysql_connexion.Mysql_connection, DialogueBox):
    def __init__(self):
        self.conn = self.connect()
        self.cursor = self.conn.cursor()

        # self.conn =  self.connect().cursor()
        self.user_txt = ''
        self.password_txt = ''
        pass

    def btn_connexion(self, username, password):
        self.user_txt = username
        self.password_txt = password
        if ((self.user_txt == '' or self.password_txt == '') or (self.user_txt == ' ' or self.password_txt == ' ')):
            print(":==:==: Please enter your username and password:)")
        else:
            self.cursor.execute(f"SELECT username, password FROM users WHERE username = '{self.user_txt}' ")
            user = self.cursor.fetchall()
            print(user)
            if (user == []):
                print("Le username ou le password est incorrect")
            elif (user[0][1] == self.password_txt):
                print('Ok')
                self.successfulBox()
                return True
                return False
            else:
                print("Le username ou le password est incorrect")
                return False
