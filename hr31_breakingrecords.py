def breakingRecords(scores):
	high = int(scores[0])
	h = 0
	low = int(scores[0])
	l = 0
	for i in scores:
		if int(i) > high:
			high = int(i)
			h += 1
		if int(i) < low:
			low = int(i)
			l += 1
	return h,l

n = int(input())
scores = input().split()
print(breakingRecords(scores))