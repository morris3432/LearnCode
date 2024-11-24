from models.conexionMongo import conectar

class Uesrs_Models:
    collection=conectar().get_collection('user')
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
        
        try:
            max_id_cursor = self.collection.aggregate([
                {"$group": {"_id": None, "max_id": {"$max": "$_id"}}}
            ])
            max_id_doc = next(max_id_cursor, None)  # Obtén el primer resultado
            max_id = max_id_doc["max_id"] if max_id_doc else 0  # Si no hay resultados, usa 0
            new_id = max_id + 1
        except Exception as e:
            print(f"Error al calcular el nuevo _id: {e}")
            return False


        # Insertar usuario en la base de datos
        try:
            self.collection.insert_one(
                {
                    "_id":new_id,
                    "user_name": username,
                    "email": email,
                    "password": password
                }
            )
            return True
        except Exception as e:
            return False
