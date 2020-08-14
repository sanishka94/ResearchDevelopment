import time
t = time.time()
total_minutes = t//60
total_hours = total_minutes//60
days = int(total_hours//24)
hours = int(total_hours - (days*24))
minutes = int(total_minutes - (total_hours*60))
seconds = int(t - (total_minutes*60))
print(t)
print('days: ', days, '\nhours: ', hours, '\nminutes: ', minutes, '\nseconds: ', seconds)

if hours < 12:
	time_day = str(hours) + ':' + str(minutes) + ' am and ' + str(seconds) + ' seconds'
else:
	time_day = str(hours) + ':' + str(minutes) + ' pm and ' + str(seconds) + ' seconds'

print(time_day)