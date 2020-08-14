print('spam'+'bam') #this is how you comment
x=y=1
print(x)
print(y)
print('Ex 2.2-1')
r=5
pi=3.14
print((4/3)*pi*(r**3))
print('Ex 2.2-2')
book = 24.95
discount = (0.6)
copies = 60
ship_first = 3
Ship_other = 0.75
books = (book*discount)*60
shipping = ship_first + ((copies-1)*Ship_other)
print(int(books+shipping))
print('Ex 2.2-3')
sec = 1
min = 60*sec
hr = 60*min
time = 6*hr+52*min
easy_mile_sec = 8*min+15*sec
tempo_mile_sec = 7*min+12*sec
total_sec = 1*easy_mile_sec+3*tempo_mile_sec+1*easy_mile_sec
total_min = total_sec//min
rem_sec = int(total_sec%min)
print(total_min, ' mins and ', rem_sec, ' seconds')