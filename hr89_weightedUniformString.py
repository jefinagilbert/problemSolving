def weightedUniformStrings(s, queries):
    prev = ''
    hmap = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    llist = []
    for i in s:
        if len(prev) > 1:
            if i == prev[0]:
                prev += i
                a = len(prev)
                llist.append(a*hmap[i])
                a = 0
                continue
        if i == prev:
            prev += i
            llist.append(2*hmap[i])
        else:
            llist.append(hmap[i])
            prev = i
    res = []
    for i in queries:
        if i in llist:
            res.append('Yes')
        else:
            res.append('No')
    return res

def weightedUniformStrings(s,queries):
    hmap = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
    b = 0
    llist = []
    for i in queries:
        if i > 26:
            for j in range(1,26):
                if i%j == 0:
                    a = i//j
                    if a*hmap[j] in s:
                        b = 1
                        llist.append('Yes')
                        break
            if b == 0:
                llist.append('No')
            b = 0
        else:
            for j in range(1,i+1):
                if i%j == 0:
                    a = i//j
                    if a*hmap[j] in s:
                        b = 1
                        llist.append('Yes')
                        break
            if b == 0:
                llist.append('No')
            b = 0
    return llist


# stuck under time complexity



s = 'aaabbbbcccddd'
queries = [9,7,8,12,5]
print(weightedUniformStrings(s,queries))