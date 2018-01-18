from genetico import Individuo,Gen,Pool
from random import randint, random

"""Genetico aplicado al problema de painting"""

class Instruccion(Gen):
    # Nuevo gen Aleatorio
    def __init__(self):
        self.videos = [50, 50, 80, 30, 410]
        self.video = self.videos[randint(0,4)]
    def mutar(self):
        self.__init__()


class Impresion(Individuo):
    def evaluar(self):
        self.score = 0
        for i in range(self.conf.ngenes):
            self.score +=self.genes[i].video

class GENETIC_CONFIG:
    gencls = Instruccion # Clase Gen
    individuocls = Impresion # Clase Individuo
    tpob = 20 # Tamaño de la población (Numero par plz)
    maxgenest = 100 # Número máximo de generaciones estancadas
    pmutacion = 0.5 # Probabilidad de mutacion
    pcruze = 0.5 # Probabilidad de cruze
    ngenes = 10 # Numero genes

pool = Pool(GENETIC_CONFIG)
pool.doSearch()
