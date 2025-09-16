import json


def ouvrir_inventaire(path="data/inventaire.json"):
    with open(path, "r", encoding="utf-8") as fichier:
        inventaire = json.load(fichier)
    return inventaire


def ouvrir_tresorerie(path="tresorie.txt"):
    with open(path, 'r', encoding='utf-8') as fichier:
        tresorerie = json.load(fichier)
    return tresorerie


def ecrire_inventaire(inventaire, path="data/inventaire.json"):
    with open(path, "w", encoding="utf-8") as fichier:
        json.dump(inventaire, fichier, ensure_ascii=False, indent=4)


def ecrire_tresorerie(tresorerie, path="tresorie.txt"):
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


def vendre(inventaire, fruit, quantite, tresorerie):
    if inventaire.get(fruit, 0) >= quantite:
        inventaire[fruit] -= quantite
        tresorerie += 1 * quantite
        print(f"\nVendu {quantite} {fruit}")
        return inventaire, tresorerie
    else:
        print(f"Pas assez de {fruit} pour vendre {quantite} unités")


if __name__ == "__main__":
    inventaire = ouvrir_inventaire()
    tresorerie = ouvrir_tresorerie()
    
    afficher_tresorerie(tresorerie)
    afficher_inventaire(inventaire)
    
    recolter(inventaire, "bananes", 20)
    vendre(inventaire, "bananes", 10, tresorerie)
    
    ecrire_inventaire(inventaire)
    ecrire_tresorerie(tresorerie)