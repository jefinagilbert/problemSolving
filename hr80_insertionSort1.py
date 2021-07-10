def insertionSort1(n, arr):
	arr2 = []
	for i in arr:
		arr2.append(i)
	arr2.sort()
	val = arr[len(arr)-1]
	for i in reversed(range(n)):
		if i == 0:
			arr[i] = val
			print()
			for j in arr:
				print(j,end=" ")
			continue
		if val < arr[i-1]:
			arr[i] = arr[i-1]
			if i == len(arr)-1:
				pass
			else:
				print()
			for j in arr:
				print(j,end=" ")
			if arr == arr2:
				break
		else:
			arr[i] = val
			val = arr[i-1]
			if i == len(arr)-1:
				pass
			else:
				print()
			for j in arr:
				print(j,end=" ")
			if arr == arr2:
				break





arr = [2,4,6,8,3]
n = 5
insertionSort1(n,arr)