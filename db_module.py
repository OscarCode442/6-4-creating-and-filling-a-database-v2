import sqlite3
from users import user_data  # Make sure you have a users.py file with user_data = [{...}, {...}]

# CREATE database and table
def create_table():
    """
    Creates the 'users' table in the 'people.db' SQLite database.
    Drops it first to avoid duplication during re-runs.
    """
    conn = sqlite3.connect("people.db")
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS users")  # Clean start

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
    print("Table 'users' created successfully.")

# INSERT multiple rows
def insert_users():
    """
    Inserts all user records from user_data into the 'users' table.
    """
    conn = sqlite3.connect("people.db")
    cursor = conn.cursor()

    for user in user_data:
        username = user.get("username")
        password = str(user.get("password"))  # Ensure TEXT type
        level = user.get("auth_level")

        cursor.execute("""
            INSERT INTO users (username, password, level)
            VALUES (?, ?, ?)
        """, (username, password, level))

    conn.commit()
    conn.close()
    print("User data inserted successfully.")

# INSERT a single row
def insertRow(username, password, level):
    """
    Inserts a single user into the 'users' table.
    """
    conn = sqlite3.connect("people.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (username, password, level)
        VALUES (?, ?, ?)
    """, (username, password, level))

    conn.commit()
    conn.close()
    print(f"Inserted user: {username}")

# READ records (all or by condition)
def getRecord(level=None):
    """
    Retrieves user records. If a level is specified, filters by level.
    """
    conn = sqlite3.connect("people.db")
    cursor = conn.cursor()

    if level is not None:
        cursor.execute("SELECT * FROM users WHERE level = ?", (level,))
    else:
        cursor.execute("SELECT * FROM users")

    records = cursor.fetchall()
    conn.close()

    return records

# UPDATE a record using a dictionary
def updateRecord(update_dict):
    """
    Updates a specific user's field based on primary key.
    Dictionary keys required:
        - db: Database name
        - table: Table name
        - pk_field: Primary key column (e.g., 'user_id')
        - pk_value: Value of the primary key
        - field_to_update: Field/column to change
        - new_value: New value for that field
    """
    db = update_dict["db"]
    table = update_dict["table"]
    pk_field = update_dict["pk_field"]
    pk_value = update_dict["pk_value"]
    field_to_update = update_dict["field_to_update"]
    new_value = update_dict["new_value"]

    query = f"""
        UPDATE {table}
        SET {field_to_update} = ?
        WHERE {pk_field} = ?
    """

    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(query, (new_value, pk_value))
    conn.commit()
    conn.close()
    print(f"Updated {field_to_update} for record with {pk_field} = {pk_value}")

# DELETE a record
def deleteRecord(db, table, pk_field, pk_value):
    """
    Deletes a specific user from the table based on primary key.
    """
    query = f"""
        DELETE FROM {table}
        WHERE {pk_field} = ?
    """

    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(query, (pk_value,))
    conn.commit()
    conn.close()
    print(f"Deleted record with {pk_field} = {pk_value} from {table}")

# RUNNING everything for testing
if __name__ == "__main__":
    # Step 1: Create table
    create_table()

    # Step 2: Insert users from users.py
    insert_users()

    # Step 3: Insert single user manually
    insertRow("john_doe", "pass123", 2)

    # Step 4: Retrieve and display all users
    print("All Users:")
    for row in getRecord():
        print(row)

    # Step 5: Update a user
    update_data = {
        "db": "people.db",
        "table": "users",
        "pk_field": "user_id",
        "pk_value": 1,
        "field_to_update": "level",
        "new_value": 5
    }
    updateRecord(update_data)

    # Step 6: Delete a user
    deleteRecord("people.db", "users", "user_id", 2)
