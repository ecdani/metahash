from gcode17 import parse
import classes

structure = """
Main = Int Int Int Int Int -> Videos -> 2@Endpoint -> 3@Request | Problem
Videos = *Int
Endpoint = Int Int -> 2@Cache | EndPoint
Cache = Int Int | pair
Request = Int Int Int | Request
"""

def getProblem(filein, dictionary):
	global structure
	dictionary['pair'] = (lambda x, y: (x,y))
	return parse(filein, structure, dictionary)
