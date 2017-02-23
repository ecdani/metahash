from time import time

files = {0:"kittens", 1:"me_at_the_zoo", 2:"trending_today", 3:"videos_worth_spreading"}

def filein(i):
	global files
	return "in/" + files[i] + ".in"
	
def fileout(name = "out"):
	return "out/" + str(name) + "-" + str(int(time())) + ".out"
