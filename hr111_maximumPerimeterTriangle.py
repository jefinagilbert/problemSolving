from itertools import permutations
def maximumPerimeterTriangle(sticks):
    llist = permutations(sticks,3)
    j = 0
    llist1 =[0,0,0]
    for i in llist:
        k = list(i)
        a,b,c = k[0],k[1],k[2]
        if a+b>c:
            if a+c>b:
                if b+c>a:
                    if (a+b+c) >= j:
                        j = a + b + c
                        llist1[0],llist1[1],llist1[2] = a,b,c
    if sum(llist1) == 0:
        return [-1]
    else:
        llist1.sort()
        return llist1


sticks = [2,3,3]
print(maximumPerimeterTriangle(sticks))

