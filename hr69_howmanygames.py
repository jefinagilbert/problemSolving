def howManyGames(p, d, m, s):
	a = []
	for i in range(s+p):
		if p == m:
			if s-p < 0:
				break
			a.append(p)
			s = s-p
			continue
		if p > s:
			return 0
		a.append(p)
		s = s - p
		if p-d <= m:
			p = m
		else:
			p = p - d
		if s-p < 0:
			break
	return len(a)

p = 100
d = 1
m = 1
s = 101
print(howManyGames(p,d,m,s))