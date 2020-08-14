import turtle
import math

N = 5 #
S = 40 #steps per circle
R = 200

def grid(gr):
	gr.pu()
	gr.bk(500)
	gr.pd()
	gr.fd(1000)
	gr.bk(500)
	gr.lt(90)
	gr.pu()
	gr.bk(500)
	gr.pd()
	gr.fd(1000)
	gr.pu()
	gr.bk(500)
	gr.rt(90)
	gr.pd()


def curve(sp):
	r_inc = R/(N*S)
	r = 0
	for i in range(N*S):
		r = r + r_inc
		curve_length = int(math.pi*r)
		step_length = curve_length/S
		step_angle = 360/S
		sp.fd(step_length)
		sp.lt(step_angle)
		sp.fd(step_length)

spiral = turtle.Turtle()

grid(spiral)
curve(spiral)

turtle.mainloop()