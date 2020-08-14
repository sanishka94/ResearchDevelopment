
fin = open('words.txt')

def histogram_get(s):
	d = dict()
	for c in s:
		d[c] = d.get(c, 0) + 1
	return d


def in_bisect(li, v):
	if len(li) == 1:
		if li[0] == v:
			return True
		else:
			return False

	m = int((len(li))/2)
	if li[m] > v:
		return in_bisect(li[:m], v)
	else:
		return in_bisect(li[m:], v)


#Ex 11.1
words_dict = dict()
words_list = []
c = 0
for word in fin:
	words_dict[word.strip()] = c
	words_list.append(word.strip())
	c += 1
#print('hello' in words_dict)
#print('hello' in words_list)
#print(in_bisect(words_list, 'hello'))


#Ex 11.2
def invert_dict(d):
	inverse = dict()
	for key in d:
		val = d[key]
		if val not in inverse:
			inverse[val] = [key]
		else:
			inverse[val].append(key)
	return inverse


def invert_dict_setdefault(d):
	inverse = dict()
	for key in d:
		val = d[key]
		inverse.setdefault(val, []).append(key)

	print(inverse)

h = histogram_get('brontosaurus')
#print(h)

#invert_dict_setdefault(h)


#Ex 11.3
def ack_old(m, n):
	if m == 0:
		return n + 1
	elif m > 0 and n == 0:
		return ack_old(m-1, 1)
	elif m > 0 and n > 0:
		return ack_old(m-1, ack_old(m, n-1))

known_mn = {'0,0':1, '1,0': 2, '0,1':2}
def ack(m, n):
	inp = str(m) + ',' + str(n)
	if inp in known_mn:
		return known_mn[inp]
	if m == 0:
		ans = n+1
		known_mn.setdefault(inp, ans)
		return ans
	elif m > 0 and n == 0:
		ans1 =  ack(m-1, 1)
		known_mn.setdefault(inp, ans1)
		return ans1
	elif m > 0 and n > 0:
		ans2 = ack(m-1, ack(m, n-1))
		known_mn.setdefault(inp, ans2)
		return ans2

'''
print(ack(3,6))
print(ack(3,7))
print(ack(3,8))
'''

#Ex 11.4
def has_duplicates_old(li):
	so_li = sorted(li)
	z = ''
	for va in li:
		if va == z:
			return True
		else:
			z = va
	return False

def has_duplicates(li):
	d = dict()
	for va in li:
		if va in d:
			return True
		d[va] = 0
	return False

t = [1,2,3,4,5,6,7,1,9]
print(has_duplicates(t))