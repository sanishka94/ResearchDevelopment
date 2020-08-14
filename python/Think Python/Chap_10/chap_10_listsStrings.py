s1 = 'spam'
t1 = list(s1)

print(t1)

s2 = 'pinning for the fjords'
t2 = s2.split()
print(t2)

s3 = 'spam-spam-spam'
t3 = s3.split('-')
print(t3)

delimiter = ' '
s4 = delimiter.join(t2)
print(s4)

empty_string = ''
s5 = empty_string.join(t2)
print(s5)

t = [4, 3, 2]
x = 1
t = t + [x]
ts = sorted(t)

print(t)
print(ts)