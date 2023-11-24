def draw_diagonal_carpet(size):
    for i in range(size + 1):
        for j in range(size + 1):
            
            if i == j:
                print('|', end='')
            else:
                print('*', end='')
        print()
draw_diagonal_carpet(10)