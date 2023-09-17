import face_recognition
from PIL import Image, ImageDraw, ImageFont
import sys
import pandas as pd
import datetime
import pygame
from FaceRecognition import stud_index
from FaceCapture import uk
from LoadDataEncodeFace import student, firstname, lastname, grupa, audiolocation

# Verificăm dacă indexul studentului nu este -1
if stud_index != -1:
    x = str(datetime.datetime.now())
    st = str(student[stud_index])
    f = firstname[stud_index]
    l = lastname[stud_index]
    g = grupa[stud_index]
    ar = "\n" + st + " " + f + " " + l + " " + g + " " + x

    # Scriem informațiile despre student și timestamp-ul în fișierul "prezenta.txt"
    f = open("./prezenta.txt", "a")
    f.write(ar)
    f.close()
    print(ar)

#afișăm imaginea recunoscută cu numele persoanei
pil_uk = Image.fromarray(uk)
draw = ImageDraw.Draw(pil_uk)
fnt = ImageFont.truetype("arial", 40)

if stud_index == -1:
    name = "Față Nerecunoscută"
else:
    name = firstname[stud_index] + " " + lastname[stud_index]
x = 100
y = uk.shape[0] - 100
draw.text((x, y), name, font=fnt, fill=(0, 0, 0))
pil_uk.show()

# anunțăm înregistrarea reușită
audioloc = audiolocation[stud_index]
pygame.init()
if stud_index == -1:
    # my_sound = pygame.mixer.Sound(r"C:\Users\Sebas\Desktop\Licenta\Sunete\registration_failed.mp3")
    my_sound = pygame.mixer.Sound(r"./sounds/registration_failed.mp3")
else:
    my_sound = pygame.mixer.Sound(audioloc)

my_sound.play()
