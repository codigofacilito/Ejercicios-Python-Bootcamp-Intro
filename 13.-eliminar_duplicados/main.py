def simple_list(numeros):
    nueva_lista = []
    
    for numero in numeros:
        if numero not in nueva_lista:
            nueva_lista.append(numero)
    
    return nueva_lista


lista = [1, 2, 3, 2, 10, 20, 10, 2, 3, 4, 5, 2, 2]
respuesta = simple_list(lista)
print(respuesta)