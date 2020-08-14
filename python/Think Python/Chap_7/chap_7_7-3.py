import math

'''
s = 'hello'
n = 2

while n > 0:
	print(s)
	n = n - 1
'''

'''while True:
	line = input('> ')
	if line == 'done':
		break
	print(line)

print('Done')'''

'''ex 7.1
def mysqrt(a):
	x = a/2
	while True:
		#print(x)
		y = (x + a/x)/2
		if abs(y-x) < 0.0000001:
			return y
			break
		x = y

def test_square_root(a):
	while a < 10:
		s = ' '
		c1 = str(a)
		c2 = mysqrt(a)
		c3 = math.sqrt(a)
		c4 = str(abs(c2 - c3))
		print(c1, s, str(c2), s, str(c3), s, c4)
		a = a+1

test_square_root(1)
'''

'''ex 7.3'''
def eval_loop():
	#user = ''
	while True:
		user = input()
		if user == 'done':
			print(res)
			break
		else:
			res = eval(user)
			print(res)

eval_loop()