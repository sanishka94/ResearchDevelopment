import anagram_sets

anagram_list = anagram_sets.all_anagrams('words.txt')

print(type(anagram_list))
olist = []
for key in anagram_list:
	if len(anagram_list[key]) > 1:
		olist.append((key, anagram_list[key]))

def store_anagrams(alist, ofile = 'anagrams.txt'):
	fout = open(ofile, 'w')
	for line in alist:
		ans = ' '.join(line[1])
		fout.write(line[0] + ', ' + ans + '\n')

def read_amagrams(aword, ifile = 'anagrams.txt'):
	fin = open(ifile)
	for line in fin:
		key, anagrams = line.split(',')
		if key == aword:
			print(anagrams)


store_anagrams(olist)
read_amagrams('abhmo')
