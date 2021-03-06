import operator, copy
from random import randint, random

class Gen:
    """Esto es una clase generica que representa un gen, hay que reescribir esta la estructura generica 
    por lo que se entienda que es un gen en el problema dado.
    El init será la función que genere un gen aleatorio. Hay que escribirla.
    """
    # Nuevo gen Aleatorio
    def __init__(self):
        pass

    def mutar(self):
        self.__init__()

class Individuo():
    """Esta clase generica representa al individuo, que es una coleccion de genes. 
    Es la definición del gen lo que hace que un individuo sea una partición de la pizza,
    distribucion de videos de youtube, una secuencia de comandos de impresion, etc.
    Hay que definir la evaluación reescribiendo evaluar.
    """
    #global ngenes
    def __init__(self,GENETIC_CONFIG):
        self.conf = GENETIC_CONFIG
        self.score = 0 # Rango de 0 a 1
        self.genes = []
        for j in range(self.conf.ngenes):
            self.genes.append(self.conf.gencls())
        self.evaluar()

    def evaluar(self):
        self.score = 0
        #for i in range(ngenes):
        #    self.score +=self.genes[i].video

    #def mutarGen(self):
       # random.choice(self.genes) = Gen()
    
    def irradiar(self):
        for i in range(self.conf.ngenes):
            if random() <= self.conf.pmutacion:
                self.genes[i].mutar()

class Pool:
    """La piscina, la población y su gestión AKA algoritmo genético.
    Esta clase en teoria no necesita ser tocada para crear un algoritmo genético,
    solo las clases Inviduo y Gen. Esta clase lo unico que necesita es la clase GENETIC_CONFIG
    como parámetro, que es una serie de atributos de configuración nada mas.

    class GENETIC_CONFIG:
        gencls = Instruccion # Clase Gen
        individuocls = Impresion # Clase Individuo
        tpob = 20 # Tamaño de la población (Numero par plz)
        maxgenest = 100 # Número máximo de generaciones estancadas
        pmutacion = 0.5 # Probabilidad de mutacion
        pcruze = 0.5 # Probabilidad de cruze
        ngenes = 10 # Numero genes
    """
    def __init__(self,GENETIC_CONFIG):
        self.conf = GENETIC_CONFIG
        #self.individuocls = IndividuoCls
        self.estancadas = 0
        self.generaciones = 0
        self.best = self.conf.individuocls(GENETIC_CONFIG)
        self.previouspool = []
        self.pool = [] # Población que juega, la mitad de previous pool.
        self.pmv = self.conf.pmutacion # Probabilidad de mutacion variable
        for i in range(self.conf.tpob):
            self.previouspool.append(self.conf.individuocls(GENETIC_CONFIG)) # Precargamos de individuos todo
        #self.evaluar() # Evaluacion inicial

    def evaluar(self):
        for i in range(len(self.pool)):
            self.pool[i].evaluar() # evaluamos cada individuo
            if (self.pool[i].score > self.best.score): # Si es mejor individuo que el mejor...
                self.best = self.pool[i]
                self.estancadas = 0
                self.pmv = self.conf.pmutacion
                print(self.best)
                self.imprimir()
    def imprimir(self):
        pass

    # Arquitectura de un algoritmo genético.
    def doSearch(self):
        print("Generación "+str(self.generaciones)+ "Score máximo: "+str(self.best.score))
        while (self.convergencia()):
            self.generaciones += 1
            self.estancadas += 1
            self.seleccionar()
            #self.seleccion_rango()
            self.cruzar()
            self.mutarPoblacion()
            self.evaluar()
            #self.combinar_simple()
            self.combinar()
            print("Generación "+str(self.generaciones)+ "Score máximo: "+str(self.best.score))
            #for i in range(len(self.pool[1].m)):
               # print(str(self.pool[1].m[i]))

    def convergencia(self):
        """Comprueba si hay convergencia (suficientes generaciones estancadas)
        e imprime el resultado
        """
        if self.estancadas >= self.conf.maxgenest:
            print("Genes finales del mejor alcanzado al converger:")
            self.best.exportar()
            #for i in range(len(self.best.genes)):
                #self.best.genes[i])
                
            return False
        return True

    def seleccion_rango(self):
        self.previouspool.sort(key=operator.attrgetter('score'), reverse=True)
        self.pool = []
        n = self.conf.tpob
        while len(self.pool) != len(self.previouspool):
            for i, individuo in enumerate(self.previouspool):
                p_i = ((2*(n-i+1)) / (n**2 + n))
                if random() <= p_i:
                    #p(i) = (2(n-i+1)) / (n**2 + n)
                    self.pool.append(copy.deepcopy(self.previouspool[i]))
                if len(self.pool) == len(self.previouspool):
                    break


    def seleccionar(self):
        """Selección fija de la mitad mejor. Desde previouspool a pool
        NO FUNCA"""
        # ordenar programas por score
        # sorted(self.previouspool, key=lambda program: program.score, reverse=True)
        # sorted(self.previouspool, key=(self.previouspool.get).score())
        #self.previouspool = sorted(self.previouspool.values(), key=operator.attrgetter('score'), reverse=True)
        self.previouspool.sort(key=operator.attrgetter('score'), reverse=True)
        self.pool = []
        #Elegir n primeros
        for i in range(int(len(self.previouspool)/2)):
            self.pool.append(copy.deepcopy(self.previouspool[i]))

    def cruzar(self):
        """Cruce de los seleccionados entre si. No generan hijos, sino que cada individuo
        puede recombinarse con otro con pcruze probabilidad. No es el mejor cruze. Ya.
        """
        # Es una permutacion? -> Grafo
        # De momento por un punto
        for i in range(len(self.pool)):
            #if random() <= self.conf.pcruze*self.pool[i].score:
            j = randint(0,int(self.conf.tpob/2)-1) # pareja
            k = randint(0,self.conf.ngenes) #pto cruze
            while k < self.conf.ngenes:
                self.pool[i].genes[k], self.pool[j].genes[k] = copy.deepcopy(self.pool[j].genes[k]), copy.deepcopy(self.pool[i].genes[k])
                k += 1

    def mutarPoblacion(self):
        # Sobre el programa
        self.pmv = self.pmv + ((1 - self.pmv) / 2000); # Mutación dinámica
        #print(self.pmv)
        for i in range(len(self.pool)):
                self.pool[i].irradiar()

    def combinar_simple(self):
        self.previouspool = copy.deepcopy(self.pool)
        print(self.previouspool)
    
    def combinar(self):
        # N primeros + n hijos
        # sorted(self.pool, key=lambda program: program.score, reverse=True)
        #pl = sorted(self.pool.values(), key=operator.attrgetter('score'), reverse=True)
        self.pool.sort(key=operator.attrgetter('score'), reverse=True)

        tpobhalf = int(self.conf.tpob/2)
        for i in range(tpobhalf-1):
            self.previouspool[tpobhalf+i] = copy.deepcopy(self.pool[i])

        #print(self.previouspool)

