import math

# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”.
def imprimir_hola_mundo():
    print('Hola Mundo!')


# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Llamar a esta función desde el programa principal solicitando el nombre al usuario.
def saludar_usuario(nombre):
    return f'Hola {nombre}'


# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
# los datos al usuario y llamar a esta función con los valores ingresados.
def informacion_personal(nombre, apellido, edad, residencia):
    print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.')


# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
# como parámetro y devuelva el área del círculo. calcular_perimetro_
# circulo(radio) que reciba el radio como parámetro y devuelva
# el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
# funciones para mostrar los resultados.
def calcular_area_circulo(radio):
    return round(math.pi * (radio ** 2), 2)


def calcular_perimetro_circulo(radio):
    return round(2 * math.pi * radio, 2)


# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar
# el resultado usando esta función.
def segundos_a_horas(segundos):
    return round(segundos / 3600, 2)


# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.
def tabla_multiplicar(numero):
    print(f"\nTabla del {numero}:")
    for i in range(11):
        print(f'{numero} x {i} = {numero * i}')


# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
# de forma clara.
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = round(a / b, 2)
    else:
        division = "No se puede dividir por cero"
    return suma, resta, multiplicacion, division


# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
# para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
    return round(peso / (altura ** 2), 2)


# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.
def celsius_a_fahrenheit(celsius):
    return round((celsius * 9 / 5) + 32, 2)


# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.
def calcular_promedio(a, b, c):
    return round((a + b + c) / 3, 2)


def main():
    print('Actividad 1: \n')

    imprimir_hola_mundo()

    print('---------------------------------------------')
    print('Actividad 2: \n')
    
    nombre = input('Ingrese su nombre: ')
    print(saludar_usuario(nombre))

    print('---------------------------------------------')
    print('Actividad 3: \n')
    
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    edad = int(input('Ingrese su edad: '))
    residencia = input('Ingrese su residencia: ')
    informacion_personal(nombre, apellido, edad, residencia)

    print('---------------------------------------------')
    print('Actividad 4: \n')
    
    radio = float(input("Ingrese el valor del radio: "))
    print(f'El valor del área del círculo es de: {calcular_area_circulo(radio)}')
    print(f'El valor del perímetro del círculo es de: {calcular_perimetro_circulo(radio)}')

    print('---------------------------------------------')
    print('Actividad 5: \n')

    segundos = int(input('Ingrese la cantidad de segundos: '))
    print(f'La cantidad de {segundos}, corresponde a {segundos_a_horas(segundos)} horas')

    print('---------------------------------------------')
    print('Actividad 6: \n')

    numero = int(input('Ingrese el número para la tabla de multiplicar: '))
    tabla_multiplicar(numero)

    print('---------------------------------------------')
    print('Actividad 7: \n')

    num1 = int(input('Ingrese el primer número: '))
    num2 = int(input('Ingrese el segundo número: '))
    suma, resta, mult, div = operaciones_basicas(num1, num2)
    print(f"Los resultados son: \n Suma: {suma}, Resta: {resta}, Multiplicación: {mult}, División: {div}")

    print('---------------------------------------------')
    print('Actividad 8: \n')
    
    peso = float(input('Ingrese su peso en kg: '))
    altura = float(input('Ingrese su altura en metros: '))
    print(f'Su índice IMC es de: {calcular_imc(peso, altura)}')

    print('---------------------------------------------')
    print('Actividad 9: \n')
    
    celsius = float(input('Ingrese los grados celsius: '))
    print(f'En fahrenheit equivale a: {celsius_a_fahrenheit(celsius)}')

    print('---------------------------------------------')
    print('Actividad 10: \n')
    
    n1 = int(input('Ingrese el valor del primer número: '))
    n2 = int(input('Ingrese el valor del segundo número: '))
    n3 = int(input('Ingrese el valor del tercer número: '))
    print(f'El valor promedio total es de: {calcular_promedio(n1, n2, n3)}')

main()