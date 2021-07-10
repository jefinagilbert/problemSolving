def split_and_join(line):
    # write your code here
    line = line.split(" ")
    a = 0
    line2 = ""
    for i in line:
    	if a < len(line) - 1:
    		line2 += i
    		line2 += "-"
    	else:
    		line2 += i
    	a += 1
    return line2
    	



if __name__ == '__main__':
	line = "this is a string"
	res = split_and_join(line)
	print(res)