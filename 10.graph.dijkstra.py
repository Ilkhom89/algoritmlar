# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 12:29:58 2022

@author: ADMIN
"""

#           1- Qadam. Graph yasaymiyz.


# Hash jadvallari yordamida graph yasaymiz

graph = {}
graph['A'] = ['B','C'] # A nuqtadan B va C ga borish mumkin

# Lekin Avvalgidan farqli ravishda bu graphda vaznlar ham bor. Vaznlarni qanday 
# qo'shamiz?
# Vaznlarni ham alohida Hash jadval ko'rinishida saqlaymiz.

graph['A'] = {}
graph['A']['B'] = 2
graph['A']['C'] = 6

# Ya'ni bir hash jadval ichida yana bir Hash jadval bo'ladi.

print(graph)

# A nuqtaning qo'shnilarini .keys() metodi yordamida ko'rishimiz mumkin:

print(graph['A'].keys())

# A nuqtadan qo'shni nuqtalarga masofani esa quyidagicha ko'ramiz:

print(graph['A']['B'])
print(graph['A']['C'])


# Yuqoridagi usul bilan Graphni qayta yarataylik:
    
graph={
    'A':{'B':2, 'B':6},
    'B':{'C':3, 'D':4},
    'C':{'D':5, 'E':6},
    'D':{'F':5},
    'E':{'F':0},
    'F':{}
}
    
from pprint import pprint as print # graphlarni chiroyliroq chiqarish uchun funksiya
print(graph)
    



#          2-Qadam. Narxlar uchun jadval.
    
    
    
# Darsimiz davomida narxlarni ham saqlab borish uchun alohida jadval 
# yaratgan edik.
    
# Bevosita qidirish algoritmini boshlashdan avval biz faqatgina 
# qo'shni tugunlargacha narxni bilamiz xolos (2 va 6), qolgan tugunlarga esa 
# narx aniq emas, shuning uchun bu joyda cheksizlik qiymatini qo'ydik.

# Yuqoridagi jadvalni kodlaymiz. Buning uchun ham alohida Hash jadval yaratamiz.    
    
    
narxlar = {
    'B': 2,
    'C': 6,
    'D': float('inf'),
    'E': float('inf'),
    'F': float('inf')
}
    




#          3-Qadam. Ota tugunlarni saqlab borish
    
    
# Narxlardan tashqari bir tugundan ikkinchi tugunga o'tishda "ota tugunlar"ni 
# ham saqlab borishimiz kerak. Qidirish boshida ba'zi tugunlar uchun ota 
# tugunlar aniq emas.


otalar = {
    'B': 'A',
    'C': 'A',
    'D': None,
    'E': None,
    'F': None,    
}
    
# Vanihoyat ishlov berilgan tugunlarni saqlab borish uchun ham bitta ro'yxat 
# tayyorlaylik (bitta tugunga 2 marta kirmaslik uchun)

ishlandi = []











#                          QIDIRISH ALGORITMI    
    










# 1. Eng arzon tugun topish uchun funksiya


def eng_arzon_tugun_top(narxlar):
    eng_arzon = float('inf')
    eng_arzon_tugun = None
    for tugun in narxlar:
        narx = narxlar[tugun]
        if narx < eng_arzon and tugun not in ishlandi:
            eng_arzon = narx
            eng_arzon_tugun = tugun
    return eng_arzon_tugun



# Funksiyani tekshirib ko'ramiz:

print(narxlar)
tugun = eng_arzon_tugun_top(narxlar)
print(f"Eng arzon tugun: {tugun}")


# 2. Dijkstra Algoritmi kodi

tugun = eng_arzon_tugun_top(narxlar) # A nuqtaga eng arzon tugundan boshlaymiz
print(tugun)

while tugun is not None:
    qoshnilar = graph[tugun] # Eng yaqin tugunning qo'shnilarini topamiz
    narx = narxlar[tugun] # Ularning narxini olamiz
    for qoshni in qoshnilar.keys(): # Har bir qo'shni uchun...
        yangi_narx = narx + qoshnilar[qoshni] # shu qo'shniga borish narxini hisoblaymiz
        if narxlar[qoshni]>yangi_narx: # agar bu tugunga borish avvalgidan arzonroq bo'lsa:
            narxlar[qoshni] = yangi_narx # shu tugunga borish narxini yangilaymiz
            otalar[qoshni] = tugun # va bu tugun otasini ham yangilaymiz.
    ishlandi.append(tugun) # tugunn ishlov berilgan tugunlar qatoriga qo'shamiz
    tugun = eng_arzon_tugun_top(narxlar)
    


# Keling endi A nuqatadan boshqa barcha nuqtalargacha borish narxini ko'ramiz:

print(narxlar)

# Yuqoridan ko'rishimiz mumkin, F nuqtagacha borish narxi 11 ekan.






















