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


class Problem:
    def __init__(self, rows,cols,ndrones,turns,maxload,weights,warehouses,orders):
        print rows,cols,ndrones,turns,maxload,len(weights),len(warehouses),len(orders)
        print warehouses[-1].x
        print orders[-1].x
        pass

def Take2 (a,b):
    return b

class Almacen:
    def __init__(self,x,y,products):
        self.x = x
        #print x,y
        #for p in products:
            #print p


class Pedido:
    def __init__(self,x,y,products):
        self.x = x
        #print x,y
        '''for p in products:
            print p'''

problem = parse("parse/redundancy.in",s,globals())