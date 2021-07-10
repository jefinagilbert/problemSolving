def pangrams(s):
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alpha = ''
    for i in s:
        if i.isalpha() and i.lower() not in alpha:
            if s.count(i) <= 0:
                return 'not pangram'
            alpha += i.lower()
    if len(alpha) != 26:
        return 'not pangram'
    else:
        return 'pangram'





s = 'We promptly judged antique Ivory Buckles for the nexxt prize'
print(pangrams(s))