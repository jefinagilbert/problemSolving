def flippingBits(n):
    a = bin(n)[2:]
    if len(a) >= 32:
        pass
    else:
        b = 32 - len(a)
        a = b*'0' + a
    c = ''
    for i in a:
        if i == '0':
            c += '1'
        else:
            c += '0'
    num = c
    dec_value = 0
    base1 = 1
    len1 = len(num);
    for i in range(len1 - 1, -1, -1):
        if (num[i] == '1'):    
            dec_value += base1
        base1 = base1 * 2  
    return dec_value

n = '1'
print(flippingBits(int(n)))


