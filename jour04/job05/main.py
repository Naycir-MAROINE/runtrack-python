# j'ai creer ma liste L
L = [1, 2, 3, 4, 5]

print( L[1])

def remplacer_valeur(index):
    L[index] = L[index-1] + L[index+1]

remplacer_valeur(3)

print( L)

print(L[-1]) # le -1 appel directement le dernier nombre entier de la liste
