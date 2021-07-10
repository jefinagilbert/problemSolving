def jimOrders(orders):
    llist = []
    llist1 = []
    llist2 = []
    j = 1
    k = 1
    for i in orders:
        llist.append(j)
        llist1.append(sum(i))
        j += 1
    for i in range(len(llist)):
        a = min(llist1)
        b = llist1.index(a)
        llist1.pop(b)
        llist2.append(llist[b])
        llist.pop(b)
    return llist2



orders = [[1,1],[1,2],[2,2]]
print(jimOrders(orders))