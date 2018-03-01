from gcode17 import parse

s = """
Main = Int Int Int Int Int Int -> 3@viaje | Problema
viaje = Int Int Int Int Int Int | Viaje
"""


# Zona de las clases

import sys

class Problema:
    '''
    rows y columns
    '''
    def __init__(self,fil,col,coch,viaj,bon,pas,listViaj):
        # Parsear archivo
        self.filas = fil
        self.columnas = col 
        self.coches = coch
        self.viajes = viaj
        self.bonus = bon
        self.pasos = pas
        self.listaViajes = listViaj

    def parsear_archivo(self):
        pass

    def escribir_archivo(self):
        pass

class Viaje:
    '''
    '''
    def __init__(self,xi,yi,xf,yf,ti,tf):
        self.xinicio = xi
        self.yinicio = yi
        self.xfinal = xf
        self.yfinal = yf
        self.turno_inicio = ti 
        self.turno_fin = tf

class Coche:
    '''
    '''
    def __init__(self):
        self.x = 0
        self.y = 0

def main():
    problem = parse("input/a_example.in",s,globals())
    print('hey')

if __name__ == '__main__':
    sys.exit(main())
