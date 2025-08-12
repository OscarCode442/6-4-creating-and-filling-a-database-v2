import sqlite3
conn = sqlite3.connect('')# Add the name of your database inside the quotes
cursor = conn.cursor()
### Add SQL to define your table inside the quotes below
cursor.execute('''
                ''')
conn.commit()
conn.close()
# Add the name of your database in the quotes below
print("Database '' created successfully.")
import sqlite3

def create_users_table():
    conn = sqlite3.connect('people.db')
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS users")

    cursor.execute("""
        CREATE TABLE users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            auth_level INTEGER
        )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_users_table()
import sqlite3

def create_database():
    conn = sqlite3.connect('people.db')
    cursor = conn.cursor()
    
    # Drop the table if it exists
    cursor.execute("DROP TABLE IF EXISTS users")
    
    # Create the table
    cursor.execute("""
        CREATE TABLE users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            level INTEGER
        )
    """)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
import sqlite3

def create_database():
    conn = sqlite3.connect('people.db')
    cursor = conn.cursor()
    
    # Drop the table if it exists
    cursor.execute("DROP TABLE IF EXISTS users")
    
    # Create the table
    cursor.execute("""
        CREATE TABLE users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            level INTEGER
        )
    """)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
import sqlite3

def create_database():
    # Connect to the database (will create it if it doesn't exist)
    conn = sqlite3.connect('people.db')
    cursor = conn.cursor()
    
    # Drop the users table if it already exists (for clean run)
    cursor.execute("DROP TABLE IF EXISTS users")
    
    # Create the users table with correct fields and types
    cursor.execute("""
        CREATE TABLE users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            level INTEGER NOT NULL
        )
    """)
    
    # Save and close
    conn.commit()
    conn.close()

# Run the function
if __name__ == "__main__":
    create_database()
import sqlite3

def create_user_table():
    conn = sqlite3.connect("people.db")
    cursor = conn.cursor()

    # Drop the table if it exists to avoid duplicates
    cursor.execute("DROP TABLE IF EXISTS users")

    # Create the table with proper schema
    cursor.execute("""
        CREATE TABLE users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            level INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_user_table()
import sqlite3
from users import user_data  # make sure users.py defines user_data as a list of dictionaries

def insert_users():
    conn = sqlite3.connect("people.db")
    cursor = conn.cursor()

    # Loop through each user dictionary in user_data
    for user in user_data:
        username = user["username"]
        password = str(user["password"])  # Convert password to string if it's an integer
        level = user["auth_level"]  # Map auth_level to level as per DB schema

        cursor.execute("""
            INSERT INTO users (username, password, level)
            VALUES (?, ?, ?)
        """, (username, password, level))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_users()
import sqlite3

def create_table():
    conn = sqlite3.connect("people.db")
    cursor = conn.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS users")

    cursor.execute("""
        CREATE TABLE users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            level INTEGER
        )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
import sqlite3
from users import user_data  # Make sure this is a list of dictionaries

def insert_users():
    # Connect to the 'people.db' database
    conn = sqlite3.connect("people.db")
    cursor = conn.cursor()

    # Loop through each user dictionary in the user_data list
    for user in user_data:
        username = user.get("username")
        password = str(user.get("password"))  # store as TEXT
        level = user.get("auth_level")  # maps to 'level' column in DB

        # Insert each user into the 'users' table
        cursor.execute("""
            INSERT INTO users (username, password, level)
            VALUES (?, ?, ?)
        """, (username, password, level))

    # Commit the insertions and close the connection
    conn.commit()
    conn.close()

# Run the function
if __name__ == "__main__":
    insert_users()