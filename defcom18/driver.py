#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Copyright 2018 Defcom Software

import sys
from gcode17 import parse

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

	def escribir_viaje(self,c,v):
		fichero = open('defcom18/out/a_example.out','w')
		salida = []
		for coche in self.listaCoches:
			cadena = str(len(coche.viajesRecorridos))
			
			for viaje in coche.viajesRecorridos:
				cadena += str(viaje)
				salida.append(cadena + "\n")
		
		for x in salida:
			fichero.write(x)
		
		fichero.close()

    def parsear_archivo(self):
        pass

    def escribir_archivo(self):
        pass

class Viaje:
    '''
    '''
    def __init__(self,xi,yi,xf,yf,ti,tf):
        self.xInicio = xi
        self.yInicio = yi
        self.xFin = xf
        self.yFin = yf
        self.turnoInicio = ti
        self.turnoFin = tf

class Coche:
    '''
    '''
    def __init__(self):
        self.x = 0
        self.y = 0
        self.viajesRecorridos = 0
        self.libre = True

    def asignarViaje(self, viaje):
        self.viaje = viaje
        self.libre = False

    def accion(self, tipoViaje = 'inicio'):
        if tipoViaje == 'inicio':
            xDestino = self.viaje.xInicio
            yDestino = self.viaje.yInicio
        else:
            xDestino = self.viaje.xFin
            yDestino = self.viaje.yFin

        # primero avanzar en eje x
        if self.x != xDestino:
            self.y = self.avanzar(self.x, xDestino)
        elif self.y != yDestino:
            self.y = self.avanzar(self.y, yDestino)
        else:
            if tipoViaje == 'inicio':
                # TODO: comprobar si ya puede iniciar el viaje destino
                # ya ha llegado al punto de partida, se inicia el transporte del pasajero
                tipoViaje = 'fin'
                self.accion(tipoViaje)
            else:
                self.libre = True

    def avanzar(self, coordCoche, coordViaje):
        # comprobar orientación
        if coordCoche < coordViaje:
            orientacion = 1
        else:
            orientacion = -1
        return coordCoche + (1 * orientacion)

def main():
    #problem = parse("C:/Users/dani/git/metahash/defcom18/input/a_example.in",s,globals())
    problem = parse("input/a_example.in",s,globals())

    # crear coches
    problem.listaCoches = []
    for i in range(0, problem.coches):
        problem.listaCoches.append(Coche());

    # Bucle de turnos
    nViaje = 0
    for i in range(0, problem.pasos):
        # Bucle de coches
        for coche in problem.listaCoches:
            if coche.libre:
                # asignar nuevo viaje
                coche.asignarViaje(problem.listaViajes[nViaje])
                nViaje = nViaje + 1
            else:
                # avanzar
                coche.accion()

if __name__ == '__main__':
    sys.exit(main())
