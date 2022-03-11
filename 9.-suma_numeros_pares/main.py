def suma_pares(numeros):
    total = 0
    
    for numero in numeros:
        if numero % 2 == 0: # Es un numero par?
            total = total + numero
            
    return total


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
resultado = suma_pares(lista)

print(resultado)