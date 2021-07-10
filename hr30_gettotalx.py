def getTotalX(a, b):
	val = 0
	val1 = 0
	val2 = 0
	b.sort()
	for i in range(1,b[0]+1):
		for j in a:
			if i%j==0:
				val += 1
		if val == len(a):
			for k in b:
				if k%i==0:
					val1 += 1
			if val1 == len(b):
				val2 += 1
			val1 = 0
		val = 0
	return val2
		
 
n = 2
m = 3
a = [2]
b = [20,30,12]
print(getTotalX(a,b))
