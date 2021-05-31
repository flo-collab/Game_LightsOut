from tkinter import *

def switch_color():
	if b["bg"] == "white":
		b["bg"]= "yellow"
	else:
		b["bg"]="white"


# Création d'une fenêtre avec la classe Tk :
fenetre= Tk()
# Ajout d'un titre à la fenêtre principale :
fenetre.title("Lights Out")
# Définition d'un icone :
fenetre.iconbitmap("logo.ico")
# Personnalisation  la couleur de l'arrière-plan de la fenêtre principale :
fenetre.config(bg = "#BECDD5")
# Définition des dimensions par défaut la fenêtre principale :
fenetre.geometry("640x480")

cadre = Frame (fenetre )
cadre.pack()

b = Button (cadre,command=switch_color, text = "bouton1",bg='yellow')
b.pack()





# Affichage de la fenêtre créée :
fenetre.mainloop()