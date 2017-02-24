from syntax import getProblem
from io import filein, fileout
from classes import *
from random import shuffle


def cholon(p):
    for c in p.caches:
        x = [i for i in range(len(p.videos))] 
        shuffle(x)
        for i in x:
            if not p.videoInCache(c.IDC, x):
                # Si el video cabe en la cache
                if p.videoFit(c.IDC, x):
                    # Intsertar video en cache
                    p.videoPush(c.IDC, x)
            # random = randint(0,len(p.videos))


def score(endpoints, requests, caches):
    sumatorio, TotalRequest = 0, 0
    for i in range(len(requests)):
        TotalRequest += requests[i].nRequest
        sumatorio += (endpoints[i].latency_DC - latencias_cache_minima()) * requests[i].nRequest
    salida = sumatorio * 1000 / TotalRequest
    print salida
    return salida


def latencias_cache_minima(IDV, endpoint, caches):
    copia = endpoint.caches.copy()  # caches
    for i in range(len(copia)):
        idcache = copia[i][1]  # ID cache
        lista_IDV_coincidente = filter(
            lambda x: x == IDV, caches[idcache].videos)
        if (len(lista_IDV_coincidente)):
            copia.pop([i])
    se = sorted(copia, key=lambda student: student[1], reverse=False)
    if len(se) == 0:
        return endpoint.latency_DC
    return se[0][1]

# Parse file #0
p = getProblem(filein(1), globals())

# PARTE RIAZA - DIEGO

# iterar caches
# meter videos id aleatorios hasta que no entren mas
solucion = cholon(p)
while (true):
    b = getProblem(filein(1), globals())
    aux = cholon(b)
    if score(aux.endpoints, aux.requests, aux.caches) > score(solucion.endpoints, solucion.requests, solucion.caches):
        solucion = aux
        p = b
        n = p.notEmptyCache()
        f = open(fileout(), 'w')
        f.write(str(n) + "\n")
        for c in p.caches:
            if not c.empty():
                f.write(str(c) + "\n")
        f.close()

# Salidap
