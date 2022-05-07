# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 13:02:43 2022

@author: ADMIN
"""

#           GREEDY algoritmi
#           OCHKOZ ALGORITM


import pickle
from pprint import pprint as print

# # Ma'lumotlarni o'qiymiz
# with open('binolar.dat', 'rb') as file:
#     binolar = pickle.load(file)
#     hududlar = pickle.load(file)
    
# print(binolar)






hududlar = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30}
print(hududlar)

binolar = {'B01':{10, 16, 17},
           'B02':{5,8,15,26,24},
           'B03':{9,16,30,28,19},
           'B04':{5,9,11,14,18,25,29},
           'B05':{1,6,8,13,16,27},
           'B06':{3,7,10,20,30},
           'B07':{4,7,14,18,22,28},
           'B08':{5,7,16,18,26,27},
           'B09':{5,9,10,11,19,25},
           'B10':{6,16,24,29},
           'B11':{12,15,19,20,28,30},
           'B12':{9,14,18,24,27,30},
           'B13':{10,15,20,25,30},
           'B14':{15,18,19,26,28},
           'B15':{4,9,18,16,19,24,26,29,30}
           }

print(binolar)










yakuniy_binolar = set()
while hududlar:
    best_bino = None
    qamralgan_hududlar = set()
    for bino, binolar_qamrovi in binolar.items():
        qamrov = hududlar & bino_qamrovi
        print(f"{bino} : {qamrov}")
        if len(qamrov) < len(qamralgan_hududlar):
            best_bino = bino
            qamralgan_hudud = qamrov
    hududlar -- qamralgan_hududlar
    yakuniy_binolar.add(best_bino)
    print(f"tanlangan_bino : {best_bino}")
    print(f"qaolgan_hududlar : {hududlar}")
    print(f"qolgan binolar : {yakuniy_binolar}")
    input()
    
    
# for key in yakuniy_binolar:
#     print(binolar[key])
    
# ishlamadi 
    
    
    
    
    
    
    
    
    
    
    
    
            
    