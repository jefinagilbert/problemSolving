def gameOfStone(n):
    if n >= 5:
        a = n%5
        b = n//5
    elif 5 > n >= 3:
        a = n%3
        b = n//3
    elif n == 2:
        a = n%2
        b = n//2
    else:
        return 'Second'
    if a == 0:
        return 'First'
    else:
        if a-5 >= 0 and a-5 != 2 and a-5 != 3 and a-5 != 5:
            if a-5 == 0:
                return 'Second'
            else:
                b+=1
        elif a-3 >= 0 and a-3 != 2 and a-3 != 3 and a-3 != 5:
            if a-3 == 0:
                return 'Second'
            else:
                b+=1
        elif a-2 >= 0 and a-2 != 2 and a-2 != 3 and a-2 != 5:
            if a-2 == 0:
                return 'Second'
            else:
                b+=1    
        else:
            return 'First'
        if b%2 == 0:
            return 'First'
        else:
            return 'Second'


# llist = []
# for i in range(1,101):
#     llist.append(gameOfStones(i))
# for i in llist:
#     print(i)




# Took it


def gameOfStones(n):
    if n%7 < 2:
        return 'Second'
    else:
        return 'First'
n = 9
print(gameOfStones(n))
