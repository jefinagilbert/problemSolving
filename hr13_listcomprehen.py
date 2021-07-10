if __name__ == '__main__':
    llist = []
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k == n:
                    continue
                else:
                    llist.append([i,j,k])
    print(llist)