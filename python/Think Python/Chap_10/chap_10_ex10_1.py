
t = [[1,2,3], [2, 4, 6], [3, 6, 9]]

def nested_sum(li):
	total = 0
	for nes in li:
		total += sum(nes)
	return total

print(nested_sum(t))