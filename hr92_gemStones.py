def gemstones(arr):
    j = ''
    a = 0
    llist = []
    for i in arr:
        if len(i) > len(j):
            j = i
    for i in j:
        if i in llist:
            continue
        for k in arr:
            if i in k:
                pass
            else:
                a = 1
                break
        if a == 1:
            a = 0
        else:
            llist.append(i)
    return len(llist)



arr = ['abcdde', 'baccd', 'eeabg']
gemstones(arr)