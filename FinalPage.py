import tkinter as tk
from tkinter import messagebox
# Variabila cu mesajul importat din alt modul
from ForwardToMail import a

def exit_application():
    root.destroy()

# Crearea ferestrei principale
root = tk.Tk()
root.title("Final Page - Email")
root.geometry("1100x700")

root.configure(bg="orange")

# Actualizarea ferestrei pentru a asigura calcule corecte ale dimensiunilor
root.update_idletasks()

# Determinarea dimensiunilor ecranului
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Determinarea coordonatelor pentru centru
x = (screen_width // 2) - (root.winfo_width() // 2)
y = (screen_height // 2) - (root.winfo_height() // 2)

# Setarea poziției ferestrei
root.geometry(f"+{x}+{y}")

# Frame pentru centrat imaginea și butonul
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Eticheta cu mesajul
label = tk.Label(frame, text=a, font=("Arial", 24))
label.pack(pady=20)

# Butonul de ieșire
exit_button = tk.Button(root, text="Exit", command=exit_application, font=("Arial", 16), height=2, width=10)
exit_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# Rularea buclei principale
root.mainloop()
