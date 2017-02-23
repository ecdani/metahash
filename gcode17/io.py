from time import time

files = {0:"small", 1:"medium", 2:"big"}

def filein(i):
	global files
	return "in/" + files[i] + ".in"
	
def fileout():
	return "out/" + str(int(time())) + ".out"
