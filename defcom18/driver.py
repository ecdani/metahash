from gcode17 import parse

s = """
Main = Int Int Int Int Int Int -> 3@viaje | Problema
viaje = Int Int Int Int Int Int | Viaje
"""


# Zona de las clases

problem = parse("parse/redundancy.in",s,globals())