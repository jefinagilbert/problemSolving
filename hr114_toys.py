def toys(w):
    w.sort()
    a = 0
    b = 0
    for i in w:
        if a == 0:
            a = i + 4
            b += 1
        if 0 <= a-i <= a:
            pass
        else:
            a = i+4
            b += 1
    return b


w = [1,2,3,4,5,10,11,12,13]
print(toys(w))