def maximizingXor(l, r):
    res = 0
    for i in range(l,r+1):
        for j in range(i,r+1):
            if i^j > res:
                res = i^j
    return res
            

l = 11
r = 12
print(maximizingXor(l,r))