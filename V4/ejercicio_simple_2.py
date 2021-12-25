# Programa que acepte un número entero n y calcule lo siguiente: n + nn + nnn

numEntero = int(input('Introduzca un numero entero: '))
calculoSolicitado = numEntero + numEntero ** 2 + numEntero ** 3

print(f'El resultado es {calculoSolicitado}')
