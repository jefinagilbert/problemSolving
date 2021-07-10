def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        if A[i] + B[i] >= k:
            pass
        else:
            return 'NO'
    return 'YES'

# simple


A = [7, 8, 9]
B = [2, 1, 3]
k = 10
print(twoArrays(k,A,B))