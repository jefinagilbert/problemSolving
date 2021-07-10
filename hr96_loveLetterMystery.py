def theLoveLetterMystery(s):
    hmap = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    s1 = ''
    s2 = ''
    if len(s)%2 == 1:
        s1 = s[0:len(s)//2]
        s2 = s[(len(s)//2)+1:]
    else:
        s1 = s[0:len(s)//2]
        s2 = s[len(s)//2:]
    temp = s2
    s2 = ''
    for i in reversed(temp):
        s2 += i
    res = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            pass
        else:
            if hmap[s1[i]] > hmap[s2[i]]:
                res += hmap[s1[i]]-hmap[s2[i]]
            else:
                res += hmap[s2[i]]-hmap[s1[i]]
    return res



s = 'abcba'
theLoveLetterMystery(s)