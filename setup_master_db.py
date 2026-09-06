import sqlite3


conn = sqlite3.connect('society.db')
cursor = conn.cursor()

print("Initializing Master Database...")


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        flat_number TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS notices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        date_posted TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        flat_number TEXT NOT NULL,
        issue_type TEXT NOT NULL,
        description TEXT NOT NULL,
        status TEXT DEFAULT 'Open',
        date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS visitors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        visitor_name TEXT NOT NULL,
        flat_number TEXT NOT NULL,
        status TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')


accounts = [
    ('Admin', 'secret123', 'secretary'),
    ('Gate Security', 'guard123', 'guard'),
    ('Flat 101', 'resident123', 'resident')
]

for account in accounts:
    try:
        cursor.execute("INSERT INTO users (flat_number, password, role) VALUES (?, ?, ?)", account)
    except sqlite3.IntegrityError:
        pass 

conn.commit()
conn.close()
print("Database fully restored! All tables and default accounts are ready.")