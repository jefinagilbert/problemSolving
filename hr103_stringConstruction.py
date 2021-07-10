def stringConstruction(s):
    i = 0
    p = 0
    string = ''
    while i < len(s):
        if s[i] in string:
            pass
        else:
            p += 1
            string += s[i]
        i += 1
    return p




s = 'abab'
stringConstruction(s)
