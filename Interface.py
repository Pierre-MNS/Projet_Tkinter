from tkinter import *
from tkinter import ttk
# Librairie PIL pour importer des images
from PIL import Image, ImageTk

# Creation de l'interface
window = Tk()
window.title("Interface Nageur")
window.minsize(1000, 800)

# Creation des 2 onglets
new_window = ttk.Notebook(window)
first_window = ttk.Frame(new_window)
second_window = ttk.Frame(new_window)
new_window.add(first_window, text="Program")
new_window.add(second_window, text="Result")

# Utilisation de la Class "Canvas" pour ajouter un ecran dans l'onglet n°2
canvas_second_window = Canvas(second_window)
canvas_second_window.pack(fill = "both", expand = True)

image_path = "Projet_Tkinter/IMG.png"
background_image_pil = Image.open(image_path)
background_image = ImageTk.PhotoImage(background_image_pil)

canvas_second_window.create_image(500, 400, image = background_image)

new_window.pack(expand = 1, fill = "both")


# Boucle de la fenêtre
window.mainloop()