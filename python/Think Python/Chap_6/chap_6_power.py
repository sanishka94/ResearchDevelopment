def is_power(a, b):
	if a % b == 0 and a / b ==1:
		return True
	elif a % b == 0:
		return is_power(a/b, b)
	else:
		return False

print(is_power(90, 3))


def gcd(a, b):
	if not b == 0:
		return gcd(b, a%b)
	else:
		return a

#print(gcd(510, 320))