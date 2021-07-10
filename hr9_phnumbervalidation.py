if "__main__" == __name__:
	N = int(input())
	number = []
	for i in range(N):
		num = input()
		number.append(num)
	for i in number:
		if len(i) == 10:
			if i.isdigit():
				if int(i[0]) == 7:
					print("YES")
				elif int(i[0]) == 8:
					print("YES")
				elif int(i[0]) == 9:
					print("YES")
				else:
					print("NO")
			else:
				print("NO")
		else:
			print("NO")
