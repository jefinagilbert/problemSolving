def count_substring(string, sub_string):
	s = 0
	count = 0
	for i in range(count,len(string)):
		if setmatch(string[count:len(sub_string)+count] ,sub_string):
			s += 1
		count += 1
	return s


def setmatch(string1,sub_string):
	return string1 == sub_string
    

if __name__ == '__main__':
    string = "ABCDCDCDC"
    sub_string = "CDC"
    
    count = count_substring(string, sub_string)
    print(count)