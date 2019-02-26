#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Copyright 2018 Defcom Software

import sys
from gcode17 import parse
from operator import  attrgetter

s = """
Main = Int Int Int Int Int Int -> 4@viaje | Problema
viaje = Int Int Int Int Int Int | Viaje
"""

# Zona de las clases


def dist(c, v):  # Distancia al origen del viaje
    return (abs(c.x - v.xi) + abs(c.y - v.yi))


def dist_ef(c, v):  # Distancia en turnos hasta poder empezar el viaje
    # O llegamos tarde porque el viaje es mas largo, o hay que esperar tiempo
    return (max(dist(c, v), tiempo(c, v)))


def tiempo(c, v):  # Tiempo hasta el comienzo
    return (v.turnoInicio - c.turno)


class Problema:
    def __init__(self, fil, col, coch, viaj, bon, pas, listViaj):
        # Parsear archivo
        #self.filas = fil
        #self.columnas = col
        self.coches = coch
        #self.viajes = viaj
        self.bonus = bon
        #self.pasos = pas
        self.listaViajes = listViaj
        self.listaCoches = []

        for i in range(0, self.coches):
            self.listaCoches.append(Coche())

    def escribir_viaje(self, file):
        fichero = open('defcom18/out/' + file + '.out', 'w')
        salida = []
        for coche in self.listaCoches:
            cadena = str(len(coche.viajesRecorridos))
            for viaje in coche.viajesRecorridos:
                cadena += " " + str(viaje)
            salida.append(cadena + "\n")
        for x in salida:
            fichero.write(x)
        fichero.close()

    def eval(self):
        self.score = 0
        for c in self.listaCoches:
            for i, v in enumerate(c.viajesRecorridos):
                c.update(i-1) # Actualiza la situacion del coche al terminar el viaje previo
                if (dist_ef(c, v) + v.dtrayecto + c.turno) < v.turnoFin:  # Si llego a completar
                    if (dist_ef(c, v) + c.turno) == v.turnoInicio:  # Si llego al bonus...
                        self.score += v.dtrayecto + self.bonus
                    else:
                        self.score += v.dtrayecto
        print(" Score solucion: " + str(self.score))

    def solve(self):
        for j, v in enumerate(self.listaViajes):  # Asignar ids
            v.n = j 

        # De vuelta a la perspectiva desde el coche #♥
        n_viajes_previos = 0
        while len(self.listaViajes) != n_viajes_previos:
            n_viajes_previos = len(self.listaViajes)
            self.listaCoches = sorted(self.listaCoches, key=attrgetter('turno'), reverse=False)  # de menos a mas
            for i, c in enumerate(self.listaCoches):
                lista_viajes_disp = []
                for k, w in enumerate(self.listaViajes):
                    if w.viable(c):
                        w.eval(c, self.bonus)
                        lista_viajes_disp.append(w)

                lista_viajes_disp = sorted(lista_viajes_disp, key=attrgetter('score'), reverse=True)  # de mas a menos
                lista_viajes_disp = sorted(lista_viajes_disp, key=attrgetter('dtrayecto'), reverse=False) # de menos a mas
                lista_viajes_disp = sorted(lista_viajes_disp, key=attrgetter('dtiempo'), reverse=False)  # de menos a mas 

                if len(lista_viajes_disp) > 0: 
                    c.addViaje(lista_viajes_disp[0])
                    self.listaViajes.remove(lista_viajes_disp[0])


class Viaje:
    def __init__(self, xi, yi, xd, yd, ti, tf):
        self.n = 0
        self.xi = xi
        self.yi = yi
        self.xd = xd
        self.yd = yd
        self.turnoInicio = ti
        self.turnoFin = tf

        self.score = 0 # Normalmente el dtrayecto + bonus si lo hay
        self.dtiempo = 0  # Distancia temporal al inicio para un coche dado
        self.dtrayecto = (abs(xi - xd) + abs(yi - yd))
    
    def viable(self, c):
        if (dist_ef(c, self) + self.dtrayecto + c.turno) < self.turnoFin:
            return True
        else:
            return False

    def eval(self, c, bonus):
        self.dtiempo = dist_ef(c, self)
        self.score = 0
        if self.dtrayecto > 5000: # optimización para el d_metropolis
            self.dtiempo += self.dtiempo*2 # pk al acabar estaremos muy en a tomar por 
        
        self.score += self.dtrayecto
        if (dist_ef(c, self) + c.turno) == self.turnoInicio:
            self.score += bonus
    
    def __str__(self):
        return str(self.n)


class Coche:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.viajesRecorridos = []
        self.turno = 0  # turno actual en el que está el coche

    def addViaje(self, v):
        self.viajesRecorridos.append(v)
        self.turno += (dist_ef(self, v) + v.dtrayecto)
        self.x = v.xd
        self.y = v.yd

    def update(self, i):
        if i < 0:
            self.turno = 0
            self.x = 0
            self.y = 0
        else:
            v = self.viajesRecorridos[i]
            # Las x e y del coche deben estar en las correctas
            self.turno += (dist_ef(self, v) + v.dtrayecto)
            self.x = v.xd
            self.y = v.yd


def main():
    score = 0
    #files = ['d_metropolis']
    files = ['a_example', 'b_should_be_easy', 'c_no_hurry','d_metropolis', 'e_high_bonus']
    for f in files:
        print("Resolviendo " + f)
        problem = parse("defcom18/input/"+f+".in", s, globals())
        print("Parsed")
        problem.solve()
        problem.eval()
        score += problem.score
        problem.escribir_viaje(f)
        print(" ...resolved")
    print("Total score: " + str(score))


if __name__ == '__main__':
    sys.exit(main())
