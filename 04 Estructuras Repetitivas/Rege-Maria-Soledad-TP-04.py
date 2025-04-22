# Trabajo Práctico 4: Estructuras repetitivas

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = input("Ingrese un numero")
digitos = 0

# "numero" al ser un input es un string, por lo tanto podemos usarlo así e iterar cada caracter
for i in numero:
    digitos += 1

print(f"Su número tiene {digitos} digitos")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

suma = 0
num1 = int(input("Ingrese su primer numero "))
num2 = int(input("Ingrese su segundo numero "))

for i in range(num1, num2 + 1):
    suma += i

print(f"El resultado es: {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

suma = 0
numero = int(input("Ingrese un numero para sumar o 0 si desea finalizar la suma "))

while numero != 0:
    suma += numero
    numero = int(input("Ingrese otro numero para sumar o 0 si desea finalizar la suma "))

print(f"El resultado es: {suma}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

num_aleatorio = random.randint(0,9)
numero = int(input("Adivine el número: "))
print(num_aleatorio)

while numero != num_aleatorio:
    numero = int(input("Número incorrecto. Adivine el número: "))

print("Correcto. El número es:", numero)

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, -1, -2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario

suma = 0
numero = int(input("Ingrese un numero entero positivo "))

if numero < 0:
    print("No puede ser negativo")
else:
    for i in range(0, numero+1):
        suma += i

    print("El resultado es: ", suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(0, 100):
    num = int(input("Ingrese su numero"))

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    if num > 0:
        positivos += 1
    else:
        negativos += 1

print(" Nros pares: ", pares)
print(" Nros impares: ", impares)
print(" Nros positivos: ", positivos)
print(" Nros negativos: ", negativos)

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

suma = 0
RANGO = 100

for i in range(0, RANGO):
    num = int(input("Ingrese su numero"))
    suma += num

print("La media es: ", suma / RANGO)

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = int(input("Ingresá un número: "))
invertido = 0

while numero > 0:
    # Determinar el último dígito
    digito = numero % 10

    # Invertir el número:
    # La variable "invertido" guarda el número.
    # En caso de que haya otro dígito, "invertido" salta un lugar multiplicándose *10 y se le suma el otro dígito.
    invertido = invertido * 10 + digito

    # Eliminar el último dígito del número original
    numero = numero // 10

print("Número invertido:", invertido)