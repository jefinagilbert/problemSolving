def twoStrings(s1, s2):
    for i in s1:
        if i in s2:
            return 'YES'
    return 'NO'


s1 = 'h'
s2 = 'world'
print(twoStrings(s1,s2))