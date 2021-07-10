def diagonalDifference(arr):
	val = 0
	j = len(arr)
	val1 = 0
	for i in range(len(arr)):
		val += arr[i][i]
	for i in range(len(arr)):
		j -= 1
		val1 += arr[i][j]
	val2 = val-val1
	if val2<0:
		val2 -= val2*2
	return val2


n = int(input())
arr = []
for i in range(n):
	arr.append(list(map(int, input().rstrip().split())))
print(diagonalDifference(arr))
