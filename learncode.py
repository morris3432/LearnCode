import sqlite3 

class ContactManager:
    def __init__(self) -> None:
        self.connection=sqlite3.connect('learncode.db',check_same_thread=False)
        
        
    def  adds(self, name, email,contrasena):
        query = '''insert into users (name, email, password )
                    values (?,?,?,?)
                '''
        self.connection.execute(query, (name, email, contrasena))
        self.connection.commit()
            
    def get_contact(self,nombre):
        cursor = self.connection.cursor()
        query = 'select * from users where name=?'
        cursor.execute(query, (nombre,))
        contacts=cursor.fetchall()
        return contacts
            
    def close_conect(self):
        self.connection.close()       