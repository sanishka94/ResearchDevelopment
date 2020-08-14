import math

class Point:
	"""docstring for Point"f __init__(self, arg):
		super(Point,.__init__()
		self.arg = arg
	"""
print(Point)
blank = Point()
print(blank)

blank.x = 3.0
blank.y = 4.0

print(blank.y)
def print_point(p):
	print('(%g, %g)' % (blank.x, blank.y))

print_point(blank)

def distance_between_points(p1, p2):
	print(math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2))

full = Point()
full.x = 6
full.y = 8

distance_between_points(blank, full)