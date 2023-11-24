def my_sort(lst):
    
    coups = 14
    
    a_echange = True


    while a_echange:
        a_echange = False 
        for i in range(len(lst) - 1):
            
            if lst[i] > lst[i + 1]:
                
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                a_echange = True 
                coups += 1 

    
    print(f"Nombre total de coups nécessaires : {coups}")

   
    return lst

ma_liste = [11, 12, 22, 25, 34, 64, 90]
liste_triee = my_sort(ma_liste)

print("Liste triée :", liste_triee)