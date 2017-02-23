from syntax import getProblem
from io import filein, fileout
from classes import *

# Parse file
p = getProblem(filein(1), globals())

# Ordenar endpoints por diferencia de latencias
sorted(p.endpoints, key = lambda x: abs(x.latency_DC - x.caches[0][1]))

# Ordenar peticiones
sorted(p.requests, key = lambda x: -x.nRequest)

# Para cada endpoint
for e in p.endpoints:
	# Para cada request
	for r in p.requests:
		# Si la peticion es del endpoint que estamos mirando
		if r.IDE == e.ID:
			# Iterar caches
			for (cid, lat) in e.caches:
				# Si el video no está en la cache
				if not p.videoInCache(cid, r.IDV):
					# Si el video cabe en la cache
					if p.videoFit(cid, r.IDV):
						# Intsertar video en cache
						p.videoPush(cid, r.IDV)
						attend = True
						break
				

# Salida
n = p.notEmptyCache()
f = open(fileout(), 'w')
f.write(str(n) + "\n")
for c in p.caches:
	if not c.empty():
		f.write(str(c) + "\n")
f.close()
