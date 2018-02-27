from genetico import Individuo,Gen,Pool
import random
from difflib import SequenceMatcher
import filecmp
import numpy as np

class Caracter(Gen):
    caracter = ""
    def __init__(self):
        self.caracter = chr(int(random.randrange(32, 126, 1)))

    def mutar(self):
        self.__init__()

    def __str__(self):
        return self.caracter
    def __repr__(self):
        return self.caracter



class Cadena(Individuo):
    objetivo = "Hola Mariano"
    score = 0

    def evaluar(self):
        self.score = 0
        for i, gen in enumerate(self.genes):
            if gen.caracter[0] == self.objetivo[i]:
            #self.score += abs(ord(gen.caracter[0] ) - ord(self.objetivo[i]))
                self.score += 1
    def exportar(self):
        for gen in self.genes:
            print (gen, end="", flush=True)
        
    def __str__(self):
        output = ""
        for gen in self.genes:
            output += gen.__str__()
            #print (self.genes[i], end="", flush=True)
        return output

    def __repr__(self):
        return self.__str__()

class GENETIC_CONFIG:
    gencls = Caracter # Clase Gen
    individuocls = Cadena # Clase Individuo
    tpob = 16 # Tamaño de la población (Numero par plz)
    maxgenest = 5000 # Número máximo de generaciones estancadas
    pmutacion = 0.1 # Probabilidad de mutacion
    pcruze = 0.5 # Probabilidad de cruze
    ngenes = 12 # Numero genes


pool = Pool(GENETIC_CONFIG())
pool.doSearch()