def gridChallenge(grid):
    hmap = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    if len(grid) > len(grid[0]):
        l = len(grid)
    else:
        l = len(grid[0])
    for i in range(len(grid)):
        g = grid[i]
        g1 = sorted(g)
        grid[i] = "".join(g1)
    for i in range(l):
        last1 = 0
        last = 0
        for j in range(l):
            if i >= len(grid) or j >= len(grid[0]):
                pass
            else:
                if last1 <= hmap[grid[i][j]]:
                    last1 = hmap[grid[i][j]]
                else:
                    return 'NO'
            if i >= len(grid[0]) or j >= len(grid):
                continue
            if last <= hmap[grid[j][i]]:
                last = hmap[grid[j][i]]
            else:
                return 'NO'
    return 'YES'







grid = ['abcde','hjkee','mpqee','rtvee']
print(gridChallenge(grid))