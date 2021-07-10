# this is my solution.. the absolute solution is in hackerrank....
def acmTeam(topic,m):
	llist = []
	a = 0
	for i in range(len(topics)):
		for j in range(i,len(topics)):
			if i == j:
				continue
			for k in range(m):
				if int(topics[i][k]) or int(topics[j][k]):
					a += 1
			llist.append(a)
			a = 0
	return [max(llist),llist.count(max(llist))]

topics = []
n,m = input().split()
for i in range(int(n)):
	topics.append(input())
print(acmTeam(topics,int(m)))