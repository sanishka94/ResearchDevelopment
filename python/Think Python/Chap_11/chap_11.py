
eng2sp = dict()

eng2sp['one'] = 'uno'
eng2sp = {'one':'uno', 'two':'dos', 'three':'tres'}

print(eng2sp['two'])
print(len(eng2sp))

print('one' in eng2sp)
print('uno' in eng2sp)

vals = eng2sp.values()
print('uno' in vals)

def histogram(s):
	d = dict()
	for c in s:
		if c in d:
			d[c] += 1
		else:
			d[c] = 1
	return d

def histogram_get(s):
	d = dict()
	for c in s:
		d[c] = d.get(c, 0) + 1
	return d

print(histogram('brontosaurus'))
print(histogram_get('brontosaurus'))


def reverse_lookup(d, v):
	for k in d:
		if d[k] == v:
			return k
	raise LookupError('value does not appear in the dictionary')

h = histogram_get('parrot')
key = reverse_lookup(h, 2)
print(key)

known = {0:0, 1:1}

def fibonacci(n):
	if n in known:
		return known[n]

	res = fibonacci(n-1) + fibonacci(n-2)
	known[n] = res
	return res

count = 3

def example():
	global count
	count += 1

example()
print(count)
