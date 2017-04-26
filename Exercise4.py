# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 21:14:00 2017

@author: rlmay
"""
x1 = []
x2 = []
va = int(raw_input("Give me a number for a list: "))
var = int(raw_input("Give me a number: "))

x = range(1, va+1)

for i in x:
    if var % i == 0:
        x1.append(i)
    else:
        x2.append(i)

print x1
