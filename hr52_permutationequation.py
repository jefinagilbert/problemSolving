def permutationEquation(p):
	n = []
	for i in range(1,len(p)+1):
		for j in range(len(p)):
			if i == p[j]:
				a = j+1
				break
		for j in range(len(p)):
			if a == p[j]:
				a = j+1
				break
		n.append(a)
	return n



p = [5,2,1,3,4]
print(permutationEquation(p))