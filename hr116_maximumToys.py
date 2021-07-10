def maximumToys(prices, k):
    prices.sort()
    a = 0
    b = 0
    for i in prices:
        if a+i > k:
            return b
        else:
            a = a+i
            b += 1
    return b



prices = [1,2,3,4]
k = 7
print(maximumToys(prices,k))