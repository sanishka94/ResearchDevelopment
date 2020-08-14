
def dict_to_tuple():
	d = {'a':0, 'b':1, 'c':2}
	t = d.items()
	print(t)

	for key, value in d.items():
		print(key, value)

def tuple_to_dict():
	t = [('a', 0),('b', 1),('c',2)]
	d = dict(t)
	print(d)

def tuple_dict_zip():
	d = dict(zip('abc', range(3)))
	print(d)


dict_to_tuple()
tuple_to_dict()
tuple_dict_zip()