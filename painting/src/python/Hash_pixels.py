# FUNCIONES
def is_not_over():
    if linea != (len(lineasFichero)-1) or columna != (len(lineasFichero[linea])-1):
        return True
    else:
        return False

# MAIN
fichero = open('../../in/learn_and_teach.in', 'r')
salida = open('../../out/Hash_pixels_learn_and_teach_100391.txt', 'w')

datos = fichero.readline() #Esto coge el numero de filas y columnas
lineasFichero = fichero.readlines() # Esto coge el dibujo en si.

lineasSalida = []

i = 0
for linea in range(len(lineasFichero)):
    for columna in range(len(lineasFichero[linea])):
        if lineasFichero[linea][columna] == "#":
            i = i + 1
            lineasSalida.append("PAINT_SQUARE " + str(linea) + " " + str(columna) + " 0")
            if is_not_over():
                lineasSalida.append("\n")

lineasSalida = lineasSalida[:-1]
salida.write(str(i) + "\n")
for x in lineasSalida:
    salida.write(x)


fichero.close()
salida.close()
