import random
import smtplib
import sys

import bcrypt

sys.path.append('../../Controler')
from Controler.Data.Models import User_Model


class User_manager(object):
    def __init__(self):
        self.users = User_Model.User()
        self.code_generat = ''

    def create_user(self, user: dict):
        print('Creating user', user)
        if len(user) != 0:
            user_info = self.users.select().where((User_Model.User.email == user['email']))
            if not user_info:
                salt = bcrypt.gensalt()  # Générer un salt aléatoire
                hashed_password = bcrypt.hashpw(user['password'].encode('utf-8'), salt)  # Générer le hachage
                User_Model.User(nom=user['nom'], prenom=user['prenom'], username=user['username'],
                                email=user['email'],
                                tel=user['tel'], password=hashed_password, profile=user['profil_id']).save()
                print("Success")
                return
            else:
                print(user_info)
                print('User existed')
                return False
        pass

    def update_user(self, user: dict):
        if len(user) != 0:
            user_email = self.users.select().where((User_Model.User.email == user['email']))
            if not user_email:
                print('User does not exist')
                return False
            else:
                for i in user_email:
                    id = i.id
                    print(f"==> id: {id}")
                self.users.update(nom=user['nom'], prenom=user['prenom'], username=user['username'],
                                  email=user['email'],
                                  tel=user['tel'], password=user['password'], profile=user['profil_id']).where(
                    User_Model.User.id == id).execute()
                print('Successfully update')
                return
        pass

    def delete_user(self, user: dict):
        user_email = self.users.select().where((User_Model.User.email == (user['email'])))
        for i in user_email:
            id = i.id
            print(f"==> id: {id}")
        self.users.delete().where(
            User_Model.User.id == id).execute()
        print('Successfully delete')
        return
        pass

    def search_user(self, user: dict):
        user_search = self.users.select().where(
            (User_Model.User.email == (user['email'])) | (User_Model.User.email == (user['tel'])))
        for response in user_search:
            return response
        pass

    def modify_user_password(self, email: str):
        code = self.code_generator(email)
        if code == self.code_generator:
            print("Code validate")
            return True
        else:
            print("code incorrect")
            return False
        pass

    def code_generator(self, email: str):
        emails = self.users.select().where(User_Model.User.email == email).execute()
        if not emails:
            print('Invalid email')
            return False
        else:
            for i in range(6):
                self.code_generat += str(random.randint(0, 9))

            print("Mot de passe généré :", self.code_generat)
            self.email_manager(email, self.code_generat)
            return self.code_generat
            # if code == self.code_generator:
            #     print("Code validate")
            #     return True
            # else:
            #     print("code incorrect")
            #     return False

    def email_manager(self, email: str, msg: str):

        # Adresse email et mot de passe de l'expéditeur
        sender_email = "almamyh27@gmail.com"
        sender_password = "ffylglfhejoylzik"
        print('1111')
        # Paramètres du serveur SMTP
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        print('+1111')

        # Connexion au serveur SMTP
        smtp_conn = smtplib.SMTP(smtp_server, smtp_port)
        smtp_conn.starttls()
        print('++1111')

        # Authentification auprès du serveur SMTP
        smtp_conn.login(sender_email, sender_password)
        print('+++1111')

        # Envoi du mail
        smtp_conn.sendmail(sender_email, email, msg)

        # Fermeture de la connexion SMTP
        smtp_conn.quit()
