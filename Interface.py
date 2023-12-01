from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# //////////////////////////////////////////
# Fonction pour ajouter les valeurs dans le tableau
def ajouter_dans_tableau():
    nageur = input1.get()
    nage = input2.get()
    longueur = input3.get()

    tableau.insert("", "end", values = (nageur, nage, longueur))
# //////////////////////////////////////////



# Creation de l'interface
window = Tk()
window.title("Interface Nageur")
window.minsize(1000, 800)

# Creation des 2 onglets
new_window = ttk.Notebook(window)
first_window = ttk.Frame(new_window)
second_window = ttk.Frame(new_window)
new_window.add(first_window, text = "Program")
new_window.add(second_window, text = "Result")

# 1) first_window
question1 = Label(first_window, text = "Qui nage ?")
input1 = Entry(first_window)

question2 = Label(first_window, text = "Quelle nage ?")
input2 = Entry(first_window)

question3 = Label(first_window, text = "Combien de longueur ?")
input3 = Entry(first_window)

question1.pack()
input1.pack()
question2.pack()
input2.pack()
question3.pack()
input3.pack()

# Bouton pour ajouter les valeurs dans le tableau
bouton_tableau = Button(first_window, text = "Ajouter", command = ajouter_dans_tableau)
bouton_tableau.pack()

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
tableau = ttk.Treeview(second_window, columns=("Nageur", "Nage", "Longueur"), show = "headings")
tableau.heading("Nageur", text = "Nageur")
tableau.heading("Nage", text = "Nage")
tableau.heading("Longueur", text = "Longueur")
tableau.place(relx = 0.5, rely = 0.5, anchor = "center")


new_window.pack(expand = 1, fill = "both")

# Boucle de la fenêtre
window.mainloop()