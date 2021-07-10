def minimumDistances(a):
	b = []
	for i in range(len(a)):
		for j in range(i):
			if i == j:
				continue
			if a[i] == a[j]:
				b.append(i-j)
	if b == []:
		return -1
	else:
		return min(b)



a = [7, 1, 3, 4, 1, 7]
print(minimumDistances(a))