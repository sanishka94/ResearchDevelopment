
def check_anagrams(word_list_2):
	letter_dict = {}
	for item in word_list_2:
		word = item.lower()
		s_word = ''.join(sorted(word))
		letter_dict[s_word] = letter_dict.get(s_word, []) + [word]
	return letter_dict

def get_anagrams(word_list_1, crit):
	#crit: number of anagrams that have to be present in order to be displayed
	d = check_anagrams(word_list_1)
	d_a = {}
	for index, anagrams in d.items():
		if len(anagrams) >= crit:
			#print(index + ' : ' + ', '.join(anagrams))
			d_a[index] = anagrams
	#print(d_a)
	#most_frequent(d_a)
	#bingo(most_frequent(d_a))
	check_metathesis(most_frequent(d_a))

def most_frequent(d_1):
	hist = {}
	for i, li in d_1.items():
		tu = tuple(li)
		hist[tu] = len(li)

	anagrams_list = []
	for anagrams, nums in hist.items():
		anagrams_list.append((nums, anagrams))
		anagrams_list.sort(reverse=True)

	final = []
	for nums, anagrams in anagrams_list:
		final.append((anagrams, nums))
		#print(', '.join(anagrams) + ' : ' + str(nums))

	return final

def bingo(l_2):
	for anagrams, index in l_2:
		if len(anagrams[0]) >= 8:
			print(anagrams)
			return

res = []

def is_metathesis(s1, s2):
	#this method assumes s1 and s2 are anagrams
	global res
	i = 0
	c = 0
	while i < len(s1):
		if not s1[i] == s2[i]:
			c += 1
		i += 1

	if c == 2:
		min_s = min(s1, s2)
		max_s = max(s1, s2)
		if not (min_s, max_s) in res:
			res.append((min_s, max_s))
		
def check_metathesis(a_list):
	for anagrams, index in a_list:
		c1 = 0
		while c1 < len(anagrams)-1:
			c2 = 1
			while c2 < len(anagrams):
				if not anagrams[c1] == anagrams[c2]:
					is_metathesis(anagrams[c1], anagrams[c2])
				c2 += 1
			c1 += 1
	for item in res:
		print(item)


fin = open('words.txt')

words = []
for item in fin:
	words.append(item.strip())

get_anagrams(words, 4)
