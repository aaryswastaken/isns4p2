#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 14:05:36 2025

@author: frindel
"""

import tkinter as tk
from tkinter import scrolledtext

class VuePrincipale(tk.Tk):
    def __init__(self, controleur):
        super().__init__()
        self.title("Fenêtre principale")
        self.resizable(height=False, width=False)

        # Référence au contrôleur
        self.controleur = controleur

        # Widgets
        self.creer_widgets()

    def creer_widgets(self):
        # Zone de texte
        self.text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=50, height=20, font=("Times New Roman", 14))
        self.text_area.grid(row=0, column=0, columnspan=2)
        self.text_area.insert(tk.INSERT, "Quelques statistiques sur les villes :" + '\n')
        self.text_area.insert(tk.INSERT, "-------------------------------------------" + '\n')

        # RadioButtons
        self.choix = tk.StringVar()
        self.choix.set("Nombre")

        tk.Label(self, text="\nChoix de descripteurs :", font='Helvetica 10 bold').grid(row=1, column=0)
        tk.Radiobutton(self, text="Nombre de villes", variable=self.choix, value="Nombre").grid(row=1, column=1, sticky='w')
        tk.Radiobutton(self, text="Distance moyenne (km)", variable=self.choix, value="Distance").grid(row=2, column=1, sticky='w')
        tk.Radiobutton(self, text="Villes reliées selon seuil (km)", variable=self.choix, value="Relier").grid(row=3, column=1, sticky='w')
        tk.Radiobutton(self, text="Effacer Scrolltext", variable=self.choix, value="Effacer").grid(row=5, column=1, sticky='w')

        # Zone de saisie
        self.entry = tk.Entry(self)
        self.entry.insert(0, "Valeur du seuil")
        self.entry.grid(row=4, column=1)

        # Bouton de choix
        bouton_choix = tk.Button(self, text="Choix")
        bouton_choix.bind('<Button-1>', self.controleur.execute_choix)
        bouton_choix.grid(row=3, column=0)

        # Fenêtre graphique
        tk.Label(self, text="\nFenêtre graphique ", font='Helvetica 9 bold').grid(row=6, column=0, columnspan=2)
        bouton_graphe = tk.Button(self, text="Graphe des villes", height=1, width=19)
        bouton_graphe.grid(row=7, column=0, columnspan=2)
