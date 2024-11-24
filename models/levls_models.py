from models.conexionMongo import conectar

class levels_models:
    collection = conectar().get_collection('levels')
    
    def get_levels(self):
        niveles = self.collection.find()
        levels=[nivel for nivel in niveles]
        return levels
    
    def  insert_level(self, id: int, name: str, description: str, comlpete: bool):
        if self.collection.find_one({"id": id}):
            return False
        
        try:
            self.collection.insert_one(
                {
                    "_id": id,
                    "name": name,
                    "description": description,
                    "complete": comlpete
                }
            )
            return True
        except Exception as e:
            print(f"Error al insertar el nivel: {e}")
            return False

