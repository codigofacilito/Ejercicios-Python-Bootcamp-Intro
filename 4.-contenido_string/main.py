mensaje = "Title: 'Nuevo ejercicio'"
nuevo_mensaje = ''
pass_caracter = False

for caracter in mensaje:
    if caracter is ':':
        pass_caracter = True

    if pass_caracter == True and caracter is not ':':
        nuevo_mensaje = nuevo_mensaje +  caracter

print(nuevo_mensaje)