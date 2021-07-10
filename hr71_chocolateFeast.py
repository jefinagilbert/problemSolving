def chocolateFeast(n, c, m):
	tot = 0
	w = 0
	rw = 0
	choc = 0
	for i in range(n):
		if i != 0:
			choc = w//m
			rw = w%m
			tot += choc
			w = choc + rw
			if w >= m:
				continue
			else:
				return tot
		choc = n//c
		w = choc
		tot += choc
		if w >= m:
			pass
		else:
			return tot
	return tot

n = 6
c = 2
m = 2
print(chocolateFeast(n,c,m))