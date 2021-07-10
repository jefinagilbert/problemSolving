def jumpingOnClouds(c):
	a = 2
	b = 0
	if len(c) <= 2:
		return 1
	for i in range(len(c)):
		
		if c[a] == 0 and len(c)-a != 2:
			b += 1
			a += 2
			print(a)
		else:
			b += 1
			a += 1
			print(a)
		if a >= len(c):
			break
	return b







c = [0,0]
print(jumpingOnClouds(c))