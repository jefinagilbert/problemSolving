def serviceLane(width, cases):
	t = []
	for i in range(len(cases)):
		t.append(min(width[cases[i][0]:cases[i][1]+1]))
	return t



width = [2, 3, 1, 2, 3, 2, 3, 3]
cases = [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]
(serviceLane(width,cases))