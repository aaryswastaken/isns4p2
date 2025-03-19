import tkinter as tk


class Fenetre(tk.Tk):
    def __init__(self):
        super().__init__()

        # self.geometry("QxB")
        self.title("Fenetre pour s'echauffer")


        self.topButton = tk.Button(text="Bouton du haut")
        self.topButton.pack(side=tk.TOP)

        self.quitButton = tk.Button(text="Quitter")
        self.quitButton.pack(side=tk.BOTTOM)
        self.quitButton.bind("<Button-1>", self.quitter)

        self.bigLabel = tk.Label(text="Un gros label de 50x15 a gauche", width=50, height=15, bg="lightblue")
        self.bigLabel.pack(side=tk.LEFT)

        self.unLabel = tk.Label(text="Un label")
        self.unLabel.pack(side=tk.TOP)

        self.bouton1 = tk.Button(text="bouton de droite 1")
        self.bouton1.pack(side=tk.TOP, fill="x")

        self.bouton2 = tk.Button(text="bouton de droite 2")
        self.bouton2.pack(side=tk.TOP, fill="x")

    def quitter(self, event):
        self.destroy()



if __name__ == "__main__":
    app = Fenetre()
    app.mainloop()
