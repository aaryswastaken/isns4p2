#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 13:11:32 2025

@author: frindel
"""
import math

class Graphe:
    """
    La classe Graphe permet de représenter un graphe géographique et d'effectuer
    diverses opérations telles que l'ajout de nœuds, le calcul de distances,
    et la recherche d'arbre couvrant de poids minimum (algorithme de Prim).
    """
    def __init__(self, convertisseur):
        self.convertisseur = convertisseur # Convertisseur de coordonnees
        self.carte = {}  # Dictionnaire de villes

    def ajouter_ville(self, ville):
        """
        Ajoute une ville au graphe.

        Args:
            nom (str): Nom de la ville.
            lat (float): Latitude de la ville.
            long (float): Longitude de la ville.
            haut (int): Altitude de la ville.
        """

    def creation_aretes(self):
        """
        Crée les arêtes du graphe sous la forme d'une liste d'adjacence.
        Chaque arête est représentée par une distance entre deux villes.
        """

    def nombre_villes(self):
        """
        Renvoie le nombre de villes dans le graphe.

        Returns:
            int: Nombre de villes.
        """
    
    
    def distance_moyenne(self):
        """
        Calcule la distance moyenne des arêtes du graphe sans utiliser de set ou de sorted.
        """

        
    def noeuds_sup_distance(self, seuil):
        """
        Retourne une liste des paires de villes avec leur distance si cette distance dépasse le seuil.
        :param seuil: Distance minimale pour inclure une arête.
        :return: Liste des tuples (ville_a, ville_b, distance).
        """



    def prim(self, sommet_depart):
        """
        Applique l'algorithme de Prim pour trouver un arbre couvrant de poids minimum.

        Args:
            sommet_depart (str): Nom du nœud de départ.

        Returns:
            list: Liste d'arêtes constituant l'arbre couvrant de poids minimum.
        """
        aag = []
        visites = [sommet_depart]
        
        while len(visites) < len(self.carte):
            dist_min = float('inf')
            arete_min = None

            # Trouve l'arête avec le poids minimum
            for sommet in visites:
                for (voisin, dist) in self.carte[sommet]["voisins"]:
                    if voisin not in visites and dist < dist_min:
                        dist_min = dist
                        arete_min = (sommet, voisin, dist_min)
            
            if arete_min:
                aag.append(arete_min)
                visites.append(arete_min[1])

        return aag
    
    
    def calcul_min_max_xy(self):
        """
        Calcule les coordonnées cartésiennes minimales et maximales des nœuds dans la structure de graphe.
        """
    
    def xy_repere_cartesien(self, nom_noeud):
        """
        Convertit les coordonnées géographiques d'un nœud en coordonnées cartésiennes.
        """
