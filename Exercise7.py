# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 18:48:59 2017

@author: rlmay
"""
import random

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []


for i in a:
    if i % 2 == 0:
        b.append(i)
        
print b

var = int(raw_input("Input the length for a list: "))

x = range(1, var+1)



d = [random.randrange(0,100,1) for i in x]

c = [i for i in a if i % 2 == 0]

print c
print d

e = [i for i in d if i % 2 == 0]

print e