
def triangle(rows):

    for n in range(1, rows + 1):
        print(' ' *(rows - n), end='')
        print('*' * (n + (n - 1)))


rows = int(input('Ingresa la cantidad de filas: '))
triangle(rows)