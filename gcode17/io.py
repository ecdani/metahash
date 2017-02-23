from time import time

files = {0:"small", 1:"medium", 2:"big"}

def filein(i):
	global files
	return "in/" + files[i] + ".in"
	
def fileout(name = "out"):
	return "out/" + str(name) + "-" + str(int(time())) + ".out"
