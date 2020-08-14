
fin = open('words.txt')

'''
def has_no_e(f):
	total = 0
	e_total = 0
	for line in fin:
		word = line.strip()
		total += 1
		if not 'e' in line:
			print(word)
			e_total += 1

	return int((e_total/total)*100)


print(has_no_e(fin))
'''

'''
def avoids(f, fb):
	for line in f:
		for l in fb:
			if l in line:
				have_l = 1
		if have_l == 0:
			print(line.strip())
		have_l = 0

avoids(fin, 'eaoiuysrp')
'''

'''
def uses_only(word, letters):
	for l in word:
		if not l in letters:
			return False
	return True

print(uses_only('herhhrretae', 'hrte'))
'''

'''
def uses_all(f, letters):
	have = 0
	count = 0
	for line in f:
		for l in letters:
			if l in line:
				have += 1
		if have == len(letters):
			print(line)
			count += 1
		have = 0
	print(count)

uses_all(fin, 'aeiou')
'''

def is_abe_rec(word):
	if len(word) <= 1:
		print(word)
		return True
	if word[0] > word[1]:
		return False
		print(word)
	return is_abe_rec(word[1:])


for lin in fin:
	print(is_abe_rec(lin))
		#print(lin)


print(is_abe_rec('flossy'))
		
fin.close()



