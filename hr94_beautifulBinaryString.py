def beautifulBinaryString(b):
    i = 0
    a = 0
    while i < len(b):
        if b[i] == '0':
            if b[i:i+3] == '010':
                a += 1
                i += 3
                continue
        i += 1
    return a


b = '0101010'
print(beautifulBinaryString(b))