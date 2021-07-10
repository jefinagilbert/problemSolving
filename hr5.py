def mutate_string(string, position, character):
	a = 0
	string2 = ""
	for i in string:
		if position == a:
			string2 += character
			a += 1
			continue
		string2 += i
		a += 1
	return string2


if __name__ == '__main__':
    s = "abracadabra"
    i, c = "5 k".split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)