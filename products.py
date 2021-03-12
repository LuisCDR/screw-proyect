from screwbase import StorageBase as sb

class Warehouse():
    path = 'warehouse.json'
    attr = {}
    
    def __init__(self, name:str, price:float, capacity:str, quantity:str, quality:str)->None:
        self.name = name
        self.price = price
        self.capacity = capacity
        self.quantity = quantity
        self.quality = quality
        Warehouse.attr.update(self.__dict__)
        if not self.__valid_by(self.name):
            self.save(Warehouse.attr)
    
    @classmethod
    def save(cls, item:dict)->None:
        item = {item.get("name"):item}
        
        if cls.is_empty():
            cls.editJson(item)
        else:
            dictItems = cls.showJson()
            dictItems.update(item)
            cls.editJson(dictItems)
    
    @staticmethod
    def __valid_by(name:str)->bool:
        return sb.valid_by(name, __class__.path)
    
    @staticmethod
    def editJson(items:dict)->any:
        sb.manageFiles(__class__.path, 'w+', **items)
        
    @staticmethod
    def showJson()->dict:
        return sb.manageFiles(__class__.path, 'r+')
    
    @staticmethod
    def is_empty()->bool:
        return sb.is_empty(__class__.path)


def main():
    print("Ingrese los datos del producto (name, price, capacity, quantity, quality)")
    data = input("(, ): ")
    data = [d for d in data.split(', ')]
    Warehouse(data[0],data[1],data[2],data[3],data[4])


if __name__ == "__main__":
    main()

