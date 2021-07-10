def findOdd(B):
	for i in B:
		if i%2 != 0:
			return 0
	return 1

def fairRations(B):
	a = 0
	bread = 0
	for i in range(len(B)):
		if B[a]%2 == 0:
			a += 1
			if a == len(B):
				if findOdd(B) == 0:
					return 'NO'
				else:
					return str(bread)
			continue
		else:
			if a == len(B) or a+1 == len(B):
				if findOdd(B) == 0:
					return 'NO'
				else:
					return str(bread)
			if B[a]%2 != 0 and B[a+1]%2 != 0:
				B[a] += 1
				B[a+1] += 1
				bread += 2
				a += 1
			else:
				if a+2 >= len(B):
					if findOdd(B) == 0:
						return 'NO'
					else:
						return str(bread)
				if B[a+2]%2 == 0:
					B[a] += 1
					B[a+1] += 1
					bread += 2
					a += 1
				else:
					B[a] += 1
					B[a+1] += 1
					bread += 2
					a += 1



a = input().split()
B = []
for i in a:
	B.append(int(i))
print(fairRations(B))