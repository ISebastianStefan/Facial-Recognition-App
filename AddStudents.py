import sqlite3

# Conectarea la baza de date
connection = sqlite3.connect('studenti.db')
cursor = connection.cursor()

def adauga_student(id, nume, prenume, grupa, cale_imagine, cale_sunet):
    # Deschiderea fișierului de imagine și citirea conținutului ca șir de octeți
    with open(cale_imagine, 'rb') as image_file:
        imagine_bytes = image_file.read()

    # Deschiderea fișierului de sunet și citirea conținutului ca șir de octeți
    with open(cale_sunet, 'rb') as sound_file:
        sunet_bytes = sound_file.read()

    try:
        # Inserarea datelor în baza de date folosind o interogare SQL parametrizată
        cursor.execute("INSERT INTO studenti (id, nume, prenume, grupa, imagine, sunet) VALUES (?, ?, ?, ?, ?, ?)",
                       (id, nume, prenume, grupa, imagine_bytes, sunet_bytes))
        connection.commit()
    except sqlite3.IntegrityError:
        # Tratarea erorii de integritate în cazul în care există deja un student cu același ID
        print(f"Studentul cu ID-ul {id} există deja. Se ignoră inserarea.")
