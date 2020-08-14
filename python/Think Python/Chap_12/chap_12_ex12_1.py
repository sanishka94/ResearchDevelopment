def most_frequent(stri):
	hist = {}
	for l in stri:
		hist[l] = hist.get(l, 0) + 1

	letter_list = []
	for letter, index in hist.items():
		letter_list.append((index, letter))
		letter_list.sort(reverse=True)

	final = []
	for index, letter in letter_list:
		final.append(letter)
	

	print(final)
	


most_frequent('heldsfgodfjhgsdfjkhcxvxbdfghodhgvhdscjblwaofhyaiol')