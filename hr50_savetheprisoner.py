def saveThePrisoner(n, m, s):
	a = s
	for i in range(m):
		if m-1 == i:
			break
		if n == a:
			a = 1
			continue
		a += 1
	return a


#second solutiion is not mine it was stolen in discussion.... but 1st went correct but it takes more time

def savetheprisoner(n,m,s):
	return ((s - 1 + m - 1) % n) + 1



n = 7
m = 7
s = 6
print(savetheprisoner(n,m,s))