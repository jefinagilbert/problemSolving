def extraLongFactorials(n):
	res = n
	for i in reversed(range(1,n)):
		res = res * i
	return res
		



n = 30
print(extraLongFactorials(n))