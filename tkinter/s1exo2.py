import tkinter as tk
from tkinter import scrolledtext, messagebox
import csv


def messageBox1(event):
    messagebox.showinfo("Titre de la box", "Ouverture d'une message box")

class Fenetre(tk.Tk):
    def __init__(self):
        super().__init__()

        self.lecture_data("./seq_7_fichier_test.csv")
        _min, _max = self.age_min_max()

        # self.geometry("QxB")
        self.title("Fenetre pour s'echauffer")


        self.topButton = tk.Button(text="Cliquez pour ouvrir une MessageBox")
        self.topButton.bind("<Button-1>", messageBox1)
        self.topButton.pack(side=tk.TOP, fill="x")

        self.quitButton = tk.Button(text="Quitter l'application")
        self.quitButton.pack(side=tk.BOTTOM, fill="x")
        self.quitButton.bind("<Button-1>", self.quitter)

        self.bigText = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=50, height=15)
        self.bigText.insert(tk.INSERT, "******** Zone de texte qui pue *******\n")
        self.bigText.pack(side=tk.LEFT)

        self.ageMoyen = tk.Button(text="Afficher age moyen")
        self.ageMoyen.bind("<Button-1>", self.affiche_age_moyen)
        self.ageMoyen.pack(side=tk.TOP)

        self.valeur_seuil = tk.DoubleVar()
        self.scale = tk.Scale(self, orient="horizontal", from_=_min, to=_max, resolution=1, tickinterval=25, label="Seuil a choisir", variable=self.valeur_seuil)
        self.scale.pack(fill="x")

        self.bouton2 = tk.Button(text="Afficher selon seuil")
        self.bouton2.bind("<Button-1>", self.affiche_selon_seuil)
        self.bouton2.pack(side=tk.TOP, fill="x")

        #radiobutton
        self.select = tk.Label(self, text="Radiobuttons:")
        self.select.pack(anchor=tk.W)

        self.choix = tk.StringVar()
        self.choix.set("Message")

        self.radio1 = tk.Radiobutton(self, text="Message simple", variable=self.choix, value="Message")
        self.radio1.pack(anchor=tk.W)

        self.radio2 = tk.Radiobutton(self, text="Lister les noms", variable=self.choix, value="Liste")
        self.radio2.pack(anchor=tk.W)

        self.radio3 = tk.Radiobutton(self, text="Effacer ScrolledText", variable=self.choix, value="Effacer")
        self.radio3.pack(anchor=tk.W)

        self.button6 = tk.Button(self, text="Choix")
        self.button6.bind("<Button-1>", self.execute_choix)
        self.button6.pack()

    def execute_choix(self, event):
        if self.choix.get() == "Message":
            self.bigText.insert(tk.INSERT, "Je viens de cocher le choix 1\n")
        elif self.choix.get() == "Liste":
            text = ""
            for nom, _ in self.dico.values():
                text += f"{nom}\n"

            self.bigText.insert(tk.INSERT, text)
        elif self.choix.get() == "Effacer":
            self.bigText.delete("1.0", tk.END)

    def quitter(self, event):
        self.destroy()

    def lecture_data(self, nom_fichier):
        """ blabla """
        
        with open(nom_fichier, newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")

            self.dico = {}
            for ligne in reader:
                ident, nom, age = ligne 
                if ident not in self.dico:
                    self.dico[ident] = [nom, int(age)]

    def age_min_max(self):
        _min, _max = 1000, 0
    
        for ident in self.dico:
            age = self.dico[ident][1]

            if age > _max:
                _max = age 

            if age < _min:
                _min = age 

        return _min, _max 

    def affiche_selon_seuil(self, event):
        seuil = self.valeur_seuil.get()

        for nom, age in self.dico.values():
            if age <= seuil:
                texte = f" -> {nom} age de {age} ans\n"
                self.bigText.insert(tk.INSERT, texte)

    def affiche_age_moyen(self, event):
        _sum, count = 0, 0

        for _, age in self.dico.values():
            _sum += age 
            count += 1 

        self.bigText.insert(tk.INSERT, f"L'age moyen est de {_sum/count:.2f} ans\n")



if __name__ == "__main__":
    app = Fenetre()
    app.mainloop()
