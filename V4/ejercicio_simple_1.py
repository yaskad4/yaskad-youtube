# Programa que acepte como dato el radio de un círculo y nos calculé el área.
import math
radioCirculo = float(input('Introduzca el valor del radio: '))

if radioCirculo < 0:
	print('El radio introducido es incorrecto')
else:
	areaCirculo = math.pi * radioCirculo ** 2
	
print('El area del circulo de radio es: ', areaCirculo)