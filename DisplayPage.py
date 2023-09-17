import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import tkinter.messagebox as mb
import sqlite3
import sys
from LocationDB import get_database_location
from CreateTable import create_table
from AddStudents import adauga_student
from DisplayDB import afiseaza_studenti
import os


class MainPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1100x700')
        self.window.title('Main Page')
        self.window.configure(bg='orange')

        # Create buttons
        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack(pady=20)

        for i in range(1, 5):
            button = tk.Button(self.button_frame, text=str(i), width=10, command=lambda num=i: self.button_click(num))
            button.pack(side='left', padx=10)

        # Create scrolled text for command line output
        self.output_text = scrolledtext.ScrolledText(self.window, height=10)
        self.output_text.pack(padx=20, pady=10, fill='both', expand=True)

        # Create "Next" button
        next_button = tk.Button(self.window, text="Next", command=self.next_page)
        next_button.pack(side='right', padx=20, pady=10)

        # Redirect stdout to both terminal and output_text
        self.console_redirector = ConsoleRedirector(self.output_text)

        # Create database connection and cursor
        self.connection = sqlite3.connect(get_database_location())
        self.cursor = self.connection.cursor()

    def button_click(self, num):
        print(f'Buton {num} apăsat')

        if num == 1:
            database_location = get_database_location()
            if database_location:
                print(f"Locația bazei de date: {database_location}")
            else:
                print("Baza de date nu a fost găsită.")
        elif num == 2:
            create_table(self.cursor)
        elif num == 3:
            # Afișați o fereastră de dialog pentru a permite utilizatorului să aleagă modul de introducere (manual sau automat)
            choice = mb.askquestion("Introducere în baza de date", "Doriți să introduceți manual sau automat în baza de date?")

            if choice == "yes":
                # Introducere manuală în baza de date
                self.introduce_manual()
            else:
                # Introducere automată în baza de date
                self.introduce_automat()
        elif num == 4:
            # Afișați studenții din baza de date
            afiseaza_studenti()

    def introduce_manual(self):
        def adauga_student_manual():
            id = id_entry.get()
            nume = nume_entry.get()
            prenume = prenume_entry.get()
            grupa = grupa_entry.get()
            imagine = imagine_entry.get()
            sunet = sunet_entry.get()

            # Adăugați studentul în baza de date
            adauga_student(id, nume, prenume, grupa, imagine, sunet)

            print("Student adăugat în baza de date")

            # Ștergeți valorile câmpurilor de introducere pentru a permite adăugarea repetată a studenților
            id_entry.delete(0, 'end')
            nume_entry.delete(0, 'end')
            prenume_entry.delete(0, 'end')
            grupa_entry.delete(0, 'end')
            imagine_entry.delete(0, 'end')
            sunet_entry.delete(0, 'end')

        # Creați o fereastră de dialog pentru introducere manuală
        dialog = tk.Toplevel(self.window)
        dialog.title("Introducere manuală")

        id_label = tk.Label(dialog, text="ID:")
        id_label.pack()
        id_entry = tk.Entry(dialog)
        id_entry.pack()

        nume_label = tk.Label(dialog, text="Nume:")
        nume_label.pack()
        nume_entry = tk.Entry(dialog)
        nume_entry.pack()

        prenume_label = tk.Label(dialog, text="Prenume:")
        prenume_label.pack()
        prenume_entry = tk.Entry(dialog)
        prenume_entry.pack()

        grupa_label = tk.Label(dialog, text="Grupă:")
        grupa_label.pack()
        grupa_entry = tk.Entry(dialog)
        grupa_entry.pack()

        imagine_label = tk.Label(dialog, text="Calea către imagine:")
        imagine_label.pack()
        imagine_entry = tk.Entry(dialog)
        imagine_entry.pack()

        sunet_label = tk.Label(dialog, text="Calea către fișierul audio:")
        sunet_label.pack()
        sunet_entry = tk.Entry(dialog)
        sunet_entry.pack()

        # Butonul de adăugare a studentului
        adauga_button = tk.Button(dialog, text="Adaugă", command=adauga_student_manual)
        adauga_button.pack(pady=10)

    def introduce_automat(self):
        # adauga_student(1, "Sebastian", "Ilie", "333A3",
        #                r"C:\Users\Sebas\Desktop\Licenta\Poze-Studenti\sebi1.jpg",
        #                r"C:\Users\Sebas\Desktop\Licenta\Sunete\registration_successful.mp3")
        # adauga_student(2, "Rav", "Voicu", "221B1",
        #                r"C:\Users\Sebas\Desktop\Licenta\Poze-Studenti\voicu1.jpeg",
        #                r"C:\Users\Sebas\Desktop\Licenta\Sunete\registration_successful.mp3")
        # adauga_student(3, "Ionescu", "Mina", "342B3",
        #                r"C:\Users\Sebas\Desktop\Licenta\Poze-Studenti\mina1.jpeg",
        #                r"C:\Users\Sebas\Desktop\Licenta\Sunete\registration_successful.mp3")
        # adauga_student(4, "Ion", "Mihnea", "111A",
        #                r"C:\Users\Sebas\Desktop\Licenta\Poze-Studenti\mihnea1.jpeg",
        #                r"C:\Users\Sebas\Desktop\Licenta\Sunete\registration_successful.mp3")
        # adauga_student(5, "Alex", "George", "223B1",
        #                r"C:\Users\Sebas\Desktop\Licenta\Poze-Studenti\george1.jpeg",
        #                r"C:\Users\Sebas\Desktop\Licenta\Sunete\registration_successful.mp3")

        adauga_student(1, "Sebastian", "Ilie", "333A3",
                       r"./students/sebi1.jpg",
                       r"./sounds/registration_successful.mp3")
        adauga_student(2, "Rav", "Voicu", "221B1",
                       r"./students/voicu1.jpeg",
                       r"./sounds/registration_successful.mp3")
        adauga_student(3, "Ionescu", "Mina", "342B3",
                       r"./students/mina1.jpeg",
                       r"./sounds/registration_successful.mp3")
        adauga_student(4, "Ion", "Mihnea", "111A",
                       r"./students/mihnea1.jpeg",
                       r"./sounds/registration_successful.mp3")
        adauga_student(5, "Alex", "George", "223B1",
                       r"./students/george1.jpeg",
                       r"./sounds/registration_successful.mp3")

        print("Baza de date populată")

    def next_page(self):
        self.window.destroy()  # Închideți fereastra de login

        # Deschideți fereastra MainPage folosind funcția os
        os.system("python FRecognitionPage.py")


class ConsoleRedirector:
    def __init__(self, output_text):
        self.output_text = output_text
        self.original_stdout = sys.stdout
        sys.stdout = self

    def write(self, message):
        self.original_stdout.write(message)
        self.output_text.insert('end', message)
        self.output_text.see('end')

    def flush(self):
        self.original_stdout.flush()


def main():
    window = tk.Tk()
    main_page = MainPage(window)

    # Centrarea ferestrei
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

    window.mainloop()


if __name__ == '__main__':
    main()
