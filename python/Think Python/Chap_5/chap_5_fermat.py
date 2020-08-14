import math

A = int(input('A = '))
B = int(input('B = '))
C = int(input('C = '))
N = int(input('N = '))

def check_fermat(a,b,c,n):
	n_sum = (a**n)+(b**n)
	n_c = c**n
	if n_sum == n_c:
		print('Holy smokes, Fermat was wrong')
	else:
		print('No, that doesn\'t work.')

check_fermat(A, B, C, N)