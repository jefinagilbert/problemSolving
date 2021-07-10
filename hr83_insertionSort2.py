
# aataya potathu... And Learn...

def insertionSort2(n,arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        if i == 1:
            for i in arr:
                print(i,end=" ")
        else:
            print()
            for i in arr:
                print(i,end=" ")

arr = [4,1,3,5,6,2]
n = 6
insertionSort2(n,arr)


# [8,7,6,5,4,3,2,1]
# 7 8 6 5 4 3 2 1
# 6 7 8 5 4 3 2 1
# 5 6 7 8 4 3 2 1
# 4 5 6 7 8 3 2 1
# 3 4 5 6 7 8 2 1
# 2 3 4 5 6 7 8 1
# 1 2 3 4 5 6 7 8










# def insertionSort2(n, arr):
#     arr2 = []
#     for i in arr:
#         arr2.append(i)
#     arr2.sort()
#     for i in range(n):
#         if i == n-1:
#             continue
#         if arr[i] < arr[i+1]:
#             if i == 1:
#                 if i == 0:
#                     for i in arr:
#                         print(i,end=" ")
#                 else:
#                     print()
#                     for i in arr:
#                         print(i,end=" ")
#                 if arr == arr2:
#                     return
#                 continue
#             for j in reversed(range(i)):
#                 if arr[j] > arr[j-1]:
#                     continue
#                 else:
#                     s = j-1
#                     if s < 0:
#                         break
#                     arr.pop(s)
#                     arr.insert(j+1,arr[j-1])
#                     break
#             if i == 0:
#                 for i in arr:
#                     print(i,end=" ")
#             else:
#                 print()
#                 for i in arr:
#                     print(i,end=" ")

#             if arr == arr2:
#                 return

#         else:
#             if i+1 == n-1:
#                 for j in reversed(range(i)):
#                     if arr[i+1] < arr[j]:
#                         continue
#                     else:
#                         s = arr[i+1]
#                         if s < 0:
#                             break
#                         arr.pop(i+1)
#                         arr.insert(j+1,s)
#                         break
#                 if i == 0:
#                     for i in arr:
#                         print(i,end=" ")
#                 else:
#                     print()
#                     for i in arr:
#                         print(i,end=" ")
#                 if arr == arr2:
#                     return
#             s = arr[i]
#             arr[i] = arr[i+1]
#             arr[i+1] = s
#             if i == 1:
#                 if i == 0:
#                     for i in arr:
#                         print(i,end=" ")
#                 else:
#                     print()
#                     for i in arr:
#                         print(i,end=" ")
#                 if arr == arr2:
#                     return
#                 continue
#             for j in reversed(range(i)):
#                 if arr[j] > arr[j-1]:
#                     continue
#                 else:
#                     s = j-1
#                     if s < 0:
#                         break
#                     arr.insert(j+1,arr[j-1])
#                     arr.pop(s)
#                     break
#             if i == 0:
#                 for i in arr:
#                     print(i,end=" ")
#             else:
#                 print()
#                 for i in arr:
#                     print(i,end=" ")
#             if arr == arr2:
#                 return 