n = int(input())
for i in range(n):
	a,b = input().split()
	try:
		print(int(a)//int(b))
	except BaseException as e:
		print("Error Code:",e)