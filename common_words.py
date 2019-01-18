# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 09:58:13 2019

@author: JOOST
"""

def checkio(string1, string2):
    set1 = set(string1.split(','))
    set2 = set(string2.split(','))
    return ','.join(sorted(list(set1.intersection(set2))))
    
    

checkio("hello,world", "hello,earth") == "hello"
checkio("one,two,three", "four,five,six") == ""
checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"

string1 = "hello,world"
string2 = "hello,earth"



set1 = set(string1.split(','))
set2 = set(string2.split(','))

shared = set1.intersection(set2)
print(shared)
