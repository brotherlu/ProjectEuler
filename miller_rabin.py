import random

_num_trials = 5

def miller_rabin(n):
	"""
	Miller Rabin Prime Test
	From Rosetta Code
	"""
	assert n>=2
	# Case == 2
	if n==2: return True
	# if n is Even
	if n%2==0: return False

	s = 0
	d = n-1

	while True:
		quo,rem = divmod(d,2)
		if rem==1: break
		s += 1
		d = quo
	assert(2**s * d == n-1)

	# Test Composition
	def try_composite(a):
		if pow(a,d,n) == 1: return False
		for i in range(s):
			if pow(a,2**i * d, n) == n-1: return False
		return True
	for i in range(_num_trials):
		a = random.randrange(2,n)
		if try_composite(a): return False

	return True


