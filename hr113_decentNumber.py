def decentNumber(n):
    i = 3
    a = n//3
    b = n%3
    j = 5
    if b != 0:
        while b%j != 0:
            b += 3
            a -= 1
            if b > n:
                break
    k = a*3
    if a < 0 or b < 0:
        return '-1'
    elif a == 0 and b == 0:
        return '-1'
    elif a == 0:
        return b*'3'
    elif b == 0:
        return k*'5'
    else:
        return k*'5'+b*'3'


n = 12002
print(decentNumber(n))