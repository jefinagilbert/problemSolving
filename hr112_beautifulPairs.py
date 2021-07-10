def beautifulPairs(A, B):
    l = len(A)
    a = 0
    sam =[]
    for i in A:
        sam.append(i)
    for i in range(l):
        if sam[i] in B:
            B.remove(sam[i])
            A.remove(sam[i])
            a += 1
    if len(A) != 0:
        if len(B) != 0:
            return a+1
    if l == a:
        return a-1


A = [1]
B = [1]
print(beautifulPairs(A,B))