# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 20:07:45 2022

@author: ADMIN
"""

# Yevklid algoritmi orqali 2 sonning eng katta umumiy bo’luvchisini
# (EKUB) topuvchi funksiya yozish.

# Buning uchun quyidagi ikki usuldan foydalanish mumkin:
    
# 1-usul Sonlarni ayirish usuli
# Deylik bizga 45 va 27 sonlari berilgan, keling ularning EKUB topamiz.

# 45-27=18
# 27–18=9
# 18–9=9
# 9–9=0

# Ayirish jarayoni to natija 0 ga (ya’ni ikki son teng) bo’lgunga qadar 
# davom etadi (rekursiya uchun to’xtash sharti).

a = 104
b = 36

def gcd(a,b):    
    if a==0:
        return b
    if a>b:
        a,b=b,a    
    return gcd(b-a,a)

print(gcd(a, b))

# 2-usuli Sonlarni bo’lish va qoldiq olish usuli
# Ikkita sondan kattasini kichigiga bo’lib qoldiq olamiz.
# Ularni o’rnini almashtiramiz
# 1- va 2-qadamlarni sonlardan biri nol bo’lib qolguncha davom ettiramiz
# Qolgan son shu ikki son uchun EKUB bo’ladi.
# 45 va 27 sonalri uchun EKUB hisoblaymiz

# 45%27=18 (qoldiq)
# 27%18=9
# 18%9=0

def gcd(a, b):
    if a == 0 :
        return b      
    return gcd(b%a, a)

print(gcd(a, b))