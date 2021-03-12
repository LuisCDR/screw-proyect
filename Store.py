from screwbase import StorageBase as sb
from userAccount import User

WAREHOUSE = "warehouse.json"
USERS = "users.json"
MD = ["r+", "w+"]

class Store():
    whread = sb.manageFiles(WAREHOUSE, MD[0])
    usread = sb.manageFiles(USERS, MD[0])
    shop_cart = []
    
    def __init__(self, product:str, userName:str)->None:
        self.product = product
        self.userName = userName
        self.warehouse = Store.whread
        self.users = Store.usread
        self.search(self.product)

    @classmethod
    def search(cls, product:str)->list:
        key_char = []
        
        for key in cls.warehouse:
            low_key = key.lower()
            
            if product in low_key:
                key_char.append(key)
                
        return key_char
    
    def show_search(self):
        selected = {}
        search_prod = self.search(self.product)
        
        for index, v in enumerate(search_prod):
            selected.update({str(index):v})
            print(index, v)
            
        return selected
    
    def select(self, num_select:int)->None:
        selected = self.show_search()
        slc_pro = self.warehouse.get(selected.get(num_select))
        Store.shop_cart.append(slc_pro)

        tmp = {f"{len(k)}  {k} : {v}" for k, v in slc_pro.items()}
        return tmp
    
    @classmethod
    def buy(cls, qty:int=1)->None:
        t_price = 0.0
        for i in enumerate(cls.shop_cart):
            quantity = cls.shop_cart[i].get("quantity")
            price = cls.shop_cart[i].get("price")
            cls.shop_cart[i].update({"quantity":quantity-qty})
            t_price = price*qty
        return cls._buy(t_price)
    
    def _buy(self, price:float)->bool:
        self.warehouse.update(Store.shop_cart[0])
        sb.manageFiles(WAREHOUSE, MD[1], **self.warehouse)
        tmp = self.users.get(self.userName)
        amount = tmp.get("amount")
        tmp.update({"amount":amount-price})
        self.users.update(tmp)
        return True
    
    #-|-#
    
    def registerOrder(self):
        pass
    
    def recommend(self):
        pass
    
    def orderTracking(self):
        pass
    
    def automaticReporting(self):
        pass

def main():
    char = input("buscador de productos por nombre: ")
    user = User.signIn("marcugo1", "unb$wj2M#k3VZr7DEBH4")
    store = Store(char, user[0])
    print(store.show_search())
    slc = int(input("selecciona un porducto : "))
    print(store.select(slc))
    qty = int(input("Ingrese la cantida: "))
    print(Store.buy(qty))
    
    
if __name__ == "__main__":
    main()