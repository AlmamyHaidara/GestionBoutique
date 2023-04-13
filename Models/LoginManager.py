import sys
sys.path.append('../Controler/Data')
sys.path.append('../Vue')
from Controler.Data.Models import User_Model, Profile_Model,Command_Model,Produit_Model,Vente_Model,Quantiter_Model,Categorie_Model
from Vue.DialogueBox import DialogueBox

class LoginManager( DialogueBox):
    def __init__(self):
      pass



    def auth_config(self,username,password):
        if ((username == '' or password == '') or (username == ' ' or password == ' ')):
            print(":==:==: Please enter your username and password:)")
        else:
            users = User_Model.User.select().where(User_Model.User.username == username).execute()
            if(not users):
                print("Le username ou le password est incorrect")
            else:
                for user in users:
                    print(user)
                    if (user.password == password):
                        print('Ok')
                        self.successfulBox()
                        return users
                    else:
                        print("Le username ou le password est incorrect")
                        return False

    def authication(self,username,password):
        users = self.auth_config(username,password)
        if(users != False):
            for user in users:
                if(user.profile == 'admin'):
                    print("Is admin")
                else:
                    print("is caisseir")
                    print(f'===!!! {user.email}, ===== {user.profile}')

