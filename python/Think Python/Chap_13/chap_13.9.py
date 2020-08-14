import string
import math
import matplotlib.pyplot as plt
import numpy as np

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

word_list = get_data('emma.txt')
sorted_list = sort_frequency(word_count(word_list))

x_vals = list()
y_vals = []

def print_list(plist):
	global x_vals, y_vals
	r = 1
	for fre, wor in plist:
		lg_r = math.log10(r)
		x_vals.append(lg_r)
		log_fre = math.log10(fre)
		y_vals.append(log_fre)
		#print(wor, lg_r, log_fre, sep='\t')
		r += 1

print_list(sorted_list)

plt.plot(x_vals, y_vals)
plt.show()
slope, intercept = np.polyfit(x_vals, y_vals, 1)
c = int(10**intercept)

print('s =', slope, sep=' ')
print('log c =', intercept, sep=' ')
print('c =', c, sep=' ')

print('f = ', c, 'r^', slope, sep='')