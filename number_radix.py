# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 20:39:05 2018

@author: JOOST
"""

def checkio(str_number: str, radix: int) -> int:
    return -1

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
    

str_number = "AF"

for i in str_number:
    print(i)
    
import string
alfabet = string.ascii_uppercase
alfabet
x = string.digits + string.ascii_uppercase
x

x.find('B')

len(str_number)
for i in str_number:

help(int)    
    
