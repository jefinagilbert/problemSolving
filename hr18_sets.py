n = int(input())
set1 = input().split()
set1 = set(set1)
k = 0
for i in set1:
	k += int(i)
print(k/len(set1))