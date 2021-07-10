import  math

def squares(a, b):
	sqrtA = math.ceil(math.sqrt(a))
	sqrtB = math.floor(math.sqrt(b))
	return sqrtB-sqrtA+1




a = 2
b = 9
print(squares(a,b))