def getMoneySpent(keyboards, drives, b):
	llist = []
	a = 0
	for i in keyboards:
		for j in drives:
			llist.append(i+j)
	llist.sort()
	for i in reversed(llist):
		if i <= b:
			a = i
			break
	if a == 0:
		return -1
	return a




b = 5
keyboards = [4]
drives = [5]
print(getMoneySpent(keyboards,drives,b))