def strangeCounter(t):
	# a = 1
	# b = 3
	# prevb = b
	# while(a<=t):
	# 	print(a,b)
	# 	if a == t:
	# 		return b
	# 	if b == 1:
	# 		b = 2*prevb
	# 		prevb = b
	# 		a += 1
	# 		continue
	# 	b = b -1
	# 	a += 1
	# copied
	rem = 3
	while t > rem:
	    t = t-rem
	    rem *= 2
	return rem-t+1


t = 100
print(strangeCounter(t))



# 2 5 11 23 47  1 4 10 22 46