def repeatedString(s, n):
    return s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")


s = 'abcd'
n = 10
print(repeatedString(s,n))