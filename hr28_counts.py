def countApplesAndOranges(s, t, a, b, apples, oranges):
	app = 0
	ora = 0
	for i in apples:
		if s<=a+i<=t:
			app += 1
	for i in oranges:
		if s<=b+i<=t:
			ora += 1
	print(app)
	print(ora)
	


s = 7
t = 11
a = 5
b = 15
apples = [-2,2,1]
oranges = [5,-5,-6]
countApplesAndOranges(s,t,a,b,apples,oranges)