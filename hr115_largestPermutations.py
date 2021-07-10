def largestPermutation(k, arr):
    llist = []
    x = 0
    llist = arr[:]
    llist.sort(reverse=True)
    for i in range(len(arr)):
        if llist[i] == arr[i]:
            pass
        else:
            a = llist[i]
            b = arr[i]
            c = arr.index(a)
            arr.remove(a)
            arr.insert(i,a)
            arr.remove(b)
            arr.insert(c,b)
            x += 1
        if x == k:
            return arr
    return arr

# Time Complexity. :(


arr = [2,1,3]
k = 1
print(largestPermutation(k,arr))