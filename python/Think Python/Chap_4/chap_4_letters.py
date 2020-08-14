import turtle
import math

H = 40 #height
W = 40 #width
D = 44 #Diagonal length
DA = 63.4
S = 30 #steps for curves

def diag_u(le):
	le.lt(DA)
	le.fd(44)
	le.rt(DA)

def diag_d(le):
	le.rt(DA)
	le.fd(44)
	le.lt(DA)

def curve(le, r):
	curve_length = int(math.pi*r)
	step_length = curve_length/S
	step_angle = 180/S
	le.fd(H/4)
	for i in range(S):
		le.fd(step_length)
		le.lt(step_angle)
	le.fd((H/4)+step_length)
	le.lt(180)

letter = turtle.Turtle()

def draw_a(le):
	diag_u(le)
	diag_d(le)
	le.pu()
	le.lt(180-DA)
	le.fd(22)
	le.lt(DA)
	le.pd()
	le.fd(20)
	le.pu()
	le.lt(DA)
	le.fd(22)
	le.lt(180-DA)
	le.fd(45)
	le.pd()

def draw_b(le):
	curve(le, H/4)
	curve(le, H/4)
	le.rt(90)
	le.fd(40)
	le.lt(90)
	le.pu()
	le.fd(30)
	le.pd()

def draw_c(le):
	le.pu()
	le.fd(25)
	le.lt(90)
	le.fd(40)
	le.lt(90)
	le.pd()
	curve(le, H/2)
	le.lt(180)
	le.pu()
	le.fd(5)
	le.pd()

draw_a(letter)
draw_b(letter)
draw_c(letter)
draw_b(letter)
turtle.mainloop()
