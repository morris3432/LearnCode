import  pymongo as pm

class conectar:
    def __init__(self):
        try:
            self.client=pm.MongoClient('mongodb://mongo:hIVwexiPYqTkfNszOpSlFwnxRjTXUQdP@junction.proxy.rlwy.net:30961')
            self.db=self.client['Learn_code']
        except Exception as e:
            print('Error connecting')    
    def get_collection(self, collection_name):
        return self.db[collection_name]