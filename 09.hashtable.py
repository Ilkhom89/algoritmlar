# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 18:05:52 2022

@author: ADMIN
"""

#####  HASH FUNKSIYA YARATISH  #####


## 1-HASH FUNKSIYA
# def hashfunk(text):
#     """kiritilgan matn uzunligini hash sifatida qaytaradi"""
#     return len(text)

# print(hashfunk("apple"))
# print(hashfunk("grape"))
# print(hashfunk("strawberry"))




# # 2-HASH FUNKSIYA
# import string
# alphabet = list(string.ascii_lowercase)  # pythondagi tayyor lotin alifbosi
# def hashfunk2(text):
#     """Kiritilgan matinni bosh harfini index sifatida qaytaradi"""
#     return alphabet.index(text[0].lower())

# print(hashfunk2("melon"))
# print(hashfunk2("raspberry"))
# print(hashfunk2("pear"))
# print(hashfunk2("peach"))






# 3-HASH FUNKSIYA. TUB SONLAR VA MODULO
# Ushbu hash funksiya 2 qadamdan iborat:

# 1.Kiritlgan matnning har bir harfini mos tub songa almashtiradi va barcha 
# sonlarni qo'shib yuboradi
# 2.Yuqoridagi yig'indini 10 ga bo'ladi va qoldiqni qaytaradi
# Masalan bad so'zi uchun hash qiymatini hisoblaymiz:

# Tub sonlar a=2, b=3, c=5, d=7, e=11, f=13, g=17, h=19 va hokazo bo'lsa, bad so'zi 3+2+7=12 bo'ladi
# bad = 3+2+7=12 va 12%10=2

# import string
# alphabet = list(string.ascii_lowercase)  # pythondagi tayyor lotin alifbosi
# primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 
#           59, 61, 67, 71, 73, 79, 83, 89, 97, 101) # 26 ta tub son

# def hashfunk3(text):
#     sum = 0
#     for t in text.lower():
#         sum += primes[alphabet.index(t)]
#     return sum % 10

# print(hashfunk3("bad"))
# print(hashfunk3("apple"))







