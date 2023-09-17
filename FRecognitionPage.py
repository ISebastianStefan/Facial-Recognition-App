import face_recognition
from PIL import Image, ImageDraw, ImageFont, ImageTk
import pandas as pd
import datetime
import pygame
import tkinter as tk
from FaceRecognition import stud_index
from FaceCapture import uk
from LoadDataEncodeFace import student, firstname, lastname, grupa, audiolocation
import os

# Creați o fereastră tkinter
window = tk.Tk()
window.title("Recunoaștere facială")

window.configure(bg="orange")

# Calculați poziția ferestrei pentru a o centra pe ecran
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width, window_height = 1100, 700
window_x = (screen_width - window_width) // 2
window_y = (screen_height - window_height) // 2

# Setați dimensiunile și poziția ferestrei
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Creați un frame pentru a ține imaginea și butonul
frame = tk.Frame(window)
frame.pack(expand=True, padx=20, pady=20)

# Redimensionați imaginea pentru a se potrivi dimensiunilor ferestrei
image_width, image_height = uk.shape[1], uk.shape[0]
scale_factor = min(window_width / image_width, window_height / image_height)
resized_image = Image.fromarray(uk).resize((int(image_width * scale_factor), int(image_height * scale_factor)))

# Încărcați și afișați imaginea recunoscută
pil_uk = resized_image.convert("RGB")
draw = ImageDraw.Draw(pil_uk)
fnt = ImageFont.truetype("arial", 40)

if stud_index == -1:
    name = "Fața Nerecunoscută"
else:
    name = firstname[stud_index] + " " + lastname[stud_index]
x = 100
y = pil_uk.size[1] - 100
draw.text((x, y), name, font=fnt, fill=(0, 0, 255))
image_label = tk.Label(frame)
image_label.pack(side=tk.LEFT)

# Redați sunetul
audioloc = audiolocation[stud_index]
pygame.init()
if stud_index == -1:
    # my_sound = pygame.mixer.Sound(r"C:\Users\Sebas\Desktop\Licenta\Sunete\registration_failed.mp3")
    my_sound = pygame.mixer.Sound(r"./sounds/registration_failed.mp3")
else:
    my_sound = pygame.mixer.Sound(audioloc)
my_sound.play()

# Actualizați eticheta cu imaginea
photo_image = ImageTk.PhotoImage(pil_uk)
image_label.config(image=photo_image)

if stud_index != -1:
    x = str(datetime.datetime.now())
    st = str(student[stud_index])
    f = firstname[stud_index]
    l = lastname[stud_index]
    g = grupa[stud_index]
    ar = "\n" + st + " " + f + " " + l + " " + g + " " + x
    f = open("./prezenta.txt", "a")
    f.write(ar)
    f.close()

# Funcție pentru gestionarea clicului pe butonul "Next"
def next_page():
    window.destroy()
    os.system("python FinalPage.py")

# Funcție pentru gestionarea clicului pe butonul "Resume"
def resume_page():
    window.destroy()
    os.system("python FRecognitionPage.py")

# Creați un frame pentru a ține butoanele
button_frame = tk.Frame(frame)
button_frame.pack(side=tk.BOTTOM, anchor=tk.SE, pady=20)

next_button = tk.Button(button_frame, text="Next", command=next_page)
next_button.pack(side=tk.RIGHT)

resume_button = tk.Button(button_frame, text="Reia", command=resume_page)
resume_button.pack(side=tk.RIGHT)

# Rulați bucla de evenimente tkinter
window.mainloop()
