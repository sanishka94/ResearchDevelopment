
WORD = ''
WORD_t = ''
COUNT = 0
isRed = False
DICT = []

def get_subwords(aword, alist):
	global COUNT, WORD_t, WORD, DICT, isRed
	if COUNT == 0:
		WORD_t = aword
		print(WORD, aword)
	COUNT += 1

	if aword in DICT:
		isRed = True
		if len(WORD) < len(WORD_t):
			WORD = WORD_t
		return

	for l in aword:
		blist = list(aword)
		blist.remove(l)
		bword = ''.join(blist)

		if bword == '':
			isRed = True
			if len(WORD) < len(WORD_t):
				WORD = WORD_t
				return
		if bword in alist:
			get_subwords(bword, alist)
			if isRed:
				DICT.append(bword)

mlist = []
fin = open('words.txt')
for line in fin:
	mlist.append(line.strip()) 

mlist.append('a')
mlist.append('i')


for item in mlist:
	COUNT = 0
	isRed = False
	if item[0] == 'b':
		break
	get_subwords(item, mlist)
print(WORD)

