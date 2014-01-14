a = lambda b: (5e5-1e3*b)/(1e3-b)

bsol=0

while bsol<1e3:
	bsol+=1
	asol = a(bsol)
	c = 1e3 - bsol - asol
	if int(c)==c and int(asol)==asol:
		print asol,bsol,c, asol*bsol*c
		break


