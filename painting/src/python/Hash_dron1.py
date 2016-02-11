# IMPORT
from math import sqrt

# GLOBALES
datosProblema = {}

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
    numeroProductos = int(linea)
    pesoDeCadaProducto = []
    for peso in fichero.readline().split():
        pesoDeCadaProducto.append(int(peso))
    diccionario["products_data"] = [numeroProductos,pesoDeCadaProducto]
    # products_data -> numeroProductos y [pesosProductos]
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
    diccionario["warehouses_data"] = datosAlmacenes
    # Fin de lecturas de almacenes

    #Lectura lineas de pedidos
    numeroPedidos = fichero.readline()
    datosPedidos = []
    for pedido in range(numeroProductos):
        datosPedido = []
        linea = fichero.readline().split()
        coordenadasPedido = (int(linea[0]), int(linea[1]))
        datosPedido.append(coordenadasPedido)
        numeroObjetosPedido = int(fichero.readline())
        datosPedido.append(numeroObjetosPedido)
        tiposProductosOrdenados = []
        linea = fichero.readline().split()
        for num in linea:
            tiposProductosOrdenados.append(int(num))
        datosPedido.append(tiposProductosOrdenados)
        datosPedidos.append(datosPedido)
    diccionario["orders_data"] = datosPedidos
    # Fin de lectura de pedidos
# CAUTION: CAST EXPLICITO A LIST AL RECUPERAR DEL DICCIONARIO
def determinarAlmacen(coord, tipoItem):
    global datosProblema
    rAlma = {}
    for alma in list(datosProblema["warehouses_data"]):
        for tipo in list(alma[1]):
            if tipo == tipoItem:
                rAlma[datosProblema["warehouses_data"].index(alma)] = distanciaEuclidea(coord, alma[0])
                #  a = alma eso es una tupla
                # print(a)
    for elem in rAlma.keys():
        minimo = rAlma[elem]



def distanciaEuclidea(coord1, coord2):
    return sqrt((abs(coord1[0]-coord2[0])**2)+(abs(coord1[1]-coord2[1]))**2)

#print(almacenes[0])

# MAIN
fichero = open('../../in/busy_day.in', 'r')
#salida = open('../../out/Hash_dron_python.txt', 'w')

datosProblema = {}
lecturaFichero(fichero,datosProblema)
# print(datosProblema["orders_data"][1][32])
determinarAlmacen(40,4)

fichero.close()
#salida.close()

def generarsolucion():
    salida = open('../../out/Hash_dron1.txt', 'w')
    salida.write('{0}\n'.format(len(lineasSalida)))
    for x in lineasSalida:
        salida.write(x)
    salida.close()

lineasSalida = []

def escribirComando(dron, comando, destino, tipop, cantidad ):
    """
    Dron 0-N
    Comando: D,Deliver W,Wait L,Load, U,Unload
    Destino, Warehouse ID o Custormer ID
    tipop: ID tipo producto 0-N
    cantidad: Cantidad a cargar o descargar si es un deliver
    """
    global lineasSalida
    lineasSalida.append('{0} {1} {2} {3} {4}\n'.format(str(dron), str(comando), str(destino), str(tipop), str(cantidad)))
