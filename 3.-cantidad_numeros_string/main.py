contador = 0
mensaje = 'Hola mundo desde Python 3.10'


for caracter in mensaje:
    if caracter.lower() in '1234567890':
        contador = contador + 1


if contador == 1:
    print('El string solo posee un número entero.')
elif contador == 0:
    print('Lo sentimos, el string no posee un número entero.')
else:
    print(f'El String posee {contador} números enteros.')