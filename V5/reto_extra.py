# Una empresa, que distribuye maíz y soja importado, recibe la mercancía en un puerto situado a 380 kilómetros de su casa matriz. El maíz se recibe en sacos o bolsas de 200 libras y la soja viene en sacos o bolsas de 100 libras. La empresa cuenta con una flota de dos camiones pequeños marca Chevrolet modelo NPR cuya capacidad de carga es 4782 Kg y seis camiones marca Mercedes Benz modelo 625CV de capacidad total de 13 toneladas.

# Haga un programa en Python que cuando se le introduzca la cantidad de sacos recibidos, tanto de maíz como de soja sea capaz de calcular cuántos camiones serían necesarios enviar para retirar la mercancía del puerto. Adicionalmente, el director de la empresa exige terminantemente no sobrepasar la capacidad de carga de los camiones a más del 80 por ciento.

# 1 tonelada = 1000 Kg
# 1 libra = 0.453592 Kg

# Entrada de datos
dataMaiz = int(input('Cuantos sacos de maíz se importaron: '))
dataSoja = int(input('Cuantos sacos de soja se importaron: '))

# Convertir los datos a kilogramos
dataMaizKg = dataMaiz * 200 * 0.453592
dataSojaKg = dataSoja * 100 * 0.453592

# Calculo de los kg totales a cargar
totalKg = dataMaizKg + dataSojaKg

# Calculo de la capacidad real de nuestros camiones
capCargaGrande = 13 * 1000 * 0.8
capCargaPeq = 4782 * 0.8

# comprobar cuantos camiones grandes necesito
cantCamionesGrandes = totalKg // capCargaGrande

# Logica de nuestro programa
if cantCamionesGrandes == 0:
    cantCamionesPeq = totalKg // capCargaPeq
    if cantCamionesPeq == 0:
        print('Necesito solo 1 camión pequeño para ir a buscar la mercancía')
    else:
        print('Necesito solo 1 camión grande para ir a buscar la mercancía')
else:
    capTotal = cantCamionesGrandes * capCargaGrande
    restante = totalKg - capTotal
    cantCamionesPeq = restante // capCargaPeq
    if cantCamionesPeq == 0:
        cantCamionesPeq = 1
        print('Total de camiones a enviar a buscar la mercancía\nGRANDES: ', int(cantCamionesGrandes),'\nPEQUEÑOS: ', int(cantCamionesPeq))
    else:
        cantCamionesGrandes += 1
        print('Total de camiones a enviar a buscar la mercancía\nGRANDES:', int(cantCamionesGrandes))