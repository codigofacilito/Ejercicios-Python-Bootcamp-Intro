from random import randint

def adivina_numero(): # parámetros = Variables dentro de los ( )
    numero_secreto = randint(0, 5)
    
    for itento in range(0, 5):
        numero_pensando = input('En qué número estoy pensando? ') # String
        numero_pensando = int(numero_pensando)
        
        if numero_pensando == numero_secreto:
            print('Felicidades, el número es correcto.')
            break
        else:
            if numero_pensando < numero_secreto:
                print('Más alto.')
            else:
                print('Más bajo.')
    
    print('Gracias por jugar.')
    
adivina_numero()