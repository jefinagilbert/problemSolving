def bonAppetit(bill, k, b):
	tot = 0
	for i in range(len(bill)):
		if i == k:
			continue
		tot += bill[i]
	tot = tot//2
	tot = b - tot
	if tot == 0:
		print("Bon Appetit")
	else:
		print(tot)



k = 1
bill = [3,10,2,9]
b = 7