mensaje = 'Hola mundo'
nuevo_mensaje = ''

vocales =  ['a', 'e', 'i', 'o', 'u']

for caracter in mensaje:
    if caracter.lower() in vocales:
        caracter = '@'

    nuevo_mensaje = nuevo_mensaje + caracter

print(nuevo_mensaje)