


def pal_num(num):
	if num <= 99999:
		return False
	if str(num)[2:] == (str(num)[2:])[::-1]:
		num += 1
		if str(num)[1:] == (str(num)[1:])[::-1]:
			num += 1
			if str(num)[1:5] == (str(num)[1:5])[::-1]:
				num += 1
				if str(num) == str(num)[::-1]:
					print(num-3)


i=100000
while i < 1000000:
	pal_num(i)
	i += 1
