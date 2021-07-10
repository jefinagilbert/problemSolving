def staircase(n):
	k = n
	for i in range(1,n+1):
		k -= 1
		print(' '*k+'#'*i)


if __name__ == '__main__':
    n = int(input())

    staircase(n)