def moyenne(note1, note2, note3):
    return (note1 + note2 + note3) / 3 
#le float et utiliser sur de nombre avec virgule et le int que les nombre entier
note1 = float(input("Entrez la première note : "))
note2 = float(input("Entrez la deuxième note : "))
note3 = float(input("Entrez la troisième note : "))
# A ne surtout pas oublier pour utiliser un nombre a virgule faut utiliser un point (.) au lieux d'utiliser une virgule(,)
moyenne_etudiant = moyenne(note1, note2, note3)

if 15 <= moyenne_etudiant <= 20:
    print("Très bon élève")
elif 11 <= moyenne_etudiant <= 14:#si tu utilise les nombre de l'intervalle 11 et 14 , il t'affichera si l'eleve a une moyenne ou pas  
    print("Bon élève")
elif 8 <= moyenne_etudiant <= 10:
    print("Élève moyen")
elif 0 <= moyenne_etudiant <= 7:
    print("Élève devant faire des efforts")
else:
    print("La moyenne n'est pas dans la plage attendue.")