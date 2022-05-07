# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 01:39:22 2022

@author: ADMIN
"""

# def sana(n):
#     print(n)
#     if n <= 1:
#         return
#     else:
#         sana(n - 1)
        
# sana(10)


# def faktorial(N):
#     i = 1
#     fakt = 1
#     while i!= N + 1:
#         fakt = fakt * i
#         i += 1
#     return fakt
    
# print(faktorial(5))


def f(n):
    if n == 1:
        return 1
    else:
        return n * f (n-1)
print(f(5))   
    
