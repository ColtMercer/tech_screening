import sqlite3
from faker import Faker

# Initialize Faker
fake = Faker()

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('database/customers.db')
cursor = conn.cursor()

# Create a table for customer data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        name TEXT,
        address TEXT,
        email TEXT,
        phone TEXT,
        company TEXT,
        job TEXT
    )
''')

# Insert fake customer data into the table
def insert_fake_customers(n):
    for _ in range(n):
        name = fake.name()
        address = fake.address()
        email = fake.email()
        phone = fake.phone_number()
        company = fake.company()
        job = fake.job()

        
        cursor.execute('''
            INSERT INTO customers (name, address, email, phone, company, job)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, address, email, phone, company, job))
    
    conn.commit()

# Insert fake customers
insert_fake_customers(10)

# Query and print out the data to verify
cursor.execute('SELECT * FROM customers')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()
