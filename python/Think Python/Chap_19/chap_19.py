import math
from collections import Counter

#short conditional statement
def factorial(n):
	return 1 if n == 0 else n * factorial(n-1)

class Kangaroo:
	def __init__(self, name, contents=None):
		self.name = name
		self.pouch_contents = [] if contents == None else contents

x = -1
y = math.log(x) if x > 0 else float('nan')

#short for loop
def capitalize_all(t):
	return [s.capitalize() for s in t]

def is_upper(t):
	return [s for s in t if s.isupper()]

g = (x**2 for x in range(5))
print(next(g))

for val in g:
	print(val)
print(sum(x**2 for x in range(5)))

#any and all functions
print(any([False, True, False]))

print(any(letter == 't' for letter in 'monty'))

def avoids(word, forbidden):
	return not any(letter in forbidden for letter in word)
#when user any with a generator expression, it stops immediately once it becomes true
def uses_all(word, required):
	for letter in required:
		if letter not in word:
			return False
	return True

	return all(letter in word for letter in required)

def subtract(d1, d2):
	return set(d1) - set(d2)

def has_duplicates(t):
	return len(set(t)) < len(t)

def uses_only(word, available):
	return set(word) <= set(available)

def avoids(word, forbidden):
	return len(set(word).intersection(set(forbidden))) == 0

print(avoids('hello', 'mine'))

#Counters
count = Counter('Parrot')
print(count)

def is_anagram(word1, word2):
	return Conter(word1) == Counter(word2)

for val, freq in count.most_common(3):
	print(val, freq)