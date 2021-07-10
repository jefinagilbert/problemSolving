def cutTheSticks(arr):
	llist = []
	for i in range(len(arr)):
		a = min(arr)
		llist.append(len(arr))
		for j in range(len(arr)):
			arr[j] -= a
		for j in range(arr.count(0)):
			arr.remove(0)
		if arr == []:
			break
	return llist
		




arr = [5,4,4,2,2,8]
print(cutTheSticks(arr))