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
    def __init__(self,xi,yi,xd,yd,ti,tf):
        self.n = 0
        self.xi = xi
        self.yi = yi
        self.xd = xd
        self.yd = yd
        self.turnoInicio = ti
        self.turnoFin = tf
        self.recorrido = False
        self.tiempoCocheAsignado = 0

        self.dtiempo = 0 # Distancia temporal
        self.dtrayecto = 0 # Distancia espacial
    
    
    def __str__(self):
        return str(self.n)

    def evaluar(self, turnoActual):
        self.dtrayecto = abs(self.xi - self.xd) + abs(self.yi - self.yd)
        self.dtiempo = self.turnoInicio - turnoActual


class Coche:
    '''
    '''
    def __init__(self, numero):
        self.numero = numero
        self.x = 0
        self.y = 0
        self.viajesRecorridos = []
        self.tiempoNec = 0
        self.turno = 0 # turno actual en el que está el coche
    
    def addViaje(self, v):
        self.viajesRecorridos.append(v)
        self.turno += self.tiempoNec
        self.x = v.xd
        self.y = v.yd

    def dist(self, xi, yi, xd, yd):
        return (abs(xi - xd) + abs(yi - yd))

    def evaluar(self, v):
        self.tiempoNec = self.dist(self.x, self.y, v.xi, v.yi) + v.dtrayecto # tiempo necesario
        self.tiempoDisp = v.turnoFin - self.turno # tiempo disponible

        self.ventanaOportunidad = self.tiempoDisp - self.tiempoNec # disponible - necesario, si es positivo se puede hacer, sino no.


def solver(problem):
     # crear coches
    problem.listaCoches = []
    for i in range(0, problem.coches):
        problem.listaCoches.append(Coche(i))

    for j, v in enumerate(problem.listaViajes):
        v.n = j
        v.evaluar(0)
    problem.listaViajes.sort(key=attrgetter('dtiempo'), reverse=False) # de menos a mas

    for k, w in enumerate(problem.listaViajes):
        for c in problem.listaCoches:
            w.evaluar(c.turno)
            c.evaluar(w)
        problem.listaCoches.sort(key=attrgetter('ventanaOportunidad'), reverse=False) # de menos a mas

        l=0
        while  l < len(problem.listaCoches) and problem.listaCoches[l].ventanaOportunidad < 0:
            l += 1
        
        if not(l >= len(problem.listaCoches)):
            problem.listaCoches[i].addViaje(problem.listaViajes.pop(i))



def main():

    files = ['a_example','b_should_be_easy','c_no_hurry','d_metropolis','e_high_bonus']
    for f in files:
        problem = parse("defcom18/input/"+f+".in",s,globals())
        solver(problem)
        problem.escribir_viaje(f)
        print f+ "resolved"


if __name__ == '__main__':
    sys.exit(main())
