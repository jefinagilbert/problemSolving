def alternatingCharacters(s):
    prev = ''
    a = 0
    for i in s:
        if i == prev:
            a += 1
        else:
            prev = i
    return a




s = 'AABAAB'
alternatingCharacters(s)