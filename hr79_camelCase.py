def camelcase(s):
	word = 0
	for i in range(len(s)):
		if i == 0:
			word += 1
			continue
		if s[i].isupper():
			word += 1
	return word


s = 'saveChangesInTheEditor'
print(camelcase(s))