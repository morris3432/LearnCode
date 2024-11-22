import pymongo

class Conect:
    def __init__(self):
        try:
            self.cliente = pymongo.MongoClient('mongodb://localhost:27017')
            self.db = self.cliente['Learn_code']
            self.collection = self.db['user']
        except Exception as e:
            print(f"Error conectando a MongoDB: {e}")

    # Buscar un usuario por nombre de usuario
    def find_user(self, username):
        return self.collection.find_one({"user_name": username})

    # Insertar un nuevo usuario
    def insert_user(self, username, email, password):
        # Verificar si el correo ya está registrado
        if self.collection.find_one({"email": email}):
            return False

        # Verificar si el nombre de usuario ya existe
        if self.collection.find_one({"user_name": username}):
            return False

        # Insertar usuario en la base de datos
        try:
            self.collection.insert_one(
                {
                    "user_name": username,
                    "email": email,
                    "password": password
                }
            )
            return True
        except Exception as e:
            return False
