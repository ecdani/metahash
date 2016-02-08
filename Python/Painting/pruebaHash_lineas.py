# FUNCIONES
def is_not_over():
    if linea != (len(lineasFichero)-1) or columna != (len(lineasFichero[linea])-1):
        return True
    else:
        return False

# MAIN
fichero = open("learn_and_teach.in", "r")
salida = open("result.txt", "w")

datos = fichero.readline() #Esto coge el numero de filas y columnas
lineasFichero = fichero.readlines() # Esto coge el dibujo en si.

lineasSalida = []

# for linea in range(len(lineasFichero)):
#     print(linea, lineasFichero[linea])
# print(len(lineasFichero))
inst = 0
flaglinea = False
iniciolinea = 0
for linea in range(len(lineasFichero)):
    for columna in range(len(lineasFichero[linea])):
        if lineasFichero[linea][columna] == "#":
            if flaglinea == False:
                flaglinea = True
                iniciolinea = columna
        elif lineasFichero[linea][columna] == ".":
            if flaglinea == True:
                flaglinea = False
                inst += 1
                lineasSalida.append("PAINT_LINE " + str(linea) +" "+ str(iniciolinea) +" "+ str(linea) +" "+ str(columna-1))
                #longlinea = 0
                if is_not_over():
                    lineasSalida.append("\n")

lineasSalida = lineasSalida[:-1]
salida.write(str(inst) + "\n")
for x in lineasSalida:
    salida.write(x)


fichero.close()
salida.close()
