def workbook(n, k, arr):
	a = 0
	book = []
	nxt = 0
	s = []
	spclprblm = 0
	pageno = 0
	for i in range(sum(arr)):
		if nxt != 0:
			if nxt - k > 0:
				pageno += 1
				for j in range(k):
					s.append(lastval)
					lastval += 1
				book.append(s)
				if pageno in s:
					spclprblm += 1
				s = []
				nxt = nxt - k
				continue
			else:
				pageno += 1
				for j in range(nxt):
					s.append(lastval)
					lastval += 1
				book.append(s)
				if pageno in s:
					spclprblm += 1
				lastval = 0
				s = []
				nxt = 0
				a += 1
				if len(arr) == a:
					break
				continue
		if k - arr[a] >= 0:
			pageno += 1
			for j in range(1,arr[a]+1):
				s.append(j)
			book.append(s)
			if pageno in s:
				spclprblm += 1
			s = []
			a += 1
			if len(arr) == a:
				break
		else:
			pageno += 1
			nxt = arr[a] - k
			for j in range(1,k+1):
				s.append(j)
			book.append(s)
			if pageno in s:
				spclprblm += 1
			s = []
			lastval = k+1
	return spclprblm


n = 4
k = 3
arr = [4,2]
print(workbook(n,k,arr))