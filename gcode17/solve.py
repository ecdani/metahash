from syntax import getProblem
from io import filein, fileout

# Parse file #0
p = getProblem(filein(0))

################################## PARTE RIAZA - DIEGO










################################## PARTE DANIEL - JOSE  

def algoritmo(requests,endpoints):
    sr = sorted(requests, key=operator.attrgetter('nRequest'), reverse=False))
    se = sorted(requests, key=lambda student: student[2], reverse=True))

