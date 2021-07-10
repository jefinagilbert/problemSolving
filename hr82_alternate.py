def alternate(s):
    llist = []
    llist2 = []
    for i in s:
        if i not in llist:
            llist.append(i)
    for i in range(len(llist)):
        for j in range(i):
            if i == j:
                continue
            a = ''
            for k in s:
                if k == llist[i] or k == llist[j]:
                    a += k
            b = a[0]
            for k in range(len(a)):
                if k == 0:
                    continue
                if k%2 == 0:
                    if b[len(b)-1] != a[k]:
                        b += a[k]
                    else:
                        break
                else:
                    if b[len(b)-1] != a[k]:
                        b += a[k]
                    else:
                        break
            if a != b:
                pass
            else:
                llist2.append(len(a))
                print(a,b)
    if llist2 == []:
        return 0
    else:
        return max(llist2)


s = 'asvkugfiugsalddlasguifgukvsa'
print(alternate(s))
