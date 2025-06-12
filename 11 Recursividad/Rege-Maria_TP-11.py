# Fc extra para validar que el número ingresado sea positivo
def pedir_numero(mensaje=''):
    while True:
        num_ingresado = int(input(f'Ingrese un número {mensaje} : '))

        if num_ingresado >= 0:
            return num_ingresado
        else:
            print('Ingrese un número mayor a 0')


# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print('---------------------------------------------')
print('Actividad 1: \n')

num = pedir_numero('para calcular su factorial')
print(f'El factorial del número {num} es: {factorial(num)}')

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique. 0 1 1 2 3 5 8 13

def fibonacci_posicion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_posicion(n - 1) + fibonacci_posicion(n - 2)

def fibonacci_serie(num):
    serie = []
    for i in range(num+1):
        serie.append(fibonacci_posicion(i))
    return serie

print('---------------------------------------------')
print('Actividad 2: \n')

num = pedir_numero('para calcular la serie de Fibonacci que existe en esa posición')
print(f'En la posición {num} de la serie se encuentra el número: {fibonacci_posicion(num)}')
print(f'La serie completa hasta el número elegido es: {fibonacci_serie(num)}')

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un
# algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

print('---------------------------------------------')
print('Actividad 3: \n')

base = int(input('Ingrese un número para la base de la potencia: '))
exponente = int(input('Ingrese un número para el exponente de la potencia: '))
print(f'El valor obtenido de la base {base} y su exponente {exponente} es: {potencia(base, exponente)}')

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto
def decimal_a_binario(num : int) -> str:
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        return decimal_a_binario(num // 2) + str(num % 2)

print('---------------------------------------------')
print('Actividad 4: \n')

num = pedir_numero('para pasar de decimal a binario')
print(f'El número {num} en binario es: {decimal_a_binario(num)}')

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
#lo es.

def es_palindromo(palabra):
    if len(palabra) <= 0:
        return True

    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False


print('---------------------------------------------')
print('Actividad 5: \n')

palabra = input('Ingrese una palabra para saber si es palíndroma: ')

if es_palindromo(palabra):
    print(f'La palabra {palabra} es palindroma')
else:
    print(f'La palabra {palabra} NO es palindroma')

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(num):
    if num // 10 == 0:
        return num
    else:
        return num % 10 + suma_digitos(num // 10)

print('---------------------------------------------')
print('Actividad 6: \n')

num = pedir_numero('para calcular la suma de los digitos')
print(f'La suma de los dígitos del número {num} es: {suma_digitos(num)}')

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
# Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

print('---------------------------------------------')
print('Actividad 7: \n')

num = pedir_numero('para determinar la base de la pirámide')
print(f'El número de bloques necesarios es de {contar_bloques(num)}')

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.

def contar_digito(num, digito):
    cuenta = 0

    # Caso base si el nro es 0, pero si el digito tb es 0, devuelve 1 (lo cuenta)
    if num == 0:
        return 1 if digito == 0 else 0

    ultimo_digito = num % 10

    if ultimo_digito == digito:
        cuenta = 1

    return cuenta + contar_digito(num // 10, digito)

print('---------------------------------------------')
print('Actividad 8: \n')

num = pedir_numero('de varias cifras')
digito = pedir_numero('para que sea el digito a contar')
print(f'El número {num} tiene {contar_digito(num, digito)} veces el digito {digito}')