def closestNumbers(arr):
    llist = []
    llist1 = []
    last = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if last == 0:
                if 0 < arr[j]-arr[i]:
                    last = arr[j]-arr[i]
                    if arr[j] < arr[i]:
                        if [arr[j],arr[i]] in llist1:
                            continue
                        llist1.append([arr[j],arr[i]])
                        llist.append(last)
                    else:
                        if [arr[i],arr[j]] in llist1:
                            continue
                        llist1.append([arr[i],arr[j]])
                        llist.append(last)
                elif 0 < arr[i]-arr[j]:
                    last = arr[i] - arr[j]
                    if arr[j] < arr[i]:
                        if [arr[j],arr[i]] in llist1:
                            continue
                        llist1.append([arr[j],arr[i]])
                        llist.append(last)
                    else:
                        if [arr[i],arr[j]] in llist1:
                            continue
                        llist1.append([arr[i],arr[j]])
                        llist.append(last)
                continue
            if 0 < arr[i]-arr[j] <= last or 0 < arr[j]-arr[i] <= last:
                if 0 < arr[j]-arr[i] <= last:
                    last = arr[j]-arr[i]
                    if arr[j] < arr[i]:
                        if [arr[j],arr[i]] in llist1:
                            continue
                        llist1.append([arr[j],arr[i]])
                        llist.append(last)
                    else:
                        if [arr[i],arr[j]] in llist1:
                            continue
                        llist1.append([arr[i],arr[j]])
                        llist.append(last)
                elif 0 < arr[i]-arr[j] <= last:
                    last = arr[i] - arr[j]
                    if arr[j] < arr[i]:
                        if [arr[j],arr[i]] in llist1:
                            continue
                        llist1.append([arr[j],arr[i]])
                        llist.append(last)
                    else:
                        if [arr[i],arr[j]] in llist1:
                            continue
                        llist1.append([arr[i],arr[j]])
                        llist.append(last)

    llist2 = []
    for i in range(len(llist)):
        if llist[i] == last:
            for j in llist1[i]:
                llist2.append(j)
    llist2.sort()
    return llist2

# lol..... Time Complexity Again Sucks

arr = [-20,-3916237,-357920,-3620601,7374819,-7330761,30,6246457,-6461594,266854,-520,-470]
print(closestNumbers(arr))