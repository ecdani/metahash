from syntax import getProblem
from io import filein, fileout
from classes import *

# Parse file #0
p = getProblem(filein(1), globals())

################################## PARTE RIAZA - DIEGO

# Ordenar peticiones
#sorted(p.request, key = lambda x: x.nRequest)

# Atender request
#for r in p.request:
#	caches = sort(p.endpoints[r.id].lattency, key = lambda (a,b): b)
#	for c in cache:
#		pass






################################## PARTE DANIEL - JOSE  

def algoritmo(requests,endpoints):
    sr = sorted(requests, key=operator.attrgetter('nRequest'), reverse=False))
    se = sorted(requests, key=lambda student: student[2], reverse=True))

