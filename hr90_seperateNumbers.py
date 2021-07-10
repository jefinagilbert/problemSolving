def separateNumbers(s):
    if s[0] == '0':
        print('NO')
        return
    for i in range(1,len(s)+1):
        if s[0:i].count('9') == len(s[0:i]):
            c = s[0:i]
            a = len(s[0:i]) + 1
            b = 0
            for j in range(len(s[i:])):
                if b+a > len(s[i:]):
                    break
                if s[i:][b:a+b].count('9') == len(s[i:][b:a+b]):
                    a = len(s[i:][b:a+b]) + 1
                if int(s[i:][b:a+b]) - int(c) == 1:
                    c = s[i:][b:a+b]
                else:
                    break
                b += a
                if b+a > len(s[i:]):
                    if s[i:][b:a+b] == '':
                        pass
                    else:
                        break
                    print('YES',s[0:i])
                    return
        else:
            c = s[0:i]
            a = len(s[0:i])
            b = 0
            for j in range(len(s[i:])):
                if b+a > len(s[i:]):
                    break
                # print(int(s[i:][b:a+b]),int(c))
                if int(s[i:][b:a+b]) - int(c) == 1:
                    c = s[i:][b:a+b]
                    if b+a >= len(s[i:]):
                        print('YES',s[0:i])
                        return
                else:
                    break
                if c.count('9') == len(s[i:][b:a+b]):
                    a = len(s[i:][b:a+b]) + 1
                    b -= 1
                b += a
                if b+a > len(s[i:]):
                    if s[i:][b:a+b] == '':
                        pass
                    else:
                        break
                    print('YES',s[0:i])
                    return
    print('NO')
if __name__ == '__main__':
    s = '010203'
    separateNumbers(s)
