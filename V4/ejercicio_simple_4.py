# Programa que sume dos horas a la hora actual y la muestre en pantalla

from datetime import datetime
horaActual = datetime.now()
hora = horaActual.hour
minuto = horaActual.minute
hora += 2

if hora > 24:
	hora -= 24

print('Dentro de 2 horas seran las:', hora, ':', minuto, sep='')
