a = int(input())
b = input().split()
shoes = []
total = 0
for i in b:
	shoes.append(int(i))
noofpurshoes = int(input())
for i in range(noofpurshoes):
	purshoes = input().split()
	if int(purshoes[0]) in shoes:
		total += int(purshoes[1])
		shoes.remove(int(purshoes[0]))
print(total)

