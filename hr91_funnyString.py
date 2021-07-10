def funnyString(s):
    slist = []
    rlist = []
    j = len(s) - 1
    for i in range(len(s)):
        slist.append(ord(s[i]))
        rlist.append(ord(s[j]))
        j -= 1
    for i in range(len(slist)):
        if i+1 >= len(slist):
            break
        if abs(slist[i]-slist[i+1]) == abs(rlist[i]-rlist[i+1]):
            pass
        else:
            return 'Not Funny'
    return 'Funny'



if __name__ == '__main__':
    s = 'bcxz'
    print(funnyString(s))