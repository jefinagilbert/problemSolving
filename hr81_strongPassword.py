def minimumNumber(n, password):
    weak = 0
    dig = 1
    upp = 1
    low = 1
    spcl  = 1
    numbers = "0123456789"
    special_characters = "!@#$%^&*()-+"
    if len(password) < 6:
        for i in password:
            if i.isdigit():
                dig = 0
            if i.isupper():
                upp = 0
            if i.islower():
                low = 0
            if i in special_characters:
                spcl = 0
        if len(password)+low+upp+spcl+dig >= 6:
            return low+upp+spcl+dig
        else:
            a = 6 - (len(password)+low+upp+spcl+dig)
            return a +low+upp+spcl+dig
            
    for i in password:
        if i.isdigit():
            dig = 0
        if i.isupper():
            upp = 0
        if i.islower():
            low = 0
        if i in special_characters:
            spcl = 0
    if low+upp+spcl+dig == 0:
        return 0
    else:
        return dig + upp + low + spcl




n = 3
password = 'zss'
print(minimumNumber(n,password))





# def minimumNumber(n, password):
#     weak = 0
#     dig = 1
#     upp = 1
#     low = 1
#     spcl  = 1
#     numbers = "0123456789"
#     special_characters = "!@#$%^&*()-+"
#     if len(password) < 6:
#         return 6 - len(password)
#     for i in password:
#         if i.isdigit():
#             dig = 0
#         if i.isupper():
#             upp = 0
#         if i.islower():
#             low = 0
#         if i in special_characters:
#             spcl = 0
#     return dig + upp + low + spcl