import math, copy, turtle

class Point:
	"""docstring for Point"f __init__(self, arg):
		super(Point,.__init__()
		self.arg = arg
	"""
class Circle:
	'''Represents a circle
	Attributes: center, radius
	'''
class Rectangle:
	'''Represents a rectangle
	attributes: width, height, corner
	'''

def arc(t, r, a):
	arc_length = int(2*math.pi*r*a/360)
	print(arc_length)
	n = int((arc_length/3)+1)
	print(n)
	step_length = arc_length/n
	print(step_length)
	step_angle = a/n
	print(step_angle)

	t.lt(step_angle/2)
	polyline(t, n, step_length, step_angle)
	t.lt(step_angle/2)

def draw_circle(t, cir):
	t.pu()
	t.fd(cir.center.x)
	t.lt(90)
	t.fd(cir.center.y - cir.radius)
	t.rt(90)
	t.pd()
	n=100
	arc_l = 2*math.pi*cir.radius
	step_l = arc_l/n
	step_a = 360/n
	for i in range(n):
		t.fd(step_l)
		t.lt(step_a)
	t.pu()
	t.rt(90)
	t.fd(cir.center.y - cir.radius)
	t.lt(90)
	t.bk(cir.center.x)
	t.pd()

def draw_rectangle(t, rec):
	t.pu()
	t.fd(rec.corner.x)
	t.lt(90)
	t.fd(rec.corner.y)
	t.pd()
	t.fd(rec.height)
	t.rt(90)
	t.fd(rec.width)
	t.rt(90)
	t.fd(rec.height)
	t.rt(90)
	t.fd(rec.width)

def distance_between_points(p1, p2):
	dist = math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)
	return dist

def print_point(p):
	print('(%g, %g)' % (p.x, p.y))

def point_in_circle(cir, p):
	dist = distance_between_points(cir.center, p)
	return dist <= 75

def rect_in_circle(cir, rect):
	pA = copy.copy(rect.corner)
	pB = copy.copy(rect.corner)
	pC = copy.copy(rect.corner)
	pD = copy.copy(rect.corner)
	pA.x += rect.width 
	pB.y += rect.height
	pC.x += rect.width
	pC.y += rect.height
	return point_in_circle(cir, pA) and point_in_circle(cir, pB) and point_in_circle(cir, pC) and point_in_circle(cir, pD)

def rect_circle_overlap_simple(cir, rect):
	pA = copy.copy(rect.corner)
	pB = copy.copy(rect.corner)
	pC = copy.copy(rect.corner)
	pD = copy.copy(rect.corner)
	pA.x += rect.width 
	pB.y += rect.height
	pC.x += rect.width
	pC.y += rect.height
	return point_in_circle(cir, pA) or point_in_circle(cir, pB) or point_in_circle(cir, pC) or point_in_circle(cir, pD)

def rect_circle_overlap_advanced(cir, rect):
	pA = copy.copy(rect.corner)
	pB = copy.copy(rect.corner)
	pC = copy.copy(rect.corner)
	pD = copy.copy(rect.corner)
	pA.x += rect.width 
	pB.y += rect.height
	pC.x += rect.width
	pC.y += rect.height
	simple =  point_in_circle(cir, pA) or point_in_circle(cir, pB) or point_in_circle(cir, pC) or point_in_circle(cir, pD)
	if pA.x >= cir.center.x >= pD.x:
		return (pD.y <= (cir.center.y + cir.radius) <= pB.y) or (pD.y <= (cir.center.y - cir.radius) <= pB.y) or simple
	elif pB.y >= cir.center.y >= pD.x:
		return (pD.x <= (cir.center.x + cir.radius) <=pA.x) or (pD.x <= (cir.center.x - cir.radius) <= pA.x) or simple
	else:
		return False


c = Circle()
c.radius = 75
c.center = Point()
c.center.x = 100
c.center.y = 170

p1 = Point()
p1.x = 226
p1.y = 100

r = Rectangle()
r.width = 100
r.height = 200
r.corner = Point()
r.corner.x = 50
r.corner.y = 80



print(rect_in_circle(c, r))
print(rect_circle_overlap_simple(c, r))
print(rect_circle_overlap_advanced(c, r))

bob = turtle.Turtle()
draw_circle(bob, c)
draw_rectangle(bob, r)
turtle.mainloop()