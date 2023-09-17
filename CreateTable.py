import sqlite3


def create_table(cursor):
    table_name = 'studenti'

    # Dacă există deja o tabelă cu același nume, se șterge și se creează una nouă
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

    # Se creează tabela cu coloanele specificate
    cursor.execute(f'''
        CREATE TABLE {table_name} (
            id INTEGER PRIMARY KEY,
            nume TEXT,
            prenume TEXT,
            grupa TEXT,
            imagine BLOB,
            sunet BLOB
        )
    ''')

    print("Baza de date creată")
