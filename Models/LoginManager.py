import sys

import bcrypt

sys.path.append('../Controler/Data')
sys.path.append('../Vue')
sys.path.append('./')

from Vue.DialogueBox import DialogueBox
from Models.Class.User_management import User_Model
from Models.Class.Command_management import Command_manager

from Controler.Data.Models import Profile_Model
from Models import page_loader


class LoginManager(DialogueBox,):
    # def __init__(self):
    #     super().__init__()
    #     pass


    def auth_config(self, username: str, password: str):
        if ((username == '' or password == '') or (username == ' ' or password == ' ')):
            print(":==:==: Please enter your username and password:)")
            return False
        else:
            users = User_Model.User.select().where(User_Model.User.username == username).execute()
            if (not users):
                print("Le username ou le password est incorrect :)")
                return False
            else:
                    print(password.encode('utf-8'))
                    print(user.password)
                    if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                        print("User data=>: ", user.username)
                        print(password.encode('utf-8'))
                        print(user.password.encode('utf-8'))
                        # if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                        if bcrypt.checkpw(password.encode('utf-8'), b'$2b$12$gTqV6PQJrb8/Uw9ZJnGkgeEBA18ufCNbK1XDOuc.h3CBN1u0DZ3hW'):
                            print("Le mot de passe est valide !")
                            print('Ok')
                            self.successfulBox()
                            return users
                        else:
                            print("Le mot de passe est invalide.")
                            print("Le username ou le password est incorrect :)")
                            return False

    def authication_conf(self, username: str, password: str):

        data = {
            "invoice_number": "INV-2023-001",
            "invoice_date": "2023-04-16",
            "customer_name": "John Doe",
            "customer_address": "123 Main St, Anytown USA",
            "invoice_items": [
                {
                    "name": "Produit 1",
                    "quantity": 2,
                    "unit_price": 10.99,
                    "total": 21.98
                },
                {
                    "name": "Produit 2",
                    "quantity": 1,
                    "unit_price": 5.50,
                    "total": 5.50
                },
                {
                    "name": "Produit 3",
                    "quantity": 3,
                    "unit_price": 8.75,
                    "total": 26.25
                }
            ],
            "total": 53.73
        }
        Command_manager.create_command(self)
        # generate_invoice(data)
        # Object testing
        # objet = {'nom': 'Technolab', 'prenom': 'ISTA', 'username': 'ISTA', 'email': 'technolabista1@gmail1.com',
        #          'tel': '89848495', 'password': 'bamako2023', 'profil_id': 1}
        # usert = User_manager()
        #
        # print(usert.modify_user_password('almamyh27@gmail.com'))
        # """
        # Cette fonction permet de verifier les critaires l'authantifications
        # :param username:
        # :param password:
        # :return: User | Bool
        # """
        # users = self.auth_config(username, password)
        # print(users)
        # if (users != False):
        #     for user in users:
        #         if (user.profile == 'admin'):
        #             print("Is admin")
        #         else:
        #             print("is caisseir")
        #             print(f'===!!! {user.email}, ===== {user.profile}')
        # pass

        """
        Cette fonction permet de verifier les critaires l'authantifications
        :param username:
        :param password:
        :return: User | Bool
        """
        users = self.auth_config(username, password)
        print(users)
        if (users != False):
            for user in users:
                print(user.profile)
                profile = Profile_Model.Profile.get(id=user.profile)
                print('==> Profile: ', profile.nom_profile)
                if (profile.nom_profile != 'Admin'):
                    print('==> Profile: ', profile.nom_profile)
                    print("Is admin")
                    page_loader.Loader.acceuile_gerant(self)
                    return True
                else:

                    print('==> Profile: ', profile.nom_profile)
                    print("is caisseir")
                    page_loader.Loader.acceuile_cassier(self)
                    print(f'===!!! {user.email}, ===== {user.profile}')
                    return True
        pass

