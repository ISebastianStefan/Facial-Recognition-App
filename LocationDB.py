import sqlite3


def get_database_location():
    connection = sqlite3.connect('studenti.db')
    cursor = connection.cursor()
    cursor.execute("PRAGMA database_list")
    database_info = cursor.fetchall()
    connection.close()

    for db in database_info:
        if db[1] == 'main':  # Verificați doar baza de date principală
            return db[2]

    return None  # Dacă nu se găsește baza de date principală