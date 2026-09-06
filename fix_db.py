import sqlite3

conn = sqlite3.connect('society.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS visitors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        visitor_name TEXT NOT NULL,
        flat_number TEXT NOT NULL,
        status TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')


try:
    cursor.execute("INSERT INTO users (flat_number, password, role) VALUES ('Gate Security', 'guard123', 'guard')")
    print("Guard account created!")
except sqlite3.IntegrityError:
    print("Guard account already exists.")

conn.commit()
conn.close()
print("Database fixed: 'visitors' table successfully added!")