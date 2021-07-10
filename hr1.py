if __name__ == '__main__':
    N = int(input())
    l = []
    k = 0
    entry = input().split()
    rc = entry[0]
    
    while N > k:
        if "append" == rc:
            l.append(entry[1])
        elif "insert" == rc:
            l.insert(int(entry[1]),int(entry[2]))
        elif "remove" == rc:
            l.remove(int(entry[1]))
        elif "reverse" == rc:
            l.reverse()
        elif "pop" == rc:
            l.pop()
        elif "print" == rc:  
            print(l)
        elif "sort" == rc:      
            l.sort()
        else:
            print("invalid")
        k += 1

    
