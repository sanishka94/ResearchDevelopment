
'''part 1
def reverse(w):
	n=1
	while n <= len(w):
		print(w[-n])
		n += 1

reverse('hello')

fruit = "banana"
for letter in fruit:
	print(letter)
'''

''' part 2
prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
	if letter == 'O' or letter == 'Q':
		print(letter + 'u' + suffix)
	else:
		print(letter + suffix)

print(prefixes[:])
'''

def find(word, letter, start):
	index = start
	while index < len(word):
		if word[index] == letter:
			return index
		index += 1
	return -1

#print(find('hellohdgfhasdlguhdbvqwertyewirup', 'r', 10))

def count_letter(word, ch):
	count = 0
	pos = 0
	while pos != -1:
		pos = find(word, ch, pos+1)
		count += 1
	print(count-1)

count_letter('baananananana', 'a')
