def gradingStudents(grades):
	llist = []
	print(grades)
	for i in grades:
		if i < 40:
			llist.append(i)
		elif i%5 == 3:
			llist.append(i+2)
		elif i%5 == 4:
			llist.append(i+1)
		else:
			llist.append(i)
	return llist



grades = [71,72,73,74,75,76,77,78,79,80,34,39]
print(gradingStudents(grades))
