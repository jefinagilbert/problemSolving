#defaultdict but i havent imported it
a = input().split()
groupa = []
groupb = []
llist = []
for i in range(int(a[0])):
	groupa.append(input())
for i in range(int(a[1])):
	groupb.append(input())
for i in groupb:
	k = 0
	m = 0
	for j in groupa:
		k += 1
		if i == j:
			m = 1
			print(k,end=" ")
	if(m==0):
		print(-1,end=" ")
	print()