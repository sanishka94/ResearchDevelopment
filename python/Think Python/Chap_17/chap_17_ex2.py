class Kangaroo:
	def __init__(self, pouch_contents=None):
		if pouch_contents == None:
			pouch_contents = []
		self.pouch_contents = pouch_contents

	def __str__(self):
		return str(self.pouch_contents)

	def put_in_pouch(self, obj):
		self.pouch_contents.append(obj)

'''kanga = Kangaroo([1, 2])
roo = Kangaroo(['hello'])'''

kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch(1)
kanga.put_in_pouch(2)
roo.put_in_pouch(3)
kanga.put_in_pouch(roo)
print(kanga)
print(roo)
