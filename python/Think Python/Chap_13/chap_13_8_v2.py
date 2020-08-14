import string
import random

suffix_map = {}
prefix = []

def get_data(name):
	alist = []
	fin = open(name)
	skip_header(fin)

	for line in fin:
		words = line.split(' ')
		for word in words:
			word = word.strip(string.punctuation + '.,\n ')
			if word != '': alist.append(word.lower())
	return alist

def skip_header(alist):
	for line in alist:
		if line.startswith('CHAPTER I'): break

def create_map(alist, leng = 2):
	global suffix_map, prefix

	for word in alist:
		if len(prefix) < leng:
			prefix.append(word)
		elif len(prefix) >= leng:
			prefix = prefix[1:] + [word]
			add_to_map(prefix[0], tuple(prefix[1:]))

def add_to_map(pre, suf):
	global suffix_map
	suffix_map.setdefault(pre, [])
	suffix_map[pre] += [suf]

def create_sentence(alist, rec=1):
	global suffix_map
	sent = ''
	for c in range(rec):
		pref = random.choice(alist)
		suff = random.choice(suffix_map[pref])
		suff = ' '.join(suff)
		sent += pref + ' ' + suff + ' '	
	print(sent)

word_list = get_data('emma.txt')
create_map(word_list, 3)
create_sentence(word_list, 3)

