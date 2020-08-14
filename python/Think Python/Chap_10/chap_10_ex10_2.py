import random


t = [1,2,3,4,5,6,7,8,9,10]

#Ex 10.2
def cumsum(li):
	culi = []
	x = 0
	for va in li:
		x += va
		culi.append(x)
	return culi

print(cumsum(t))

#Ex 10.3
def middle(li):
	new_li =  li[1:-1]
	return new_li

print(middle(t))

#Ex 10.4
def chop(li):
	del li[0]
	del li[-1]

chop(t)
print(t)

#Ex 10.5
def is_sorted(li):
	so = sorted(li)
	return so == li

y = [1,2,4,3]

print(is_sorted(y))

#Ex 10.6
def is_anagram(s1, s2):
	l1 = list(s1)
	l2 = list(s2)
	return sorted(l1) == sorted(l2)

print(is_anagram('loow', 'owll'))

#Ex 10.7
def has_duplicates(li):
	so_li = sorted(li)
	z = ''
	for va in li:
		if va == z:
			return True
		else:
			z = va
	return False

print(has_duplicates([1, 2, 2, 2]))


#Ex 10.8
y = 1
c = 0
tot = 100001
while y < tot:
	y += 1
	
	x = 1
	birthdays = []
	while x < 24:
		day_of_year = random.randint(1, 365)
		birthdays.append(day_of_year)
		x += 1

	if has_duplicates(birthdays):
		c += 1

print(int((c/tot)*100), '%')




