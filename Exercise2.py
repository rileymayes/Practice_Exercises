# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 12:23:06 2017

@author: rlmay
"""

number = int(raw_input("Give me a number: "))

if number % 2 == 1:
    print "Number is odd.\n"
else:
    print "Number is even.\n"
    
if number % 4 == 0:
    print "Number is a multiple of 4."
elif number % 4 == 1:
    print "Number is odd and not a multiple of 4."
elif number % 4 == 2:
    print "Mumber is even and not a multiple of 4."
else:
    print "Number is not a multiple of 4, and it is odd."
    
num = int(raw_input("Give me a number to check: "))
check = int(raw_input("Give me a number to check with: "))

if num % check == 0:
    print "Check divides evenly into the number."
else:
    print "Check does not divide evenly in the number."