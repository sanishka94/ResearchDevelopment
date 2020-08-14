t = tuple()

a, b = 1, 2

b, a = a, b

addr = 'monty@python.org'
uname, domain = addr.split('@')

print(a, b)
print(uname, domain)


t = divmod(7, 3)
td, r = divmod(7, 3)
print(td, r)

def min_max(t):
	return min(t), max(t)

print(min_max(t))

#gather
def printall(*args):
	print(args)

printall(1, 2.0, '3')

#scatter
print(divmod(*t))

def sumall(*args):
	tot = 0
	for va in args:
		tot += va
	return tot
print(sumall(1, 2, 3, 4))

#zip
s = 'abc'
n = [0, 1, 2]
print(zip(s, n))
for pair in zip(s, n):
	print(pair)

s1 = 'abcd'
s2 = 'ebsr'
for x1, x2 in zip(s1, s2):
	print(x1 == x2)

for index, element in enumerate('abc'):
	print(index, element)

