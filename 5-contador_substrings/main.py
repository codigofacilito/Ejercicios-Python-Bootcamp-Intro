def contador_substrings(sentence, substring):
    count = 0
    longitud_sentence = len(sentence)
    
    for pos in range(0, longitud_sentence):
        if sentence[pos: pos + len(substring)]  == substring:
            count += 1
    
    return count


print(contador_substrings('Hola mundo', 'o'))
print(contador_substrings('Nuevo ejercicio en PyWombat', 'ue'))
print(contador_substrings('PyWombat Ejercicios de Python con extensión Py', 'Py'))