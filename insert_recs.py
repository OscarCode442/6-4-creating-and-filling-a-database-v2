import sqlite3
from users import users_data

conn = sqlite3.connect('') # Insert the name of your database inside the quotes
cursor = conn.cursor()

for user in users_data:
    #cursor.execute("INSERT INTO fertilizers (brand, price, type) VALUES (?, ?, ?)", (fertilizer['brand'], fertilizer['price'], fertilizer['type']))
    # create a similar line of code to the above line insert the user INSTEAD of fertilizer data into the users table
    pass
conn.commit()
conn.close()

print("Data inserted successfully.")
# insert_recs.py
import sqlite3
from users import users_data  # Import the user data

# Connect to the database
conn = sqlite3.connect('people.db')
cursor = conn.cursor()

# Insert each record from users_data
for user in users_data:
    # Note: We're mapping 'auth_level' to 'level' and converting password to TEXT
    cursor.execute('''
        INSERT INTO users (username, password, level)
        VALUES (?, ?, ?)
    ''', (user['username'], str(user['password']), user['auth_level']))

# Commit the changes and close the connection
conn.commit()
conn.close()