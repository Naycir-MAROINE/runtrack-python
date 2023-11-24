def arrondir(nombre):
    partie_entiere = int(nombre)
    partie_decimale = nombre - partie_entiere
    nombre_arrondi = partie_entiere + (1 if partie_decimale >= 0.5 else 0)

    return nombre_arrondi

def tri_bulles(liste):
    n = 0
    for element in liste:
        n += 1

    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]

    return liste

ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

liste_arrondie = [arrondir(nombre) for nombre in ma_liste]

liste_triee = tri_bulles(liste_arrondie)

print("Liste arrondie et triée :", liste_triee)