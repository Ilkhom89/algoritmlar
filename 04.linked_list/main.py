# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 01:21:30 2022

@author: ADMIN
"""

from linkedlistfuncs import Node, LinkedList

## Linked List yaratamiz
llist = LinkedList()

## uchta node (tugun) yaratamiz 
llist.head = Node("Dushanba")
tuesday = Node("Seshanba")
wednesday = Node("Chorshanba")
# thursday = Node("Payshanba")
# friday = Node("Juma")
# saturday = Node("Shanba")
# sunday = Node("Yakshanba")

## Tugunlarni bog'laymiz
llist.head.next = tuesday
tuesday.next = wednesday
# wednesday.next = thursday
# thursday.next = friday
# friday.next = saturday
# saturday.next = sunday

## Linked Listni konsolga chiqaramiz
# llist.printList()


## List boshiga yangi tugun qo'shamiz
llist.push("Yakshanba")
# llist.printList()


##Listni o'rtasiga yangi tugun qo'shamiz
llist.insertAfter(llist.head.next, "Dushanba kechasi")
#llist.printList()


## List oxiriga yangi tugun qo'shish
llist.append("Pyshanba")
llist.append("Juma")
# llist.printList()


## Element o'chiramiz
llist.deleteNode("Dushanba kechasi")
llist.printList()





















