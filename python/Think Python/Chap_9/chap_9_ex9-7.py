

fin = open('words.txt')


def three_doubles(word):
	if len(word) < 6:
		return False
	if (word[0] == word[1]) and (word[2] == word[3]) and (word[4] == word[5]):
		print(word)
		return True
	return three_doubles(word[1:])


for lin in fin:
	if three_doubles(lin):
		print(lin)

#print(three_doubles('helloobbs'))

fin.close()