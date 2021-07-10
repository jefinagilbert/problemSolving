def plusMinus(arr):
	p = 0
	n = 0
	z = 0
	for i in arr:
		if(i>0):
			p += 1
		elif(i==0):
			z += 1
		elif(i<0):
			n += 1
	print(format(p/len(arr),'.6f'))
	print(format(n/len(arr),'.6f'))
	print(format(z/len(arr),'.6f'))


arr = [-4,3,-9,0,4,1]
plusMinus(arr)