def timeInWords(h, m):
	hmap = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'quarter',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',30:'half',20:'twenty',21:'twenty one',22:'twenty two',23:'twenty three',24:'twenty four',25:'twenty five',26:'twenty six',27:'twenty seven',28:'twenty eight',29:'twenty nine',30:'half'}
	if m > 30:
		if h == 12:
			h = 0
		m = 60 - m
		if m == 15:
			string = hmap[m] + ' ' + 'to' + ' ' + hmap[h+1]
			return string
		string = hmap[m]  + ' ' + 'minutes' + ' ' + 'to' + ' ' + hmap[h+1]
		return string
	else:
		if m == 0:
			string = hmap[h] + " " + "o' clock"
			return string
		if m == 1:
			string = hmap[m] + ' ' + 'minute' + ' ' + 'past' + ' ' + hmap[h]
			return string
		if m == 30:
			string = hmap[m] + ' ' + 'past' + ' ' + hmap[h]
			return string	
		if m == 15:
			string = hmap[m] + ' ' + 'past' + ' ' + hmap[h]
			return string
		string = hmap[m] + ' ' + 'minutes' + ' ' + 'past' + ' ' + hmap[h]
		return string


h = 1
m = 1
print(timeInWords(h,m))