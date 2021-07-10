def merge_the_tools(string, k):
    # your code goes here
    llist = []
    llist1 = []
    j = 0
    m = ""
    a = ""
    for i in string:
    	j += 1
    	m += i
    	if j % k == 0:
    		llist.append(m)
    		m = ""
    if m != "":
    	llist.append(m)
    for i in llist:
    	for j in i:
    		if j not in a:
    			a += j
    	llist1.append(a)
    	a = ""
    for i in llist1:
    	print(i)





if __name__ == '__main__':
    string = "AAABCADDE"
    k = 3
    merge_the_tools(string,k)