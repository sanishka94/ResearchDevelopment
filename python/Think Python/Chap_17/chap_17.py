class Time_old:
	'''Represents the time of day'''
	def __init__(self, hour=0, minute=0, second=0):
		self.hour = hour
		self.minute = minute
		self.second = second

	def __str__(self):
		return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

	def __add__(self, other):
		if isinstance(other, Time):
			return self.add_time(other)
		else:
			return self.increment(other)

	def __radd__(self, other):
		return self.__add__(other)

	def __lt__(self, other):
		t1 = self.hour, self.minute, self.second
		t2 = other.hour, other.minute, other.second
		return t1 < t2

	def add_time(self, other):
		seconds = self.time_to_int() + other.time_to_int()
		return int_to_time(seconds)


	def print_time(self):
		print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

	def time_to_int(self):
		minutes = self.hour*60 + self.minute
		return minutes*60 + self.second

	def increment(self, seconds):
		seconds += self.time_to_int()
		return int_to_time(seconds)

	def is_after(self, other):
		return self.time_to_int() > other.time_to_int()

class Time:
	'''Represents the time of day'''
	def __init__(self, hour=0, minute=0, second=0):
		seconds = second + minute*60 + hour*3600
		self.seconds = seconds

	def __str__(self):
		minute, second = divmod(self.seconds, 60)
		hour, minute = divmod(minute, 60)
		return '%.2d:%.2d:%.2d' % (hour, minute, second)

	def __add__(self, other):
		if isinstance(other, Time):
			return self.add_time(other)
		else:
			return self.increment(other)

	def __radd__(self, other):
		return self.__add__(other)

	def add_time(self, other):
		sec = self.seconds + other.seconds
		return int_to_time(sec)

	def print_time(self):
		print(str(self))

	def time_to_int(self):
		return self.seconds

	def increment(self, other):
		return int_to_time(self.seconds + other)

	def is_after(self, other):
		return self.seconds > other.seconds

class Point:
	'''Represents a point with x and y'''
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __str__(self):
		return '(%.d, %.d)' % (self.x, self.y)

	def __add__(self, other):
		if isinstance(other, Point):
			return self.add_point(other)
		else:
			return self.move(other)

	def __radd__(self, other):
		return self.__add__(other)

	def add_point(self, other):
		x1 = self.x + other.x
		y1 = self.y + other.y
		return Point(x1, y1)

	def move(self, other):
		x1 = self.x + other[0]
		y1 = self.y + other[1]
		return Point(x1, y1)


def int_to_time(seconds):
	return Time(0, 0, seconds)

def print_attributes(obj):
	for attr in vars(obj):
		print(attr, getattr(obj, attr))


start = Time(9, 45)
duration = Time(1, 35)
print(start + duration)
print(start + 1337)
print(1337 + start)

p1 = Point(3, 4)
change = Point(5, 5)
print(p1 + change)
print((6, 6) + p1)

t1 = Time(7, 43)
t2 = Time(7, 41)
t3 = Time(7, 37)
print(sum([t1, t2, t3]))
print(vars(t1))
print_attributes(t2)
