def climbingleaderboard(ranked,player):
	llist = []
	r = ranked
	res = []
	for i in player:
		for j in range(len(ranked)):
			if i > ranked[j]:
				ranked.insert(j,i)
				m = ranked[0]
				a = 1
				for k in ranked:
					if m == k:
						if k == i:
							break
						pass
					else:
						a += 1
						if i == k:
							break
						m = k
				res.append(a)
				ranked = r
				break
			if i<=ranked[len(ranked)-1]:
				ranked.append(i)
				m = ranked[0]
				a = 1
				for k in ranked:
					if m == k:
						if k == i:
							break
						pass
					else:
						a += 1
						if k == i:
							break
						m = k
				res.append(a)
				ranked = r
				break
	return res
#yeah i got it but i cant run it before the time ends

			
r = int(input())  
ranked = input().split()
p = int(input()) 
player = input().split()
rr = []
pp = []
for i in ranked:
	rr.append(int(i))
for i in player:
	pp.append(int(i))
print(climbingleaderboard(rr,pp))
