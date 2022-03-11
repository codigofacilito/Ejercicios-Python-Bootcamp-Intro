def array_diff(lista_a, lista_b):
    nueva_lista = []
    
    for numero in lista_a:
        if numero not in  lista_b and numero not in nueva_lista:
            nueva_lista.append(numero)
    
    for numero in lista_b:
        if numero not in  lista_a and numero not in nueva_lista:
            nueva_lista.append(numero)
    
    return nueva_lista

lista_a = [1]
lista_b = [1, 2, 3, 2]

respuesta = array_diff(lista_a, lista_b)
print(respuesta)