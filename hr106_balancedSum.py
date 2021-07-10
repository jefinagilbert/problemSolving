def balancedSum(arr):
    for i in range(len(arr)):
        a = sum(arr[0:i])
        b = sum(arr[i+1:len(arr)])
        if a == b:
            return 'YES'
    return 'NO'

    # upside is mine.... Down is Stolen... But this is Disgusting////


def balancedSums(arr):
    tot = sum(arr)
    add = 0
    for i in arr:
        if add == tot-i-add:
            return "YES"
        add+=i
    return "NO"


arr = [1,2,3,4]
print(balancedSums(arr))