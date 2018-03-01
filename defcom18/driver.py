from gcode17 import parse

s = """
Main = Int Int Int Int Int  -> nPesos-> nAlmacenes -> nPedidos | Problem
nPesos = Int -> Pesos | Take2
Pesos = *Int
nAlmacenes = Int -> 1@Ware | Take2
Ware = Int Int -> Ware2 | Almacen
Ware2 = *Int
nPedidos = Int -> 1@Coord | Take2
Coord = Int Int -> Cant | Pedido
Cant = Int -> CantsProd | Take2
CantsProd = *Int
"""


# Zona de las clases

import sys

class Problema:
    '''
    rows y columns
    '''
    def __init__(self):
        # Parsear archivo

    def parsear_archivo:
        pass

    def escribir_archivo:
        pass

class Viaje:
    '''
    '''
    def __init__(self):
        pass

class Coche:
    '''
    '''
    def __init__(self):
        self.x = 0
        self.y = 0

def main():
    problem = parse("input/redundancy.in",s,globals())

if __name__ == '__main__':
    sys.exit(main())
