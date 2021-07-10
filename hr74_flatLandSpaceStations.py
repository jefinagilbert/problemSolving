def flatlandSpaceStations(n, c):
	a = []
	tot = []
	for i in range(n):
		if i in c:
			tot.append(0)
		else:
			for j in c:
				if j == i:
					continue
				if j < i:
					a.append(i-j)
				else:
					a.append(j-i)
			tot.append(min(a))
			a = []
	return max(tot)


# terminated due to time complexity

n = 20
c = [13,1,11,10,6]
print(flatlandSpaceStations(n,c))
