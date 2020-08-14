import turtle

'''def koch(k, length):
	if length < 3:
		return
	l = length//3
	k.fd(l)
	k.lt(60)
	k.fd(l)
	k.rt(120)
	k.fd(l)
	k.lt(60)
	k.fd(l)'''

def koch(k, length):
	if length < 300:
		k.fd(length)
		return
	l = length//3
	koch(k, l/3)
	k.lt(60)
	koch(k, l/3)
	k.rt(120)
	koch(k, l/3)
	k.lt(60)
	koch(k, l/3)

def snowflake(k, length):
	koch(k, length)
	k.lt(60)
	koch(k, length)
	k.rt(120)
	koch(k, length)
	k.lt(60)
	koch(k, length)

def bigsnowflake(k, length):
	snowflake(k, length)
	k.lt(60)
	snowflake(k, length)
	k.rt(120)
	snowflake(k, length)
	k.lt(60)
	snowflake(k, length)

ko = turtle.Turtle()
koch(ko, 3000)

turtle.mainloop()