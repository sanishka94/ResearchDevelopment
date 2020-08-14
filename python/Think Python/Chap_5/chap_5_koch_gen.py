import turtle

def koch(k, length):
	if length < 3:
		k.fd(length)
		return
	l = length//3
	koch(k, l/1.5)
	k.lt(60)
	koch(k, l/1.5)
	k.rt(120)
	koch(k, l/1.5)
	k.lt(60)
	koch(k, l/1.5)

koch(turtle.Turtle(), 3000)

turtle.mainloop()