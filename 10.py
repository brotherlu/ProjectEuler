import miller_rabin as p

val = 2
summation = 0
while val <=2e6:
	if p.miller_rabin(val):
		summation+=val
		print val,summation
	val+=1

