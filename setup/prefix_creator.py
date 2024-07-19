import sqlite3
import ipaddress

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('database/prefixes.db')
cursor = conn.cursor()

# Create a table for prefixes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS prefixes (
        id INTEGER PRIMARY KEY,
        prefix TEXT
    )
''')

# Insert prefixes into the table
def insert_prefixes():
    # Generate 5 child prefixes within the parent prefix range
    child_prefixes = ['10.10.1.0/24', '10.10.2.0/24', '10.10.3.0/24', '10.10.4.0/24', '10.10.5.0/24']

    for prefix in child_prefixes:
        cursor.execute('''
            INSERT INTO prefixes (prefix)
            VALUES (?)
        ''', (prefix,))
    
    conn.commit()

# Insert the prefixes
insert_prefixes()

# Query and print out the data to verify
cursor.execute('SELECT * FROM prefixes')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()
