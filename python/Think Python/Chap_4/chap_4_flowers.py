import turtle
import math


def arc(n_a, step_length_a, step_angle_a):
	for i in range(n_a):
		pet.fd(step_length_a)
		pet.lt(step_angle_a)


def petal(t, l,angle_p):
	h_angle = int(angle_p/2)
	steps = int(360/angle_p)+4
	step_length = l/steps
	step_angle = angle_p/steps
		
	arc(steps, step_length, step_angle)
	t.fd(step_length)
	t.lt(int(180-angle_p))
	arc(steps, step_length, step_angle)
	t.fd(step_length)

pet = turtle.Turtle()
length = 100
p = 8
angle = 360/p
for x in range(p):
	petal(pet, length, angle)
	pet.lt(180)
turtle.mainloop()