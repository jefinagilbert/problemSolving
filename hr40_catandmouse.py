def catAndMouse(x, y, z):
	a = z-x
	b = z-y
	if a < 0:
		a -= 2*a
	if b < 0:
		b -= 2*b
	if a==b:
		return 'Mouse C'
	elif a>b:
		return 'Cat B'
	elif a<b:
		return 'Cat A'



x = 1
y = 3
z = 2
print(catAndMouse(x,y,z))