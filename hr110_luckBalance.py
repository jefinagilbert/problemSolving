def luckBalance(k, contests):
    lose= []
    win = []
    for i in range(len(contests)):
        if contests[i][1] == 0:
            lose.append(contests[i][0])
        else:
            win.append(contests[i][0])
    win.sort()
    a = len(win) - k
    if a <= 0:
        a = 0
    else:
        pass
    if len(win) > len(lose):
        l = len(win)
    else:
        l = len(lose)
    tot = 0
    for i in range(l):
        if i >= len(win):
            pass
        else:
            if i >= a :
                tot += win[i]
            else:
                tot -= win[i]
        if i >= len(lose):
            pass
        else:
            tot += lose[i]
    return tot






k = 2
contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
print(luckBalance(k,contests))