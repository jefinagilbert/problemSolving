def utopianTree(n):
	a = 0
	k = 1
	for i in range(n+1):
		if k % 2 == 0:
			a = a* 2
		else:
			a += 1
		if i == n:
			return a
		k = i
		



n = [0,1]
for i in n:
	print(utopianTree(i))