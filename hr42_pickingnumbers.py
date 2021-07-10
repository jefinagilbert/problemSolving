def pickingNumbers(a):
	l = []
	llist = []
	llist2 = []
	llist3 = []
	val = [0,1,-1]
	p = 0
	for i in range(len(a)):
		for j in range(len(a)):
			if a[i] - a[j] in val:
				l.append(a[j])
		if l != []:
			llist.append(l)
		l = []
	for i in range(len(llist)):
		for j in range(len(llist[i])-1):
			for k in range(len(llist[i])):
				if j == k:
					continue
				if llist[i][j] - llist[i][k] in val:
					pass
				else:
					p = 1
					for o in llist[i]:
						if o == llist[i][j]:
							pass
						else:
							llist3.append(o)
					llist2.append(llist3)
					llist3 = []
		if p == 0:
			if llist[i] in llist2:
				pass
			else:
				llist2.append(llist[i])
		p = 0
	l = []
	for i in llist2:
		l.append(len(i))
	l.sort()
	return l[len(l)-1]


# this solution is not mine i dont know that there is a function called count if i know that i will be 
# making it more easier that this... but in this i havent used any big functions so iam very glad about me....
def pickingnumbers():
	l=[int(i) for i in input().split()]
	maximum=0
	for i in l:
		c=l.count(i)
		d=l.count(i-1)
		c=c+d
		if c > maximum:
			maximum=c
	return maximum
	

#a = input().split()
#b = []
#for i in a:
#	b.append(int(i))
print(pickingnumbers())
