import sqlite3

conn = sqlite3.connect('society.db')
cursor = conn.cursor()

try:
    cursor.execute("INSERT INTO users (flat_number, password, role) VALUES ('Flat 101', 'resident123', 'resident')")
    conn.commit()
    print("Resident account 'Flat 101' successfully added to the database!")
except sqlite3.IntegrityError:
    print("Account already exists.")

conn.close()