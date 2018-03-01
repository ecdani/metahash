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

problem = parse("parse/redundancy.in",s,globals())