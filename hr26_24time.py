def timeConversion(s):
	if 'PM' in s:
		k = int(s[:2])
		if k == 12:

			return s[:len(s)-2]
		k = str(k+12)
		for i in s[2:]:
			if i == 'P' or i == 'M':
				continue
			k += i

		return k
	elif 'AM' in s:
		k = int(s[:2])
		if k == 12:
			k = '00'
			for i in s[2:]:
				if i == 'A' or i == 'M':
					continue
				k += i
			return k
		return s[:len(s)-2]




s = '06:40:03AM'
print(timeConversion(s))