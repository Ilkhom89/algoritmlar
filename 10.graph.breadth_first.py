# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 04:32:54 2022

@author: ADMIN
"""

from collections import deque


def search(start_node, target = 'elon musk'):
    search_queue = deque()
    search_queue += graph[start_node]
    searched = set()
    
    
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person == target:
                print(f'{target}ni topdik !')
                print(searched)
                return True
        
            else:
            
                search_queue += graph[person]
                searched.add(person)
    return False
        
    

if __name__ == '__main__':





    graph = {'siz' : ['ali', 'vali', 'tohir'],
             'ali' : ['aziza', 'olim'],
             'vali': ['botir', 'ziyoda'],
             'tohir':['elon musk','mohir'],
             'aziza':[],
             'olim' :[],
             'botir':[],
             'ziyoda':[],
             'elon musk':[],
             'mohir':[]
             }
    
    
    search("siz","elon musk")          # ishladi
    # search("botir","elon musk")      # ishlamadi