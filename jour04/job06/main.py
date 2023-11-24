
def echanger_premiere_et_derniere(liste):
    if len(liste) >= 2:
        print("Liste avant l'échange :", liste)

        liste[0], liste[-1] = liste[-1], liste[0]

        print("Liste après l'échange :", liste)
    else:
        print("La liste est vide ou ne contient pas assez d'éléments pour effectuer l'échange.") # on a utiliser la premiere liste pour effectuer l'echange de la 2em liste

ma_liste = [1, 2, 3, 4, 5]
echanger_premiere_et_derniere(ma_liste)