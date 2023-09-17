import sqlite3
from LocationDB import get_database_location
from CreateTable import create_table
from AddStudents import adauga_student
from DisplayDB import afiseaza_studenti

# Definirea conexiunii și a cursorului
connection = sqlite3.connect('studenti.db')  # Aici se creează o bază de date nouă numită "studenti"
cursor = connection.cursor()  # Folosit pentru interacțiunea cu baza de date

Menu_Prompt = """-- Baza de date --

Alegeti una din opțiuni:

1) Afișare locație bază de date, dacă există
2) Creare baza de date pentru studenți
3) Adăugare studenți, dacă baza de date există
4) Afișare conținut bază de date
5) Ieșire

"""

def menu():
    while (user_input := input(Menu_Prompt)) != '5':
        if user_input == '1':
            # Obținerea locației bazei de date
            database_location = get_database_location()
            if database_location:
                print(f"Locația bazei de date: {database_location}")
                print("---------------------------")
            else:
                print("Baza de date nu a fost găsită.")
                print("---------------------------")
        elif user_input == '2':
            create_table(cursor)
        elif user_input == '3':
            # Adăugare de studenți (pentru 5 studenți)
            # adauga_student(1, "Sebastian", "Ilie", "333A3", r"C:\Users\Sebas\Desktop\Licenta\Poze-Studenti\sebi1.jpg", r"C:\Users\Sebas\Desktop\Licenta\Sunete\registration_successful.mp3")
            # adauga_student(2, "Rav", "Voicu", "221B1", r"C:\Users\Sebas\Desktop\Licenta\Poze-Studenti\voicu1.jpeg", r"C:\Users\Sebas\Desktop\Licenta\Sunete\registration_successful.mp3")
            # adauga_student(3, "Ionescu", "Mina", "342B3", r"C:\Users\Sebas\Desktop\Licenta\Poze-Studenti\mina1.jpeg", r"C:\Users\Sebas\Desktop\Licenta\Sunete\registration_successful.mp3")
            # adauga_student(4, "Ion", "Mihnea", "111A", r"C:\Users\Sebas\Desktop\Licenta\Poze-Studenti\mihnea1.jpeg", r"C:\Users\Sebas\Desktop\Licenta\Sunete\registration_successful.mp3")
            # adauga_student(5, "Alex", "George", "223B1", r"C:\Users\Sebas\Desktop\Licenta\Poze-Studenti\george1.jpeg", r"C:\Users\Sebas\Desktop\Licenta\Sunete\registration_successful.mp3")
            adauga_student(1, "Sebastian", "Ilie", "333A3", r"./students/sebi1.jpg", r"./sounds/registration_successful.mp3")
            adauga_student(2, "Rav", "Voicu", "221B1", r"./students/voicu1.jpeg", r"./sounds/registration_successful.mp3")
            adauga_student(3, "Ionescu", "Mina", "342B3", r"./students/mina1.jpeg", r"./sounds/registration_successful.mp3")
            adauga_student(4, "Ion", "Mihnea", "111A", r"./students/mihnea1.jpeg", r"./sounds/registration_successful.mp3")
            adauga_student(5, "Alex", "George", "223B1", r"./students/george1.jpeg", r"./sounds/registration_successful.mp3")
            print("Terminat")
        elif user_input == '4':
            afiseaza_studenti()
        else:
            print("Terminat.")
            connection.close()
            exit()

menu()
