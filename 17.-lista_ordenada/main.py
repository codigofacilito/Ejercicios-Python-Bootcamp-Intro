def ordenamiento(numeros):
    pos = 1
    ordenamiento = True

    while pos < len(numeros):
        if numeros[pos] < numeros[pos - 1]:
            ordenamiento = False

        pos += 1

    return ordenamiento


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
respuesta = ordenamiento(lista)

print(respuesta)