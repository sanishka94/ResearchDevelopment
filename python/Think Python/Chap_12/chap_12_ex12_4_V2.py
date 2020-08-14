
#initialize
memo = {}
memo[''] = ['']
trail_list = []

def is_reducible(word, word_dict):
	#find if 'word' is reducible
	if word in memo: return memo[word]

	ilist = []
	for child in children(word, word_dict): 
		if is_reducible(child, word_dict): ilist.append(child)

	memo[word] = ilist
	return ilist 

def children(word, word_dict):
	#find the children of 'word'
	clist = []
	for l in range(len(word)):
		aword = word[:l] + word[l+1:]
		if aword in word_dict: clist.append(aword)
	return clist 

def get_words(file_name):
	#get words from a text file into a list
	fin = open(file_name)
	gdict = {}
	for item in fin:
		gitem = item.strip().lower()
		gdict[gitem] = gitem

	for letter in ['a', '', 'i']: gdict[letter] = letter

	return gdict 

def find_reducible(word_dict):
	#find all the reducible words
	flist = []
	for word in word_dict:
		fword = is_reducible(word, word_dict)
		if fword != []: flist.append(word)

	return flist 

def find_longest_red(flist):
	#find the longest word or words in a list
	llist = []
	for fword in flist:
		llist.append((len(fword), fword))
		llist.sort(reverse=True)
	
	flen = llist[0][0]
	for length, word in llist:
		if length == flen: return word 

def red_trail(word):
	#prove the word is reducible
	if len(word) == 0: return
	
	trail_list.append(word)
	t = is_reducible(word, word_dict)
	red_trail(t[0])
	return trail_list 


word_dict = get_words('words.txt')
red_list = find_reducible(word_dict)

#print(red_trail(find_longest_red(red_list)))

for word in red_trail(find_longest_red(red_list)): print(word, end=' ')
print('\n')




