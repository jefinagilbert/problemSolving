def print_formatted(number):
    # your code goes here
    i = 1
    w=len(bin(number)[2:])
    while i <= number:
    	print(str(i).rjust(w,' '),octal(i).rjust(w,' '),hexadecimal(i).upper().rjust(w,' '),binary(i).rjust(w,' '),sep=' ')
    	i += 1
def octal(i):
	i = oct(i)
	i = i[2:]
	return i

def hexadecimal(i):
	i = hex(i)
	i = i[2:]
	return i

def binary(i):
	i = bin(i)
	i = i[2:]
	return i

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)