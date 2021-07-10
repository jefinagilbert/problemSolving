def marsExploration(s):
    res = 0
    a = 0
    b = 3
    for i in range(len(s)):
        c = s[a:b]
        for j in range(len(c)):
            if j == 0:
                if c[j] != 'S':
                    res += 1
            elif j == 1:
                if c[j] != 'O':
                    res += 1
            elif j == 2:
                if c[j] != 'S':
                    res += 1
        a += 3
        b += 3
        if b > len(s):
            break
    return res






s = 'SOSSOSSOS'
print(marsExploration(s))