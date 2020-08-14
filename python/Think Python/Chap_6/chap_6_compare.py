import math

def compare(x, y):
	if x > y:
		return 1
	elif x == y:
		return 0
	else:
		return -1

#print(compare(-1, 1))

def hypotenuse(x, y):
	xx = x**2
	yy = y**2
	yy_xx = xx + yy
	h = math.sqrt(yy_xx)
	return h

test = hypotenuse(5, 4)
#print(test)

def is_between(x, y, z):
	return x <= y <= z

#print(is_between(1, 6, 6))

def factorial(n):
	if not isinstance(n, int):
		print('Factorial is only defined for integers.')
	elif n < 0:
		print('Factorial is not defined for negative integers.')
	elif n == 0:
		return 1
	else:
		return n * factorial(n-1)

print(factorial(1.5))

