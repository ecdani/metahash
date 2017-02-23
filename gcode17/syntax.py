from gcode17 import parse
import classes

structure = """

"""

def getProblem(filein):
	global structure
	return parse(filein, structure, globals())
