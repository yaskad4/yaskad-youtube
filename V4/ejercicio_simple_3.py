# Programa que acepte una cadena de caracteres y cuente el tamaño de la cadena y cuántas veces aparece la letra a sea mayúscula o minúscula.

cadenaChar = input('Introduzca una cadena de texto: ')
cadenaChar = cadenaChar.lower()
largoCadena = len(cadenaChar)
charA = cadenaChar.count('a')
charAcentuadas = cadenaChar(á)

print('El largo de la cadena es: ',largoCadena)
print('En la cadena hay ', charA, 'letras a')
print('Si contamos las a acentuadas tenemos un total de ', charA + charAcentuadas, 'letras a')