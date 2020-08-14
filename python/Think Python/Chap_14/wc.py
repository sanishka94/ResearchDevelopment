def linecount(filename):
	count = 0
	for line in open(filename):
		count += 1
	return count

#print(linecount('chap_14_8.py'))
print(__name__)
if __name__ == '__main__':
	print(linecount('wc.py'))
