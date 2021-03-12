import json
from os import stat

class StorageBase:
    
    @staticmethod
    def valid_by(data:str, path:str)->bool:
        if __class__.is_empty(path):
            return False
            
        else:
            json_data = __class__.manageFiles(path, 'r+')

            if data in json_data.keys(): return True
            else: return False
        
    
    @staticmethod
    def manageFiles(file:str, mode:str, **dictItems:dict)->any:
        if mode == 'r+':
            with open(file, 'r+') as fl:
                return json.load(fl)
            
        elif mode == 'w+':
            with open(file, 'w+') as fl:
                json.dump(dictItems, fl, indent=4, separators=(',', ':'))
        
        else:
            return "error con algún atributo"


    @staticmethod
    def is_empty(path:str)->bool:
        stats = stat(path)
        return stats.st_size==0
