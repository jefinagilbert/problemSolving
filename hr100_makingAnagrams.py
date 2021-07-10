def makingAnagrams(s1, s2):
    if len(s1) >= len(s2):
        llist = []
        a = 0
        for i in s2:
            if i in llist:
                continue
            if i in s1:
                if s1.count(i) - s2.count(i) <= 0:
                    pass
                else:
                    a += s1.count(i) - s2.count(i) 
            else:
                a += s2.count(i)
            llist.append(i)
        llist = []
        for i in s1:
            if i in llist:
                continue
            if i in s2:
                if s2.count(i) - s1.count(i) <= 0:
                    pass
                else:
                    a += s2.count(i) - s1.count(i)
            else:
                a += s1.count(i)
            llist.append(i)
        return a
    else:
        llist = []
        a = 0
        for i in s1:
            if i in llist:
                continue
            if i in s2:
                if s2.count(i) - s1.count(i) <= 0:
                    pass
                else:
                    a += s2.count(i) - s1.count(i)
            else:
                a += s1.count(i)
            llist.append(i)
        llist = []
        for i in s2:
            if i in llist:
                continue
            if i in s1:
                if s1.count(i) - s2.count(i) <= 0:
                    pass
                else:
                    a += s1.count(i) - s2.count(i) 
            else:
                a += s2.count(i)
            llist.append(i)
        return a


s1 = 'djfladfhiawasdkjvalskufhafablsdkashlahdfa'
s2 = 'absdjkvuahdakejfnfauhdsaavasdlkj'
print(makingAnagrams(s1,s2))