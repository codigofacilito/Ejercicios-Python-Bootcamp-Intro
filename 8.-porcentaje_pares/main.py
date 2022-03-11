def pares(numbers):
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count += 1

    return count > len(numbers) / 2

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
respuesta = pares(lista_numeros)

print(respuesta)