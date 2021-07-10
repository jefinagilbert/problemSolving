def kaprekarNumbers(p, q):
	string = ''
	for i in range(p,q+1):
		if i == 1:
			string += str(i) + ' '
			continue
		a = str(i*i)
		for j in range(1,len(str(a))+1):
			if j == len(str(a)):
				break
			if int(a[:j]) + int(a[j:]) == i:
				if int(a[:j]) == 0 or int(a[j:]) == 0:
					continue

				if a[j:][0] == '0' and int(a[j:]) != 1:
					if a[:j][len(a[:j])-1] == '0' and a[j:][0] == '0':
						pass
					else:
						continue
				# print(a[:j],a[j:])
				string += str(i) + ' '
	if string == '':
		print("INVALID RANGE")
	else:
		print(string)
p = 1
q = 99999
kaprekarNumbers(p,q)

