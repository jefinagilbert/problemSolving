a = input().split()
b = input().split()
llist = []
for i in a:
	for j in b:
		llist.append([int(i),int(j)])
k = 0
for i in llist:
	if(k==len(llist)-1):
		print(tuple(i))
	else:
		print(tuple(i),end=" ")
	k += 1
