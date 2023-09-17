from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
import os

# Crearea ferestrei principale
root = Tk()
image = PhotoImage(file='assets\\vector1.png')

# Setarea dimensiunilor și poziționarea ferestrei în centru
height = 430
width = 530
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.overrideredirect(True)

root.config(background="#F5B800")

# Eticheta de bun venit
welcome_label = Label(text="Sistem de recunoaștere facială", bg="#F5B800", font=("Trebuchet Ms", 15, "bold"), fg="#FFFFFF")
welcome_label.place(x=110, y=25)

# Eticheta pentru imagine
b_label = Label(root, image=image, bg="#F5B800")
b_label.place(x=130, y=65)

# Eticheta pentru progresul de încărcare
progress_label = Label(root, text="Se încarcă...", font=("Trebuchet Ms", 13, "bold"), fg="#FFFFFF", bg="#F5B800")
progress_label.place(x=190, y=340)

# Stilul pentru bara de progres
progress = ttk.Style()
progress.theme_use('clam')
progress.configure("red.Horizontal.TProgressbar", background="#ffcb10")

# Crearea barei de progres
progress = Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate', style="red.Horizontal.TProgressbar")
progress.place(x=60, y=370)

def top():
    # Funcția pentru deschiderea paginii de autentificare
    root.withdraw()
    os.system("python LoginPage.py")
    root.destroy()


i = 0

def load():
    global i
    if i <= 10:
        # Actualizarea etichetei și valorii barei de progres
        txt = 'Se încarcă...' + (str(10 * i) + '%*')
        progress_label.config(text=txt)
        progress_label.after(600, load)
        progress['value'] = 10 * i
        i += 1
    else:
        top()

# Apelarea funcției pentru încărcare
load()

# Configurarea ferestrei
root.resizable(False, False)
root.mainloop()
