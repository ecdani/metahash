import operator, copy
from random import randint, random

# MAIN

tpob = 10 # Tamaño de la población (Numero par plz)

maxgenest = 200 # Número máximo de generaciones estancadas
pmutacion = 0.05 # Probabilidad de mutacion
pcruze = 0.5 # Probabilidad de cruze
tcruze # Tipo de cruce

individuo = # Mapeo del individuo
gen = # Mapeo del gen
tgenes = # Numero genes


class Gen:
    def __init__(self):
        # Nuevo gen Aleatorio

class Individuo(BaseClassName):
    global tgenes
    def __init__(self):
        self.score = 0
        self.genes = {}
        for j in range(tgenes):
            self.genes[j] = Gen()

    def evaluar(self):
        self.score = 0
        # TODO

    def mutarGen(self):
        for i in range(tgenes):
            if random() >= 0.99: #TODO No hacerlo hardcoded
                self.genes[i] = Gen()

class Pool:
    global maxgenest,pcruze,tgenes,pmutacion,tpob
    def __init__(self):
        self.estancadas = 0
        self.generaciones = 0
        self.best = Program()
        self.previouspool = {}
        self.pool = {} # Población, lista de programas.
        self.pmv = pmutacion
        for i in range(tpob):
            self.previouspool[i] = Program()
        self.evaluar()

    def evaluar(self):
        for i in range(len(self.pool)):
            self.pool[i].evaluar()
            if (self.pool[i].score > self.best.score):
                self.best = self.pool[i]
                self.estancadas = 0

    def doSearch(self):
        print("Generación "+str(self.generaciones)+ "Score máximo: "+str(self.best.score))
        while (self.convergencia()):
            self.generaciones += 1
            self.estancadas += 1
            self.seleccionar()
            self.cruzar()
            self.mutarPoblacion()
            self.evaluar()
            self.combinar()
            print("Generación "+str(self.generaciones)+ "Score máximo: "+str(self.best.score))
            #for i in range(len(self.pool[1].m)):
               # print(str(self.pool[1].m[i]))

    def convergencia(self):
        if self.estancadas >= maxgenest:
            print("Programa:")
            for i in range(len(self.best.genes)):
                print(self.best.genes[i])
            print("Memoria:")
            self.best.evaluarfinal()
            for i in range(len(self.best.m)):
                print(str(self.best.m[i]))
            return False
        return True

    # Selección fija de la mitad mejor
    def seleccionar(self):
        # ordenar programas por score
        # sorted(self.previouspool, key=lambda program: program.score, reverse=True)
        # sorted(self.previouspool, key=(self.previouspool.get).score())
        ppl = sorted(self.previouspool.values(), key=operator.attrgetter('score'), reverse=True)
        self.pool = {}
        #Elegir n primeros
        for i in range(int(len(self.previouspool)/2)):
            self.pool[i] = copy.copy(ppl[i])

    def cruzar(self):
        # Es una permutacion? -> Grafo
        # De momento por un punto
        for i in range(len(self.pool)):
            if random() >= pcruze:
                j = randint(0,int(tpob/2)-1) # pareja
                k = randint(0,tgenes) #pto cruze
                while k < tgenes:
                    self.pool[i].genes[k], self.pool[j].genes[k] = self.pool[j].genes[k],self.pool[i].genes[k]
                    k += 1

    def mutarPoblacion(self):
        # Sobre el programa
        self.pmv = self.pmv + ((1 - self.pmv) / 200); # Mutación dinámica
        for i in range(len(self.pool)):
            if random() >= self.pmv:
                mutarIndividuo(self.pool[i])

    def mutarIndividuo (self, individuo):
        for i in range(tgenes):
            if random() >= 0.99: #TODO No hacerlo hardcoded
                individuo.genes[i].mutarGen()

    def combinar(self):
        # N primeros + n hijos
        # sorted(self.pool, key=lambda program: program.score, reverse=True)
        pl = sorted(self.pool.values(), key=operator.attrgetter('score'), reverse=True)

        tpobhalf = int(tpob/2)
        for i in range(tpobhalf):
            self.previouspool[tpobhalf+i] = pl[i]


def score(endpoints, requests, caches):
    sumatorio, TotalRequest = 0, 0
        for i in range(len(requests)):
            TotalRequest += requests[i].nRequest
            sumatorio += (endpoints[i].latency_DC -  latencias_cache_minima()  ) * requests[i].nRequest
        return sumatorio*1000 / TotalRequest

def latencias_cache_minima(IDV,endpoint,caches):
    copia = endpoint.caches.copy() #caches
    for i in range(len(copia)):
        idcache = copia[i][1] #ID cache
        lista_IDV_coincidente = filter( lambda x : x == IDV,caches[idcache].videos)
        if (len(lista_IDV_coincidente))
            copia.pop([i])
    se = sorted(copia, key=lambda student: student[1], reverse=False))
    if len(se) == 0:
        return endpoint.latency_DC
    return se[0][1]



             latency_DC - endpoints[requests[i].].IDV
            # calcular la diferencia entre el tiempo de servir el video i desde el datacenter o el servidor de la menor latencia
             hacer un sumatorio de las diferencias y multiplicar por el numero de request de i
        EL resultado de la linea anterio *1000 y / ntotal request
        ntotal request = sumatorio numero de requests de todos los i




pool = Pool()
pool.doSearch()
