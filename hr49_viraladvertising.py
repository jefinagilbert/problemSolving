def viralAdvertising(n):
	shares = 5
	cum = 0
	liked = 1
	for i in range(1,n+1):
		if i == 1:
			shares = 5*i
		else:
			shares = 3 * liked
		liked = shares//2
		cum += liked
	return cum






n = 5
print(viralAdvertising(n))