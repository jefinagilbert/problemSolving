def sockMerchant(n, ar):
	arr = []
	op = 0
	arr1 = []
	for i in ar:
		arr.append(i)
	for i in range(len(ar)):
		if ar[i] in arr:
			arr.remove(ar[i])
			if ar[i] in arr:
				arr.remove(ar[i])
				op += 1
	return op

		

		



n = 7
ar = [1,1,3,1,2,1,3,3,3,3]
print(sockMerchant(n,ar))