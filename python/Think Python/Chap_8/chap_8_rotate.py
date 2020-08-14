
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


print(rotate_word('cheer', 7))

