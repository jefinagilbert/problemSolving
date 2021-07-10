import math
def encryption(s):
	llist = []
	if math.sqrt(len(s)).is_integer():
		r = int(math.sqrt(len(s)))
		c = int(math.sqrt(len(s)))
	else:
		r = int(math.sqrt(len(s)))
		c = int(math.sqrt(len(s))) + 1
	a = 0
	b = c
	print(len(s),r,c)
	if r*c < len(s):
		r = c
	for i in range(r):
		llist.append(s[a:b])
		a = b
		b = b + c
	print(llist)
	a = ''
	b = ''
	for i in range(len(llist[0])):
		for j in range(len(llist)):
			if len(llist[j]) <= i:
				break
			a += llist[j][i]
		b += a + ' '
		a = ''
	return b

s = 'iffactsdontfittotheorychangethefacts'
print(encryption(s))

