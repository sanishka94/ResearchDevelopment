
fin = open('words.txt')

def rotate_word(w, r):
	res = ''
	r = r % 26
	for l in w:
		if l.islower():
			case = 97
		else:
			case = 65

		i = (ord(l)-case)
		new_i = ((i+r)%26)+case
		c = chr(new_i)
		res = res + c
	return res

d = dict()
for word in fin:
	d[word.strip()] = []


def rotate_pairs(li):
	for wo in li:
		c = 1
		while c < 26:
			rot_wo = rotate_word(wo, c)
			if rot_wo in li:
				print(wo + ' ' + rot_wo)
			li.setdefault(wo, []).append(rot_wo)
			c += 1


rotate_pairs(d)