

def rev_age():
	me = 1
	while me < 10:
		str_me = str(me).zfill(2)
		mom = int(str_me[::-1])
		if me < (mom-10):
			check_age(mom, me)
		me += 1


def check_age(mom_age, age):
	count = 0
	ages = str(age) + ' ' + str(mom_age)
	while mom_age < 100:
		str_mom_age = str(mom_age)
		str_age = (str(age)[::-1]).zfill(2)
		if str_mom_age == str_age:
			count += 1
			ages = ages + ' | ' + str(age) + ' ' + str(mom_age)
		mom_age += 1
		age += 1
	if count == 7:
		print(ages)
		return ages


rev_age()