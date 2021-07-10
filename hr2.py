def swap_case(s):
	s1 = ""
	for i in s:
		if i.islower():
			i = i.upper()
		elif i.isupper():
			i = i.lower()
		s1 += i
	return s1
	

if __name__ == '__main__':
    s = "HackerRank.com presents 'Pythonist 2'."
    res = swap_case(s)
    print(res)
    	