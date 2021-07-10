def migratoryBirds(arr):
	arr.sort()
	llist = [0,0,0,0,0]
	for i in arr:
		if i == 1:
			llist[0] += 1
		elif i == 2:
			llist[1] += 1
		elif i == 3:
			llist[2] += 1
		elif i == 4:
			llist[3] += 1
		elif i == 5:
			llist[4] += 1
	arr2 = []
	for i in llist:
		arr2.append(i)
	arr2.sort()
	for i in range(len(llist)):
		if llist[i] == arr2[len(arr2)-1]:
			return i+1
	



arr = [1,4,4,4,5,3]
print(migratoryBirds(arr))