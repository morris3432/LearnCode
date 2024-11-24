import gridfs.errors
from conexionMongo import conectar
import gridfs
from bson import ObjectId

class Model_ImageUser:
    def __init__(self):
        self.db = conectar()  # Establece la conexión a la base de datos
        self.collection = self.db.get_collection("image_user")  # Obtén la colección de usuarios
        self.fs = gridfs.GridFS(self.db.db)  # Usa la conexión de la base de datos para trabajar con GridFS

    def select_image(self, user_id):
        """Recupera los metadatos de una imagen por user_id"""
        return self.collection.find_one({"user_id": user_id})
    def insert_image(self, user_id, title, file_path):
        """Inserta una imagen en la base de datos"""
        try:
            with open(file_path, 'rb') as image_file:
                # Almacena los datos binarios en GridFS
                file_id = self.fs.put(image_file, filename=title)
                # Almacena los metadatos en la colección
                self.collection.insert_one({
                    "user_id": user_id,
                    "title": title,
                    "file_id": file_id
                })
                print("Imagen insertada correctamente")
        except FileNotFoundError:
            print(f"El archivo {file_path} no se encuentra.")
        except Exception as e:
            print(f"Ocurrió un error al insertar la imagen: {e}")

    def get_image_file(self, file_id):
        """Recupera un archivo de imagen de GridFS por file_id"""
        try:
            file = self.fs.get(ObjectId(file_id))
            return file.read()
        except gridfs.errors:
            print(f"No se encontró el archivo con id {file_id}")
            return None
        except Exception as e:
            print(f"Ocurrió un error al recuperar la imagen: {e}")
            return None
