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
        
    def lier_vue(self, vue):
        self.vue = vue

    def remplir_graphe(self):
        """
        Remplit le graphe en lisant les données d'un fichier CSV et en ajoutant les villes correspondantes.
        """
        
        
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