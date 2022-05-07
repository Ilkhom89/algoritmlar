# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 23:06:01 2022

@author: ADMIN
"""

array= [1,5,565,554,884,557,77,44,552,995,954,53,2,855,255,56,666,55,41]
print(sorted(array))
print(array)

def findMax(array):
    max = array[0]
    max_index = 0
    for n in range(1,len(array)):
        if array[n]>max:
            max = array[n]
            max_index = n
    return max_index

def selectSort(array):
    newArray = []
    for n in range(len(array)):
        max_index = findMax(array)
        newArray.append(array.pop(max_index))
    return newArray

print(max(array))
print(findMax(array))
print(array.index(max(array)))
print(selectSort(array))

