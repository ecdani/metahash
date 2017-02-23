from gcode17 import parse
import classes

structure = """
Main = Int Int Int Int Int -> Videos -> 2@Endpoint -> 3@Request | Problem
Videos = *Int
Endpoint = Int Int -> 2@Cache | Endpoint
Cache = Int Int | pair
Request = Int Int Int | Request
"""

def pair(x,y):
	return (x,y)

def getProblem(filein):
	global structure
	return parse(filein, structure, globals())
