a = 'ha'
b = 'hehehehehe'

c = b.replace('he', a, 2)

print(c)


w = 'www.hellowmynameis.com'
x = w.strip('wcom.')

print(x)


d = b.count('he', 0, 4)
print(d)


def is_palindrome(a):
	if a == a[::-1]:
		return True
	else:
		return False

print(is_palindrome('nananan'))
