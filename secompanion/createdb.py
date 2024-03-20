# import mysql.connector

# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='abdul4prof',
# )

# my_cursor = mydb.cursor()
# my_cursor.execute("CREATE DATABASE secompanion")
# my_cursor.execute("SHOW DATABASES")


# for db in my_cursor:
#    print(db)
   
import sqlite3

# Connect to SQLite database (creates a new file if it doesn't exist)
conn = sqlite3.connect('secompanion.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute SQL queries to create a database table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS secompanion (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
""")

# Save changes and close the connection
conn.commit()
conn.close()


# ALTER TABLE query
# alter_query = "ALTER TABLE users MODIFY COLUMN password_hash VARCHAR(255);"

# # Execute ALTER TABLE query
# my_cursor.execute(alter_query)

# # Commit the changes
# mydb.commit()

# # Close the cursor and database connection
# my_cursor.close()
# mydb.close()