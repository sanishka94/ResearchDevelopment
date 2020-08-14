import turtle
import math

def polyline(t, n, l, a):
	"""Draws n line segments with a given length and angle
	between them. t is a turtle"""
	for i in range(n):
		t.fd(l)
		t.lt(a)

def polygon(t, n, l):
	a = 360/n
	polyline(t, n, l, a)

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

def circle(t, r):
	arc(t, r, 360)

def square(t, l):
	polyline(t, 4, l, 90)


bob = turtle.Turtle()
circle(bob,50)

turtle.mainloop()
