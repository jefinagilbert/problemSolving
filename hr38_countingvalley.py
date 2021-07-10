def countingValleys(steps, path):
	a = 0
	b = 0
	for i in path:
		if i == 'U':
			a += 1
		if i == 'D':
			a -= 1
			if a == -1:
				b += 1
	return b

#firstsolution
def countingvalleys(steps, path):
    llist = []
    dlist = []
    a = 0
    for i in path:
        if i == 'U':
            llist.append(i)
            if len(dlist) == 0:
                pass
            else:
                dlist.remove('D')
                if len(llist) != 0:
                    llist.remove('U')
        else:
            dlist.append(i)
            if len(llist) == 0:
                if len(dlist) == 1:
                    a += 1
            else:
                llist.remove('U')
                if len(dlist) != 0:
                    dlist.remove('D')
                
    return a

steps = 8
path = "UDDDUDUU"
print(countingValleys(steps,path))