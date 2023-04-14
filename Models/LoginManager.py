import sys

sys.path.append('../Controler/Data')
sys.path.append('../Vue')
sys.path.append('./')

from Vue.DialogueBox import DialogueBox

from Models.User_management import User_Model, User_manager


class LoginManager(DialogueBox):
    def __init__(self):

        pass

    def auth_config(self, username: str, password: str):
        if ((username == '' or password == '') or (username == ' ' or password == ' ')):
            print(":==:==: Please enter your username and password:)")
        else:
            users = User_Model.User.select().where(User_Model.User.username == username).execute()
            if (not users):
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

    def authication_conf(self, username: str, password: str):
        objet = {'nom': 'Technolab', 'prenom': 'ISTA', 'username': 'ISTA', 'email': 'technolabista1@gmail.com',
                 'tel': '89848495', 'password': 'bamako2023', 'profil_id': 1}
        usert = User_manager()

        print(usert.search_user(objet).email)

        # users = self.auth_config(username, password)
        # if (users != False):
        #     for user in users:
        #         if (user.profile == 'admin'):
        #             print("Is admin")
        #         else:
        #             print("is caisseir")
        #             print(f'===!!! {user.email}, ===== {user.profile}')
        pass
