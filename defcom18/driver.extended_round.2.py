#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Copyright 2018 Defcom Software

import sys
from gcode17 import parse
from operator import itemgetter, attrgetter
import copy

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
    '''
    rows y columns
    '''

    def __init__(self, fil, col, coch, viaj, bon, pas, listViaj):
        # Parsear archivo
        self.filas = fil
        self.columnas = col
        self.coches = coch
        self.viajes = viaj
        self.bonus = bon
        self.pasos = pas
        self.listaViajes = listViaj
        self.listaCoches = []

        for i in range(0, self.coches):
            self.listaCoches.append(Coche(i))

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

    def eval(self):  # ¿Como pueden coger viajes que no pueden llegar a término?
        self.score = 0
        for c in self.listaCoches:  # si el tiempo para empezar es menor...
            for i, v in enumerate(c.viajesRecorridos):
                # Actualiza la situacion del coche al terminar el viaje previo
                c.update(i-1)
                if (dist_ef(c, v) + v.dtrayecto + c.turno) < v.turnoFin:  # Si llego a completar
                    if (dist_ef(c, v) + c.turno) == v.turnoInicio:  # Si llego al bonus
                        self.score += v.dtrayecto + self.bonus
                    else:  # Si no llego al bonus
                        self.score += v.dtrayecto
        print " Score solucion: " + str(self.score),

    def solve(self):

        for j, v in enumerate(self.listaViajes):  # Asignar ids
            v.n = j
        initial_lenght = len(self.listaViajes)

        self.listaViajes = sorted(self.listaViajes, key=attrgetter('dtrayecto'), reverse=True)  # de menos a mas
        self.listaViajes = sorted(self.listaViajes, key=attrgetter('turnoInicio'), reverse=False)  # de menos a mas

        for k, w in enumerate(self.listaViajes):
            listaCochesProv = []
            for c in self.listaCoches:
                if c.viable(w):
                    c.eval(w, self.bonus)
                    listaCochesProv.append(c)
            # listaCochesProv.sort(key=attrgetter('preferencia','score'), reverse=False) # de menos a mas
            listaCochesProv = sorted(listaCochesProv, key=attrgetter('score'), reverse=False)  # de menos a mas
            listaCochesProv = sorted(listaCochesProv, key=attrgetter('preferencia'), reverse=True)  # de mas a menos
            if len(listaCochesProv) > 0:
                listaCochesProv[0].addViaje(w)
            self.listaViajes.pop(k)
            '''
            if len(listaCochesProv)>0:
                w.coche = listaCochesProv[0]
                w.score = copy.deepcopy(w.coche.score)
    
            if w.coche != False :
                coche = w.coche
                viaje = self.listaViajes.pop(k)
                coche.addViaje(viaje)
            else:
                self.listaViajes.pop(k)'''


class Viaje:
    def __init__(self, xi, yi, xd, yd, ti, tf):
        self.n = 0
        self.xi = xi
        self.yi = yi
        self.xd = xd
        self.yd = yd
        self.turnoInicio = ti
        self.turnoFin = tf
        self.recorrido = False
        self.tiempoCocheAsignado = 0
        self.coche = False

        # Idea: De los viajes viables, no coger el que se haga más rápido, sino el que ofrezca más score.
        self.score = 0
        self.ratioTiempoScore = 0

        self.dtiempo = 0  # Distancia temporal al inicio para un coche dado
        self.dtrayecto = (abs(xi - xd) + abs(yi - yd))

    def addCoche(self, coche):
        self.coche = coche

    def __str__(self):
        return str(self.n)


class Coche:
    def __init__(self, numero):
        self.numero = numero
        self.x = 0
        self.y = 0
        self.viajesRecorridos = []
        self.tiempoNec = 0
        self.turno = 0  # turno actual en el que está el coche
        self.preferencia = 0
        self.score = 0  # Variable auxiliar

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

    def dist(self, xi, yi, xd, yd):
        return (abs(xi - xd) + abs(yi - yd))

    def viable(self, w):
        if (self.dist(self.x, self.y, w.xi, w.yi) + w.dtrayecto + self.turno) >= w.turnoFin:
            return False
        return True

    def eval(self, w, bonus):

        dAlInicio = self.dist(self.x, self.y, w.xi, w.yi)
        tAlInicio = abs(w.turnoInicio - self.turno)

        if len(self.viajesRecorridos) > 0:
            self.preferencia = w.turnoInicio - self.viajesRecorridos[-1].turnoFin
        else:
            self.preferencia = w.turnoInicio

        self.score = 0
        if w.turnoInicio >= self.turno:
            if dAlInicio > tAlInicio:
                self.score += dAlInicio
            else:
                self.score += tAlInicio
        else:
            self.score += dAlInicio
            self.score += tAlInicio


def main():
    score = 0
    files = ['a_example', 'b_should_be_easy', 'c_no_hurry', 'd_metropolis', 'e_high_bonus']
    for f in files:
        print "Resolviendo " + f,
        problem = parse("defcom18/input/"+f+".in", s, globals())
        problem.solve()
        problem.eval()
        score += problem.score
        problem.escribir_viaje(f)
        print " ...resolved"
    print "Total score: " + str(score)


if __name__ == '__main__':
    sys.exit(main())
