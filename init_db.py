#init_db.py
import sqlite3

def init_db():
    # Połączenie z bazą (utworzy plik kontakty.db jeśli nie istnieje)
    conn = sqlite3.connect('kontakty.db')
    cur = conn.cursor()

    # Tworzenie tabeli (jeśli nie istnieje)
    cur.execute('''
    CREATE TABLE IF NOT EXISTS kontakty (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        imie TEXT,
        nazwisko TEXT,
        telefon TEXT,
        email TEXT,
        ulica TEXT,
        numer TEXT,
        kod TEXT,
        miasto TEXT,
        uwagi TEXT
    )
    ''')

    conn.commit()
    conn.close()

# Dodaj to, jeśli chcesz mieć możliwość uruchomienia pliku samodzielnie:
if __name__ == "__main__":
    init_db()