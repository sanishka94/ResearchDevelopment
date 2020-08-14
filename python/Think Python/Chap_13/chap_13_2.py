import random

for i in range(10):
	x = random.random()
	y = random.randint(5, 10)
	#print(x)
	#print(y)

t = [1, 2, 4, 3]
#print(random.choice(t))

h = ['a', 'b', 'b', 'd']


def histogram(s):
	d = dict()
	for c in s:
		if c in d:
			d[c] += 1
		else:
			d[c] = 1
	return d

def choose_from_hist(ahist):
	r = random.randint(0, len(ahist)-1)
	return ahist[r]

runs = 40000
res = []
for i in range(runs):
	res.append(choose_from_hist(h))


adict = histogram(res)
for val in adict:
	prob = (adict[val]/runs)*100
	print(val, str(prob), sep='\t')

