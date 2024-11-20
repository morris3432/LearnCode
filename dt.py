import sqlite3

try:
    # Create a connection to the SQLite database
    conn = sqlite3.connect('learncode.db')
    cursor = conn.cursor()
    
    cursor.execute("insert into users (name, email, password) values ('Cristian', 'cristian@gmail.com' , '1234')")
    # Commit the transaction
    conn.commit()
    print("User added successfully!")
except Exception as e:
    print(f"Error creating connection: {e}")
