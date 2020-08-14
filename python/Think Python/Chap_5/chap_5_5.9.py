def print_something(s):
	print(s)

def do_n(fn, n):
	if n <= 0:
		pass
	else:
		print_something(n)
		do_n(fn, n-1)

do_n(print_something, 5)