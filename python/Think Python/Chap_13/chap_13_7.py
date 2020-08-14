import string
import random
ckey = 0

tot = 0
def get_data(name):
	fin = open(name)
	glist = []
	for item in fin:
		item = item.replace('-', ' ')
		item = item.lower().strip()
		glist.extend(item.split(' '))

	return glist

def clean_data(cilist):
	global tot
	clist = []
	forbidden = string.punctuation + '1234567890'

	for item in cilist:
		flag = True
		for let in item:
			if let in forbidden:
				flag = False

		if item != '' and flag:
			clist.append(item.strip(string.punctuation))
	tot = len(clist)
	return clist
	
def word_count(alist):
	d = dict()
	for word in alist:
		d[word] = d.setdefault(word, 0) + 1

	return d

bo_words = clean_data(get_data('Nacha Regules by Manuel Galvez.txt'))
bo_words_count = word_count(bo_words)

def create_list(cdict):
	word_list = []
	cfreq_list = []
	cfreq = 0
	for word in cdict:
		word_list.append(word)
		cfreq += cdict[word]
		cfreq_list.append(cfreq)
	
	return word_list, cfreq_list
	
def random_word(wlist, nlist):
	global ckey
	ckey = 0
	rnum = random.randint(1, tot)
	bisect_search(rnum, nlist)
	return wlist[ckey]


def bisect_search(val, blist):
	global ckey
	if len(blist) == 1:
		if val <= blist[0]:
			return
		elif val > blist[0]:
			ckey += 1
			return

	m = int(len(blist)/2)
	if blist[m] < val:
		ckey += m
		bisect_search(val, blist[m:])
	else:
		bisect_search(val, blist[:m])



wlist, nlist = create_list(bo_words_count)
resdict = {}
for i in range(20):
	word = random_word(wlist, nlist)
	resdict[word] = resdict.get(word, 0) + 1

print(resdict)

