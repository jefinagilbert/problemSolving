def quickSort(arr):
    p = arr[0]
    left = []
    right = []
    equal = []
    for i in range(len(arr)):
        if arr[i] == p:
            equal.append(arr[i])
        elif arr[i] > p:
            right.append(arr[i])
        elif arr[i] < p:
            left.append(arr[i])
    return left+equal+right


    


arr =[4, 5, 3, 7, 2]
quickSort(arr)