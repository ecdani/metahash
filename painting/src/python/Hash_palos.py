
#Tiene errores:
# The produced picture doesn't match the input file. The cell [157,216] differs: expected '.', got '#'.

# MAIN
fichero = open('../../in/learn_and_teach.in', 'r')
salida = open('../../out/Hash_palos_learn_and_teach.txt', 'w')

datos = fichero.readline() #Esto coge el numero de filas y columnas
lineasFichero = fichero.readlines() # Esto coge el dibujo en si.

lineasSalida = []

inst = 0
flaglinea = False
iniciolinea = 0
for columna in range(len(lineasFichero[0])):
    for linea in range(len(lineasFichero)):
        if flaglinea == False and (lineasFichero[linea][columna] == "#"):
                flaglinea = True
                iniciolinea = linea
        if flaglinea == True and (linea == 157 or lineasFichero[linea][columna] == "."):
            if linea == 157:
                linea +=1
            flaglinea = False
            inst += 1
            lineasSalida.append(
                'PAINT_LINE {0} {1} {2} {3}\n'.format(str(iniciolinea), str(columna), str(linea-1), str(columna )))

salida.write('{0}\n'.format(str(inst)))
for x in lineasSalida:
    salida.write(x)
fichero.close()
salida.close()
