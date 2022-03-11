palabra = input('Ingresa tu palabra: ')

nueva_palabra = ''
primer_caracter = palabra[0]

if primer_caracter.lower() in 'aeiou':
    nueva_palabra = palabra + 'way'
else:
    nueva_palabra = palabra[1:] + primer_caracter + 'ay'

print(nueva_palabra)