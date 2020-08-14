
fin = open('words.txt')
words = []
for va in fin:
	words.append(va.strip())

#Ex 10.10
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


#Ex 10.11
def find_reverse_pair(li_1):
	for word in li_1:
		rev_word = word[::-1]
		if in_bisect(words, rev_word):
			print(word + ' ' + rev_word)


#Ex 10.12.1
def two_way_interlocked_pairs(li_2):
	word_1 = ''
	word_2 = ''
	for word in li_2:
		word_1 = word[::2]
		word_2 = word[1::2]
		if in_bisect(li_2, word_1) and in_bisect(li_2, word_2):
			print(word_1 + ' + ' + word_2 + ' = ' + word)

#Ex 10.12.2
def three_way_interlocked_pairs(li_3):
	word_1 = ''
	word_2 = ''
	word_3 = ''
	for word in li_3:
		word_1 = word[::3]
		word_2 = word[1::3]
		word_3 = word[2::3]
		if in_bisect(li_3, word_1) and in_bisect(li_3, word_2) and in_bisect(li_3, word_3):
			print(word_1 + ' + ' + word_2 + ' + ' + word_3 + ' = ' + word)

three_way_interlocked_pairs(words)




