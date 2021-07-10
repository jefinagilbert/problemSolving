def angryProfessor(k, a):
	b = 0
	for i in range(len(a)):
		if a[i] <= 0:
			b += 1
	if b >= k:
		return 'NO'
	else:
		return 'YES'


m = int(input())
aa = []
res = []
for i in range(m):
	n,k = input().split()
	a = input().split()
	for j in a:
		aa.append(int(j))
	res.append(angryProfessor(int(k),aa))
	aa = []
for i in res:
	print(i)