print('Hello, World!')
second = 1
minute = 60*second
kilometer = 1
mile = 1.61*kilometer
dist = 10*kilometer/mile
time = 42*minute+42*second 
secsPerMile = time/dist
minutesPerMile = secsPerMile//minute
secsRemaining = (secsPerMile%minute)//1
print(int(minutesPerMile), 'minutes and', int(secsRemaining), 'seconds per mile')
speed = dist/time
print(int(speed*60*60), 'miles per hour')
