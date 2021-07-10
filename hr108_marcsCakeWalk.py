def marcsCakewalk(calorie):
    a = 0
    j = 0
    calorie.sort()
    for i in reversed(calorie):
        a += i*(2**j)
        j += 1
    return a

calorie = [7,4,9,6]
marcsCakewalk(calorie)