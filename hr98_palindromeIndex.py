def palindromeIndex(s):
    if s[::-1] == s:
        return -1
    for i in range(len(s)):
        temp = s[0:i]+s[i+1:]
        if temp == temp[::-1]:
            return i

    #havent Solved/loop exists
        




s = 'aab'
print(palindromeIndex(s))