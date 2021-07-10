def icecreamParlor(m, arr):
    a = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if i == j:
                continue
            if arr[i] + arr[j] == m:
                return [i+1,j+1]





arr = [2,2,4,3]
m = 4
print(icecreamParlor(m,arr))