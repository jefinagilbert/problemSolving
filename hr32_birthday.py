def birthday(s, d, m):
	val = 0
	val1 = 0
	j = 0
	for i in range(len(s)):
		for j in s[i:m+i]:
			val += j
		if val == d:
			val1 += 1
		val = 0
	return val1

s = [1,2,1,3,2]
d = 3
m = 2
print(birthday(s,d,m))