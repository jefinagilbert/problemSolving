def missingNumbers(arr, brr):
    arr1 = []
    for i in brr:
        if i in arr:
            arr.remove(i)
        else:
            if i not in arr1:
                arr1.append(i)
    arr1.sort()
    return arr1


arr = []
brr = []
k = input().split()
for i in k:
    arr.append(int(i))
k = input().split()
for i in k:
    brr.append(int(i))

print(missingNumbers(arr,brr))