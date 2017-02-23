from gcode17 import parse

class Problem:
	def __init__(self, size, commands):
		self.size = size
		self.commands = commands

class Command:
	pass

class Box(Command):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
	def __str__(self):
		return "box(%d,%d,%d,%d)" % (self.x , self.y, self.width, self.height)
		
class Circle(Command):
	def __init__(self, x, y, radius, params):
		self.x = x
		self.y = y
		self.radius = radius
		self.params = params
	def __str__(self):
		return "circle(%d,%d,%d," % (self.x, self.y, self.radius) + str(self.params) + ")"
		
class Form(Command):
	def __init__(self, x, params):
		self.x = x
		self.params = params
	def __str__(self):
		return "form(%d," % self.x + str(self.params) + ")" 

struct = """
Main = Int -> 1@Command | Problem
Command = circle Int Int Int -> Wii | Circle
Wii = *Int
Command = box Int Int Int Int | Box
Command = form Int *Int | Form"""

_, main = parse("in.txt", struct, globals())

print main.size
print map(str, main.commands)
