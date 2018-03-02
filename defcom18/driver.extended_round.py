#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Copyright 2018 Defcom Software

import sys
from gcode17 import parse
from operator import itemgetter, attrgetter

s = """
Main = Int Int Int Int Int Int -> 4@viaje | Problema
viaje = Int Int Int Int Int Int | Viaje
"""

# Zona de las clases

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
        self.listaCoches = []

    def escribir_viaje(self,file):
        fichero = open('defcom18/out/'+file+'.out','w')
        salida = []
        for coche in self.listaCoches:
            cadena = str(len(coche.viajesRecorridos))

            for viaje in coche.viajesRecorridos:
                cadena += " " + str(viaje)

            salida.append(cadena + "\n")

        for x in salida:
            fichero.write(x)

        fichero.close()


class Viaje:
    '''
    '''
    def __init__(self,xi,yi,xf,yf,ti,tf):
        self.xi = xi
        self.yi = yi
        self.xFin = xf
        self.yFin = yf
        self.turnoInicio = ti
        self.turnoFin = tf
        self.recorrido = False
        self.tiempoCocheAsignado = 0
    
    def __str__(self):
        return str(self.n)

class Coche:
    '''
    '''
    def __init__(self, numero):
        self.numero = numero
        self.x = 0
        self.y = 0
        self.viajesRecorridos = []
        self.libre = True
        self.turnosUsados = 0
        self.fin = False
        self.tiempo = 0
    

    def dist(self, xi, yi, xd, yd):
        return abs(xi - xd) + abs(yi - yd)

    def evaluar(self, v):
        self.tiempo = self.dist(self.x, self.y, v.xi, v.yi) + self.dist(v.xi, v.yi, v.xFin, v.yFin)
        for vr in  self.viajesRecorridos:
            self.tiempo += vr.tiempoCocheAsignado


def solver(problem):
     # crear coches
    problem.listaCoches = []
    for i in range(0, problem.coches):
        problem.listaCoches.append(Coche(i))

    for i, v in enumerate(problem.listaViajes):
        v.n = i
        for c in problem.listaCoches:
            c.evaluar(v)
        problem.listaCoches.sort(key=attrgetter('tiempo'), reverse=False)

        v.tiempoCocheAsignado = c.tiempo
        problem.listaCoches[0].viajesRecorridos.append(v)


def main():

    files = ['a_example','b_should_be_easy','c_no_hurry','d_metropolis','e_high_bonus']
    for f in files:
        problem = parse("defcom18/input/"+f+".in",s,globals())
        solver(problem)
        problem.escribir_viaje(f)


if __name__ == '__main__':
    sys.exit(main())
