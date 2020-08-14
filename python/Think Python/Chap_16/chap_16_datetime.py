from datetime import *

def age(bday):
	dnow = datetime.now()
	aage = dnow - bday
	return aage

def time_till_next_bday(bday):
	dnow = datetime.now()
	next_year = bday.year + (age(bday).days // 365) + 1
	new_bday = datetime(next_year, bday.month, bday.day)
	return new_bday - dnow

def doubleday(bday1, bday2):
	return max(bday1, bday2) + abs(bday1 - bday2)

def n_day(bday1, bday2, n):
	return min(bday1, bday2) + ((abs(bday1 - bday2))/(n-1))*n

birthday = datetime(1994, 10, 15)
birthday2 = datetime(1997, 1, 30)
print(age(birthday))
print(time_till_next_bday(birthday))
print(doubleday(birthday, birthday2))
print(n_day(birthday, birthday2, 4))