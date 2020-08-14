import math

def estimate_pi():
	con = 2*(math.sqrt(2))/9801
	diff = 1e-15
	k = 0
	tot = 0
	while True:
		cur = ((math.factorial(4*k))+(1103+26390*k))/(((math.factorial(k))**4)*(396**(4*k)))
		tot += (con * cur)
		if abs(con*cur) < diff:
			break
		k += 1
	pi = 1/tot
	print('estimated pi is: ' + str(pi))
	print('actual pi is: ' + str(math.pi))

estimate_pi()