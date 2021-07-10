def anagram(s):
    if len(s)%2 == 1:
        return -1
    else:
        res = 0
        llist = []
        a = s[0:len(s)//2]
        b = s[len(s)//2:]
        print(a,b)
        for i in a:
            if i in b:
                temp = b
                b = ''
                k = 0
                for j in temp:
                    if k == 1:
                        b += j
                        continue
                    if j == i:
                        k = 1
                    else:
                        b += j
            else:
                res += 1
        return res

# sucks in TimeComplexity


q = int(input())
for i in range(q):
    s = input()
    print(anagram(s))