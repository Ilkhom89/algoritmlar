# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 03:41:28 2021

@author: ADMIN
"""
######    LINEAR    SEARCH     ##########

# Bizga quyidagi massiv berilgan:

# myList = [1,3,4,6,7,8,10,12,23,45,56,78,99]

# Massiv ichidan bizga kerakli qiymatning indeksini (tartib raqamini) linear 
# search yordamida qaytaruvchi funksiya yozing. Agar qidiralayotgan qiymat 
# massiv ichida mavjud bo’lmasa -1 yoki None qiymatini qaytaring.


# myList1 = [1,3,4,6,7,8,10,12,23,45,56,78,99]



# def linear_search(list, item):
#     for n in range(len(list)):
#         if list[n]==item:
#             return n
#     return None

# mylist = [1,3,4,6,7,8,10,12,23,45,56,78,99]
# item = int(input("nechi sonni qidirayabsiz?: "))
# javob3 = linear_search(mylist,item)
# print(javob3)







#####  BINARY    SEARCH    #####


# Massiv ichidan bizga kerakli qiymatning indeksini (tartib raqamini) binary 
# search yordamida qaytaruvchi funksiya yozing. Agar qidiralayotgan qiymat 
# massiv ichida mavjud bo’lmasa -1 yoki None qiymatini qaytaring.

# def binary_search(list, item):
#     low = 0
#     high = len(list)-1
#     while low <= high:
#         mid = (low + high)//2
#         guess = list[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None

# myList1 = [1,3,4,6,7,8,10,12,23,45,56,78,99]
# print(linear_search(myList1,11))
# print(binary_search(myList1,99))

# myList2 = [18,12,25,1,3,4,10,5,23,4,13,89]
# myList2.sort()
# print(linear_search(myList2,13))
# print(binary_search(myList2,13))


# mevalar = ['olma','anor','olcha','behi','shaftoli','anjir']
# mevalar.sort()
# print(mevalar)
# print(binary_search(mevalar,'behi'))
# print(linear_search(mevalar,'behi'))