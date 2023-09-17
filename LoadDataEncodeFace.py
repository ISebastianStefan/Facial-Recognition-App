import sqlite3
import face_recognition
import pandas as pd

# Citirea datelor din fișierul CSV
ia = pd.read_csv('./studenti_audio_img.csv')
photolocation = ia["imagine"].tolist()
audiolocation = ia["sunet"].tolist()

# Conectarea la baza de date SQLite
connection = sqlite3.connect('studenti.db')
cursor = connection.cursor()

# Executarea unei interogări pentru a obține datele studenților
cursor.execute("SELECT * FROM studenti")
results = cursor.fetchall()

# Definirea listelor goale pentru a stoca datele
student = []
firstname = []
lastname = []
grupa = []
student_encod = []
stud = []

# Iterarea prin rezultatele interogării și extragerea datelor
for row in results:
    student.append(row[0])
    firstname.append(row[1])
    lastname.append(row[2])
    grupa.append(row[3])
    # photolocation.append(row[4])
    # audiolocation.append(row[5])
    # print(student)

# Încărcarea imaginilor și codificarea fețelor
n = len(student)
for i in range(n):
    stud.append(face_recognition.load_image_file(photolocation[i]))
    student_encod.append(face_recognition.face_encodings(stud[i])[0])
