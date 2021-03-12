# sign up -> registrase, suscribirse <-- log up
# sign in -> iniciar sesion <-- login
# clave api watson
# i_h44N7yQtYsA8MDhq-VroQly8ORSs7utN_whcEQkYyk
# url watson
# https://api.us-south.assistant.watson.cloud.ibm.com/instances/0aabb710-5d49-4be2-ab25-40111a7d7fbe



# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
from schema import Schema, Regex
from screwbase import StorageBase as sb


class User():
    re:tuple = (r"^[A-Z][a-z]+$", 
              r"^[A-z0-9_-]{3,10}$", 
              r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
              r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")
    
    path = "users.json"
    attr = {}
    
    def __init__(self, fName:str, lName:str, uName:str, amount:float, email:str ,password:str, **userData:dict)->None:
        self.firstName = fName
        self.lastName = lName
        self.userName = uName
        self.amount = amount
        self.email = email
        self.password = password
        User.attr.update(self.__dict__)
    
    @classmethod
    def signUp(cls):
        if cls.is_sub(cls.attr.get("userName")):
            print('Ya existe una cuenta con ese nombre de usuario')
            res = input("Desea iniciar sesion: ")
            return {
                "si": lambda : cls.signIn(cls.attr.get("userName"), cls.attr.get("password")),
                "no": lambda: print("Adios")
                }.get(res, lambda: None)()
            
        else:
            user = cls.attr
            if cls.__auth_logUp(user):
                cls.__saveUser(user)
                print("cuenta aprobada")

    @classmethod
    def __auth_logUp(cls, user:dict):
        schema = Schema({
            'firstName':Regex(cls.re[0]),
            'lastName':Regex(cls.re[0]),
            'userName':Regex(cls.re[1]),
            'amount': float,
            'email': Regex(cls.re[2]),
            'password':Regex(cls.re[3])
            })
        return schema.is_valid(user)
    
    @classmethod
    def signIn(cls, userName:str, password:str):
        if cls.is_sub(userName):
            if cls.__auth_logIn(userName, password):
                return (userName, password)
    
    @staticmethod
    def __auth_logIn(userName, password):
        values = {'userName': userName, 'password': password}
        
        schema = Schema({
            'userName': Regex(__class__.re[1]),
            'password': Regex(__class__.re[3])
            })
        
        return schema.is_valid(values)
    
    
    
    @classmethod
    def __saveUser(cls, user:dict):
        user = {user.get('userName'):user}
        
        if cls.is_empty():
            cls.editUsers(user)
            
        else:
            dictUsers = cls.showUsers()
            dictUsers.update(user)

            cls.editUsers(dictUsers)
            
        
    @staticmethod
    def is_sub(userName):
        return sb.valid_by(userName, __class__.path)
    
    @staticmethod
    def editUsers(user):
        return sb.manageFiles(__class__.path, 'w+', **user)
    
    @staticmethod
    def showUsers():
        return sb.manageFiles(__class__.path, 'r+')
    
    @staticmethod
    def is_empty():
        return sb.is_empty(__class__.path)
        

def main()->None:
    # print("Ingresa tu primer nombre, apellido, alias, amount, correo")
    # User("Lucia", "Juro", "luciaj1", 1000.50, "luiciaj1@gmail.com","unb$wj2M#k3VZr7DEBH4")
    # User(dataUser[0],dataUser[1],dataUser[2],dataUser[3], dataUser[4], password=password)
    # User("Angel", "Baca", "angleb2", 2200.5,"angelb2@gmail.com", "unb$wj2M#k3VZr7DEBH4")
    # User("Marcus", "Hugo", "marcugo1", 4200.5,"marcugo1@gmail.com", "unb$wj2M#k3VZr7DEBH4")
    # User("Abril", "Cacerez", "abrilc2", 1200.5,"abrilc2@gmail.com", "unb$wj2M#k3VZr7DEBH4")
    User("Lazaro", "Gonzales", "lazar56", 100.0, "lazar56@gmail.com", "unb$wj2M#k3VZr7DEBH4").signUp()
    

if __name__ == "__main__":
    main()
