# def beautifulTriplets(d, arr):
# 	a = 0
# 	for i in range(len(arr)):
# 		for j in range(len(arr)):
# 			for k in range(len(arr)):
# 				if i == k == j:
# 					continue
# 				if arr[j]-arr[i] == arr[k]-arr[j] == d:
# 					a += 1
# 	return a

# my solution takes more time


#arr = [1,2,4,5,7,8,10]
#d = 3
#print(beautifulTriplets(d,arr))
d = 3
seq=[1,6,7,7,8,10,12,13,14,19]
print(sum([(i+d in seq and i-d in seq) for i in seq]))