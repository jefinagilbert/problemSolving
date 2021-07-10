#this was copied in discussion.. this is not my code
def kangaroo(x1, v1, x2, v2):
	if (x2 - x1) * (v2 - v1) < 0 and (x2 - x1) % (v2 - v1) == 0 :
		return 'YES'
	else:
		return 'NO'

x1 = 0
v1 = 3
x2 = 4
v2 = 2
print(kangaroo(x1,v1,x2,v2))
