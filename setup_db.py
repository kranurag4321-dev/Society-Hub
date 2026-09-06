import sqlite3


conn = sqlite3.connect('society.db')
cursor = conn.cursor()


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


try:
    cursor.execute("INSERT INTO users (flat_number, password, role) VALUES ('Admin', 'secret123', 'secretary')")
    cursor.execute("INSERT INTO notices (title, content) VALUES ('Welcome', 'The new Society Hub database is live!')")
    conn.commit()
    print("Database built successfully! 'society.db' created.")
except sqlite3.IntegrityError:
    print("Database already exists and is ready to go.")

conn.close()