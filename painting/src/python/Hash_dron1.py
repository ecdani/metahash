# IMPORT
from math import sqrt
from operator import itemgetter, attrgetter

# GLOBALES
dicc = {} # Mother of all data structures
lineasSalida = [] # Buffer de instrucciones en String.

# FUNCIONES
def lecturaFichero():
    global dicc
    fichero = open('../../in/busy_day.in', 'r')

    ### Lectura linea inicial ###
    linea = fichero.readline().split()
    dicc["filas"] = int(linea[0])
    dicc["columnas"] = int(linea[1])
    dicc["drones"] = int(linea[2])
    dicc["turnos"] = int(linea[3])
    dicc["max_load"] = int(linea[4])

    ### Lectura de productos y pesos ###
    linea = fichero.readline()
    dicc["nproductos"] = int(linea)
    for peso in fichero.readline().split():
        dicc["pesos"].append(int(peso))

    ### Lectura lineas de almacenes ###
    dicc["nalmacenes"] = int(fichero.readline())

    dicc["almacenes"] = []
    for almacen in range(dicc["nalmacenes"]):
        linea = fichero.readline().split()
        x = int(linea[0])
        y = int(linea[1])
        linea = fichero.readline().split()
        stocks = []
        for stock in linea:
            stocks.append(int(stock))
        dicc["almacenes"].append({'x':x, 'y':y, 'productos':stocks})

    ### Lectura lineas de pedidos ###
    dicc["npedidos"] = fichero.readline()
    for pedido in range(dicc["npedidos"]):
        linea = fichero.readline().split()
        x = int(linea[0])
        y = int(linea[1])
        nitems = int(fichero.readline())

        linea = fichero.readline().split()
        productos = []
        for producto in linea:
            productos.append(int(producto)) # Productos individuales
        dicc["pedidos"].append({'x':x, 'y':y,'nitems':nitems, 'productos':productos})
    fichero.close()


def determinarAlmacen(pedido, keyproducto):
    """
    Determina el almacén más cercano a las coordenadas origen dadas para el
    tipo de producto dado.
    :param x: Coordenada origen x
    :param y: Coordenada origen y
    :param producto: ID producto
    :return:
    """
    global dicc
    rAlma = {} # Ranking Almacenes
    for almacen in list(dicc['almacenes']):
        for prod in list(almacen['productos']):
            if prod == pedido['productos'][keyproducto]:
                rAlma[dicc['almacenes'].index(almacen)] = distanciaEuclidea(pedido['x'],pedido['y'],almacen['x'],almacen['y'])

    min = rAlma[(rAlma.keys())[0]] # Cogemos un minimo random, pero real.
    mejorAlmacen = (rAlma.keys())[0]

    for idalmacen in rAlma.keys():
        if min > rAlma[idalmacen]:
            min,mejorAlmacen = rAlma[idalmacen], idalmacen

    dicc["almacenes"][mejorAlmacen]['productos'][keyproducto] =- 1 # Decrementamos stock

    pedido['productos'][keyproducto] = {'producto': pedido['productos'][keyproducto],'mejorAlmacen':mejorAlmacen, 'scoreAlmacen': rAlma[mejorAlmacen] }
    # En teoría no necesitamos devolver si guardamos los datos junto al producto del pedido.
    # AlmaDet = {'id': mejorAlmacen, 'score':rAlma[mejorAlmacen]}
    # return AlmaDet


def distanciaEuclidea(x1,y1,x2,y2):
    return sqrt((abs(x1-x2)**2)+(abs(y1-y2))**2)

def generarSolucion():
    """
    Escribe un txt con los comandos solucion
    :return:
    """
    global lineasSalida
    salida = open('../../out/Hash_dron1.txt', 'w')
    salida.write('{0}\n'.format(len(lineasSalida)))
    for x in lineasSalida:
        salida.write(x)
    salida.close()

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

############################### MAIN ###################################

lecturaFichero()

rOrders = {}
for pedido in dicc["pedidos"]:
    dicc["pedidos"][pedido]['score'] = 0
    for keyproducto in pedido['productos'].keys():
        determinarAlmacen(pedido,keyproducto)
        dicc["pedidos"][pedido]['score'] += dicc["pedidos"][pedido]['productos'][keyproducto]['scoreAlmacen']

sorted(dicc["pedidos"], key=attrgetter('score')) # En orden ascendente en teoría

nDron = 0
indice = 0
for pedido in dicc['pedidos']:
    indice =+ 1
    nDron = (indice % dicc['drones']) + 1
    carga = 0
    for producto in pedido['productos']:
        if carga > dicc['max_load']:
            escribirComando(nDron,"D",producto['mejorAlmacen'],producto['producto'],1)
            carga = 0
        escribirComando(nDron,"L",producto['mejorAlmacen'],producto['producto'],1)
        carga += dicc["pesos"][producto['producto']]

generarSolucion()


#######################################################################

