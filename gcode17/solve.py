from syntax import getProblem
from io import filein, fileout
from classes import *

# Parse file #0
p = getProblem(filein(0), globals())

################################## PARTE RIAZA - DIEGO

# Ordenar peticiones
sorted(p.requests, key = lambda x: -x.nRequest)

# Para cada peticion
for r in p.requests:
	# Ordenar caches por latencia
	caches = sorted(p.endpoints[r.IDE].caches, key = lambda (a,b): b)
	# Iterar caches
	for (cid, lat) in caches:
		# Si el video no esta en la cache
		if not p.videoInCache(cid, r.IDV):
			# Si el video cabe en la cache
			if p.videoFit(cid, r.IDV):
				# Intsertar video en cache
				p.videoPush(cid, r.IDV)
				break
		# Si el video ya esta en al cache
		else:
			# Terminar
			break

# Salida
n = p.notEmptyCache()
f = open(fileout(), 'w')
f.write(str(n) + "\n")
for c in p.caches:
	if not c.empty():
		f.write(str(c) + "\n")
f.close()
