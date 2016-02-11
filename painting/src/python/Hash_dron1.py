
#FUNCIONES
def lecturaFichero(fichero, diccionario):
    # Lectura linea inicial
    linea = fichero.readline().split()
    diccionario["rows"] = int(linea[0])
    diccionario["columns"] = int(linea[1])
    diccionario["drones"] = int(linea[2])
    diccionario["turns"] = int(linea[3])
    diccionario["max_load"] = int(linea[4])
    # Fin Procesamiento linea inicial

    # Lectura de productos y pesos
    linea = fichero.readline()
    diccionario["nProducts"] = int(linea)
    pesoDeCadaProducto = []
    for peso in fichero.readline().split():
        pesoDeCadaProducto.append(int(peso))
    diccionario["weights"] = pesoDeCadaProducto
    # Fin de productos y pesos

    # Lectura lineas de almacenes. Tenemos un array de datos de almacen
    numeroAlmacenes = int(fichero.readline())
    datosAlmacenes = []
    # Cada posicion del array tiene una lista de dos elementos.
    #   array[0] = coordenadas en una tupla (x,y)
    #   array[1] = array con articulos de cada tipo
    for almacen in range(numeroAlmacenes):
        datosAlmacen = []
        cantidadesDeProductos = []
        linea = fichero.readline().split()
        coordenadasAlmacen = (int(linea[0]), int(linea[1]))
        datosAlmacen.append(coordenadasAlmacen)
        linea = fichero.readline().split()
        for elem in linea:
            cantidadesDeProductos.append(int(elem))
        datosAlmacen.append(cantidadesDeProductos)
        datosAlmacenes.append(datosAlmacen)
    







# MAIN
fichero = open('../../in/busy_day.in', 'r')
salida = open('../../out/Hash_dron_python.txt', 'w')

datosProblema = {}
lecturaFichero(fichero,datosProblema)
print(datosProblema)

fichero.close()
salida.close()


