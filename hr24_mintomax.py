def miniMaxSum(arr):
	llist = []
	val = 0
	for i in range(len(arr)):
		for j in range(len(arr)):
			if i!=j:
				val += arr[j]
		llist.append(val)
		val = 0
	llist.sort()
	print(llist[0],llist[len(llist)-1])






arr = [5,5,1,2,3]
miniMaxSum(arr)