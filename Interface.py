from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# //////////////////////////////////////////
# Fonction pour add les valeurs dans le table
def add_tables():
    swimmer = input1.get()
    swim = input2.get()
    lenght = input3.get()

    table.insert("", "end", values = (swimmer, swim, lenght))
# //////////////////////////////////////////



# Creation de l'interface
window = Tk()
window.title("Interface swimmer")
window.minsize(1000, 800)

# Creation des 2 onglets
new_window = ttk.Notebook(window)
first_window = ttk.Frame(new_window)
second_window = ttk.Frame(new_window)
new_window.add(first_window, text = "Program")
new_window.add(second_window, text = "Result")

# 1) first_window
question1 = Label(first_window, text = "Who swim ?")
input1 = Entry(first_window)

question2 = Label(first_window, text = "Which swim ?")
input2 = Entry(first_window)

question3 = Label(first_window, text = "How many lenght ?")
input3 = Entry(first_window)

question1.pack()
input1.pack()
question2.pack()
input2.pack()
question3.pack()
input3.pack()

# Bouton pour ajouter les valeurs dans le table
Button_Tables = Button(first_window, text = "add", command = add_tables)
Button_Tables.pack()

# 2) second_window
# Chargement de l'image de fond
img = Image.open("Projet_Tkinter/IMG.png")
img = img.resize((1000, 800), Image.ADAPTIVE)  # Redimensionnez l'image à la taille de la fenêtre
img = ImageTk.PhotoImage(img)

# Affichage de l'image de fond dans un canevas (Canvas)
canvas = Canvas(second_window, width = 1000, height = 800)
canvas.create_image(0, 0, image = img, anchor = "nw")
canvas.pack()

# Creation du tableau
table = ttk.Treeview(second_window, columns=("swimmer", "swim", "lenght"), show = "headings")
table.heading("swimmer", text = "swimmer")
table.heading("swim", text = "swim")
table.heading("lenght", text = "lenght")
table.place(relx = 0.5, rely = 0.5, anchor = "center")


new_window.pack(expand = 1, fill = "both")

# Boucle de la fenêtre
window.mainloop()