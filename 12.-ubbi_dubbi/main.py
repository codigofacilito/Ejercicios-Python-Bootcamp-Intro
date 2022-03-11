palabra = input('Ingresa tu palabra: ')
nueva_palabra = ''

for caracter in palabra:
    if caracter in 'aeiou':
        caracter =  'ub' + caracter

    nueva_palabra = nueva_palabra + caracter

print(nueva_palabra)