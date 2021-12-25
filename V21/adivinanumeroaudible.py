

import random
from io import BytesIO
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

def convierte_a_audio(texto):
    
    tts = gTTS(texto, lang='es')
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    audio_final = AudioSegment.from_file(fp, format="mp3")
    return audio_final

def devuelve_limite_superior():
    limite = 0
    while not limite in [10, 100, 1000]:
        limite = int(input('Ingrese el limite superior (10,100 o 1000): '))
    return limite

def devuelve_limite_intentos(valor):
    if valor == 10:
        return 3
    elif valor == 100:
        return 6
    else:
        return 9

def devuelve_numero_aleatorio(limite):
    return random.randint(1, limite)

def bienvenida():    
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
    texto_ejemplo = 'Hola, como te llamas? '
    audio_ejemplo = convierte_a_audio(texto_ejemplo)
    play(audio_ejemplo)
    bienvenida()
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