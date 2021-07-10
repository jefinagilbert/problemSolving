def hackerrankInString(s):
    string = 'hackerrank'
    string2 = ''
    a = 0
    b = 0
    for i in range(len(s)):
        print(s[a:len(s)])
        for j in range(a,len(s)):
            if string[b] == s[j]:
                string2 += string[b]
                a = j+1
                b += 1
                if string2 == string:
                    return 'YES'
                if b == len(string):
                    return 'NO'
                break
            if len(s)-1 == j:
                return 'NO'
    if string2 == string:
        return 'YES'
    else:
        return 'NO'

# n = int(input())
# val = []
# for i in range(n):
#     s = input()
#     val.append(hackerrankInString(s))
# for i in val:
#     print(i)
s = 'knarrekcah'
print(hackerrankInString(s))