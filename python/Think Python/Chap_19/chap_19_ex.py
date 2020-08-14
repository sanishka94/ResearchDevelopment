from collections import defaultdict

d = defaultdict(dict)

def binomial_coeff(n, k):
	'''Compute the binomial coefficient "n choose k".
	n: number of trials
	k: number of successes

	returns int
	'''

	if k == 0:
		return 1
	if n == 0:
		return 0

	res = binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
	return res

def binomial_coeff_n(n, k):
	return 1 if k == 0 else 0 if n == 0 else binomial_coeff_n(n-1, k) + binomial_coeff_n(n-1, k-1)

def binomial_coeff_d(n, k):
	if k == 0: return 1
	elif n == 0: return 0
	else:
		if n in d:
			if k in d[n]:
				return d[n][k]
		res = binomial_coeff_d(n-1, k) + binomial_coeff_d(n-1, k-1)
		d[n][k] = res
		return res


print(binomial_coeff_d(100, 15))
print(d)