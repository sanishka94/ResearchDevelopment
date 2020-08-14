
cheeses = ['Cheddar', 'Edam', 'gouda']
numbers = [42, 123]
empty = []
print(cheeses, numbers, empty)
print('Edams' in cheeses)

for cheese in cheeses:
	print(cheese)

for i in range(len(numbers)):
	numbers[i] = numbers[i] * 2

print(numbers)
print(len(numbers))
print(range(3))

#list methods
t = ['a', 'b', 'd', 'r', 'c', 'g']
t.sort()
t.append('y')
t.extend(cheeses)
t.sort()
c = t
print(c)
print(sum(numbers))

print(c[7].capitalize())

#deleting items
x = t.pop(6) #if index is not provided, the last element will be selected
print(t)
print(x)

del t[3]
print(t)

t.remove('gouda')
print(t)

del t[2:4]
print(t)