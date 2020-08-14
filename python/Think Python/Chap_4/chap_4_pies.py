import math
import turtle

pie = turtle.Turtle()

"""
c: center angle
a: interior edge angle
b: exterior edge angle
r: radius
s: side length
p: number of sides
"""

p = 5
c = 360/p
r = 50

print(c)

a = (180-c)/2
b = 180-a
s = int(2*(r*math.cos((a/180)*math.pi)))
print(b)
print(s)
pie.pu()
pie.pd()
for i in range(p):
	pie.fd(r)
	pie.lt(b)
	pie.fd(s)
	pie.lt(b)
	pie.fd(r)
	pie.lt(180)

turtle.mainloop()