def unicos(lista):
    nueva_lista = []
    
    for numero in lista:
        if numero not in nueva_lista:
            nueva_lista.append(numero)

    return nueva_lista

lista = [1, 2, 1, 2, 3, 1, 2, 3]
resultado = unicos(lista)

print(resultado)