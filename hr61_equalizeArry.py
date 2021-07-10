def equalizeArray(arr):
	a = 0
	llist = []
	for i in arr:
		for j in arr:
			if i != j:
				a += 1
		llist.append(a)
		a = 0
	return min(llist)


arr = [3,3,2,3,1]
print(equalizeArray(arr))