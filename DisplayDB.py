import sqlite3

connection = sqlite3.connect('studenti.db')  # aici se creează o nouă bază de date numită studenti
cursor = connection.cursor()  # este utilizat pentru a interacționa cu baza de date

def afiseaza_studenti():
    cursor.execute("SELECT * FROM studenti")
    studenti = cursor.fetchall()

    for student in studenti:
        id_student = student[0]
        nume = student[1]
        prenume = student[2]
        grupa = student[3]
        # imagine = student[4]  # Dacă doriți să accesați imaginea într-un mod specific

        print(f"ID: {id_student}")
        print(f"Nume: {nume}")
        print(f"Prenume: {prenume}")
        print(f"Grupa: {grupa}")
        print("---------------------------")
