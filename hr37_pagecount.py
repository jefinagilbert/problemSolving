def pageCount(n, p):
	llist = []
	f = 0
	l = 0
	for i in range(n+1):
		if i%2 == 0:
			llist.append([i,i+1])
	print(llist)
	for i in range(len(llist)):
		for j in range(2):
			if llist[i][j] == p:
				break
		if llist[i][j] == p:
			break
		f += 1
	for i in reversed(range(len(llist))):
		for j in range(2):
			if llist[i][j] == p:
				break
		if llist[i][j] == p:
			break
		l += 1
	if f>l:
		return l
	else:
		return f
n = 6
p = 2
print(pageCount(n,p))