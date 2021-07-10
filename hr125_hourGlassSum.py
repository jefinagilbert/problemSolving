def hourglassSum(arr):
    llist = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if j+2 >= len(arr[i]):
                continue
            if i+2 >= len(arr):
                continue
            a = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            llist.append(a)
    return max(llist)


arr = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]
print(hourglassSum(arr))