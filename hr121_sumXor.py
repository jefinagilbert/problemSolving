def sumXor(n):
    c = 0
    while(n):
        c += n%2 if 0 else 1
        n /= 2
    c = pow(2,c)
    return c

#but i had a solution... It is really worse...

n = 0
print(sumXor(n))