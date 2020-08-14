import copy

class Point:
	"""docstring for Point"f __init__(self, arg):
		super(Point,.__init__()
		self.arg = arg
	"""

class Rectangle:
	'''Represents a rectangle
	attributes: width, height, corner
	'''

def print_point(p):
	print('(%g, %g)' % (p.x, p.y))

def move_rectangle(rect, dx, dy):
	rect.corner.x += dx
	rect.corner.y += dy

def move_rectangle_new(rect, dx, dy):
	rect2 = copy.deepcopy(rect)
	rect2.corner.x += dx
	rect2.corner.y += dy
	return rect2


def main_code_p1():
	print(box.corner.x, box.corner.y, sep='\t \t')
	move_rectangle(box, 5, 10)
	print(box.corner.x, box.corner.y, sep='\t \t')

def main_code_p2():
	print_point(p1)
	print_point(p2)
	print(p1 is p2)
	print(p1 == p2)
	print(box2 is box)
	print(box2.corner is box.corner)
	print(box3 is box)
	print(box3.corner is box.corner)

def main_code_p2ex():
	print_point(box.corner)
	box4 = move_rectangle_new(box, 20, 40)
	print_point(box.corner)
	print_point(box4.corner)
	print(box4 is box)
	print(box4.corner is box.corner)

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

p1 = Point()
p1.x = 3.0
p1.y = 4.0
p2 = copy.copy(p1)
box2 = copy.copy(box)
box3 = copy.deepcopy(box)


#main_code_p2ex()
print(type(p1))
print(isinstance(p1, Point))
print(hasattr(p1, 'x'))
print(hasattr(p1, 'z'))
print(hasattr(box, 'corner'))

p3 = Point()

#x = p3.x
#print(x)
try:
	x = p3.x
except AttributeError:
	x = 0

print(x)