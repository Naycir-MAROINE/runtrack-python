
abc = "abcdefghijklmnopqrstuvwxyz" * 10

caractère_par_ligne = 1

for i in range(len(abc)):
    print(abc[:i].center(30)) 
    caractère_par_ligne += 2



