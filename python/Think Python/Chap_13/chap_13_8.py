import string
import random

ndict = {}
plist = ('the', 'a')

def get_data(name):
	fin = open(name)
	glist = []
	for item in fin:
		item = item.replace('-', ' ')
		item = item.lower().strip()
		glist.extend(item.split(' '))

	return glist

def clean_data(cilist):
	clist = []
	forbidden = string.punctuation + '1234567890'

	for item in cilist:
		flag = True
		for let in item:
			if let in forbidden:
				flag = False

		if item != '' and flag:
			clist.append(item.strip(string.punctuation))
	return clist

#word_list = clean_data(get_data('Nacha Regules by Manuel Galvez.txt'))
word_list = clean_data(get_data('emma.txt'))

def markov_analysis(alist):
	global plist, ndict
	pre_word = ''
	for word in alist:
		if pre_word in plist: ndict.setdefault(word, [])
		
		if pre_word in ndict:
			if word not in ndict[pre_word]: ndict.get(pre_word, []).append(word)

		pre_word = word

markov_analysis(word_list)

nlist = list(ndict)

def make_sentence(l=1):
	global plist, nlist, ndict
	sent = random.choice(plist)
	for c in range(l):
		noun = random.choice(nlist) 
		suffix = random.choice(ndict[noun])
		noun2 = random.choice(nlist)
		sent = sent + ' ' + noun + ' ' + suffix + ' ' + noun2
	return sent

print(make_sentence(2))