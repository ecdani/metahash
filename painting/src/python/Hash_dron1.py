# MAIN
fichero = open('../../in/learn_and_teach.in', 'r')
salida = open('../../out/Hash_lineas_learn_and_teach_123175.txt', 'w')

datos = fichero.readline() #Esto coge el numero de filas y columnas
lineasFichero = fichero.readlines() # Esto coge el dibujo en si.

lineasSalida = []

inst = 0
flaglinea = False
iniciolinea = 0
for linea in range(len(lineasFichero)):
    for columna in range(len(lineasFichero[linea])):
        if flaglinea == False and lineasFichero[linea][columna] == "#":
                flaglinea = True
                iniciolinea = columna
        elif flaglinea == True and (columna == 800 or lineasFichero[linea][columna] == "."):
                flaglinea = False
                inst += 1
                lineasSalida.append(
                    'PAINT_LINE {0} {1} {2} {3}\n'.format(str(linea), str(iniciolinea), str(linea), str(columna - 1)))

salida.write('{0}\n'.format(str(inst)))
for x in lineasSalida:
    salida.write(x)
fichero.close()
salida.close()


