# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 22:12:03 2017

@author: rlmay
"""
import random

x1 = []
x2 = []
x3 = []
x4 = []

x = range(1, 21)

for i in x:
    a = random.randrange(1, 21, 1)
    b = random.randrange(1, 21, 1)
    x1.append(a)
    x2.append(b)

for i in x1:
    if i in x2:
        x3.append(x2)

print x3