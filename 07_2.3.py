# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 20:41:04 2022

@author: ADMIN
# """

# from random import randrange

# def qsort(array):
#     if len(array) < 2:
#         return array
#     else:
#         # pivot = array.pop(0) # tayanch nuqta 1-element olinadi
#         pivot = array.pop(randrange(len(array))) # tayanch nuqta ixtiyoriy
#         kichik = [i for i in array if i <= pivot]
#         katta = [i for i in array if i > pivot]
#         # print(f"{kichik} + [{pivot}] + {katta}")
#         return qsort(kichik) + [pivot] + qsort(katta)

# if __name__ == '__main__':
#     array1 = [64,454,611,2115,544,-56,48,-9787,442,2216,4562]
#     print(qsort(array1))
#     array2 = list(range(20))
#     print(qsort(array2))
#     array3 = ['apple','anor','behi','grape','orange','melon','watermelon']
#     print(qsort(array3))
    







# BU funksiyaga tushunmadim git hubdan topib ko'r

# def binarySearch(array,value,start=0,end=None):
#     if end is None:
#         end = len(array)-1
#     if start>end:
#         return None
    
#     mid = (start+end)//2
#     if array[mid]==value:
#         return mid
#     elif array[mid]>value:
#         return binarySearch(array,value,start,mid-1)
#     else:
#         return binarySearch(array,value,mid+1,end)
#     return None

# array =  [45,65,88,121,354,454,547,654,758,874,917]
# print(qsort(array))


