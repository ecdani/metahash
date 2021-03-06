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
        self.listaCoches = []

    def escribir_viaje(self):
        """
        c = Coche()
        c.viajesRecorridos.append(1)
        c.viajesRecorridos.append(2)
        c.viajesRecorridos.append(3)
        c.viajesRecorridos.append(4)

        c2 = Coche()
        c2.viajesRecorridos.append(5)
        c2.viajesRecorridos.append(6)

        self.listaCoches.append(c)
        self.listaCoches.append(c2)
        """

        fichero = open('out/a_example.out','w')
        salida = []
        for coche in self.listaCoches:
            cadena = str(len(coche.viajesRecorridos))

            for viaje in coche.viajesRecorridos:
                cadena += " " + str(viaje)

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
        self.recorrido = False

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

    def calcularDistancia(self, xInicio, yInicio, xDestino, yDestino):
        return (xInicio - xDestino) + (yInicio - yDestino)

    def comprobarDistancia(self, viaje):
        distancia = self.calcularDistancia(self.x, self.y, viaje.xInicio, viaje.yInicio) + self.calcularDistancia(viaje.xInicio, viaje.yInicio, viaje.xFin, viaje.yFin)
        if abs(distancia) > viaje.turnoFin:
            return False
        else:
            return abs(distancia)

    def asignarViaje(self, listaViajes, totalTurnos):
        for i, viaje in enumerate(listaViajes):
            turnos = self.comprobarDistancia(viaje)
            if viaje.recorrido == False and turnos != False :
                #self.viaje = viaje
                if self.turnosUsados + turnos < totalTurnos:
                    self.viajesRecorridos.append(i)
                    viaje.recorrido = True
                    #turnosUsados = turnosUsados + viaje.turnoFin
                    print('El coche ' + str(self.numero) + ' ha sido asignado con el viaje ' + str(i))
                    return turnos
        self.fin = True
        return 0

    '''
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
    '''
    def accion(self):

        pass

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
        problem.listaCoches.append(Coche(i));

    # Bucle de turnos - deprecated
    #for i in range(0, problem.pasos):
    # Bucle de coches
    for coche in problem.listaCoches:
        turnosUsados = 0
        while turnosUsados < problem.pasos and coche.fin == False:
        #if coche.libre:
            # asignar nuevo viaje
            turnosUsados = turnosUsados + coche.asignarViaje(problem.listaViajes, problem.pasos)
            print(turnosUsados)
        # avanzar
        #coche.accion()
        #print('Turno ' + str(i) + ' - el coche ' + str(coche.numero) + ' se mueve')
    problem.escribir_viaje()

if __name__ == '__main__':
    sys.exit(main())
