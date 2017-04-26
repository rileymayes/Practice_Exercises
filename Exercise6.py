# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 16:41:52 2017

@author: rlmay
"""

a = [5, 10, 15, 20, 25, 30, 35, 40]

print a[:-1]
print a[::-1]

var = str(raw_input("Give me a string: "))
reversed_var = var[::-1]

if var == reversed_var:
    print "This is a palindrome!"
else:
    print "This is not a palindrome!"
    
print reversed_var