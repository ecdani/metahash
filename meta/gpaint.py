from genetico import Individuo,Gen,Pool
from random import randint, random
import filecmp
import numpy as np

"""Genetico aplicado al problema de painting"""
r = 14
c = 80

class Instruccion(Gen):
    # Nuevo gen Aleatorio
    def __init__(self):
        global r,c
        #self.videos = [50, 50, 80, 30, 410]
        #self.video = self.videos[randint(0,4)]
        self.tipo = randint(0,2)
        if self.tipo == 0: #PRINT_SQUARE
            x = randint(0,c-1)
            y = randint(0,r-1)
            s = 0 # Es dificil controlar que el square no se valla de madre con la S
            self.p = [y,x,s] # parametros
        elif self.tipo == 1:# PRINT_LINE
            self.p = [randint(0,r-1),randint(0,c-1),randint(0,r-1),randint(0,c-1)] # parametros
        else: # ERASE
            self.p = [randint(0,r-1),randint(0,c-1),randint(0,r-1),randint(0,c-1)] # parametros
    def mutar(self):
        self.__init__()


class Impresion(Individuo):
    def evaluar(self):
        self.score = 0
        #for i in range(self.conf.ngenes):
            #self.score +=self.genes[i].video
        self.imprimir()
        if self.validez():
            self.score = r*c - self.conf.ngenes
            self.exportar()

    def validez(self):
        return filecmp.cmp('meta/in/logo.in', 'meta/out/impresion.out') 
    
    def exportar(self):
        salida = open('meta/out/output.txt', 'w')
        lineasSalida = []
        i = 0
        while i < self.conf.ngenes:
            i += 1
            gen = self.genes[i]
            if gen.tipo == 0:
                lineasSalida.append('PAINT_SQUARE {0} {1} {2}\n'.format(str(gen.p[0]), str(gen.p[1]), str(gen.p[2])))
            elif gen.tipo == 1:
                lineasSalida.append('PAINT_LINE {0} {1} {2} {3}\n'.format(str(gen.p[0]), str(gen.p[1]), str(gen.p[2]), str(gen.p[3])))
            else:
                lineasSalida.append('ERASE_CELL {0} {1}\n'.format(str(gen.p[0]), str(gen.p[1])))

        salida.write('{0}\n'.format(str(len(self.genes))))
        for x in lineasSalida:
            salida.write(x)
        salida.close()

    def imprimir(self):
        salida = open('meta/out/impresion.out', 'w')
        a = np.zeros((c,r), dtype=bool)
        i = 0
        while i < self.conf.ngenes:
            gen = self.genes[i]
            if gen.tipo == 0:
                # a.append('PAINT_SQUARE {0} {1} {2}\n'.format(str(gen.p[0]), str(gen.p[1]), str(gen.p[2])))
                                        #R    C   S
                x  = gen.p[1] - gen.p[2]
                y  = gen.p[0] - gen.p[2] 
                xf = gen.p[1] + gen.p[2]
                yf = gen.p[0] + gen.p[2]

                while x <= xf:
                    while y <= yf:
                        a[x][y] = True
                        y += 1
                    y = gen.p[0] - gen.p[2]
                    x += 1

            elif gen.tipo == 1:
                #a.append('PAINT_LINE {0} {1} {2} {3}\n'.format(str(gen.p[0]), str(gen.p[1]), str(gen.p[2]), str(gen.p[3])))
                x  = gen.p[1]
                y  = gen.p[0]
                xf = gen.p[3]
                yf = gen.p[2]
                while x <= xf:
                    while y <= yf:
                        a[x][y] = True
                        y += 1
                    y = gen.p[0]
                    x += 1
            else:
                #a.append('ERASE_CELL {0} {1}\n'.format(str(gen.p[0]), str(gen.p[1])))
                                    #  R   C
                a[gen.p[1]][gen.p[0]] = False
            i += 1

        salida.write('{0} {1}\n'.format(str(r),str(c)))

        x = 0
        y = 0

        while y < r:
            while  x < c:
                if a[x][y] == True:
                    salida.write('#')
                else:
                    salida.write('.')
                x += 1
            salida.write('\n')
            x = 0
            y += 1

        salida.close()



class GENETIC_CONFIG:
    gencls = Instruccion # Clase Gen
    individuocls = Impresion # Clase Individuo
    tpob = 20 # Tamaño de la población (Numero par plz)
    maxgenest = 10000 # Número máximo de generaciones estancadas
    pmutacion = 0.5 # Probabilidad de mutacion
    pcruze = 0.5 # Probabilidad de cruze
    ngenes = 10 # Numero genes

pool = Pool(GENETIC_CONFIG)
pool.doSearch()
