def beautifulDays(i, j, k):
	bb = ''
	d = 0
	for a in range(i,j+1):
		for b in reversed(str(a)):
			bb += b
		c = int(bb)-a
		if c < 0:
			c -= 2*c
		if c%k==0:
			d += 1
		bb = ''
	return d

i = 20
j = 23
k = 6
print(beautifulDays(i,j,k))