def taumBday(b, w, bc, wc, z):
	if bc < wc:
		tot = b * bc
		if z+bc < wc:
			tot += (bc+z)*w
		else:
			tot += wc * w
	else:
		tot = w * wc
		if z+wc < bc :
			tot += (wc+z)*b
		else:
			tot += bc * b
	return tot

b = 5
w = 9
bc = 2
wc = 3
z = 4
print(taumBday(b,w,bc,wc,z))