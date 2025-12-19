#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ADOUM OUMAR IDRISS
# Matricule :22A692FS

"""
Script de détection de doublons dans une liste
Sans utiliser de collections ou de sets
"""

def detecter_doublons(liste):
    """
    Détecte et retourne les éléments en double d'une liste donnée
   
    Args:
        liste (list): La liste à analyser
       
    Returns:
        list: Liste des éléments qui apparaissent plus d'une fois
    """
    doublons = []  # Liste pour stocker les éléments en double
    elements_vus = []  # Liste pour garder trace des éléments déjà rencontrés
   
    for element in liste:  # Parcourir chaque élément de la liste
        if element in elements_vus:  # Vérifier si l'élément a déjà été vu
            if element not in doublons:  # Si c'est un nouveau doublon
                doublons.append(element)  # Ajouter à la liste des doublons
        else:
            elements_vus.append(element)  # Ajouter aux éléments vus
   
    return doublons  # Retourner la liste des doublons

def afficher_resultats(liste_originale, doublons):
    """
    Affiche les résultats de manière formatée
   
    Args:
        liste_originale (list): La liste originale
        doublons (list): La liste des doublons détectés
    """
    print("\n" + "="*50)  # Ligne de séparation
    print("RÉSULTATS DE L'ANALYSE")  # Titre des résultats
    print("="*50)  # Ligne de séparation
    print(f"Liste originale : {liste_originale}")  # Afficher la liste originale
    print(f"Taille de la liste : {len(liste_originale)} éléments")  # Afficher la taille
   
    if doublons:  # Si des doublons ont été trouvés
        print(f"Doublons détectés : {doublons}")  # Afficher les doublons
        print(f"Nombre de doublons : {len(doublons)}")  # Afficher le nombre de doublons
    else:
        print("Aucun doublon détecté !")  # Message si aucun doublon
    print("="*50 + "\n")  # Ligne de séparation

def exemple_utilisation():
    """
    Montre un exemple d'utilisation de la fonction
    """
    print("\n" + "="*50)  # Ligne de séparation
    print("EXEMPLE D'UTILISATION")  # Titre de l'exemple
    print("="*50)  # Ligne de séparation
   
    # Créer une liste de test avec des doublons
    liste_test = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7]  # Liste avec plusieurs doublons
    print(f"Liste de test : {liste_test}")  # Afficher la liste de test
    #SOULEYMAN MAHAMAT TAHIR 23A169FS

    # Appeler la fonction de détection
    resultat = detecter_doublons(liste_test)  # Détecter les doublons
   # ADOUM OUMAR IDRISS 22A692FS
    # Afficher les résultats
    afficher_resultats(liste_test, resultat)  # Afficher formaté

def menu_interactif():
    """
    Menu interactif pour tester la fonction avec différentes listes
    """
    while True:  # Boucle principale du menu
        print("\n" + "="*50)  # Ligne de séparation
        print("MENU INTERACTIF - DÉTECTION DE DOUBLONS")  # Titre du menu
        print("="*50)  # Ligne de séparation
        print("1. Tester avec une liste prédéfinie")  # Option 1
        print("2. Saisir votre propre liste")  # Option 2
        print("3. Voir un exemple")  # Option 3
        print("4. Quitter")  # Option 4
        print("="*50)  # Ligne de séparation
       
        choix = input("Votre choix (1-4) : ").strip()  # Demander le choix
       
        if choix == "1":  # Option 1 : Liste prédéfinie
            tester_liste_predéfinie()  # Appeler la fonction
        elif choix == "2":  # Option 2 : Liste personnalisée
            tester_liste_personnalisee()  # Appeler la fonction
        elif choix == "3":  # Option 3 : Exemple
            exemple_utilisation()  # Afficher l'exemple
        elif choix == "4":  # Option 4 : Quitter
            print("\nMerci d'avoir utilisé le programme ! Au revoir !")  # Message d'adieu
            break  # Sortir de la boucle
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 4.")  # Message d'erreur

def tester_liste_predéfinie():
    """
    Teste la fonction avec différentes listes prédéfinies
    """
    print("\n" + "="*50)  # Ligne de séparation
    print("LISTES PRÉDÉFINIES")  # Titre de la section
    print("="*50)  # Ligne de séparation
   
    # Définir différentes listes de test
   #HASSAN MBODOU ADAM 23A624FS
    listes_tests = [
        [1, 2, 3, 4, 5],  # Liste sans doublons
        [1, 2, 2, 3, 4, 4, 5],  # Liste avec doublons
        ["a", "b", "a", "c", "b", "d"],  # Liste de chaînes avec doublons
        [1, 1, 1, 1],  # Tous les éléments sont identiques
        [],  # Liste vide
        [10, 20, 30]  # Petite liste sans doublons
    ]
   
    descriptions = [
        "Liste sans doublons",
        "Liste numérique avec doublons",
        "Liste de chaînes avec doublons",
        "Tous éléments identiques",
        "Liste vide",
        "Petite liste sans doublons"
    ]
  
     # AYOUB AHMAT HAMAT 22A406FS
      #ISSA ABAKAR ISSA 23A989FS
    # Tester chaque liste
    for i, (liste, desc) in enumerate(zip(listes_tests, descriptions)):  # Parcourir les listes
        print(f"\nTest {i+1}: {desc}")  # Afficher le numéro du test et description
        doublons = detecter_doublons(liste)  # Détecter les doublons
        afficher_resultats(liste, doublons)  # Afficher les résultats

def tester_liste_personnalisee():
    """
    Permet à l'utilisateur de saisir sa propre liste
    """
    print("\n" + "="*50)  # Ligne de séparation
    print("SAISIE DE LISTE PERSONNALISÉE")  # Titre de la section
    print("="*50)  # Ligne de séparation
   
    # Instructions pour l'utilisateur
    print("Instructions :")  # Titre des instructions
    print("- Entrez les éléments un par un")  # Première instruction
    print("- Appuyez sur Entrée sans rien écrire pour terminer")  # Deuxième instruction
    print("- Les éléments peuvent être des nombres ou des chaînes")  # Troisième instruction
    print("="*50)  # Ligne de séparation
   
    liste_perso = []  # Initialiser la liste personnalisée
    compteur = 1  # Compteur pour l'affichage
   
    while True:  # Boucle de saisie
        element = input(f"Élément {compteur} (Entrée pour terminer) : ").strip()  # Demander l'élément
       
        if element == "":  # Si l'utilisateur appuie sur Entrée sans rien écrire
            break  # Terminer la saisie
       
        # Essayer de convertir en nombre si possible
        try:
            # Essayer de convertir en entier
            element_converted = int(element)  # Conversion en entier
        except ValueError:  # Si ce n'est pas un entier
            try:
                # Essayer de convertir en flottant
                element_converted = float(element)  # Conversion en flottant
            except ValueError:  # Si ce n'est pas un nombre
                element_converted = element  # Garder comme chaîne
       
        liste_perso.append(element_converted)  # Ajouter à la liste
        compteur += 1  # Incrémenter le compteur
    #ADOUM OUMAR IDRISS
   #Matricule:22A692FS
    # Analyser la liste saisie
    if liste_perso:  # Si la liste n'est pas vide
        print("\nListe saisie :", liste_perso)  # Afficher la liste
        doublons = detecter_doublons(liste_perso)  # Détecter les doublons
        afficher_resultats(liste_perso, doublons)  # Afficher les résultats
    else:
        print("\nListe vide saisie. Aucune analyse possible.")  # Message pour liste vide

if __name__ == "__main__":
    """
    Point d'entrée principal du programme
    """
    print("Bienvenue dans le programme de détection de doublons !")  # Message de bienvenue
    print("Ce programme détecte les éléments en double sans utiliser")  # Description
    print("de collections ou de sets (seulement des listes).")  # Suite description
   
    menu_interactif()  # Lancer le menu interactif
