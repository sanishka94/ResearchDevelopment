import copy

class Time:
	'''Represents the time of day.
	attributes: hour, minute, second
	'''

def print_time(t):
	print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))

def is_after(t1, t2):
	t1_t = t1.hour*3600 + t1.minute*60 + t1.second
	t2_t = t2.hour*3600 + t2.minute*60 + t2.second
	return t1_t > t2_t

def add_time_old(t1, t2):
	sum = Time()
	sum.hour = t1.hour + t2.hour
	sum.minute = t1.minute + t2.minute
	sum.second = t1.second + t2.second
	if sum.second >= 60:
		sum.second -= 60
		sum.minute += 1
	if sum.minute >= 60:
		sum.minute -= 60
		sum.hour += 1
	return sum

def increment_m(time, seconds):
	time.second += seconds
	time.minute += time.second // 60
	time.second = time.second % 60
	time.hour += time.minute // 60
	time.minute = time.minute % 60
	nextday = time.hour > 24
	time.hour = time.hour % 24
	return nextday

def increment_p(time, seconds):
	t = Time()
	t.second = time.second + seconds
	t.minute = time.minute + t.second // 60
	t.second = t.second % 60
	t.hour = time.hour + t.minute // 60
	t.minute = t.minute % 60
	nextday = t.hour > 24
	t.hour = t.hour % 24
	return t, nextday

def valid_time(time):
	if time.hour < 0 or time.minute < 0 or time.second < 0:
		return False
	if time.minute >= 60 or time.second >= 60:
		return False
	return True

def add_time(t1, t2):
	if not valid_time(t1) or not valid_time(t2):
		raise ValueError('invalid time object in add_time')
	return int_to_time(time_to_int(t1) + time_to_int(t2))

def increment(time, seconds):
	assert valid_time(time)
	return int_to_time(time_to_int(time) + seconds)

def time_to_int(time):
	minutes = time.hour * 60 + time.minute
	seconds = minutes * 60 + time.second
	return seconds

def int_to_time(seconds):
	time = Time()
	minutes, time.second = divmod(seconds, 60)
	time.hour, time.minute = divmod(minutes, 60)
	return time

def mul_time(t, n):
	prod = time_to_int(t) * n
	return int_to_time(prod)


time = Time()
time.hour = 11
time.minute = 59
time.second = 30

time2 = Time()
time2.hour = 10
time2.minute = 20
time2.second = 3

race_time = Time()
race_time.hour = 1
race_time.minute = 48
race_time.second = 35
distance = 13
print_time(mul_time(race_time, 1/distance))


#print(is_after(time, time2))
done = add_time(time, time2)
#print_time(done)
done2, day = increment_p(time, 500)
print_time(done2)
print_time(increment(time2, 500))

print('next day: ', day)

print(time_to_int(int_to_time(3513)))
print_time(int_to_time(3513))