def findMedian(arr):
    arr.sort()
    return arr[len(arr)//2]


arr = [5,3,1,2,4]
print(findMedian(arr))