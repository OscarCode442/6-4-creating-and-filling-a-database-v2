import sqlite3

def showRecords():
    title = "All Records From the Table Users: "
    conn = sqlite3.connect('people.db')
    cursor = conn.cursor()
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(title)
    for row in rows:
        print(f"{row[0]} {row[1]} {row[2]} {row[3]}")
    conn.close()

showRecords()
# show_all_records.py
import sqlite3

# Connect to the database
conn = sqlite3.connect('people.db')
cursor = conn.cursor()

# Retrieve all records from the users table
cursor.execute("SELECT * FROM users")
records = cursor.fetchall()

# Print each record
for record in records:
    print(record)

# Close the connection
conn.close()