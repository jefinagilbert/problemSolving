def circularArrayRotation(a, k, queries):
	n = []
	for i in range(k):
		a.insert(0,a[len(a)-1])
		a.pop()
	for i in queries:
		n.append(a[i])
	return n

n = 3
k = 2
q = 3
a = [1,2,3]
queries = [0,1,2]
print(circularArrayRotation(a,k,queries))