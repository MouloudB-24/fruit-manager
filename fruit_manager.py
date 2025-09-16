import json
import os

DATA_DIR = "data"
PRIX = os.path.join(DATA_DIR, "prix.json")
INVENTAIRE_PATH = os.path.join(DATA_DIR, "inventaire.json")
TRESORERIE_PATH = os.path.join(DATA_DIR, "tresorerie.json")

def ouvrir_prix(path="data/prix.json"):
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(path):
        prix_defaut = {
            "bananes": 2,
            "mangues": 4,
            "ananas": 5,
            "noix de coco": 3,
            "papayes": 6
        }
        with open(path, 'w', encoding='utf-8') as fichier:
            json.dump(prix_defaut, fichier, ensure_ascii=False, indent=4)
    with open(path, 'r', encoding='utf-8') as fichier:
        prix = json.load(fichier)
    return prix


def ouvrir_inventaire(path="data/inventaire.json"):
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(path):
        quantite_defaut = {
            "bananes": 200,
            "mangues": 400,
            "ananas": 500,
            "noix de coco": 300,
            "papayes": 600
        }
        with open(path, 'w', encoding='utf-8') as fichier:
            json.dump(quantite_defaut, fichier, ensure_ascii=False, indent=4)
    with open(path, "r", encoding="utf-8") as fichier:
        inventaire = json.load(fichier)
    return inventaire


def ouvrir_tresorerie(path="data/tresorerie.txt"):
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as fichier:
            json.dump(1000.0, fichier)
    with open(path, 'r', encoding='utf-8') as fichier:
        tresorerie = json.load(fichier)
    return tresorerie


def ecrire_inventaire(inventaire, path="data/inventaire.json"):
    with open(path, "w", encoding="utf-8") as fichier:
        json.dump(inventaire, fichier, ensure_ascii=False, indent=4)


def ecrire_tresorerie(tresorerie, path="data/tresorerie.txt"):
    with open(path, 'w', encoding='utf-8') as fichier:
        json.dump(tresorerie, fichier, ensure_ascii=False, indent=4)


def afficher_inventaire(inventaire):
    print("Inventaire actuel de Plantation")
    for fruit, quantite in inventaire.items():
        print(f"- {fruit.capitalize()} : {quantite} unités")


def afficher_tresorerie(tresorerie):
    print(f"\nTrésorerie actuelle : {tresorerie: .2f} $")
  

def recolter(inventaire, fruit, quantite):
    inventaire[fruit] = inventaire.get(fruit, 0) + quantite
    print(f"\nRécolté {quantite} {fruit} supplémentaire !")
    return inventaire


def vendre(inventaire, fruit, quantite, tresorerie, prix):
    if inventaire.get(fruit, 0) >= quantite:
        inventaire[fruit] -= quantite
        tresorerie += prix.get(fruit, 0) * quantite
        print(f"\nVendu {quantite} {fruit}")
        return inventaire, tresorerie
    else:
        print(f"Pas assez de {fruit} pour vendre {quantite} unités")


if __name__ == "__main__":
    inventaire = ouvrir_inventaire()
    tresorerie = ouvrir_tresorerie()
    prix = ouvrir_prix()
    
    afficher_tresorerie(tresorerie)
    afficher_inventaire(inventaire)
    
    recolter(inventaire, "bananes", 20)
    vendre(inventaire, "bananes", 10, tresorerie, prix)
    
    ecrire_inventaire(inventaire)
    ecrire_tresorerie(tresorerie)