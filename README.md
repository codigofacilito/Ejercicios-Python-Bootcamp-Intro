# Ejercicios Bootcamp

### 1.-Reemplaza vocales por @.

Dado un string de longitud N. Donde N es mayor a 0.

Ejemplo.

```
'Hola mundo'
```

Desarrolla un programa en Python que permite reemplazar todas las vocales del string por arrobas (@).

```
'H@l@ m@nd@'
```

### 2.-Reemplazar vocales por posiciones

Dado un string de longitud N. Donde N es mayor a 0.

Ejemplo.

```
'Hola mundo'
```

Desarrolla un programa en Python que permite reemplazar todas las vocales del String por  sus correspondiente posición en la lista.

Donde las posiciones serán las siguientes.

- a = 1
- e = 2
- i = 3
- o = 4
- u = 5

Salida.

```
'H4l1 m5nd4'
```

### 3.-Cantidad de números en un string.

Dado un String de longitud N. Donde N es mayor a 0.

Ejemplo.

```
Hola mundo desde Python en su versión 3.10
```

Desarrolla un programa en Python que permita conocer la cantidad de números que posee el string.
El programa deberá imprimir en consola, la cantidad de números que posee el string.

Ejemplo.

```
El String posee 3 números enteros.
```

- En caso el string posea un solo número entero el mensaje será el siguiente:

'El string solo posee un número entero.'

- En caso el string no posea algún número entero el mensaje será el siguiente:

'Lo sentimos, el string no posee un número entero.'

- Desarrolla un programa que permita eliminar el Primer y último carácter de un string.

### 4.- Contenido de un string

Dado el siguiente string.

```
Title: 'Nuevo ejercicio'
```

Desarrolla un programa en Python que permita generar un nuevo string con todos los caracteres *después* de los dos puntos (:). El programa deberá imprimir en consola el nuevo string.

Ejemplo.

```
$ python main.py
'Nuevo ejercicio'
```

### 5.- Contador de substrings.

Desarrolla una función que permita conocer la cantidad de veces que existe un substring en un string.

La función debe cumplir con los siguientes requerimientos.

- La función debe tener por nombre _contador\*substrings*.
- La función debe recibir como argumento el string a evaluar y el substring del cual se quiere conocer la cantidad de coincidencias.
- La función debe retornar, mediante un número entero, la cantidad de veces que existe el substring en el string original.

Ejemplos.

```
>>> contador_substrings('Hola mundo', 'o')
2

>>> contador_substrings('Nuevo ejercicio en PyWombat', 'ue')
1

>>> contador_substrings('Contador de caracteres', 'de')
1

>>> contador_substrings('PyWombat Ejercicios de Python con extensión Py', 'Py')
3
```

**Restricción**: No es posible utilizar el método *count* del String. 😵‍💫

### 6.-  Cantidad de dígitos número entero.

Definir una función la cual nos permita conocer cuántos dígitos posee un número.

- La función debe tener por nombre *cantidad_digitos*.
- La función debe poseer el parámetro *numero*.
- La función debe retornar la cantidad de dígitos del parámetro.
- **No** es posible utilizar la función *str*.

Ejemplos

```
>>> cantitdad_digitos(10)
2

>>> cantitdad_digitos(2019)
4

>>> cantitdad_digitos(1234567890)
10
```

### 7.- Fizz Buzz

Escribir un programa que muestre en pantalla los números del 1 al 100, sustituyendo los múltiplos de 3 por la palabra “fizz”, los múltiplos de 5 por “buzz” y los múltiplos de ambos, es decir, los múltiplos de 3 y 5 (o de 15), por la palabra “fizzbuzz”.

### 8.- Porcentaje números pares

Dado un listado de números enteros con Longitud N. Donde N es mayor a 0.

Ejemplo.

```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
```

Define una función que permita conocer si más del 50% de los números son pares.

La función debe cumplir con los siguientes puntos.

- Debe tener por nombre *pares*.
- La función debe recibir, de forma obligatoria, un listado de números enteros.
- La función retorna verdadero, o falso, dependiendo si más de la mitad de los números pares.

Ejemplo.

```
>>> pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
True

>>> pares([2, 2, 2, 2, 3, 4, 2])
True

>>> pares([2, 1, 1, 1, 1, 3, 10])
False
```

### 9.- Suma de números pares

Desarrolla una función en Python que permita sumar números pares-

- La función debe tener por nombre _suma\*pares*.
- La función debe recibir como argumento un litado de números enteros.
- La función debe retornar la suma de todos los números pares positivos del listado.

Ejemplo.

```
>>> suma_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12])
42

>>> suma_pares([2, 2, 2, 2, 3, 4, 2])
14

>>> suma_pares([2, 1, 1, 1, 1, 3, 10])
12
```

9.5 Mover el primer caracter al final de un string.

### 10.- Pig Latin*

*Pig Latin* es un "lenguaje" de broma utilizado como lenguaje secreto en niños de países de habla inglesa.

Sus reglas son simples.

- Si la palabra comienza con una vocal (a, e, i, o, u) se deberá agregar *way* al final de la palabra. Ejemplos: "air" se convierte en
"airway". "eat" se convierte en "eatway"
- Si la palabra comienza con otro carácter, se toma la primera letra y se añade al final, agregando "ay". Ejemplos: "Python" se convierte en "ythonpay". "Demo" se convierte en "emoday"

Con todo esto en mente, desarrolla una función la cual nos permita hacer la traducción entre el Ingles y el Pig Latin.

La función debe cumplir con los siguiente requerimientos.

- La función debe tener por nombre _*pig\latin*.
- La función debe recibir como valor de entrada el string que se desea convertir (Se asume que se encuentra en inglés).
- La función debe retornar la traducción de cada palabra al Pig Latin.

Ejemplo.

```
>>> pig_latin('Python')
ythonpay

>>> pig_latin('School')
choolSay

>>> pig_latin('Hello World')
elloHay orldway
```

### 11.- Advina el número

Define una función llamada _adivina\*numero*. La función debe cumplir con los siguiente requerimientos.

- La función no poseerá parámetro alguno.
- La función elegirá un número aleatorio entre el 1 y el 100.
- La función preguntará al usuario que número se ha elegido.
- Cada vez que el usuario ingrese un número la función imprimirá alguno de los siguientes mensajes (Dependiendo cual sea el caso). Esto para darle una pista al usuario en su siguiente turno.
    - Más alto.
    - Más bajo.
    - Correcto.
- Si el usuario responde incorrectamente en 3 ocasiones seguidas la función finalizará con el mensaje:
*Lo sentimos, el número que estaba pensando es <Número>*.
- Si el usuario responde correctamente la función finalizará en ese momento.

Ejemplo 1.

```
En que número estoy pensando: 10
Más alto.

En que número estoy pensando: 55
Más bajo.

En que número estoy pensando: 30
Más alto.

Lo sentimos, el número que estaba pensando es 41.
```

Ejemplo 2.

```
En que número estoy pensando: 40
Más alto.

En que número estoy pensando: 60
Más alto.

En que número estoy pensando: 61
Correcto
```

## 12.- Ubbi Dubbi

Ubbi Dubbi es un "lenguaje" de broma utilizado como lenguaje secreto en niños de países de habla inglesa.

Su regla es simple.

- Se deben anteponer *ub* a todas las vocales en una palabra. Ejemplo: mi *milk* se convierte en *mubilk*, python se convierte en *pythubon* y *example* se convierte en *ubexubamplube* (En palabras largas puede ser difícil de pronunciar).

Con esto en mente, desarrolla una función que nos permita realizar la traducción del ingles al Ubbi Dubbi. La función debe cumplir con los siguiente requerimientos.

- La función debe tener por nombre _*ubbi\dubbi*.
- La función debe recibir como valor de entrada el string que se desea convertir (Se asume que se encuentra en ingles).
- La función debe retornar la traducción de cada palabra al Ubbi Dubbi.

Ejemplos.

```
>>> ubbi_dubbi('program')
prubogrubam

>>> ubbi_dubbi('demo')
dubemubo

>>> ubbi_dubbi('car')
cubar
```

### 13.-  Eliminar elementos duplicados de una lista.

Dada una lista de números enteros.

Ejemplo:

```
[1, 2, 3, 2, 10, 20, 10, 2, 3, 4, 5, 2, 2]
```

Desarrolla una función que elimine todos los elementos duplicados dentro de la colección.

La función debe cumplir con los siguientes requerimientos.

- La función debe tener por nombre *simple_list*.
- La función debe recibir como argumento una lista de números enteros.
- La función debe retornar una lista con elementos únicos dentro de ella.
- Si dentro de la lista existen 2 o más elementos duplicados, la lista debe retornar únicamente un elemento único.

Ejemplo.

```
lista_a = [1, 2, 3, 2, 10, 20, 10, 2, 3, 4, 5, 2, 2]
>>> simple_list(lista_a)
[1, 2, 3, 10, 20, 4, 5]

lista_b = [110, 20, 45, 50]
>>> simple_list(lista_b)
 [110, 20, 45, 50]

lista_c = [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4]
>>> simple_list(lista_c)
[1, 2, 3, 4]
```

## 14.- Diferencias entre 2 listas.

Define la función _array\*diff*, que recibe como argumento dos listas de números enteros (lista *a* y *b*).

La función debe retornar un nuevo listado con todos aquellos elementos de la lista *a* que no se encuentren en la lista *b* y viceversa.

**Ejemplos:**

```
>>> array_diff([1], [1, 2, 3, 2])
[2, 3]
```

```
>>> array_diff([1, 2, 3, 2], [1])
[2, 3]
```

```
>>> array_diff([1, 4, 3, 5], [1, 2, 3, 2])
[4, 5, 2]
```

### 15.- Validador de contraseñas

Desarrolla un script el cual nos permita validar contraseñas para los usuarios de CódigoFacilito. El script debe cumplir con los siguientes requerimientos.

- Las validaciones se deben hacerse sobre la función _is\_valid\*password*.
- La función debe poseer como parámetro la variable *password*.
- La función debe recibir como argumento (al momento de su llamado) una string en texto plano.
- La función debe retornar un True en caso el parámetro cumpla con las validaciones de una contraseña segura.
- La función debe retornar un False en caso el parámetro **no** cumpla con las validaciones de contraseña segura.

Una contraseña será segura siempre y cuando cumpla con los siguientes puntos.

- Poseer una longitud mínima de 6 caracteres.
- Contar con por lo menos una letra en Mayúsculas.
- Contar con por lo menos una vocal en Mayúsculas.
- Contar con por lo menos tres dígitos.
    - Los dígitos no deben ser consecutivos. Por ejemplo 123 o 456 no son combinaciones válidas. Por el contrario 168 y 414 si lo so
- Poseer por lo menos con un carácter espacial (?*%&@)
- Las contraseñas no pueden comenzar con la palabra _Password_.

Ejemplo.

```
>>> is_valid_password('password')
False

>>> is_valid_password('Password152?')
True

>>> is_valid_password('pywombat')
False

>>> is_valid_password('ExamplePyWombat123?')
False

>>> is_valid_password('ExamplePyWombat135?')
True

```

### 16.-  Multiplicación de dos listados

Dado 2 listas de números enteros.

Ejemplo.

```
lista_uno = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_dos = [2, 5, 7, 8, 1, 3, 5, 6, 8, 10]

```

Desarrolla una función que permita multiplicar cada uno de los elementos de ambos listados.

- La función tendrá por nombre *multiplicacion*.
- La función debe recibir, de forma obligatoria, 2 lista de números enteros.
- La función debe validar que ambas listas poseen exactamente la misma cantidad de elementos.
- Si las listas no cumplen con el punto anterior la función retornará un listado vacío.
- La función retornara una nueva lista con el resultado de multiplicar cada uno de los elementos de ambos listados. El primer elemento de la primera lista con el primer elemento de la segunda lista, el segundo elemento de la primera lista con el segundo elemento de la segunda lista y así sucesivamente.

Ejemplo.

```
>>> multiplicacion(lista_uno, lista_dos)
[2, 10, 21, 32, 5, 18, 35, 48, 72, 100]
```

### 17.- Lista ordenada?

- Define una función llamada *ordenamiento*.
- La función debe recibir como argumento un listado de números enteros con longitud N.
- La función debe retornar True, o False, si el listado se encuentra ordenado de forma ascendente.
- 

Ejemplo.

```
>>> ordenamiento([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
True

>>> ordenamiento([1, 2, 3, 4, 5, 6, 2, 1 ])
False

>>> ordenamiento([9, 20, 32, 45, 60, 89, 90])
True

```

Restricciones: No es posible utilizar el método/función sort que Python nos ofrece.

### 18.-  Valores unicos.

- Define una función llamada *unicos*.
- La función debe recibir como argumento un listado de números enteros de longitud N.
- La función debe retornar un nuevo listado con todos aquellos elementos que *no* se encuentre duplicados.
- 

Ejemplo.

```
>>> unicos([1, 2, 1, 2, 3, 1, 2, 3])
[1, 2, 3]

>>> unicos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

>>> unicos([1, 2, 3, 2, 4, 5, 7, 1, 2])
[1, 2, 3, 4, 5, 7]
```

### 19.- Factorial

Definir una función la cual nos permita conocer el factorial de un número.

- La función debe tener por nombre *factorial*.
- La función debe poseer el parámetro *valor*.
- La función debe retornar el factorial del parámetro.
- La función **no** debe hacer uso de ningún tipo ciclo.

Ejemplos.

```
>>> factorial(3)
6

>>> factorial(5)
120

>>> factorial(15)
1307674368000
```

**20.- Triangulo en consola**

Escribe un programa en Python que imprima en consola un triangulo de asterisco (*) de N filas.

- El programa debe pedir al usuario la cantidad de filas que desea imprimir.

```
Ingresa la cantidad de filas: 10
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
```

```
Ingresa la cantidad de filas: 3
  *
 ***
*****
```