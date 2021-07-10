def minimumAbsoluteDifference(arr):
    llist = []
    arr.sort()
    print(arr)
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if i == j:
                continue
            llist.append(abs((arr[i])-(arr[j])))
    return min(llist)

def minimumAbsoluteDifference(arr):
    min_abs = min((abs(arr[i] - arr[i-1]) for i in range(1, len(arr))))
    s = set()
    for x in arr:
        if x in s:
            return 0
        for d in range(1, min_abs):
            if x + d in s or x - d in s:
                min_abs = d
                break
        s.add(x)
    return min_abs


#this is my simple solution
def minimumAbsoluteDifference(arr):
    arr.sort()
    return min((abs((arr[i])-(arr[i-1])) for i in range(1,len(arr))))




arr = []
st = input().split()
for i in st:
    arr.append(int(i))
print(minimumAbsoluteDifference(arr))