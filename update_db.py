import sqlite3

conn = sqlite3.connect('society.db')
cursor = conn.cursor()


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

conn.commit()
conn.close()
print("Database upgraded: Helpdesk Ticketing table successfully added!")