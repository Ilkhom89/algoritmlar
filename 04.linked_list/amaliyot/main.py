# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 18:40:47 2022

@author: ADMIN
"""

from linkedlistfunc import Node , LinkedList
llist = LinkedList()

llist.head = Node("06:25 - uyg'onish")
yuv = Node("06:40 - ertalabki yuvinish")
zav =Node("07:50 - nonushta")


llist.head.next = yuv
yuv.next = zav

# llist.printList()

llist.push("06:20 - uyg'onishga tayyargarlik")
# llist.printList()

llist.insertAfter(llist.head.next,"06:30 - badantarbiya")
# llist.printList()

llist.append("08:00 - o'z ustimda ishlash 'MASHLG'ULOT'")
llist.append("12:30 - tushlik ")
llist.append("13:00 - kitob o'qish")
llist.append("16:00 - jismoniy mashqlar")
llist.append("16:30 - oilaviy mashg'ulotlar ")
llist.append("18:00 - o'z ustimda ishlash 'MASHG'ULOT'")
llist.append("19:30 - kechki ovqat")

llist.printList()