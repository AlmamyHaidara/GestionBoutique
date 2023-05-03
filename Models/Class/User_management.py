
import random
import smtplib
import sys

import bcrypt

sys.path.append('../../Controler')
from Controler.Data.Models import User_Model


import profile
import random
import smtplib
import sys
import re
import bcrypt
import peewee

sys.path.append('../../Controler')
from Controler.Data.Models import User_Model
from Controler.Data.Models import Profile_Model

class User_manager(object):
    def __init__(self):
        self.users = User_Model.User()
        self.code_generat = ''



    def create_user(self, us:dict):
        print('Creating user', us)
        profile_id:any
        # if us['nom'] == '' or us['nom'] == ' ' or us['prenom'] == '' or us['prenom'] == ' ' or us['username'] == '' or us['username'] == ' ' or us['email'] == ' ' or us['email'] == ' ' or us['tel'] == ' ' or us['tel'] == ' ' or us['tel'] == '' or us['profil'] == ' ' or us['profil'] == ' ' or us['profil'] == '' or us['password'] == '' or us['password'] == ' ' :
        for user in us:
            if ((us[user] == '') or (us[user] ==' ')):
                print('Veuiller remplire correctement les differente champs', user)
                break

        if self.regex_mail(us['email']):
            try:
                user_email = self.users.get(email = us['email'] , username = us['username'])
            except User_Model.User.DoesNotExist:
                print(f'==========>>>>>> {us["profil"]}')
                profile_id = Profile_Model.Profile.get(nom_profile = us['profil'])
                print('Cette utilisateur nexiste pas dans la base de donner')
                print(f'==========>>>>>> {profile_id}')
                print('================Password: ', us['password'])
                if self.regex_password(us['password']):
                    salt = bcrypt.gensalt()  # Générer un salt aléatoire
                    hashed_password = bcrypt.hashpw(us['password'].encode('utf-8'), salt)  # Générer le hachage
                    self.users.create(nom=us['nom'], prenom=us['prenom'],username = us['username'], email=us['email'], tel=us['tel'],
                                  password=hashed_password, profile=profile_id)
                    print("Success")
                    pass
                else:
                    print("Warning password invalid")
                    return False
            else:
                print('User existed')
                return
        else:
            print('User email is invalid')
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



    def search_user(self, user: dict):
        user_search = self.users.select().where(
            (User_Model.User.email == (user['email'])) | (User_Model.User.email == (user['tel'])))
        for response in user_search:
            return response
        pass

    # def modify_user_password(self, email: str):
    #     code = self.code_generator(email)
    #     if code == self.code_generator:
    #         print("Code validate")
    #         return True
    #     else:
    #         print("code incorrect")
    #         return False
    #     pass
    #
    #     if self.regex_mail(user['email']):
    #             user_email = User_Model.User().select().where((User_Model.User.email == user['email']))
    #             if not user_email:
    #                 print('User does not exist')
    #                 return False
    #             else:
    #                 profil = Profile_Model.Profile().get(nom_profile = user['profil'])
    #                 print('Profile: ', profil)
    #                 for i in user_email:
    #                     id = i.id
    #                     print(f"==> id: {id}")
    #                 User_Model.User().update(nom=user['nom'], prenom=user['prenom'], username=user['username'],
    #                                   email=user['email'],
    #                                   tel=user['tel'], profile = profil).where(
    #                     User_Model.User.id == id).execute()
    #                 print('Successfully update')
    #                 return
    #     else:
    #         return False
    #     pass

    def delete_user(self, email: str):
        user_email = self.users.get(email = email)
        print('Deleting user: ', user_email.email)
        print('Deleting user: ', user_email.id)
        self.users.delete().where(User_Model.User.id == user_email.id).execute()
        print('Successfully delete')
        return True

        
        pass


    def modify_user_password(self, email: str):
        if self.regex_mail(email):

            code = self.code_generator(email)
            if code == self.code_generator:
                print("Code validate")
                return True
            else:
                print("code incorrect")
                return False
            pass
        else:
            return False
    def regex_mail(self, email: str):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        # Vérifier si l'adresse e-mail correspond à l'expression régulière
        if re.match(pattern, email):
            return True
        else:
            return False
        pass

    def regex_password(self, password: str):
        # Définir l'expression régulière pour un mot de passe valide
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&.])[A-Za-z\d@$!%*?&.]{8,}$'
        # 'Bamakomali2023@'
        print('================Password: ', password)

        # Vérifier si le mot de passe correspond à l'expression régulière
        if re.match(pattern, password):
            return True
        else:
            return False
    def All_user_list(self):
        data=[]
        profil = ""
        users = self.users.select().execute()
        for user in users:
            profil = Profile_Model.Profile.select().where(Profile_Model.Profile.id == user.profile_id)
            data.append(user.id)
            data.append(user.nom)
            data.append(user.prenom)
            data.append(user.username)
            data.append(user.email)
            data.append(user.tel)
            data.append( profil[0].nom_profile)
        print("DATA: ",data)
        chunk_size = 7
        # Liste pour stocker les sous-tableaux
        chunks = []
        # Parcourir les données et extraire les sous-tableaux
        for i in range(0, len(data), chunk_size):
            chunks.append(data[i:i + chunk_size])
        # Afficher les sous-tableaux
        print(chunks)
        return chunks

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
