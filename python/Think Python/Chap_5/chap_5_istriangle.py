def is_triangle(a, b, c):
	if a >= b+c or b >= a+c or c >= a+b:
		print('No')
	else:
		print('Yes')

A = int(input('A = '))
B = int(input('B = '))
C = int(input('C = '))

is_triangle(A, B, C)