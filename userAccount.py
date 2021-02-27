# sign up -> registrase, suscribirse <-- log up
# sign in -> iniciar sesion <-- login
# clave api watson
# i_h44N7yQtYsA8MDhq-VroQly8ORSs7utN_whcEQkYyk
# url watson
# https://api.us-south.assistant.watson.cloud.ibm.com/instances/0aabb710-5d49-4be2-ab25-40111a7d7fbe

# Regex("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$").is_validate()


# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
from schema import Schema, Regex, SchemaUnexpectedTypeError
import json
import os

class AccountScrew():
    re:list[str] = (r'[A-Z][a-z]+', 
              r'[A-z0-9_-]{3,10}', 
              r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+', 
              r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}')
    
    def __init__(self)->None:
        pass
    
    @classmethod
    def signUp(cls, user:object):
        print(AccountScrew.__exist(user.uName), "function __exist")
        if AccountScrew.__exist(user.uName):
            print('Ya existe una cuenta con ese nombre de usuario')
            res = input("Desea iniciar sesion: ")
            if res == 'si' or 's': cls.signIn(user) 
            else: return "Adios"            
        else:
            if AccountScrew.__auth_logUp(dict(user)):
                cls.__saveUser(dict(user))
                print("cuenta aprobada")
    
    @classmethod
    def __auth_logUp(cls, user:dict):
        print(cls.re[0])
        schema = Schema([{
            'firstName':Regex(cls.re[0]),
            'lastName':Regex(cls.re[0]),
            'userName':Regex(cls.re[1]),
            'email':Regex(cls.re[2]),
            'password':Regex(cls.re[3])
            }])
        try:
            
            return schema.is_valid(user)
        except SchemaUnexpectedTypeError as es:
            print("ERROR", es)
    
    @classmethod
    def signIn(cls, uName:str=None, password:str=None, **user:dict):
        user = dict(user)
        uName = uName or user['userName']
        password = password or user['password']
        if AccountScrew.__exist(uName):
            if AccountScrew.auth_logIn(uName, password):
                print('Cuenta iniciada corectamente', uName)
        elif AccountScrew.__exist(uName)==None:
            if AccountScrew.auth_logIn(uName, password):
                print('Cuenta iniciada corectamente', uName)
                print('Gracias primer usuario')
        
    
    @staticmethod
    def __auth_logIn(uName, password):
        values = {'userName': uName, 'password': password}
        
        schema = Schema([{
            'userName': Regex(AccountScrew.re[1]),
            'password': Regex(AccountScrew.re[3])
            }])
        
        return schema.is_valid(values)
    
    @classmethod
    def __saveUser(cls, user:dict):
        try:
            with open('users.json', 'a+') as jUser:
                json.dump(user, jUser)
        except:
            print('Error')
    
    @staticmethod
    def subscribers(userName):
        all_results = {}
        if AccountScrew.file_is_empty("users.json"): return "empty"
        else:
            with open("users.json", "r") as jUser:
                json_data = json.load(jUser)
                for key, value in json_data.items():
                    if userName in value:
                        all_results[key] = value[2]
                        print(all_results,"function subscribers")
                        return all_results
    
    @staticmethod
    def showUsers():
        with open("users.json", "r+") as jUser:
            json_data = json.load(jUser)
            for jd in json_data:
                print(jd)
    
    @staticmethod
    def file_is_empty(path):
        stat = os.stat(path)
        print("size file json",stat.st_size)
        return stat.st_size==0
    
    @staticmethod
    def __exist (userName):
        if userName in AccountScrew.subscribers(userName): return True
        elif AccountScrew.subscribers(userName) == "empty": return False
        else: return False
        

class User():
    def __init__(self, fName:str, lName:str, uName:str, mail:str, password:str, **userData:dict)->None:
        self.fName = fName
        self.lName = lName
        self.uName = uName
        self.mail = mail
        self.password = password
    
    def __iter__(self):
        yield 'firstName', self.fName
        yield 'lastName', self.lName
        yield 'userName', self.uName
        yield 'email',self.mail
        yield 'password', self.password
        

def main()->None:
    # print("Ingresa tu primer nombre, apellido, alias, mail")
    # inputUser = input('Separados por comas(,): ')
    # dataUser = [iUser for iUser in inputUser.split(',')]
    # password = input("ingresa tu contraseña: ")
    user = User('Jose', 'Sal', 'jnos3', 'jnos3@gmail.com', '&unb$wj2M#k3VZr7DEBH')
    # user = User(dataUser[0],dataUser[1],dataUser[2],dataUser[3], password=password)
    AccountScrew.signUp(user)
    # AccountScrew.signIn(user)
    # AccountScrew.subscribers()
    # AccountScrew.showUsers()

if __name__ == "__main__":
    main()