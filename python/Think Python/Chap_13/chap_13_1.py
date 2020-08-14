import string

def get_data(name):
	fin = open(name)
	glist = []
	for item in fin:
		temp_word = item.lower().strip()
		glist.extend(temp_word.split(' '))	

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
	
def word_count(alist):
	d = dict()
	for word in alist:
		d[word] = d.setdefault(word, 0) + 1

	return d

def sort_frequency(sdict):
	slist = []
	for item in sdict:
		slist.append((sdict[item], item))
	slist.sort(reverse=True)
	return slist


word_book = clean_data(get_data('Nacha Regules by Manuel Galvez.txt'))
word_list = get_data('words.txt')

word_book_dict = sort_frequency(word_count(word_book))

def diff_list(alist, blist):
	other_words = []
	for num, word in alist:
		if not word in blist: other_words.append(word)
	return other_words

def diff_set(alist, blist):
	aset = set(alist)
	bset = set(blist)
	return aset.difference(bset)

print(sorted(diff_set(word_book, word_list)))
#print(sorted(diff_list(word_book_dict, word_list)))

