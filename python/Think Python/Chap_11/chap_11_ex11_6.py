

def read_dictionary(filename):
    """Reads from a file and builds a dictionary that maps from
    each word to a string that describes its primary pronunciation.

    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the
    key for the second pronunciation of "abdominal" is "abdominal(2)".

    filename: string
    returns: map from string to pronunciation
    """
    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d


if __name__ == '__main__':
    d = read_dictionary('c06d')
#    for k, v in d.items():
#       print(k, v)


def check_homophones():
	dict = read_dictionary('c06d')
	for w in dict:
		if w.isalpha() and len(w) > 3:
			print(w)
			w1 = w[1:]
			w2 = w[0] + w[2:]
			if w1 in dict and w2 in dict:
				if dict[w1] == dict[w] and dict[w2] == dict[w]:
					return w


strin = check_homophones()
print(strin)

