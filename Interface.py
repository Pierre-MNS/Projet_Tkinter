from tkinter import *
from tkinter import ttk

# //////////////////////////////////////////
# Function for adding values to the table
def ajouter_dans_tableau():
    nageur = input1.get()
    nage = input2.get()
    longueur = input3.get()

    tableau.insert("", "end", values = (nageur, nage, longueur))
# //////////////////////////////////////////



# Interface creation
window = Tk()
window.title("Interface Nageur")
window.minsize(1000, 800)

# Creating the 2 tabs
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

question3 = Label(first_window, text = "Nombre de longueur ?")
input3 = Entry(first_window)

question1.pack(ipady = 20, ipadx = 50)
input1.pack()
question2.pack(ipady = 20, ipadx = 44)
input2.pack()
question3.pack(ipady = 20, ipadx = 23)
input3.pack()

# Button to add values to the table
bouton_tableau = Button(first_window, text = "Ajouter", command = ajouter_dans_tableau)
bouton_tableau.configure(background = "green")
bouton_tableau.pack(pady=50, ipady = 20, ipadx = 50)

# 2) second_window
# Table creation
tableau = ttk.Treeview(second_window, columns = ("Nageur", "Nage", "Longueur"), show = "headings")
tableau.heading("Nageur", text = "Nageur")
tableau.heading("Nage", text = "Nage")
tableau.heading("Longueur", text = "Longueur")

style = ttk.Style()
style.theme_use("default")
style.configure("Treeview.Heading", background="OrangeRed")  # Changez la couleur selon vos préférences
tableau.column("Nageur", anchor = "center")
tableau.column("Nage", anchor = "center")
tableau.column("Longueur", anchor = "center")

tableau.pack()

new_window.pack(expand = 1, fill = "both")

# Window loop
window.mainloop()