while True:
    try:
        N = int(input(" (N) : "))
        if N > 0:
            break
        else:
            print("Veuillez entrer un entier supérieur à zéro.")
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")


for i in range(1, N+1):
    print(f"\nTable de multiplication de {i} :\n")
    for j in range(1, 11):
        result = i * j
        print(f"{i} x {j} = {result}")