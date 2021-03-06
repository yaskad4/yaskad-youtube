# Crear un juego (utilizando Python) donde la computadora piense, o escoja un numero entre 1 y un limite,
# y este limite solo puede ser 10, 100 o 1000, y nos da un numero limitado de veces para que nosotros adivinemos
# el numero. La cantidad de intentos seran: 3, 5 y 8 para los limites 10, 100 y 1000 respectivamente.
# Cuando le digamos un numero y este es menor que el numero que escogio la computadora, esta nos respondera
# incorrecto, el numero que he pensado es mayor. Y viceversa.
# Si lo adivinamos, en un numero menor o igual al numero de intentos, habremos ganado, de lo contrario habra 
# ganado la computadora.

import random

def devuelve_limite_superior():
    # Funcion que devuelve cual sera el limite superior para la eleccion del numero aleatorio
    limite = 0
    while not limite in [10, 100, 1000]:
        limite = int(input('Ingrese el limite superior (10,100 o 1000): '))
    return limite

def devuelve_limite_intentos(valor):
    # Funcion que devuelve la cantidad de intentos que tendra el jugador para adivinar el numero, dependiendo del limite superior
    if valor == 10:
        return 3
    elif valor == 100:
        return 6
    else:
        return 9

def devuelve_numero_aleatorio(limite):
    # Funcion que devuelve un numero aleatorio entre 1 y el limite superior
    return random.randint(1, limite)

def bienvenida():    
    # Funcion que muestra un mensaje de bienvenida al jugador
    nombre = input('Hola, como te llamas? ')
    print(f'''
    Bienvenido {nombre} al Juego de Adivinar un numero
    **************************************************
    Las reglas son simples
    Yo pienso un numero entre 1 y el limite que vos elijas.
    Iras diciendome en un numero finito de intentos un numero.
    Te ire diciendo si el numero que he pensado es mayor
    o menor al numero que me has dado, si lo adivinas habras ganado.
    Pero si se te acaban los intentos y no lo has adivinado, 
    pues adivina quien habra ganado.\n''')

if __name__ == '__main__':
    bienvenida()
    # Variables a inicializar
    limite_superior = devuelve_limite_superior()
    limite_intentos = devuelve_limite_intentos(limite_superior)
    numero_pensado = devuelve_numero_aleatorio(limite_superior)
    cantidad_de_intentos = 0
    numero_adivinado = 0

    while True:
        cantidad_de_intentos += 1
        numero_adivinado = int(input('Ingrese un numero entre 1 y ' + str(limite_superior) + ': '))
        if numero_adivinado > numero_pensado:
            if cantidad_de_intentos == limite_intentos:
                print(f'PERDISTE!. se acabaron los intentos. El numero era {numero_pensado}')
                break
            print(f'Intentalo otra vez, el numero es menor. Te quedan {limite_intentos - cantidad_de_intentos} intentos')
        elif numero_adivinado < numero_pensado:
            if cantidad_de_intentos == limite_intentos:
                print(f'PERDISTE!. se acabaron los intentos. El numero era {numero_pensado}')
                break
            print(f'Intentalo otra vez, el numero es mayor. Te quedan {limite_intentos - cantidad_de_intentos} intentos')
        else:
            print(f'GANASTE!. Acertaste en {cantidad_de_intentos} intentos')
            break


