def multiplicacion(lista_a, lista_b):
    if len(lista_a) == len(lista_b):
        
        nueva_lista = []
        longitud_lista = len(lista_a)
        
        for pos in range(0, longitud_lista):
            resultado = lista_a[pos] * lista_b[pos]
            nueva_lista.append(resultado)
    
    return nueva_lista


lista_uno = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_dos = [2, 5, 7, 8, 1, 3, 5, 6, 8, 10]

resultado = multiplicacion(lista_uno, lista_dos)
print(resultado)