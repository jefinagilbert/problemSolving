def formingMagicSquare(s):
	a = 0
	b = 0
	for i in range(len(s)):
		for j in range(len(s[i])):
			a += s[i][j]
		if a != 15:
			for k in range(len(s[i])):
				b += s[k][i]
			if b != 15:
				c = 15 - b
				if a+c == b+c:
					s[i][i] +=  c
				else:

			b = 0
		a = 0
	return s
# NO solution found


s =  [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
for  i in s:
	print(i)
res = formingMagicSquare(s)
for i in res:
	print(i)