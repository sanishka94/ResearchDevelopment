from collections import namedtuple

def printall(*args, **kwargs):
	print(args, kwargs)

def _namedtuple_():
	Point = namedtuple('Point', ['x', 'y'])
	p = Point(1, 2)
	print(p)
	print(p.x, p.y)
	print(p[0], p[1])
	x, y = p
	print(x, y)

def _printall_():
	printall(1, 2, letter = 'A')
	Point = namedtuple('Point', ['x', 'y'])
	d = dict(x=1, y=2)
	p = Point(**d)
	print(p.y)

#_namedtuple_()
_printall_()
