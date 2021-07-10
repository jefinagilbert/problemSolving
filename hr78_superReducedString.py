def recus(s):
	prev = ''
	a = ''
	for i in range(len(s)):
		if i == len(s)-1 and prev == '':
			a += s[i]
			break
		elif i == len(s)-1 and len(prev)==1:
			if prev == s[i]:
				break
			else:
				a += prev+s[i]
				break
		if prev == s[i]:
			prev = ''
			continue
		if len(prev) == 1:
			a += prev
		prev = s[i]
	if a == '':
		return 'Empty String'
	else:
		return a


def superReducedString(s):
	b = recus(s)
	a = b
	for i in b:
		if recus(a) == a:
			return a
		else:
			a = recus(a)

# def superReducedString(s):
# 	a = ''
# 	for i in range(len(s)):
# 		if i%2 == 1:
# 			continue
# 		if i+2 == len(s):
# 			break
# 		elif i+1 == len(s):
# 			a += s[i]
# 			break
# 		if s[i] == s[i+1]:
# 			pass
# 		else:
# 			if i+2 == len(s):
# 				break
# 			elif i+1 == len(s):
# 				a += s[i]
# 				break
# 			a += s[i]+s[i+1]
			
# 	print(a)
		




s = 'abcddcb'
print(superReducedString(s))
