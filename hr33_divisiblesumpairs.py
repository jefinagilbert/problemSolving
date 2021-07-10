def divisibleSumPairs(n, k, ar):
	val = 0
	for i in range(len(ar)):
		for j in range(i+1,len(ar)):
			if ar[i] + ar[j] == k:
				val += 1
			else:
				for l in range(1,ar[i]+ar[j]):
					if (ar[i] + ar[j])/l == k:
						val += 1
	return val


n = 6
k = 3
ar = [1,3,2,6,1,2]
print(divisibleSumPairs(n,k,ar))