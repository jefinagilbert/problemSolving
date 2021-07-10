def happyLadybugs(b):
	llist = []
	llist1 = []
	llist2 = []
	for i in b:
		if i not in llist:
			llist.append(i)
	if '_' not in b:
		if len(llist) == 1:
			if b.count(llist[0]) > 1:
				return 'YES'
			else:
				return 'NO'
		else:
			for i in llist:
				if b.count(i) <= 1:
					return 'NO'
		a = b[0]
		c = ''
		for i in b:
			if i in c:
				return 'NO'
				break
			if i != a:
				a = i
				c += prev
			prev = i
		return 'YES'
	for i in llist:
		if i == '_':
			continue
		if b.count(i) <= 1:
			return 'NO'
	return 'YES'


b = 'AACBB_C'
print(happyLadybugs(b))