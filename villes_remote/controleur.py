#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 14:12:58 2025

@author: frindel
"""

from Graphe import Graphe
from Ville import Ville
from ConvertisseurDeCoordonnees import ConvertisseurDeCoordonnees

import tkinter as tk

import csv

class Controleur:
    def __init__(self, l_canvas, h_canvas, offset_earth, offset_screen):
        # Crée une instance de Graphe avec les informations de canvas
        self.l_canvas = l_canvas
        self.h_canvas = h_canvas
        convert = ConvertisseurDeCoordonnees(l_canvas, h_canvas, offset_earth, offset_screen)
        
        self.fichier = 'extrait_villes.csv'
        self.graphe = Graphe(convert)

        self.parent = None

        self._post_init()

    def _post_init(self):
        self.remplir_graphe()
        
    def lier_vue(self, vue):
        self.vue = vue
    
    def link_parent(self, parent):
        self.parent = parent 

    def remplir_graphe(self):
        """
        Remplit le graphe en lisant les données d'un fichier CSV et en ajoutant les villes correspondantes.
        """

        with open(self.fichier, "r") as file_handler:
            lines = file_handler.readlines()

            for line in lines:
                _i, nom, lat, lon, haut = line.split(", ")
                
                ville = Ville(nom, lat, lon, haut)
                self.graphe.ajouter_ville(ville)
        
        self.graphe.creation_aretes()
        
        
    def obtenir_noms_noeuds(self):
        """
        Retourne les noms de toutes les villes dans le graphe.
        """
        return list(self.graphe.carte.keys())

    def obtenir_coordonnees(self, nom_noeud):
        """
        Retourne les coordonnées cartésiennes d'un nœud dans le graphe.
        """
        return self.graphe.xy_repere_cartesien(nom_noeud)

    def obtenir_prim_aag(self, noeud):
        """
        Récupère la liste des arcs dans l'algorithme de Prim pour un nœud donné.
        """
        return self.graphe.prim(noeud)

    def execute_choix(self, event):
        """
        Exécute une action en fonction du choix sélectionné par l'utilisateur dans l'interface.
        """

        match self.parent.choix.get():
            case "Nombre":
                cnt = self.graphe.nombre_villes()

                self.parent.text_area.insert(tk.INSERT, f"Il y a {cnt} villes")
            case "Distance":
                d_moy = self.graphe.distance_moyenne()

                self.parent.text_area.insert(tk.INSERT, f"La distance moyenne est de {d_moy}") 
            case "Relier":
                try:
                    seuil = int(self.parent.entry.get())
                except ValueError:
                    return 
                
                pairs = self.graphe.noeuds_sup_distance(seuil)

                self.parent.text_are.insert(tk.INSERT, f" -- Seuil: {seuil}, cnt: {len(pairs)}")
                for pair in pairs:
                    self.parent.text_area.insert(tk.INSERT, f"({pair[0]}, {pair[1]}, {pair[2]})\n")
            case "Effacer":
                self.parent.text_area.delete(1.0, tk.END)