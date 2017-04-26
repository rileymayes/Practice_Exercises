# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 14:56:20 2017

@author: rlmay
"""
import random

x2 = []
x3 = []
x4 = []
x6 = []

x = range(0,100)

for i in x:
    x1 = random.randrange(0, 100, 1)
    x2.append(x1)
    if x1 < 5:
        x3.append(x1)
    else:
        x4.append(x1)
        
#print x3
#print x2        
var = int(raw_input("Give me a number: "))

for i in x:
    x5 = random.randrange(0, 100, 1)
    if x5 < var:
        x6.append(x5)
    else:
        print x5
        
print x6