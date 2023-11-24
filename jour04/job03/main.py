def ajouter_melon():
    
    fruits = ["pomme", "cerise", "orange"]
       # j'ai ajouter "melon" sur ma liste initial
    
    fruits.append("Melon")

    
    return fruits
       # cela ma permis de creer une nouvelle liste, ou il y aura le melon 

nouvelle_liste = ajouter_melon()
print(nouvelle_liste)
