mensaje = 'Hola mundo'
nuevo_mensaje = ''

vocales =  ['a', 'e', 'i', 'o', 'u']

for caracter in mensaje:
    caracter = caracter.lower() 
    
    if caracter in vocales:
        
        if caracter == 'a':
            caracter = '1'
        
        elif caracter == 'e':
            caracter = '2'
        
        elif caracter == 'i':
            caracter = '3'
        
        elif caracter == 'o':
            caracter = '4'
        
        elif caracter == 'u':
            caracter = '5'

    nuevo_mensaje = nuevo_mensaje + caracter

print(nuevo_mensaje)