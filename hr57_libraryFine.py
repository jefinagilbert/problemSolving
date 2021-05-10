def leapyear(year):
	if (year % 4) == 0:
		if (year % 100) == 0:
			if (year % 400) == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False

def libraryFine(d1, m1, y1, d2, m2, y2):
	hmap = {'1':31,'2':28,'3':31,'4':30,'5':31,'6':30,'7':31,'8':31,'9':30,'10':31,'11':30,'12':31}
	lhmap = {'1':31,'2':29,'3':31,'4':30,'5':31,'6':30,'7':31,'8':31,'9':30,'10':31,'11':30,'12':31}
	b = 0
	m = 0
	y = 0
	if y2 < y1:
		return 10000
	elif y2 > y1:
		return 0
	if y1 == y2:
		if leapyear(y2) == False:
			if m2 == m1:
				b = d1 - d2
				if b < 0:
					b = 0
			else:
				for i in range(m2,m1+1):
					# if i == m2:
					# 	b += hmap[str(i)] - d2
					if i == m1:
						#b += d1
						m += 1
					if i != m1 and i != m2:
						#b += hmap[str(i)]
						m += 1
		else:
			if m2 == m1:
				b = d1 - d2
				if b < 0:
					b = 0
			else:
				for i in range(m2,m1+1):
					# if i == m2:
					# 	b += lhmap[str(i)] - d2
					if i == m1:
						#b += d1
						m += 1
					if i != m1 and i != m2:
						#b += lhmap[str(i)]
						m += 1
		return b*15 + m*500
	# else:
	# 	for j in range(y2,y1+1):
	# 		if leapyear(j) == False:
	# 			if j == y2:
	# 				for i in range(m2,12+1):
	# 					if i == m2:
	# 						b += hmap[str(i)] - d2
	# 					else:
	# 						#b += hmap[str(i)]
	# 						m += 1
	# 				continue
	# 			if j == y1:
	# 				for i in range(1,m1+1):
	# 					if i == m1:
	# 						b += d1
	# 					else:
	# 						#b += hmap[str(i)]
	# 						m += 1
	# 				break
	# 			if j != y1 and j!=y2:
	# 				y += 1
	# 			for i in range(1,12+1):
	# 				b += hmap[str(i)]
					
	# 		else:
	# 			if j == y2:
	# 				for i in range(m2,12+1):
	# 					if i == m2:
	# 						b += lhmap[str(i)] - d2
	# 					else:
	# 						#b += lhmap[str(i)]
	# 						m += 1
	# 				continue
	# 			if j == y1:
	# 				for i in range(1,m1+1):
	# 					if i == m1:
	# 						b += d1
	# 					else:
	# 						#b += lhmap[str(i)]
	# 						m += 1
	# 				break
	# 			for i in range(1,12+1):
	# 				b += lhmap[str(i)]
	# return b*15 + m*500,y

d1 = 5 # returned date
m1 = 5
y1 = 2014
d2 = 23  # duedate
m2 = 2
y2 = 2014
print(libraryFine(d1,m1,y1,d2,m2,y2))