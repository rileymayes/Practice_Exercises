# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:10:53 2017

@author: rlmay
"""
def real_number(s):
    if s.isdigit() and 0 <= int(s) <=100:
        return True
    else:
        return False


def main():
    name = raw_input("What is your name: ")
    print "Your name is", name, "."
    
    age = raw_input("What is your age: ")
    
    if real_number(age) is True:
        print "Your age is", age, "."
    else:
        print "You need to pick a valid age: 0-100."
    
    sage = 100 - int(age)
    
    print "Your name is",name , "and you will be 100 years old in", sage, "years."
    
    rep = int(raw_input("Give me another number: "))
    
    for n in range(rep):
        print "\nYour name is Riley, and you will be 100 years old in", sage, "years.\n"
    