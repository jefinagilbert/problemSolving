def findDigits(n):
	k = 0
	for i in str(n):
		if n%int(i) == 0:
			k += 1
	return k




n = 142
print(findDigits(n))