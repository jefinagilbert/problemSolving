def lonelyinteger(a):
    llist = []
    for i in a:
        if i in llist:
            continue
        else:
            if a.count(i) == 1:
                return i
            else:
                llist.append(i)



a = [0,0,1,2,1]
print(lonelyinteger(a))