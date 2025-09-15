inventaire = {
    "bananes": 120,
    "mangues": 232,
    "ananas": 400,
    "noix de coco": 165,
    "papayes": 200
}

def afficher_inventaire(inventaire):
    print("Inventaire actuel de Plantation")
    for fruit, quantite in inventaire.items():
        print(f"- {fruit.capitalize()} : {quantite} unités")
        

def recolter(inventaire, fruit, quantite):
    inventaire[fruit] = inventaire.get(fruit, 0) + quantite
    print(f"\n Récolté {quantite} {fruit} supplémentaire !")
    

def vendre(inventaire, fruit, quantite):
    if inventaire.get(fruit, 0) >= quantite:
        inventaire[fruit] -= quantite
        print(f"\n Vendu {quantite} {fruit}")
    else:
        print(f"Pas assez de {fruit} pour vendre {quantite} unités")


if __name__ == "__main__":
    afficher_inventaire(inventaire)
    recolter(inventaire, "bananes", 20)
    vendre(inventaire, "bananes", 10)
    print()
    afficher_inventaire(inventaire)