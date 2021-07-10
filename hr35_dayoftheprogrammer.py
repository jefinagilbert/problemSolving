def dayOfProgrammer(year):
	if 1700<=year<=1917:
		if year%4==0:
			a = 244
		else:
			a = 243
		
	else:
		if year%4==0:
			if year%100==0:
				if year%400==0:
					a = 244
				else:
					a = 243
			else:
				a = 244
		else:
			a = 243

	b = 256 - a
	c = str(b) + '.09.' + str(year)
	return c




year = 1800
print(dayOfProgrammer(year))